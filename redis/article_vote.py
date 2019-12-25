from time import time
ONE_WEEK_IN_SECONDS = 7 * 96400
VOTE_SCORE = 432


def article_vote(conn, user, article):
    cutoff = time() - ONE_WEEK_IN_SECONDS
    if conn.zscore("time:", article) < cutoff:
        return
    article_id = article.partition(":")[-1]
    if conn.sadd("voted:", article_id, user):
        conn.zincrby("score:", article, VOTE_SCORE)
        conn.hincrby(article, "votes", 1)



def post_article(conn, user, title, link):
    article_id = str(conn.incr("article:"))
    voted = "voted:" + article_id
    conn.sadd(voted, user)
    conn.expire(voted, ONE_WEEK_IN_SECONDS)
    now = time()
    article = "article:" + article_id
    conn.hmset(article, {
        "title" : title,
        "link" : link,
        "poster" : user,
        "time" : now,
        "votes" : 1,
    }
    )
    conn.zadd("score:", article, now + VOTE_SCORE)
    conn.zadd("time:", article, now)
    return article_id


ARTICLES_PER_PAGE = 25
def get_articles(conn, page, order = "score:"):
    start = (page - 1) * ARTICLES_PER_PAGE
    end = start + ARTICLES_PER_PAGE

    ids = conn.zrevrange(order, start, end)
    articles = []
    for id in ids:
        article_data = conn.hgetall(id)
        article_data["id"] = id
        articles.append(article_data)
    return articles

def add_remove_groups(conn, article_id, to_add=[], to_remove=[]):
    article = "article:" + article_id
    for group in to_add:
        conn.sadd("group:" + group, article)
    for group in to_remove:
        conn.srem("group:" + group, article)


def get_group_article(conn, group, page, order="score:"):
    key = order + group
    if not conn.exists(key):
        conn.zinterstore(key, ["group:" + group, order], aggregate = "max",)
        conn.expire(key, 60)
    return get_articles(conn, page, key)


def check_login(conn, token):
    return conn.hget("login:", token)

def update_token(conn, token, user, item=None):
    time = time()
    conn.hset("login:", user)
    conn.zadd("recent:", token, time)
    if item:
        conn.zadd("view:"+token, item, time)
        conn.zremrangebyrank("view:"+token, 0, -26)



QUIT = False
LIMIT = 1000000
def clean_sessions(conn):
    while not QUIT:
        size = conn.zcard("recent:")
        if size <= LIMIT:
            time.sleep()
            continue
        end_index = min(size - LIMIT, 100)
        tokens = conn.zrange("recent:", 0, end_index-1)
        session_keys = []
        for token in tokens:
            session_keys.append("viewed:"+ token)
        conn.delete(*session_keys)
        conn.hdel("login:", *tokens)
        conn.zrem("recent:", *tokens)


def add_to_cart(conn, session, item, count):
    if count <= 0:
        conn.hrem('cart:' + session, item)
    else:
        conn.hset('cart:' + session, item, count)

def clean_full_session(conn):
    while not QUIT:
        size = conn.zcard("recent:")
        if size <= LIMIT:
            time.sleep(1)
            continue
        end_index = min(size - LIMIT, 100)
        sessions = conn.zrange("recent:", 0, end_index)
        session_keys = []
        for sess in sessions:
            session_keys.append("viewed:", sess)
            session_keys.append("card:" + sess)
        conn.delete(*session_keys)
        conn.hdel("login:", *sessions)
        conn.zrem("recent:", *sessions)


def cache_request(conn, request, callback):
    if not can_cache(conn, request):
        return callback(request)
    
    page_key = "cache:" + hash_request(request)
    content = conn.get(page_key)
    if not content:
        content = callback(request)
        conn.setex(page_key, content, 300)
    return content

def schedule_row_cache(conn, row_id, delay):
    conn.zadd("delay:", row_id, delay)
    conn.zadd("schedule:", row_id, time.time())

def cache_rows(conn):
    while not QUIT:
        next = conn.zrange("schedule:", 0, 0 withscores = True)
        now = time.time()
        if not next or next[0][1] > now:
            time.sleep(0.05)
            continue
        row_id = next[0][0]
        delay = conn.zscore("delay:", row_id)
        if delay <= 0:
            conn.zrem("delay:", row_id)
            conn.zrem("schedule:", row_id)
            conn.delete("inv:" + row_id)
            continue

        row = Inventory.get(row_id)
        conn.zadd("schedule:", row_id, now + delay)
        conn.set("inv:" + row_id, json.dumps(row.to_dict()))


def update_token(conn, token, user, item=None):
    timestamp = time.time()
    conn.hset('login:', token, user)
    conn.zadd('recent:', token, timestamp)
    if item:
        conn.zadd('viewed:' + token, item, timestamp)
        conn.zremrangebyrank('viewed:' + token, 0, -26)
        conn.zincrby('viewed:', item, -1)

def rescale_viewed(conn):
    while not QUIT:
        conn.zremrangebyrank('viewed:', 0, -20001)
        conn.zinterstore('viewed:', {'viewed:', 0.5})
        time.sleep(300)

def can_canche(conn, request):
    item_id = extract_item_it(request)
    if not item_id or is_dynamic(request):
        return False
    rank = conn.zrank('viewed:', item_id)
    return rank is not None and rank < 10000
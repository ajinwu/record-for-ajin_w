from concurrent import futures
from flags import save_flag, get_flag, show, POP20_CC

MAX_WORKS = 20

def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + ".gif")
    return cc

# def download_many(cc_list):
#     works = min(MAX_WORKS, len(cc_list))
#     with futures.ThreadPoolExecutor(works) as executor:
#         res = executor.map(download_one, sorted(cc_list))
    
#     return len(list(res))

# download_many(POP20_CC)

def download_many(cc_list):
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = "scheduled for {}:{}"
            print(msg.format(cc, future))
        result = []

        for future in futures.as_completed(to_do):
            res = future.result()
            msg = "{} result {}"
            print(msg.format(future, res))
            result.append(res)
    return len(result)

download_many(POP20_CC)

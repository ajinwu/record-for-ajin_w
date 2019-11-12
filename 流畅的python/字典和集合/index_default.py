import sys
import re
import collections

WORD_RE = re.compile("\w+")
# index = collections.defaultdict(list)
index = {}
with open(sys.argv[1], encoding="utf-8") as f:
    for line_no, line in enumerate(f, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            col = match.start() + 1
            location = (line_no, col)
            # index[word].append(location)
            index.setdefault(word,[]).append(location)
for word in sorted(index, key = str.upper):
    print(word, index[word])
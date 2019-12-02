from unicodedata import normalize
s2 = "cafe\u0301"
s1 = "café"
print(s1 == s2)
print(len(s1), len(s2))
print(len(normalize("NFC", s1)), len(normalize("NFC", s2)))
print(len(normalize("NFD", s1)), len(normalize("NFD", s2)))
print(len(normalize("NFD", s1)) == len(normalize("NFD", s2)))

micro = "μ"
from unicodedata import name
print(name(micro))
micro_cf = micro.casefold()
print(name(micro_cf))
print(micro == micro_cf)

import unicodedata
def shave_marks(txt):
    norm_txt = normalize("NFD", txt)  # 分解基字符和组合记号
    shaved = "".join(c for c in norm_txt if not unicodedata.combining(c)) # 去掉组合记号
    print(shaved)
    return normalize("NFC", shaved) # 重新规范化

print(shave_marks("café"))


import locale
l = ["éac","eac"]
print(sorted(l, key = locale.strxfrm))

import pyuca
coll = pyuca.Collator()
print(sorted(l, key=coll.sort_key))
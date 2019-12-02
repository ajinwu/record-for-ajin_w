import chardet
city = "São Paulo"
print(city.encode())
print(city.encode("utf-16"))
print(city.encode("iso8859_1"))
print(city.encode("cp437", errors = "ignore"))
print(city.encode("cp437", errors = "replace"))

octes = b"Montr\xe9al"
print(octes.decode("cp1252"))
print(octes.decode("iso8859_7"))
print(octes.decode("koi8_r"))
with open("/home/ajin_w/github/record-for-ajin_w/流畅的python/文本和字节序列/编码.py","rb") as f:
    print(chardet.detect(f.read()))

print(chardet.detect(b"Montr\xe9al"))
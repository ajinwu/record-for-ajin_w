city = "São Paulo"
print(city.encode())
print(city.encode("utf-16"))
print(city.encode("iso8859_1"))
print(city.encode("cp437", errors = "ignore"))
print(city.encode("cp437", errors = "replace"))

octes = b"Montr\xe9al"
print(octes.decode("cp1252"))
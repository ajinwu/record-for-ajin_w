def tag(name:str, *content:str, cls=None, **attrs: dict) -> str:
    if cls is not None:
        attrs["class"] = cls
    if attrs:
        attr_str = "".join("%s=%s" %(attr, value)
        for attr, value in sorted(attrs.items())
        )
    else:
        attr_str = ""
    if content:
        return "\n".join("</%s%s>%s</%s>" %(name, attr_str, c, name) 
        for c in content
        )
    else:
        return "<%s %s />" %(name, attr_str)

print(tag("br"))
print(tag("p", "hello", "word"))
mytag = {"name":"img", "title":"pic", "src":"sun.jpg","cls":"test"}
print(tag(**mytag))

from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return "<pre>{}</pre>".format(content)

@htmlize.register
def _(text:str):
    content = html.escape(text).replace("\n", "</br>\n")
    return "<p>{0}</p>".format(content)

@htmlize.register
def _(n: int):
    return "<pre>{0} (0x{0:x})</pre>".format(n)


@htmlize.register
def _(seq:abc.MutableSequence):
    inner = "<li>\n</li>".join(htmlize(item) for item in seq)
    return "<ul>\n</li>" + inner + "</li>\n</ul>"


print("hello")
print(htmlize(5))
print(htmlize([1,2,3]))


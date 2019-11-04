import bisect
import sys
HAYSTACK = [1, 3, 5, 8, 12, 15, 20, 21, 23, 23, 28, 40]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * "  |"
        print(ROW_FMT.format(needle, position, offset))



def grade(score,breakpoint=[60,70,80,90], grades = "FDCBA"):
    i = bisect.bisect(breakpoint,score)
    return grades[i]
print(list(grade(score) for score in [33, 99, 77, 79, 89, 90, 100]))


# if __name__ == '__main__':
#     if sys.argv[-1] == 'left':
#         bisect_fn = bisect.bisect_left
#     else:
#         bisect_fn = bisect.bisect
#     print("DEMO:", bisect_fn.__name__)
#     print("haystack ->", " ".join("%2d" % n for n in HAYSTACK))
#     demo(bisect_fn)
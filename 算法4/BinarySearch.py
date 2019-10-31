import sys
class BinnarySearch:
    def rank(key, l):
        lo = 0
        hi = len(l) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if key < l[mid]:
                hi = mid - 1
            elif key > l[mid]:
                lo = mid + 1
            else:
                return mid
        return -1

l = int(sys.argv[0])

l.sort()
while sys.stdin:
    int key = int(sys.stdin.read())
    if BinnarySearch().rank(key, l):
        sys.stdout.print(key)

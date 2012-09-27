ways = {}

def how_many_ways(h,w):
    if ways.has_key((h,w)):
        return ways[(h,w)]
    if ways.has_key((w,h)):
        return ways[(w,h)]
    if h == 1:
        return w + 1
    if w == 1:
        return h + 1
    ways[(h,w)] = how_many_ways(h-1,w) + how_many_ways(h,w-1)
    return ways[(h,w)]

def findLargest(l):
    lo , hi = 0 , len(l)
    left , right = l[0] , l[-1]
    
    while(lo<hi):
        mid = (lo + hi)//2
        if(left > l[mid]):
            hi = mid
        else:
            lo = mid +1
    return l[lo-1]

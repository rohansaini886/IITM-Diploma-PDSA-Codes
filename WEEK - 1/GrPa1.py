def find_Min_Difference(L, P):
    L1 = sorted(L)
    s = len(L1)
    min_diff = 10000000000
    for i in range(s):
        if i + P - 1 < s:
            diff = L1[i + P - 1] - L1[i]
            if min_diff > diff:
                min_diff = diff
    return min_diff
L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))

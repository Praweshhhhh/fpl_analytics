#eg:1    W=50
# val = [60, 100, 120]
# wt = [10, 20, 30]
# max_W = 50

#eg:2 W=8
# wt = [3, 4, 6, 5]
# val = [2, 3, 1, 4]
# max_W = 8

#eg: 3 W = 850
wt = [62,44,61,47,49,49,53,51,53,55,52,52,53,55,46,62,51,55,53,48,61,47,52,50,55,46,65,65,70,77,60,73,74,56,58,60,75,59,97,86,89,85,120,121,125,106,61,60,57,51,116,62,64,99,73,93,110,82,73,80,76,109,97]
val = [122,126, 133,135,137,137,143,143,153,156,160,170,123,123,123,123,124,127,128,128,130,133,142,142,143,144,167,178,181,210,123,125,127,130,133,137,139,149,169,175,177,200,204,221,233,251,126,129,131,132,132,136,139,146,153,155,158,165,168,194,198,205,210]
max_W = 850
max_E = 11
n = len(wt)
t = [[[-1] * (max_E+1) for _ in range(max_W+1)] for _ in range(n+1)]

def knapsack(wt,val,max_W,n,max_E):
    if n == 0 or max_W == 0 or max_E == 0:
        return 0
    if t[n][max_W][max_E] != -1:
        return t[n][max_W][max_E]
    if wt[n-1] <= max_W:
        t[n][max_W][max_E] = (max(val[n-1] + knapsack(wt,val,max_W - wt[n-1],n-1,max_E -1), knapsack(wt,val,max_W,n-1,max_E)))
        return t[n][max_W][max_E]
    elif wt[n-1] > max_W:
        t[n][max_W][max_E] = knapsack(wt,val,max_W,n-1,max_E)
        return t[n][max_W][max_E]


print(knapsack(wt,val,max_W,n,max_E))
    
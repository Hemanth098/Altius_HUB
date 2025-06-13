nums = list(map(int,input().split()))
k = int(input())
res = []
for i in range(0,len(nums)-k+1):
    p = sorted(nums[i:i+k])
    res.append(p[k//2])
print(res)
def arrayManipulation(n, queries):
    arr=[]
    for i in range(n):
        arr.append(0)
    for q in queries:
        a,b,k=q[0],q[1],q[2]
        for x in range(a-1,b):
            arr[x]=arr[x]+k
            
    return max(arr)

n,m=map(int, input().rstrip().split())
queries=[]

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

result = arrayManipulation(n, queries)
print(str(result))


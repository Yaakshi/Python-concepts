def matchingStrings(stringList, queries):
    ansarr=[]
    for x in range(len(queries)):
        count=0
        for y in range(len(stringList)):
            if(queries[x]==stringList[y]):
                count+=1
        ansarr.append(count)
    return ansarr

stringList_count = int(input().strip())
stringList = []

for _ in range(stringList_count):
    stringList_item = input()
    stringList.append(stringList_item)

queries_count = int(input().strip())
queries = []

for _ in range(queries_count):
    queries_item = input()
    queries.append(queries_item)

res = matchingStrings(stringList, queries)
print('\n'.join(map(str, res)))


import math

def hourglassSum(arr):
    sums = []
    i=0
    j=0
    
    for i in range(1,5):
        for j in range(1,5):
            sums.append(
                arr[i-1][j-1]   #top left
                +arr[i-1][j]    #top mid
                +arr[i-1][j+1]  #top right
                +arr[i][j]      #mid
                +arr[i+1][j-1]  #bot left
                +arr[i+1][j]    #bot mid
                +arr[i+1][j+1]) #bot right
    
    return max(sums)

matrix=[]

# for i in range(6):
#     arr=[]
#     for j in range(6):
#          arr.append(int(input()))
#     matrix.append(arr)
print("2D array: ")
for _ in range(6):
    matrix.append(list(map(int, input().rstrip().split())))

result = hourglassSum(matrix)

print("Maximum of the sum of hourglasses: "+str(result))


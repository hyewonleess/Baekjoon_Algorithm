n = int(input())
array = []
for _ in range(n):
    name, score = input().split()
    array.append((name, score))

sorted(array, key = lambda data: data[1])

#for i in range(len(array)):
    #print(array[i][0], end = ' ')
    
for data in array:
    print(data[0], end = ' ')

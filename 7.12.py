n = 10
list = [int(i) for i in range(n)]
k = int(input()) % n
C = int(input())

#list.insert(k, C)
#list = list[:k] + [C] + list[k:]
#list = list[:k] + [C] + [list[i] for i in range(k, n)]

res_list = []

for i in range(len(list)):
    if i == k:
        res_list.append(C)
        res_list.append(list[i])
    else:
        res_list.append(list[i])
        
print(res_list)

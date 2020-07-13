n = int(input())
a = [int(x) for x in input().split(" ")]
b = [int(x) for x in input().split(" ")]

index_map = {}
for i,aa in enumerate(a):
    index_map[aa] = i

offset_list = []
for i,bb in enumerate(b):
    if index_map[bb] < i:
        offset_list.append(n-(i-index_map[bb]))
    else:
        offset_list.append(index_map[bb]-i)

fre_dict = {}
most_occur = 0
for oo in offset_list:
    if oo not in fre_dict:
        fre_dict[oo] = 1
    else:
        fre_dict[oo]+=1
    if fre_dict[oo] > most_occur:
        most_occur = fre_dict[oo]
print(most_occur)
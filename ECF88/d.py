import heapq
n = int(input())

def heap_push(arr, ele):
    heapq.heappush(arr,-1*ele) 
    return arr

def heap_look(arr):
    ele = -1*heapq.heappop(arr) 
    heapq.heappush(arr,-1*ele)
    return arr, ele
nums = [int(x) for x in input().split(" ")]

value = []

if max(nums)<=0:
    value.append(0)
else:
    max_element = []
    heapq.heapify(max_element)
    max_ending_here = 0
    max_so_far = 0
    for it in nums:
        max_ending_here = max_ending_here + it
        max_element = heap_push(max_element, it)
        if(max_ending_here < 0):
            max_ending_here = 0
            max_element = []
            heapq.heapify(max_element)
        else:
            max_element, max_ele = heap_look(max_element)
            curr_max = max_ending_here - max_ele
            if(max_so_far < curr_max):
                print(max_element)
                max_so_far = curr_max
    value.append(max_so_far)
print(max(value))
    


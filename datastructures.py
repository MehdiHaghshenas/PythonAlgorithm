from multiprocessing.managers import DictProxy


# dictionary
tempDict = {}
tempDict[1] = "d"
tempDict[2] = "3"
tempDict = {
    1: "me",
    2: "hag"
}
del tempDict[2]
print(tempDict)

# for
for i in range(5, 10):
    print(i)

 # array
arr1 = [1, 3, 4, 5, 6]
arr1 = [i for i in range(10)]
arr1.append(11)
arr1.insert(0,333)
arr2 = arr1.copy()
arr2[3]=333
arr2.sort(reverse=True)
print(arr1.pop())
print(arr1.pop(0)) # Queue
print(arr1)
print(arr2)

# Stack using deque
from collections import deque
queue = deque(["Ram", "Tarun", "Asif", "John"])
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Birbal")
print(queue)
print(queue.pop())
print(queue.pop()) # Queue
print(queue.popleft())
print(queue)

 # array
arr1 = [[1, 3, 4],[2, 5, 6]]
arr1 = [[i*j for j in range(3)] for i in range(10)]
arr1.append(11)
arr1.insert(0,333)
print(arr1.pop())
print(arr1.pop(0)) # Queue
print(arr1)


myset = {"apple", "banana", "cherry"}
myset = set()
myset.add("mehdi")
myset.add("fateme")
myset.add("fateme")
print(len(myset))
print(myset)
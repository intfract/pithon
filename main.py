import math

def gcd(a, b):
  if a == 0:
    return b
  if b == 0:
    return a
  return gcd(b, a - b)

print(gcd(48, 32))  # 16

def sortedIndex(a: list, item):
  start = 0
  end = len(a)
  depth = math.log(len(a) + 1, 2)
  i = 0
  while i <= math.ceil(depth):
    mid = (start + end) // 2
    if start >= end:
      break
    if item == a[mid]:
      return mid # returns the index of element
    elif item > a[mid]:
      start = mid + 1
    else:
      end = mid
    i += 1
  return mid  # returns the insertion position

print(sortedIndex(['a', 'b', 'c', 'd'], 'b'))  # 1
print(sortedIndex([0, 1, 2, 3], 1.5))  # 2

def sortedInsert(a: list, item):
  a.insert(sortedIndex(a, item), item)
  return a

print(sortedInsert([0, 1, 2, 3], 1.5)) # [0, 1, 1.5, 2, 3]
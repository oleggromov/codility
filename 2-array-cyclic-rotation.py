def solution1(arr, k):
  result = []
  length = len(arr)

  if length > 0:
    rotations = k % length if k > length else k
    for i in range(length - rotations, 2 * length - rotations):
      index = i % length if i > length - 1 else i
      result.append(arr[index])

  return result

def solution2(arr, k):
  result = []
  length = len(arr)

  if length > 0:
    index = length - k
    for i in range(length):
      result.append(arr[index % length])
      index += 1

  return result

def solution3(arr, k):
  len_arr = len(arr)
  split_point = len_arr - k % len_arr if len_arr > 0 else 1
  return arr[split_point:] + arr[0:split_point]

assert solution3([], 3) == []
assert solution3([1,2,3], 1) == [3,1,2]
assert solution3([4,5,6], 2) == [5,6,4]
assert solution3([7,8,9], 3) == [7,8,9]
assert solution3([8,9,0], 4) == [0,8,9]
assert solution3([1,2,3,4,5], 9) == [2,3,4,5,1]
assert solution3([1,1,2,3,5], 42) == [3,5,1,1,2] # codility failed test
assert solution3([3,8,9,7,6], 3) == [9,7,6,3,8]


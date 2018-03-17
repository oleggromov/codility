def solution(arr, k):
  result = []
  length = len(arr)

  if length > 0:
    rotations = k % length if k > length else k

    for i in range(length - rotations, 2 * length - rotations):
      index = i % length if i > length - 1 else i
      result.append(arr[index])

  return result

assert solution([], 3) == []
assert solution([1,2,3], 1) == [3,1,2]
assert solution([4,5,6], 2) == [5,6,4]
assert solution([7,8,9], 3) == [7,8,9]
assert solution([8,9,0], 4) == [0,8,9]
assert solution([3,8,9,7,6], 3) == [9,7,6,3,8]


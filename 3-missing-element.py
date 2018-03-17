def solution(arr):
  sum = 0
  for num in arr:
    sum += num

  number = len(arr) + 1
  return int(number * (1 + number) / 2 - sum)


assert solution([1,3,5,2]) == 4
assert solution([7,6,5,4,3,2]) == 1
assert solution([1,2,4,5]) == 3

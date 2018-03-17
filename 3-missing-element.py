def solution(arr):
  sum = 0
  for number in arr:
    sum += number

  number = len(arr) + 1
  return number * (1 + number) / 2 - sum


print(solution([1,3,5,2]))
assert solution([1,3,5,2]) == 4
assert solution([7,6,5,4,3,2]) == 1
assert solution([1,2,4,5]) == 3

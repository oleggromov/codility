def solution(arr):
  diff_len = len(arr) - 1
  diffs = [None] * diff_len

  smallest = 1_000_000

  forward = 0
  backward = 0

  for index in range(0, diff_len):
    forward += arr[index]
    backward += arr[diff_len - index]

    if diffs[index] is None:
      diffs[index] = forward
    else:
      diffs[index] = abs(diffs[index] - forward)
      if diffs[index] < smallest:
        smallest = diffs[index]

    if diffs[diff_len - index - 1] is None:
      diffs[diff_len - index - 1] = backward
    else:
      diffs[diff_len - index - 1] = abs(diffs[diff_len - index - 1] - backward)
      if diffs[diff_len - index - 1] < smallest:
        smallest = diffs[diff_len - index - 1]

  return smallest

print(solution([1,1]))
assert solution([1,1]) == 0
print(solution([3,1,2,4,3]))
assert solution([3,1,2,4,3]) == 1

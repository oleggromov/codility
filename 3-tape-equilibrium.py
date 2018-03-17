def solution(arr):
  diff_len = len(arr) - 1
  diffs = [None] * diff_len

  smallest = 1_000_000

  forward = 0
  backward = 0

  for index in range(0, diff_len):
    reverse_index = diff_len - index - 1
    forward += arr[index]
    backward += arr[diff_len - index]

    if diffs[index] is None:
      diffs[index] = forward
    else:
      diffs[index] = abs(diffs[index] - forward)
      if diffs[index] < smallest:
        smallest = diffs[index]

    if diffs[reverse_index] is None:
      diffs[reverse_index] = backward
    else:
      diffs[reverse_index] = abs(diffs[reverse_index] - backward)
      if diffs[reverse_index] < smallest:
        smallest = diffs[reverse_index]

  return smallest



print(solution([1,1]))
assert solution([1,1]) == 0
print(solution([3,1,2,4,3]))
assert solution([3,1,2,4,3]) == 1

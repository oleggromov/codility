def solution(arr):
  diff_len = len(arr) - 1
  diffs = [None] * diff_len

  smallest = 1_000_000

  forward = 0
  backward = 0

  for index in range(0, diff_len):
    forward += arr[index]
    backward += arr[diff_len - index]

    if index < diff_len / 2:
      diffs[index] = forward
      diffs[diff_len - index - 1] = backward
    else:
      diffs[index] = abs(diffs[index] - forward)
      diffs[diff_len - index - 1] = abs(diffs[diff_len - index - 1] - backward)
      if diffs[index] < smallest:
        smallest = diffs[index]
      if diffs[diff_len - index - 1] < smallest:
        smallest = diffs[diff_len - index - 1]

  return smallest

print(solution([3,1,2,4,3]))

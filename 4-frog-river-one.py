def solution(x, leaves):
  fallen = {}
  for (i, leaf) in enumerate(leaves):
    if leaf <= x:
      fallen[leaf] = True
    if len(fallen.keys()) == x:
      return i

  return -1

assert solution(5, [1,4,3,2]) == -1
assert solution(5, [1,3,1,4,2,3,5,4]) == 6
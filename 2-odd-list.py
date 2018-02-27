def solution(A):
  uneven = {}

  for number in A:
    if number in uneven:
      del uneven[number]
    else:
      uneven[number] = True

  return list(uneven.keys()).pop()

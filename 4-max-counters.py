def solution(count, ops):
  counters = [0] * count
  largest = 0

  for op in ops:
    if op == count + 1:
      # this is even worse than counters = [largest] * count
      for i in range(0, len(counters)):
        counters[i] = largest
    else:
      counters[op-1] += 1
      if largest < counters[op-1]:
        largest = counters[op-1]

  return counters

print(solution(5, [3,4,4,6,1,4,4]))
assert solution(5, [3,4,4,6,1,4,4]) == [3,2,2,4,2]

def solution(N):
  binary = bin(N)[2:]

  in_gap = False
  longest = 0
  current = 0

  for bit in binary:
    if bit == '1':
      if in_gap:
        if current > longest:
          longest = current

        current = 0
      else:
        in_gap = True
    else:
      current += 1

  return longest

assert solution(0) == 0
assert solution(0b1111) == 0
assert solution(0b111111101111) == 1
assert solution(0b0100001) == 4
assert solution(0b101000) == 1
assert solution(0b101001000) == 2
assert solution(0b10110001) == 3
assert solution(0b10000000000000000000000000001) == 27

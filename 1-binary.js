const assert = (condition, error) => {
  if (!condition) {
    throw new Error(error)
  }
}

function solution (number) {
  const binary = number.toString(2)

  let isGap = false
  let current = 0
  let longest = 0

  for (let i = 0; i < binary.length; i++) {
    if (binary[i] === '1') {
      if (isGap) {
        if (current > longest) {
          longest = current
        }

        current = 0
      } else {
        isGap = true
      }
    } else {
      current++
    }
  }

  return longest
}

assert(solution(parseInt('0', 2)) === 0, '0 returns 0 ')
assert(solution(parseInt('1111', 2)) === 0, '1111 returns 0 ')
assert(solution(parseInt('111111101111', 2)) === 1, '111111101111 returns 1 ')
assert(solution(parseInt('0100001', 2)) === 4, '0100001 returns 4')
assert(solution(parseInt('101000', 2)) === 1, '101000 returns 1')
assert(solution(parseInt('101001000', 2)) === 2, '101001000 returns 2')
assert(solution(parseInt('10110001', 2)) === 3, '10110001 returns 2')
assert(solution(parseInt('10000000000000000000000000001', 2)) === 27, '10000000000000000000000000001 return 27')

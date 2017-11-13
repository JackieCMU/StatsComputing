maxSubSum = function(list) {
  accum = 0
  maxSum = 0
  for (value in list) {
    accum = accum + value
    if (accum > maxSum) {
      maxSum = accum
    } else if (accum < 0) {
      accum = 0
    }
  }
  return(maxSum)
}


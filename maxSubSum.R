# add value each time
# if accumulative sum is smaller than max
# if accumulative sum is less than 0
# ignore the current accumulative sum, reset it as 0
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

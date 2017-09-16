# the code would like to store the u nearest neighbors of y based on Euclidian distance between x and y(yT*y is the same, thus it could be ignored) and index of each x by increasing. However, it is wrong.

find.it <- function(x, y, k) {
  upper.bound = 10e6	# set a bound 
  knn = c()		# initialize vector to contain distance
  index.knn = c()	# initialize vector to contain index of x
  if(k > nrow(x)) {		# output error if row of x > k
    return('There is an error. The k is too big')
  }
  for (i in 1 : nrow(x)) { 
    distance = (crossprod(x[i, ]) - 2 * (x[i, ] %*% y))[1]	# Euclidian Distance without yT*y
    if(length(knn) < k) {	# to store first k distance and index
      knn = c(knn, distance)
      index.knn = c(index.knn, i)
      upper.bound = max(knn)
      if(distance < upper.bound) {	# sort by increasing
        if(distance == min(knn)) {	# place on the 1st
          posInsert  = 1
        } else {
          posInsert = max(which(distance > knn)) + 1
        }
        knn[(posInsert + 1) : length(knn)] = knn[posInsert : (length(knn) - 1)]
        index.knn[(posInsert + 1) : length(knn)] = index.knn[posInsert : (length(knn) - 1)]
        knn[posInsert] = distance
        index.knn[posInsert] = i
      }
    } else if(distance < upper.bound) {	# insert new distance < upper bound
      if(distance <= min(knn)) { # insert in the 1st
        posInsert = 1
      } else {
        posInsert = max(which(distance > knn)) + 1
      }
      if(posInsert == k) {	# the position is last one, just insert without shifting
        knn[k] = distance
        index.knn[k] = i
      }
      else {	# insert and shift
        knn[(posInsert + 1) : k] =  knn[posInsert : (k - 1)]
        index.knn[(posInsert + 1) : k] =  index.knn[posInsert : (k - 1)]
        knn[posInsert] = distance
        index.knn[posInsert] = i
      }
      upper.bound = max(knn)	# renew upper bound to filter higher value
    }
  }
  return(list(min.k = min(knn), knn = knn, index.knn = index.knn))	# return a list of minimal distance, k lowerest distance and index by increasing
}

if(!require('testthat')) {
  install.packages('testthat')
  library('testthat')
}

x = matrix(c(1, 1, 20, 17, 9, 9, 6, 8), nrow = 4)
z = matrix(c(20, 17, 1, 1, 6, 8, 9, 9), nrow = 4)
y = c(1, 2)

test_that("k nearest neighbor of y", {
  expect_equal(find.it(x, y, 5), 'There is an error. The k is too big')	# should output error
  expect_equal(find.it(x, y, 1), list('min.k' = 44, 'knn' = 44, 'index.knn' = 1))	# should get what is expected 
  expect_equal(find.it(x, y, 3), find.it(x, y, 3))
  expect_equal(find.it(x, y, 2), find.it(-x, -y, 2))	# multiply by -1, the result should be the same
  expect_equal(find.it(x, y, 2)$knn, find.it(z, y , 2)$knn)	# the distance shoud be the same
  expect_equal(find.it(x, y, 2)$min.k, find.it(z, y, 2)$min.k)	# the minimal value should be the same
  expect_equal((sum(find.it(x, y, 2)$index.knn != find.it(z, y, 2)$index.knn) > 0), TRUE)	# random position, the index should be different
})

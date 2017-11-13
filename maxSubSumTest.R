source("maxSubSum.R")
library(assertthat)
library(testthat)

test_that("maxSubSum works on select examples", {
  expect_equal(maxSubSum(c(1, 2, 3, 4)), 10)
  expect_equal(maxSubSum(c(-1, -2, -3, -4)), 0)
  expect_equal(maxSubSum(c(-1, 1, -1, 1, -1, 1)), 1)
  expect_equal(maxSubSum(c(31, -41, 59, 26, -53, 58, 97, -23, 84)), 248)
})

test_that("maxSubSum on the empty vector", {
  expect_equal(maxSubSum(c()), 0)
})

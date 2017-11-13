source("maxSubSum.R")
args = commandArgs(trailingOnly = TRUE)
list = as.numeric(strsplit(args[1], ",")[[1]])
maxSubSum(list)
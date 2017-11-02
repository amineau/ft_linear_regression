#!/usr/local/bin/Rscript

theta0 <- 0
theta1 <- 0

commandArgs() -> arguments
strtoi(arguments[6]) -> mileage
result <- theta0 + theta1 * mileage
paste(result)

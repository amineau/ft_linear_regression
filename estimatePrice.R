#!/usr/local/bin/Rscript

theta0 <- 0
theta1 <- 0

commandArgs(trailingOnly = TRUE) -> argv
if (length(argv) != 1) {
    print("Bad number of arguments")
    quit()
}
strtoi(argv[1]) -> mileage
if (is.na(mileage)) {
    print(paste(mileage,"is not numeric"))
    quit()
}
result <- theta0 + theta1 * mileage
print(result)

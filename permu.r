
set.seed(1)
n <- 100
tr <- rbinom(100, 1, 0.5)
y <- 1 + tr + rnorm(n, 0, 3)

# The difference in means is, as we would expect (given we made it up), about 1:

diff(by(y, tr, mean))
## [1] 1.341

# To obtain a single permutation of the data, we simply resample without replacement and calculate the difference again:

s <- sample(tr, length(tr), FALSE)
diff(by(y, s, mean))
## [1] -0.2612

# Here we use the permuted treatment vector s instead of tr to calculate the difference and find a very small difference. If we repeat this process a large number of times, we can build our approximate permutation distribution (i.e., the sampling distribution for the mean-difference). We'll use replicate do repeat our permutation process. The result will be a vector of the differences from each permutation (i.e., our distribution):

dist <- replicate(2000, diff(by(y, sample(tr, length(tr), FALSE), mean)))

# We can look at our distribution using hist and draw a vertical line for our observed difference:

hist(dist, xlim = c(-3, 3), col = "black", breaks = 100)
abline(v = diff(by(y, tr, mean)), col = "blue", lwd = 2)


# At face value, it seems that our null hypothesis can probably be rejected. Our observed mean-difference appears to be quite extreme in terms of the distribution of possible mean-differences observable were the outcome independent of treatment assignment. But we can use the distribution to obtain a p-value for our mean-difference by counting how many permuted mean-differences are larger than the one we observed in our actual data. We can then divide this by the number of items in our permutation distribution (i.e., 2000 from our call to replicate, above):

sum(dist > diff(by(y, tr, mean)))/2000  # one-tailed test
## [1] 0.009
sum(abs(dist) > abs(diff(by(y, tr, mean))))/2000  # two-tailed test
## [1] 0.018


# Using either the one-tailed test or the two-tailed test, our difference is unlikely to be due to chance variation observable in a world where the outcome is independent of treatment assignment.



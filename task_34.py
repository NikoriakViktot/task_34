import concurrent.futures
import math
#
# We have the following input list of numbers, some of them are prime.\
# You need to create a utility function that takes as input a number and returns
# a bool, whether it is prime or not.
# Use ThreadPoolExecutor and ProcessPoolExecutor to create different concurrent
# implementations for filtering NUMBERS.
# Compare the results and performance of each of them.

NUMBERS = [
   2,
   1099726899285419,
   1570341764013157,
   1637027521802551,
   1880450821379411,
   1893530391196711,
   2447109360961063,
   3,
   2772290760589219,
   3033700317376073,
   4350190374376723,
   4350190491008389,
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,
]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt + 1, 2):
        if n % i == 0:
            return False
    return True

def executer():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(NUMBERS, executor.map(is_prime, NUMBERS)):
            print('%d is prime: %s' % (number, prime))

#
# Task 2
#
# Requests using concurrent and multiprocessing libraries
# Download all comments from a subreddit of your choice using
# URL: https://api.pushshift.io/reddit/comment/search/ .
# As a result, store all comments in chronological order in JSON and dump it to a file.
# For this task use concurrent and multiprocessing libraries for making requests to Reddit API.



if __name__ == '__main__':
    executer()
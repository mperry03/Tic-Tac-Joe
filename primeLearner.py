'''
Guess the prime numbers!
to guess the numbers in order, run python -m primeLearner.py order
to guess the numbers at random, run python -m primeLearn.py random
to guess in order starting at any prime, run python -m primeLearner.py anywhere
'''


import argparse


parser = argparse.ArgumentParser()
parser.add_argument('which_mode')
args = parser.parse_args()
which_mode = args.which_mode

def main():

    primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
                 199,
                 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
                 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
                 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
                 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
                 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
                 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
                 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]  # more to be added!

    #List the primes in any order
    if which_mode == 'random':
        retry = True

        while retry:
            correct = True
            print("Type the primes in any order!")
            while correct:
                correct_count = 0
                for prime in primeList:
                    primeGuess = int(input ())
                    if primeGuess in primeList:
                        correct_count += 1
                    if primeGuess not in primeList:
                        print("\nYou got", correct_count, "primes correct")
                        print("The next prime is", prime, "\n")
                        correct = False
                        tryAgain = input("Try Again? Y/N: ")
                        if tryAgain == 'Y':
                            retry = True
                        else:
                            retry = False
                        break
 ################################################################

    #Type the primes in order starting at 2
    elif which_mode == 'order':
        retry = True

        while retry:
            correct = True
            print("Type the primes in order!")
            while correct:
                correct_count = 0
                for prime in primeList:
                    primeGuess = int(input())
                    if primeGuess == prime:
                        correct_count += 1
                    if primeGuess != prime:
                        print("\nYou got", correct_count, "primes correct")
                        print("The next prime is", prime, "\n")
                        correct = False
                        tryAgain = input("Try Again? Y/N: ")
                        if tryAgain == 'Y':
                            retry = True
                        else:
                            retry = False
                        break
################################################################

    elif which_mode == 'anywhere':
        retry = True

        while retry:
            correct = True
            print("Type the primes in order starting at any prime!")
            firstPrime = int(input())
            start = primeList.index(firstPrime)
            truncPrimes = []
            for i in range(start + 1, len(primeList)):
                truncPrimes.append(primeList[i])
            while correct:
                correct_count = 1
                for prime in truncPrimes:
                    primeGuess = int(input())
                    if primeGuess == prime:
                        correct_count += 1
                    if primeGuess != prime:
                        print("\nYou got", correct_count, "primes correct")
                        print("The next prime is", prime, "\n")
                        correct = False
                        tryAgain = input("Try Again? Y/N: ")
                        if tryAgain == 'Y':
                            retry = True
                        else:
                            retry = False
                        break

main()

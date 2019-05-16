# Mersenne Twister Randomness Analyzer (mersenne-analyzer)

## About

The Mersenne Twister is a pseudo-random number generator developed by Makoto Matsumoto and Takuji Nishimura in 1997. This project uses the MT19937 implementation of the algorithm.

This project aims to determine the randomness of the Mersenne Twister via a T-Test, that returns a P-Value. If the P-Value is significant, then it can be said that the Mersenne Twister is not random.

## Usage

### What each file does

* analyzer.py generates random numbers and does a T-Test with them
* generator.py saves the data used in analyzer.txt to a text file

### Replicating my results

In the current state of the repository, if you clone it, when you run analyzer.py you will get the exact same numbers generated and the same exact results.

### Getting your own results

If you wish to run the program for yourself and get your own results, change the value of "seed" in analyzer.py to what you wish. If you also need the data, change it in generator.py as well.
import numpy as np
import time

start = time.time()
seed = 15212
print("The seed is {}".format(seed))
print("Saving data to text file seed{}.txt ...".format(seed))
runs = 100_000_000
arr = np.random.choice(np.array(range(0,9), dtype=np.uint8), runs)
np.savetxt("seed{}.txt".format(seed), arr, fmt='%d', newline='', header='This file contains {} numbers generated by seed {} of the Mersenne Twister. '.format(runs, seed))
print("It took {:.2f} seconds to generate and save {} pseudo-random numbers to seed{}.txt".format(time.time()-start,runs,seed))
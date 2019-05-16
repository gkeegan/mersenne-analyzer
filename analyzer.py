from scipy.stats import ttest_1samp
import numpy as np
import time

# Generate numbers
start = time.time()
seed = 15212
print("The seed is {}".format(seed))
runs = 100_000_000
arr = np.random.choice(np.array(range(0,9), dtype=np.uint8), runs)
print("It took {:.2f} seconds to generate {} random numbers using the Mersenne Twister".format(time.time()-start,runs))

# Do a T-Test
start = time.time()
mean = 4.5
t, p = ttest_1samp(arr, mean)
print("t = {}, p = {}".format(t,p))
print("It took {:.2f} seconds to do the T-Test".format(time.time()-start))
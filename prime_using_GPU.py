import cupy as cp
import matplotlib.pyplot as plt

# Define the upper limit
LIMIT = int(input("Enter the limit to compute the prime numbers ==> "))

def sieve_of_eratosthenes(limit):
    # Initialize an array of true values (all numbers are prime initially)
    is_prime = cp.ones(limit, dtype=cp.bool_)

    # 0 and 1 are not prime
    is_prime[:2] = False

    # Start from 2, the first prime number
    for num in cp.arange(2, int(cp.sqrt(limit)) + 1):
        if is_prime[num]:
            # Mark multiples of the current prime number as False (non-prime)
            is_prime[num * num:limit:num] = False

    # Return an array of prime numbers
    primes = cp.nonzero(is_prime)[0]
    return primes

# Finding primes on the GPU using CuPy
primes_gpu = sieve_of_eratosthenes(LIMIT)

# Copy primes to host memory (CPU) for plotting with Matplotlib
primes_cpu = cp.asnumpy(primes_gpu)

theta_range = primes_cpu
radius_val = primes_cpu

# Creating polar plot with dynamic figure size
fig, ax = plt.subplots(figsize=(20, 20), subplot_kw={'projection': 'polar'})

ax.plot(theta_range, radius_val, marker='.', linestyle='None')

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

limit = int(input("Enter the limit to compute the prime numbers ==> "))
nums = range(0, limit+1)

def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
          return False
    return True


primes = []
for num in tqdm(nums, desc="Finding prime numbers"):
    if is_prime(num):
        primes.append(num)

theta_range = primes
radius_val = primes

# creating polar plot with dynamic figure size
fig, ax = plt.subplots(figsize=(15, 15), subplot_kw={'projection': 'polar'})

ax.plot(theta_range, radius_val, marker='X', linestyle='None')

plt.tight_layout()
plt.show()  # display single plot
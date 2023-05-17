import time
import random

# random number generation implementation
def generate_random_numbers():
    global arr
    how_long = int(input('how long do you want the list to be: '))
    arr = [random.randint(0, 100) for _ in range(how_long)]
    print(arr)

#  the quick sort implementation
def Sort(arr):
    if len(arr) <= 1:
        return arr

    # Record the start time
    start_time = time.time()

    # Sort the array
    pivot = arr[len(arr) // 2]
    left = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]

    # Record the end time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed time:", elapsed_time, "seconds")
    
   # Recursively sort the left and right subarrays, and concatenate the results
    return Sort(left) + middle + Sort(right)

generate_random_numbers()
sorted_list = Sort(arr)
print(sorted_list)
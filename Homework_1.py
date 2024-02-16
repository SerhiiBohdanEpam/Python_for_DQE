# The first task: create list of 100 random numbers from 0 to 1000
# add library 'random'
import random

# create a blank list
random_list = []
# Traverse through all the numbers from 0 to 100
for i in range(101):
    # add the random numbers from 0 to 1000
    random_list.append(random.randint(0, 1000))
# Print the list
print(random_list)


# The second task: sort list from min to max(without using sort())
# Define a function to perform selection sort

def selection_sort(nums):
    # Traverse through all array elements starting from 0 to the second last
    for numbers in range(len(nums)):
        # Find the minimum element in remaining unsorted array
        min_index = numbers
        # Traverse the array from the next element to the end
        for j in range(numbers + 1, len(nums)):
            # If the current element is smaller than the min element, update the min_index
            if nums[j] < nums[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the 'remaining' list
        # Python allows for tuple assignment which makes swapping straightforward
        nums[numbers], nums[min_index] = nums[min_index], nums[numbers]
    # Return the sorted list
    return nums


# print the list
print(selection_sort(random_list))

# The third task: calculate average for even and odd numbers
# Create two empty lists: one to hold the even numbers and the other for odd numbers

even_numbers = []
odd_numbers = []

# Traverse through all numbers from the list
for num in random_list:
    # use operator % to determine the type of number
    if num % 2 == 0:
        # add even numbers to the even list
        even_numbers.append(num)
    else:
        # add odd numbers to the odd list
        odd_numbers.append(num)


# Define function for calculate average of a list
def average(lst):
    # calculate the average result and return it
    return sum(lst) / len(lst)


# print Average value of even numbers and odd numbers
print("Average value of even numbers: ", average(even_numbers))
print("Average value of odd numbers: ", average(odd_numbers))

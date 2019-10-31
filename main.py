import random


def quicksort_checker(numbers):
	last_num = 0
	status_switch = False
	
	for index, num in enumerate(numbers):
		if index > 0:
			if num >= last_num:
				status_switch = True
			else:
				status_switch = False
				break
			
		last_num = num
	
	return status_switch
	

def quicksort(numbers, pivot_index):
	pivot = numbers[pivot_index]
	
	original_pivot_index = pivot_index
	pivot_index = pivot_index-1
	
	while pivot_index >= 0:
		if numbers[pivot_index] >= pivot:
			numbers.insert(original_pivot_index+1, numbers.pop(pivot_index))
		elif numbers[pivot_index] < pivot:
			numbers.insert(original_pivot_index-1, numbers.pop(pivot_index))
		
		pivot_index = pivot_index-1
		
	return numbers


nums = [7, 17, 35, 40, 130, 3, 4, 21, 38, 20]

while not quicksort_checker(nums):
	piv = random.randint(1, len(nums)-1)
	nums = quicksort(nums, piv)

print(nums)

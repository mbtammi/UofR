from random import randint
#Only importing random for testing purposes.

# Let's create a list of random numbers between 1-50 and the list size is between 5-30
listSize = randint(5, 30)
listOfRandoms = [randint(1, 50) for _ in range(listSize)]

print(listOfRandoms)

# Assignment 3 part programs.

print("How many integers in the list?", len(listOfRandoms))
print("What is the max value?", max(listOfRandoms))
print("What is the min value?", min(listOfRandoms))
print("What is the range?", (max(listOfRandoms) - min(listOfRandoms)))

#Lets also do it without the max and min functions.
max_value = float('-inf')
min_value = float('inf')

# Loop to find max and min values
for num in listOfRandoms:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

# Calculate the range
value_range = max_value - min_value

# Results printed again.
print("AGAIN: What is the max value?", max_value)
print("AGAIN: What is the min value?", min_value)
print("AGAIN: What is the range?", value_range)


copyOfList = list(set(listOfRandoms))
copyOfList.sort(reverse=True)
biggestThree = copyOfList[:min(3, len(copyOfList))]
print("What are the biggest three?", biggestThree)

copyOfList = list(set(listOfRandoms))
copyOfList.sort()
smallestThree = copyOfList[:min(3, len(copyOfList))]
print("What are the smallest three?", smallestThree)

print("What is the mean of this group?", sum(listOfRandoms) / len(listOfRandoms))

sorted = sorted(listOfRandoms)
middlepoint = len(listOfRandoms) // 2

#for testing:
median_value = (sorted[middlepoint] + sorted[-middlepoint - 1]) / 2

print("What is the median?",  (sorted[middlepoint] + sorted[-middlepoint - 1]) / 2)

ocurrencies = {}
for num in listOfRandoms:
    ocurrencies[num] = ocurrencies.get(num, 0) + 1

mode_value = max(ocurrencies, key=ocurrencies.get)
print("What is the mode?", mode_value)

mean_value = sum(listOfRandoms) / len(listOfRandoms)
variance_value = sum((x - mean_value) ** 2 for x in listOfRandoms) / len(listOfRandoms)
print("What is the variance?", variance_value)

frequencies = {}
for num in listOfRandoms:
    frequencies[num] = frequencies.get(num, 0) + 1

print("\nFrequencies Table:")
for num, count in frequencies.items():
    print(f"number: {num} , {count} time(s)" )



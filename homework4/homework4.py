#--Lists--

# 3.1 List Operations

favorite_fruits = ["mango", "strawberry", "blueberry", "orange", "kiwi"]

#I encountered this error: NameError: name 'mango' is not defined
#I originally wrote: favorite_fruits = [ mango, strawberry, blueberry, orange, kiwi ]
#Without quotes, Python thought each fruit was a variable name, not text. I fixed it by putting quotes around each fruit so they are strings.

# 1. Print the second food
print(favorite_fruits[1])

#I encountered this error: SyntaxError: Missing parentheses in call to 'print'
#I originally wrote: print favorite_fruits[1] In Python 3, print is a function, so it needs parentheses.
#I fixed it by writing print(favorite_fruits[1]).


# 2. Print the last food using negative indexing
print(favorite_fruits[-1])

# 3. Add a new food to the end
favorite_fruits.append("pear")

# 4. Insert "apple" at the start
favorite_fruits.insert(0, "apple")

# 5. Remove the third item
del favorite_fruits[2]

#I encountered this error: ValueError: list.remove(x): x not in list
#I originally wrote: favorite_fruits.remove(4)
#.remove() looks for a matching VALUE, not a position, and there is no 4 in my list.cI fixed it by using del favorite_fruits[2], which removes the item at index 2 (the third item).


# 6. Print the length
print(len(favorite_fruits))

# 7. Loop through and print each food in uppercase
for fruit in favorite_fruits:
    print(fruit.upper())

#I encountered this error: TypeError: str.upper() takes no arguments (1 given)
#I originally wrote: print favorite_fruits[i].upper(i)
#In my loop, i was already the fruit itself (not an index), and .upper() doesn't take anything
#inside the parentheses. I fixed it by writing print(fruit.upper()).


# 8. New list with only the first and last food (using slicing)
new_list = favorite_fruits[:1] + favorite_fruits[-1:]
print(new_list)

#I encountered this error: NameError: name 'favorite' is not defined
#I originally wrote: new_list = [ favorite.fruits[0] , favorite.fruits[-1] ]
#I typed a period instead of an underscore, so Python looked for a variable called "favorite".
#I fixed it by spelling the name correctly as favorite_fruits (and switched to slicing as the assignment asks).


# 9. Check if "potato" is in the list
if "potato" in favorite_fruits:
    print("A potato!")
else:
    print("No potato!")


# 3.2 Slicing and Striding

numbers = list(range(21))  # 0 to 20, inclusive


def get_first_15(numbers):
    """Returns the first 15 elements of a list."""
    return numbers[:15]


def get_every_5th(lst):
    #Returns every 5th element (index 0, 5, 10, ...).
    return lst[::5]


def reverse_and_stride(lst):
    #Reverses the list, then returns every 3rd element of the reversed list.
    reversed_lst = lst[::-1]
    return reversed_lst[::3]


step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)
print(step1)
print(step2)
print(step3)


# 3.3 Nested Lists

# Named nested_numbers so it doesn't overwrite the numbers list from 3.2
nested_numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 1. Print the third row
print(nested_numbers[2])

# 2. Print the second item in the second row
print(nested_numbers[1][1])

# 3. Add [10, 11, 12] as a new row
nested_numbers.append([10, 11, 12])


# 4. Sum all numbers in a nested list
def sum_nested(lst):
    #Loops through each row, adds up every number, and returns the total.
    total = 0
    for row in lst:
        for num in row:
            total += num
    return total


print(sum_nested(nested_numbers))


# 3.4 Create a 5x5 List

def create_5x5():
    #Uses nested for loops to build a 5x5 list of numbers 1 to 25.
    grid = []
    count = 1
    for r in range(5):
        row = []
        for c in range(5):
            row.append(count)
            count += 1
        grid.append(row)
    return grid


def replace_multiples_of_3(grid):
    #Returns a new 5x5 list where every multiple of 3 is replaced with "?".
    new_grid = []
    for row in grid:
        new_row = []
        for num in row:
            if num % 3 == 0:
                new_row.append("?")
            else:
                new_row.append(num)
        new_grid.append(new_row)
    return new_grid


def sum_without_question_marks(grid):
    #Adds up every element that is not "?" and returns the sum.
    total = 0
    for row in grid:
        for item in row:
            if item != "?":
                total += item
    return total


grid_5x5 = create_5x5()
grid_with_questions = replace_multiples_of_3(grid_5x5)
grid_sum = sum_without_question_marks(grid_with_questions)
print(grid_5x5)
print(grid_with_questions)
print(grid_sum)


#--Dictionaries--

# 4.1 Dictionary Operations

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

# 1. Print Katie's age
print(ages["Katie"])

# 2. Change Mira's age to 100
ages["Mira"] = 100

# 3. Add Milana with an age of 52
ages["Milana"] = 52

# 4. Remove Mariam
del ages["Mariam"]

# 5. Print each person's name and age
for name, age in ages.items():
    print(name, age)


print("Favorite function result:", sum_nested([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) 
#File : homework1.py

# -- Variables and Data Types --
a = 10
print(a)
print(type(a))
b=1.5
print(b)
print(type(b))
c=3j
print(c)
print(type(c))
d="hello"
print(d)
print(type(d))
e=[1,2,3]
print(e)
print(type(e))
f= {"name":"Ellen" , "favorite fruit" : "strawberry"}
print(f)
print(type(f))
g = (1,2)
print(g)
print(type(g))
h = ["apple", "banana","strawberry",]
print(h)
print(type(h))
i = True
print(i)
print(type(i))
j = None
print(j)
print(type(j))
k = [True, "blue", 12]
print(k)
print(type(k))
l = str(14)
print(l)
print(type(l))
m = 1e4
print(m)
print(type(m))

#How many different data types did you find? -- 9 data types
#List the data types -- int, float, complex, str, dict, tuple, list, bool, NoneType
#What variables have the same data types? -- 1.5 and 10000.0 are both float, 'hello' and '14' are both str, [1,2,3] , ['apple, 'banana', 'strawberry' ] and ['True', 'Blue', 12] are all list
# What was the data type of l? Why is it not an integer? What does str() do? -- l was not an integer because the str() command turned it into a str(), the str() function turns any text into a str() data type
#Look up one more data type not given above. Repeat the same procedure -- set -- ex) {1,2,3}

n = {1,2,3}
print(n)
print(type(n))


# -- Booleans --
print(10 > 9) #True, 10 is greater than 9
print (10==9) #False, 10 is not equal to 9
print(10<=9) #False, 10 is not less than or equal to 9
print(bool("abc")) #True, the string has content
print(bool(123)) #True, any non zero number will return true
print(bool(["apple", "cherry", "banana"])) #True, the list is non empty
print(bool(True)) #True, the boolean returns itself
print(bool(False)) #False, the boolean returns itself
print(bool(0)) #False, a zero value returns False
print(bool("")) #False, an empty string will return Falsehw1_vscode(1)hw
print(bool(" ")) #False, an empty string will return False #wrong - will return True because a string with a space is not empty
print(bool(())) #False, an empty tuple will return false
print(bool([])) #False, an empty list will return false
print(bool(True and False)) #False, the boolean cannot be both True and False
print(bool(True and True)) #True, the boolean is able to be True and True, and will therefore return True
print(bool(False and False)) #True, the boolean is able to be False and False, and therefore return True #wrong - False and False will return False
print(bool(not(False))) #True, because the not of False is True
print(bool(not(True))) #False, because the not of True is False

#What pattern do you notice about expressions returning True or False? -- I notice that each line is essentially a yes or no question, and Python answers it by using True or False
#Which expression surprised you about its result? -- I was surprised by print(bool(" ")) being True, as my understanding was that a space did not cont as a string
#Create an expression, not given above, that will return True. Why is it True? -- print(bool((10+5)==15)) -- This will be True because python evaluates 10 + 5 first to get 15, and then compares 15 to 15, which is equivalent.
#Create an expression, not given above, that will return False. Why is it False? -- print(bool(None) -- will return False because None represents nothing in python


# -- Operators --
# -- Arithmetic Operators --
print(10 + 5) #15, + performs addition
print(10 - 5) #5, - performs subtraction
print(2 * 4) #8, * performs multiplication
print(6 / 3) #2, / performs division
print(5 % 2) #1, % provides the remainder
print(3 ** 2) #9, ** performs exponentiation
print(15 // 2) #7, // is floor divison, aka will round down
# -- Comparison Operators --
print (5 == 2) #False, == compares the two values and decides they are not equal
print(10 != 10) #False, != claims the two values are dissimilar, however 10 is equal to 10
print(2 < 5) #True, < checks to see if 5 is greater than 2, and determines that it is
print(12 > 5) #True, > checks to see if 12 is greater than 5, and determines that it is
print(5 <= 6) #True, <= checks to see if 5 is less than or equal to 6, and determines that it is
print(1 >= 10) #False, >= checks to see if 1 is greater than or equal to 10, and determines that it is not
# -- Assignments Operators --
x = 5 
x += 5 #adds 5 to x, x = 10
x -= 4 # subracts 4 from x, x = 6
x *= 3 #multiplies x by 3, x = 18
#the final value of x is 18

# -- Logical Operators --
#What does the operator and do? -- Combines 2 booleans and only returns True if BOTH booleans return True
#Write an expression that results in True. -- (10 + 5 == 15) and (12 + 3 == 15)
#Write an expression that results in False. -- bool(" ") and bool(0)
#What does the operator or do? Combines 2 booleans and returns True if Either boolean returns True
#Write an expression that results in True. -- bool(True) or bool(False) 
#Write an expression that results in False. -- (2 <= 1) or bool({})
#What does the operator not do? -- Reverses the result of a boolean. So if something would otherwise return True, it returns False, and vice versa
#Write an expression that results in True. -- bool(not False)
#Write an expression that results in False -- bool(not(4 + 5 == 9))

# -- More Questions --
#What is the difference between / and //? -- / is division, // is floor division, meaning it rounds down to the nearest integer
#What is the difference between % and //? -- % calculates the remainder (so 7%2 = 1), (7//2 = 3)
#What operator would you use to calculate the remainder when dividing two numbers? Give an example.? the % operator. ex) 7%2=1
#How do assignment operators work? -- It shorthands an operation with = into one step

# -- Strings --
my_string = "hello"
print(my_string) #prints: hello
print(my_string[0]) #prints: h
print(my_string[1]) #prints: e
print(my_string[2]) #prints: l
print(my_string[3]) #prints: l
print(my_string[4]) #prints: o
print(my_string[-1]) #prints: o
print(my_string[1:3]) #prints: el
print(my_string[0:5:2]) #prints: hlo
print(len(my_string)) #prints: 5
print(my_string + "goodbye") #prints: hellogoodbye
print(7 * (my_string)) #prints: hellohellohellohellohellohellohello

#Define the term slicing. For which of the manipulations did you slice your string? -- slicing is using indexing to take certain portions of a string. I used slicing for print(my_string[1:3]) and print(my_string[0:5:2]) 
# Call the following, describe the result:

name = "Oski"
print("Hello, my name is", name)
#prints: Hello, my name is Oski
# Call the following, describe the result.
name = "Oski"
print(f"Hello, my name is {name}")
#prints: Hello, my name is Oski
# What is the difference between the two last print statements? -- the second is an f string, where a variable can be swapped in for the actual value.


# -- Terminal Commands  --
#cd
#Changes directories. Use it to move from one folder to another
#Example: cd Desktop
#ls
#Lists the files and folders within current directory
#Example: ls
#ls -a
#List all, similar to ls, but shows hidden files as well
#Example: ls -a
#mkdir
#Makes a directory, use it to create a new folder
#Example: mkdir folder_1
#Cat
#Displays the contents of the file
#Example: cat file_1
#pwd
#prints the directory, or full path
#Example: pwd
#cd ..
#Moves up one level in the directory into the parent folder
#Example: cd ..
#cd .
#Remains in the current directory
#Example: cd . 
#cd ~
#goes to the home directory
#Example: cd ~
#cp
#copies a file from one location to another
#Example: cp file.1
#mv
#moves a file to a new location
#Example: mv file.1
#rm
# permanently deletes a file
#Example: rm badfile
#clear
#Clears all current text
#Example: Clear
#grep
#searches for a specific word or pattern
#Example: grep "hi" file.1

#Look up 3 other commands not present. Define and explain how to use them on the command line. -- 1) touch: creates a new file ex) touch file.2     2)history: shows a list of prior run commands   ex) history     3) wc: gives a word count      ex) wc file.1
#What is the difference between ls and ls -a? - ls -a will show all files, including hidden ones. 
# What is a hidden file? -- A hidden file is one that begins with a dot. It is unique in that it will only show up if you ask for it
#Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to use them on the command line. 1) -h: makes a file readable by a human, so will show file sizes in KB/MB/GB EX)ls-lh   2) -v: prints what the command is doing as it runs it  EX) cp -v file.1     3)-r: for rm, allows you to delete a folder and everything inside of it.    EX) rm -r bad_folder
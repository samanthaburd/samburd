#--2: Homework 1 + 2 Review--
# Git vs GitHub
# git is a tool, which runs on your computer, that tracks changes to files
#GitHub is a website that hosts git repositories so that you can back them up online, save them, and share with others

#Terminal vs Command Line
#Terminal is this, aka the window you type into
# The command line is the actual line itself where you type commands

#Remote vs Local Repository
#A local repository is stored on your own, local computer
#A remote repository is a copy stored on a server, like GitHub

#Version Control
#The system that records the changes to files over time so you can see history and work with others

#Staging area
# An area where you can input changes to put in your next commit

#Git add
# Adds changes from working directory to the staging area

#Git Commit
# commits everything in the staging area to your local repository

#Git push
#Uploads local commits to the remote repository

#Git status
#Tells you which files have been modified and overall status of git

#Git pull
#Downloads the changes from the remote repository to your local copy

#pwd
#prints your working directory, or the full path of the folder you're in

#ls
#lists files and folders in current directory

#cd
#"Change directory." Moves you into another folder

#nano
#Opens a simple text editor inside the terminal for editing a file.

#touch
#Creates a new, empty file (or updates the timestamp of an existing one).

#mv
#Moves a file/folder to a new location, or renames it.

#rm
#Removes (deletes) a file. It does not go to the trash, so it's permanent.

# cat
#Prints the contents of a file to the terminal.

# ---------- 2.2 A Directory Tree ----------

# Q1: pwd

# Q2: ls

# Q3: cd ../brianna_repo
#     git pull

# Q4: mv homework.py ../judy_decal/homework/
#     (doing this from inside brianna_repo)

# Q5: cd ../judy_decal/homework

# Q6: cat homework.py

# Q7: git add .
#     git commit -m "done with hw"
#     git push origin main
#     (have to be in the judy_decal repo for this)

# Q8: the error means there's stuff on github that judy doesn't have on her
#     computer yet, like she changed something on github or pushed from
#     somewhere else. she tried to push without pulling first so git
#     rejected it bc it would overwrite those changes.
#     fix:
#     git pull origin main
#     git push origin main
#     (might have to fix merge conflicts after pulling if there are any)

# Q9: cd ~/Recent

#2.3 entered into folder

#-- Homework 3 Review --
# ---------- 3.1 Data Types ----------

def checkDataType(x):
    return type(x).__name__


# ---------- 3.2 Conditionals ----------

def evenOrOdd(n):
    if n % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

# ---------- 4 Loops ----------

def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


# ---------- 5.1 Lists ----------

def duplicateList(lst):
    new_list = []
    for item in lst:
        new_list.append(item)
        new_list.append(item)
    return new_list


# ---------- 5.2 Debugging ----------

# the error: missing a colon after def square(num), and the return
# line wasn't indented so it's not inside the function

def square(num):
    return num * num


def evenOrOdd(n):
    if n % 2 == 0:
        print ('Even')
    else:
        print ('Odd')

evenOrOdd(5)
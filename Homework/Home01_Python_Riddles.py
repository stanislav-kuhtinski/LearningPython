__author__ = 'stanislav-kuhtinski'
print("Hi, I will aks you some riddles about the Python.")
print("You have 3 attempts to answer the question")
print("Let\'s begin!\n")

count = 0
limit = 3
# First question
question = input("In Python, what is one function to output content to the console? ")
if question == "Print()" or question == "print()":
    count += 1

# Second question
question = input("What symbol can you use to comment out one line of code? ")
if question == "#":
    count += 1

# Third question
question = input("How do you create a variable “a” that is equal to 2? ")
if question == "a=2" or question == "a = 2":
    count += 1

print("Thank you, you have aswered {} questions. {} correct answers" .format(limit, count))
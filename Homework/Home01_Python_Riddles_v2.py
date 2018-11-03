__author__ = 'stanislav-kuhtinski'

print("Hi, I will aks you some riddles about the Python.")
print("You may skip the question by hitting the Enter")
print("Let\'s begin!\n")
# this is dict
quiz_dictionary = {'In Python, what is one function to output content to the console? ': 'print()',  # First question
                   'What symbol can you use to comment out one line of code? ': '#',  # Second question
                   'How do you create a variable “a” that is equal to 2? ': 'a = 2',  # Third question
                   }
# this is list counter[0] - quiz length, counter[1] - answers, counter[2] - correct answers
counter = [0, 0, 0]
counter[0] = len(quiz_dictionary)

for question in quiz_dictionary.keys():
    answer = input(question)
    if answer.lower() == quiz_dictionary.get(question):
        print('Correct answer!')
        counter[1] += 1
        counter[2] += 1
    elif not answer.lower():
        print('You skipped the question')
    else:
        print('The answer is incorrect!')
        counter[1] += 1

print("Thank you! We had {} questions. You have answered {} questions. {} correct answers".format(counter[0], counter[1], counter[2]))

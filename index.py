import os

import time
import openai

openai.api_key = "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"

models = ["code-cushman-001", "code-davinci-002"]  

def multiplinput():
    print("Please enter your code, and press Ctrl + Z or Command + Z and press enter once you are done")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    code = '\n'.join(contents)
    return code

def fixCode(purpose, attempt, model, code = ""):
    response = openai.Completion.create(
        model= models[model],
        prompt= code + purpose,
        temperature= 0,
        max_tokens=2000,
        top_p=0.1,
        frequency_penalty=1,
        presence_penalty=1
    )

    x = response['choices'][0]['text']
    print(x)



# fixCode("make a list of 5 strings in python that say 'dogs', 'cats', 'horse', 'rabbit', 'space', and the variable's name should be 'listing'", 0)

def fix(purpose, models):
    satisfactory = False
    attempts = 0
    code = multiplinput()
    while satisfactory == False:
        fixCode('"Fix this code in python"', attempts, models, code)
        satisfactorychoice = print("That was the code! Was the code satisfactory? (y/N)")
        
        if satisfactorychoice == "y":
            satisfactory = True
        else:
            retrychoice = input("Sorry to hear that. Want to try again? (y/N)")
            if retrychoice == "y":
                continue
    print("Have a nice day!")
    
                




def prototype(purpose, models):
    attempts = 0
    while(True):
        fixCode(purpose, attempts, models)
        if input("Do you think the code is too wordy, or do you want to regenerate the code in general? (y/N)") ==  "y":
            attempts += 1
        else:
            break
    print("Thank you for trying the code out!")
    
    

def optimize(purpose, models):
    satisfactory = False
    attempts = 0
    code = multiplinput()
    while satisfactory == False:
        fixCode('"Optimize this code"', attempts, models, code)
        satisfactorychoice = print("That was the code! Was the code satisfactory? (y/N)")
        if satisfactorychoice == "y":
            satisfactory = True
        else:
            retrychoice = input("Sorry to hear that. Want to try again? (y/N)")
            if retrychoice == "y":
                continue
    print("Have a nice day!")


def main():
    print("Hello! Welcome to Codetween, a program meant to ")
    print("Do you want the code to generate fast but be less accurate, or generate slowly but be more accurate? (input 0 for fast, 1 for slow)")
    models = input()
    models = int(models)
    print("To begin, enter your code, and the purpose of this said code. Tip: explain to the AI as if it is 5, and make sure you define what language.")
    purpose = input("Purpose = ")
    whatwant = input("Enter 1 to fix your code\nenter 2 to prototype\nenter 3 to optimize")
    if whatwant == "1":
        print("please wait....")
        fix(purpose, models)
    elif whatwant == "2":
        print("please wait....")
        prototype(purpose, models)
    elif whatwant == "3":
        print("please wait....")
        optimize(purpose, models)
    else:
        print("that's not a valid number")
    


main()



    








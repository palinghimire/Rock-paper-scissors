# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=('yes','no')):
    #this make it so it stores error as a message to use later
    error = f"please enter a valid options from the following list :{valid_ans}"

    while True:
        #gets user response abd make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            #check if user response is a word in the list
            if item == user_response:
                return item
            #check if the user response is the same as 
            #the first letter of an item in the list
            elif user_response == item[0]:
                return item

        #prints error if the user dose not enter somthing that is valid
        print(error)
        print()


def instructions():
    """prints instructions"""

    print("""
*** instructions ***
      
to begin choose a numer of rounds to play or you can play infinite mode).
          
then play against the computer. you need to chose eather R (rock) P (paper) S (sissors) 
 
rules are as follows 
          
          paper beats rock 

          Rock beats scissors

          scissors beat paper

good luck
    """)

#main routine

print()
print("rock / paper / scissors game")
print()


#ask user if they need help
#shows them if requested
help = string_checker("do you want help? ")

#display the if the user want to see instructions
if help == "yes":
    instructions()

print()
print("program continues")
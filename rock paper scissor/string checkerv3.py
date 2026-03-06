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

# main routine goes here 

yes_no = ["yes", "no"]
rps_list = ["rock", "paper", "scissors,", "xxx"]



want_instructions = string_checker("do you want to see the instructions?",)

print("you chose: ", want_instructions)

user_choice = string_checker ("choose: ", rps_list)
print("you chose: ", user_choice)
def int_checker(question):
    """integer_checker to see if your equal to or more than 13 """

    while True:
        error = "please enter a numer that is 1 or more:"

        to_check = input(question)

        # check for infinte mode
        if to_check == "":
            return "infinite"


        try:
            response = int(to_check)
            # checks if the number is more than / equal to 1

            if response < 1:
                print(error)

            else:
                return response
        
        except ValueError:
                print(error)

# main routine starts here

#intialis game veriables 
mode = "regular"


print("rock / paper / scissor game")
print()
#Instructions 

#ask user for number of rounds/ infinite mode
num_round = int_checker("how many rounds would you like? push <enter> for infinite mode: ")

#game loop starts here


#game loop ends here

#game history / statistics area
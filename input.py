
def user_choice():
    
    # This original choice value can be anything that isn't an integer
    choice = 'wrong'
    
    # While the choice is not a digit, keep asking for input.
    while choice.isdigit() == False:
        
        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Choose a number: ")
        
        if choice.isdigit() == False:
            # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
            #clear_output()
            
            print("Sorry, but you did not enter an integer. Please try again.")
            
    
    # Optionally you can clear everything after running the function
    #clear_output()
    
    # We can convert once the while loop above has confirmed we have a digit.
    print(choice)
    return int(choice)

user_choice()
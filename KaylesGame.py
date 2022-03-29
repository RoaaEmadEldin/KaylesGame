# Cairo University -FCAI - Programming 1 - 2022
# Program Name: Kayles Game
# Program Description: A program for Kayles Game by Python.
# Last Modification Date: 11/3/2022
# Author: Roaa Emad Eldin Muhammad


# Allow the User to Choose the Length of the Game List
Kayles = []
list_length = int(input("Please Enter the Length of the List You Want (Divisible by 10):"))
for i in range(1, list_length + 1):
    Kayles.append(i % 10)
empty_list = ['-' for i in range(len(Kayles))]
print("Choose Your Numbers from this List:", Kayles)
print(f"You Can Choose From 1 : {len(Kayles)}.\n"
      "The First Group of Numbers is from 1:10, the Second is from 11:20, etc..")
player = 1
for i in range(0, len(Kayles)):   # To loop len(Kayles) times ---> from 0 to (len(Kayles) - 1)
    num = int(input(f"Please Player {player}, Enter the Numbers of Tokens to Remove:"))
    # To Check Whether the Numbers of Tokens Valid or Not and Decide the State of the Game.
    if num == 1:
        n1 = int(input(f"Player {player}, Enter Your Number:"))
        # To Check if the Number Entered is Greater than the Greatest Number in the List
        if n1 > len(Kayles):
            print(f"Number Doesn't Exist in the List!, Choose From 1 : {len(Kayles)}")
            continue  # Ends Current if Loops and Continues (Returns) to the for loop.
        # To Check Whether the Number Have Been Taken Before or Not.
        elif Kayles[n1 - 1] == '-':
            print("Please Enter a Number which Hasn't Taken Before!")
            continue
        else:   # The Number Does Exist in the List and Haven't Been Taken Before
            del Kayles[n1 - 1]
            Kayles.insert(n1 - 1, '-')
            print(*Kayles)
            if Kayles == empty_list:  # Check the Winner
                print(f"PLAYER {player} WINS!!")
                exit()
    elif num == 2:
        while True:  # while True --> Allows the Users to Re-enter their Numbers If an Error Messages Appeared to Them.
            print("** Please Enter Two Adjacent Numbers **")
            n1 = int(input(f"Player {player}, Enter Your First Number:"))
            n2 = int(input(f"Player {player}, Enter Your Second Number:"))
            # To Check if the Numbers Entered are Greater than the Greatest Number in the List
            if n1 > len(Kayles) or n2 > len(Kayles):
                print(f"Number Doesn't Exist in the List!, Choose From 1 : {len(Kayles)}")
                continue  # End the Current if Loop and Continues to the while True loop to Re-enter the Inputs.
            if n1 - n2 == 1 or n2 - n1 == 1:  # Checks If the Two Entered Numbers are Adjacent
                break
            else:
                print("Please Enter Two Adjacent Numbers!")
        # To Check Whether the Numbers Have Been Taken Before or Not.
        if Kayles[n1 - 1] == '-' or Kayles[n2 - 1] == '-':
            print("Please Enter a Number which Hasn't Taken Before!")
            continue
        else:    # The Numbers Do Exist in the List and Haven't Been Taken Before
            del Kayles[n1 - 1]
            Kayles.insert(n1 - 1, '-')
            del Kayles[n2 - 1]
            Kayles.insert(n2 - 1, '-')
            print(*Kayles)
            if Kayles == empty_list:   # Check the Winner
                print(f"PLAYER {player} WINS!!")
                exit()
    else:
        print("Invalid Numbers, Please Enter 1 or 2:")
        continue
    # Reverse the Player Turns
    if player == 1:
        player = 2
    else:
        player = 1

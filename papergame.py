import random
print("First letter of the input must be capital and remaining must be small")
user1_choice=input("enter the choice")
game_choice_inputs=["Rock","Paper","Scissor"]
user2_choice=random.choice(game_choice_inputs)
print(f"\n user1 input {user1_choice} user2 input {user2_choice}")
if(user1_choice==user2_choice):
    print("your both choices are same,it is a draw")
elif(user1_choice=="Rock"):
    if(user2_choice=="Scissor"):
        print("Rock wins")
    else:
        print("Paper wins")
elif(user1_choice=="Scissor"):
    if(user2_choice=="Rock"):
        print("Rock wins")
    else:
        print("Scissor wins")
elif(user1_choice=="Paper"):
    if(user2_choice=="Rock"):
        print("Paper wins")
    else:
        print("Scissor wins")
    

    


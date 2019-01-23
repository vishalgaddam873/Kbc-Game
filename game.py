import json
import os

ans_key = ['','D','C','B','C','A','D','D','A','A','B']
options = ['A','B','C','D']
money = [0,3000,5000,10000,20000,80000,120000,500000,1200000,5000000]

def user_choice():
     player_choice = input("Enter your Choice: ")
     return player_choice

def check_answer(qes_count,player_choice):
    if qes_count == 1 and player_choice == ans_key[qes_count]:
        return("You Won " + str(money[qes_count]))
    elif qes_count == 2 and player_choice == ans_key[qes_count]:
        return("You Won " + str(money[qes_count]))
    elif qes_count == 3 and player_choice == ans_key[qes_count]:
        print("You Crossed  First Level of the Game")
        return("You Won " + str(money[qes_count]))
    elif qes_count == 4 and player_choice == ans_key[qes_count]:
        return("You Won " + str(money[qes_count]))
    elif qes_count == 5 and player_choice == ans_key[qes_count]:
        return("You Won " + str(money[qes_count]))
    elif qes_count == 6 and player_choice == ans_key[qes_count]:
        print("You Crossed Second Level of the Game")
        return("You Won " + str(money[qes_count]))
    elif qes_count == 7 and player_choice == ans_key[qes_count]:
        return("You Won " + str(money[qes_count]))
    elif qes_count == 8 and player_choice == ans_key[qes_count]:
        return("You Won " + str(money[qes_count]))
    elif qes_count == 9 and player_choice == ans_key[qes_count]:
        return("You Won " + str(money[qes_count]))
    elif qes_count == 10 and player_choice == ans_key[qes_count]:
        return("You Won 1 Crore rupeess")


def play_game():
    qes_count = 0
    counter = 0
    with open('questions.json') as content:
        questions = json.load(content)
        while counter <  len(questions['data']):
            print(questions['data'][counter]['question'])
            print(questions['data'][counter]['answer'])
            print("")
            player_choice = user_choice().upper()
          
            if 'QUIT' in player_choice:
                print("Thanks For Playing Nicely! You Won "+ str(money[counter])  + " Rupess")
                break
            if 'A' in player_choice or 'B' in player_choice or 'C' in player_choice or 'D' in player_choice:
                qes_count+=1
                ans = check_answer(qes_count,player_choice)
                if ans:
                    print(ans)
                else:
                    print("")
                    print("Sadley! Your answer is Wrong")
                    print("Thanks For Playing Nicely! You Won "+ str(money[qes_count-1])  + " Rupess")
                    break
                print("")
                counter +=1
            else:
                os.system('clear')
                print("Enter Valid options! You have options like A or B or C or D :)")
                print("")
                counter = counter
play_game()
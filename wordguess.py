
import random
# create word sequences with dictionaries 
D1=dict(crawled=' crawl ',stimulate=' stimulation ',difficult=' difficulty ',answer=' answer ',derive=' get ',phone=' mobile phone ',game=' games '
        ,hello=' hello ',economic=' economics ',protocol=' etiquette ')
D2=dict( crawl ='crawled', stimulation ='stimulate', difficulty ='difficult', answer ='answer', get ='derive', mobile phone ='phone', games ='game'
        , hello ='hello', economics ='economic', etiquette ='protocol')
# start the game
print(
"""
             welcome to the word guessing game. 
    guess the words according to the chinese, or guess the chinese meaning according to the words. .
"""
)
x='y'
while x=='y' or x=='Y':
    print(" there are two rules in this game ：\n")
    print("1: guess words according to chinese \n")
    print("2: guess chinese according to the words \n")
    print(" please enter your choice ：")
    a=int(input())
    if a==1 :
        iscontinue="y"
        while iscontinue=="y" or iscontinue=="Y":
            
            word=random.choice(list(D1.values()))
            print(" randomly generated in chinese means :", word)

            guess = input("\n please guess the words that satisfy the chinese meaning. : ")
            while guess != D2[word] and guess != "":
                print(" sorry, it's not correct. ")
                guess = input(" keep guessing. : ")
           
            if guess == D2[word]:
                print(" that's great. you guessed right. !\n")
            iscontinue=input("\n\n whether to continue or not （Y/N)：")
    elif a==2 :
        iscontinue="y"
        while iscontinue=="y" or iscontinue=="Y":    
            word=random.choice(list(D1.keys()))
            print(" randomly generate words as :", word)

            guess = input("\n please guess the chinese meaning of a given word. : ")
            while guess != D1[word] and guess != "":
                print(" sorry, it's not correct. ")
                guess = input(" keep guessing. : ")
           
            if guess == D1[word]:
                print(" that's great. you guessed right. !\n")
            iscontinue=input("\n\n whether to continue or not （Y/N)：")
    else:
        x=input(" do you want to re-enter if the input is illegal? （Y/N)：")

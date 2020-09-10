#Importing Needed Modules
from random import choice 
from sys import exit
from time import sleep
############################
def magic8ball(answers) :
    '''Game Fucnction'''
    print("Ask Me A Yes-No Question")
    question=str(input("question>> "))
    if question=="" :
        print("Exiting....")
        sleep(2)
        exit()
    else :
        print(choice(answers))
        print("I Hope That Helped!")
        replay()
############################
def replay() :
    '''Function To Ask User If He-She Would To Olay Again?'''
    print("Do You Have Another Question? [Y/N]")
    Ans=str(input("ans>> "))
    if Ans=="Y" or Ans=="y" :
        magic8ball(answers)
    elif Ans=="N" or Ans=="n" :
        print("Exiting....")
        sleep(2)
        exit()
    else :
        print("Not Found.Please Reply With Y/N")
        replay()
###$########################
def main() :
    ''' Main Function '''
    
    print("Hello,I Am The Magic 8 Ball.What's Your Name? ")
    name=str(input("name>> "))
    print("Hi ",name)
    magic8ball(answers)
##########################  
answers=["It Is Certain","Without A Doubt","Yes,definetly","it is decidedly so.","Without a doubt."," Yes – definitely.","You may rely on it.","As I see it, yes","Most likely.","Outlook good","Yes","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good","Very doubtfu"]
main()
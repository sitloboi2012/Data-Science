#Problem 703A Codeforce
#Description: 
#Rules of the game are very simple: at first number of rounds n is defined. In every round each of the players throws a cubical dice with distinct numbers from 1 to 6 written on its faces. Player, whose value after throwing the dice is greater, wins the round. In case if player dice values are equal, no one of them is a winner.

#In average, player, who won most of the rounds, is the winner of the game. In case if two players won the same number of rounds, the result of the game is draw.

#Mishka is still very little and can't count wins and losses, so she asked you to watch their game and determine its result. Please help her!

n = int(input())

mishka = 0
chris = 0

for i in range(n):
    m , c = map(int,input().split())
    if m > c :
        mishka += 1
    elif c > m:
        chris += 1
    else:
        pass


if mishka > chris:
    print("Mishka")
elif chris > mishka:
    print("Chris")
elif mishka == chris:
    print("Friendship is magic!^^")
else:
    pass



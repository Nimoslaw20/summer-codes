from random import randint

##def gen():
##      x = randint(3, 6)
##      for  i in range(10):
##            print(x)
##            gen()
##
##      
##gen()
      
def game():
      num = randint(1,10)
      guess = eval(input('Enter your guess: '))
      score = 0
      if guess==num:
            print('You got it!')
            score += 1
      else:
            print('Sorry. The number is ', num)
      print('Your score is: ', score)
      game()

game()

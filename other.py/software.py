#intro to softwar design

#goal: print a list of words delimeted by commas

#solution1:
#list_of_words = ["hello", "yes", "goodbye", "last"]
#print(list_of_words[0] + "," +list_of_words[1] + "," + list_of_words[2] + "," + list_of_words[3]) 
#^too long and hard to edit

#solution 2:
#list_of_words = ["hello", "yes", "goodbye", "last"]
#to_print = ""

#for i in range(4):
 # to_print += list_of_words[i]
  #if i != 3:
   # to_print += ","

#print(to_print)
#better to change "," but we hardcoded "4", the fix:

#list_of_words = ["hello", "yes", "goodbye", "last"]
#to_print = ""

#for i in range(len(list_of_words)):
 # to_print += list_of_words[i]
  #if i != len(list_of_words) -1:
   # to_print += ","

#print(to_print)

#solution 3:
#list_of_words = ["hello", "yes", "goodbye", "last"]
#print(",".join(list_of_words))

#Best Solution:
#delimeter = "," 
#list_of_words = ["hello", "yes", "goodbye", "last"]
#print(delimeter.join(list_of_words))

#example 2, number guessing game
#guess = 1

#while True:
 # num = input("please guess the number (between 0-100): ")
  #try:
   # num = int(num)
  #except:
   # print("invalid number, please guess again.")
    #continue 

  #if num < 45:
   # print("your guess was under")
  #elif num > 45:
   # print("your guess was over")
  #else:
   # break

  #guess += 1
#print(f"you guessed it in {guess} guesses")
#^45 is hardcoded so it can easily break code

#import numbers
#from tkinter.tix import MAX


class GuessNumber:
  def _init_(self, numbers, min=0, max=100):
    self.number = numbers
    self.guesses = 0
    self.min = min
    self.max = max
  def get_guess(self):
    guess = input(f"please guess a number ({self.min} - {self.max}): ")

    if self.valid_number(guess):
      return int(guess)
    else:
      print("please enter a valid number. ")
      return self.get_guess()

  def valid_number(self, str_number):
    try:
      number = int(str_number)
    except:
      return False

    return self.min <= number <= self.max

  def play(self):
    while True:
      self.guess += 1

      guess = self.get_guess()

      if guess < self.number:
        print("your guess was under. ")
      elif guess > self.number:
        print("your guess was over. ")
      else: #they guessed it
        break
    print(f"you guessed it in {self.guesses} guesses. ")

game = GuessNumber(56,0,100)
game.play()

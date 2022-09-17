# lets build a robot barista!
print("\n\nhello, wellcom to network coffes shop")

#print(input("What is your name?"))
name = input("What is your name?\n")
#a variable is a method of storing data for reuse

if name == "Ben" or name == "carmella":
  answer = input("are you evil?\n")
  if answer == "yes":
    print("you're not welcome here Evil " + name + "!! Get out!!\n\n")
    exit()
  else:
    print("hello " + name  + " , thank you so much for coming in today")
elif name == "loki":
  print("you're not welcome here Evil " + name + "!! Get out!!\n\n")
  exit()
else:
  print("hello " + name  + " , thank you so much for coming in today")

#if 2 > 3:
  #print("it is true")
#else:
  #print("not true")

#price = 8

menu = "black coffee, expresso, latte, Frapp, and cappucino"
print(name + ", What would you like from our menu today? Here is what we are serving.\n\n"
+ menu)

order = input()


if order == "Frapp":
  price = 13
elif order == "Black coffee":
  price = 3
elif order == "expresso":
  price = 5
elif order == "latte":
  cream = input("do you want wipped cream?\n")
  if cream == "yes":
    price = 11
  else:
    price = 9
elif order == "camppucino":
  price = 10
else:
  print("sorry, we dont have that here.")
  price = 0
  exit()

quantity = input("how many coffees would you like?\n")

total = price * int(quantity)
#need to define ^as int because the imput was a string originally
#it will print 8 "10"s if you dont
print("thank you. Your total is: $" + str(total))

if quantity == "1":
  print("sounds good " + name + " , we'll have your " + str(quantity) + " " + order + " ready for you in a moment.\n\n")

else:
  print("sounds good " + name + " , we'll have your " + str(quantity) + " " + order + "s ready for you in a moment.\n\n")





#food = input("What would you like to eat today\n")
#print("ok " + name + " I will get you " + food + " in just a moment\n")



#name = "Enrique"
#^ a word with nothing on it is a variable

#print(name)

#name = "iron man"

#print(name)
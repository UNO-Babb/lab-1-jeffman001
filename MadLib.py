#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
object1 = input ("enter an object:  ")
problem1 = input ("enter a Problem: ")
verb1 = input ("enter a Verb: ")
person1 = input ("enter a person: ")
place1 = input ("enter a Place: ")
name1 = input ("enter your Name: ")
reward1 = input ("enter a Reward: ")
reward2 = input ("enter another Reward: ")
  #Print the story with the user supplied words.
print(name1 + " had set out on a quest")
print("the destination was set, " + place1 + ",")
print("of course this was no ordinary trip. " + name1 + " had heard of " + place1 + "'s " + problem1 + " problem")
print("to deal with it they first needed " + person1 + "'s help")
print("strangely, " +person1+ " didn't want " + reward1 + " or " + reward2 + ", intead they requested a " + object1 + ".")
print ("but once " + name1 + " got " + person1 + "'s help,")
print (" the " + problem1 + " were sure to be dealt with.")

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()

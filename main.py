def story1():
  print("chose story 1")
  name = input("What is your name? ")
  fruit = input ("What is your favorite fruit? ")
  store = input("Name a store:")
  enemy = input("Name an enemy:")
  print("My name is (%s). I was in the mood for some (%s). So I went to (%s) to get (%s). But (%s) got the last of (%s) so I was furious."%(name, fruit, store, fruit, enemy, fruit))
def story2():
  print("chose story 2")
  num = input("How many siblings do you have? ")
  child = input("Are you an only, middle, oldest, or younger child? ")
  eyes = input("What color are your eyes? ")
  height = input("How tall are you? ")
  print("I have (%s) siblings. I am a (%s) child. I have (%s) colored eyes. I am (%s) feet tall."%(num, child, eyes, height))
def randomStory():
  print("chose random")
  sport = input("What is your favorite sport? ")
  team = input("What is your favorite sports team? ")
  state = input("What state is the team from? ")
  visit = input("How many times have you gone to their stadium? ")
  print("My favorite sport is (%s). My favorite team is (%s). They are from (%s) state. I have gone to their stadium (%s) times."%(sport, team, state, visit))
def storyPicker(storyChoice):
  if storyChoice == "1":
    story1()
  elif storyChoice == "2":
    story2()
  elif (storyChoice == "r") or (storyChoice == "R"):
    randomStory()
  
def main():
  print("Welcome to MadLibz!\n Choose your story:")
  storyChoice = input("Enter 1, 2, or (R)andom: ")
  storyPicker(storyChoice)

if __name__ == "__main__":
    main()

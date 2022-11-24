# Jxcob-Vfx 2022

# SAM - Machine Learning Chatbot

# import data libraries and external dictionary files
import chat, os, time, sys, accounts
from chat import chat
from accounts import accounts

times = 0

# set account booleans
LOGGED_IN = False
CURRENT_ACCOUNT = None

# simple subroutine to print text stylistically
def typewriter(str1):
  for x in str1:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(0.05)

# simple subroutine to print bold text
def bold(text):
  print(f"\033[1m{text}\033[0m")

# "about" section for end user utilizing \typewriter()\ function
def about():
  os.system("clear")
  typewriter("\033[1mAbout SAM\033[0m\n\n")
  typewriter("SAM stands for Social and Algorithmic Machine Learning.\n\n")
  typewriter("SAM functions as a chatbot and uses user-oriented learning to identify unknown\nuser inputs and store data on how it should respond.\n\n")
  typewriter("More information at github.com/Jxcob-Vfx/sam\n\n")
  typewriter("Press enter to continue "); input(""); main()

# simulated AI training tutorial for end user introduction to the software
def tutorial():
  os.system("clear")
  typewriter("Hi, I'm SAM!\n\n")
  typewriter("I'm a machine learning social algorithm, or chatbot.\n\n")
  typewriter("Let's try having a conversation!\n\n")
  input("Press enter to continue ")
  os.system("clear")
  bold("Mission: Say hello"); print()
  typewriter("This is your input field. It's where you can communicate with me.\n\n")
  typewriter("Type 'hello' into the input field - capitalization doesn't matter.\n\n")
  tut1 = str(input("> ")); print()
  passed = 0
  while passed == 0:
    if tut1.lower() == str("hello"):
      passed += 1
    else:
      typewriter("Not quite. Type 'hello' into the input field.\n\n")
      tut1 = str(input("> ")); print()
  os.system("clear")
  bold("Mission Passed"); print()
  typewriter("Good job! Now I can respond.\n\n")
  typewriter("Hi! How are you today?\n\n")
  input("Press enter to continue ")
  os.system("clear")
  bold("Mission: Train SAM"); print()
  typewriter("Sometimes I don't how to respond to you.\n\n")
  typewriter("I asked you 'how are you today?'\n\n")
  typewriter("Respond to that question in the input field.\n\n")
  tut2 = str(input("> ")); print()
  typewriter("I dont' know how to respond to that. What should I say?\n\n")
  whatToSay = str(input("> "))
  os.system("clear")
  bold("Mission: Train SAM"); print()
  typewriter("Now type what you typed earlier.\n\n")
  typewriter("How are you today?\n\n")
  typewriter(f"Hint: You typed '{tut2}'\n\n")
  passed1 = 0
  while passed1 == 0:
    tut3 = str(input("> ")); print()
    if tut3 == tut2:
      passed1 += 1
      typewriter(f"{whatToSay}\n\n")
      typewriter("Good job! You just successfully trained my AI!\n\n")
      input("Press enter to continue ")
      os.system("clear")
      bold("Tutorial Passed!"); print()
      input("Press enter to continue ")
      main()
    else:
      typewriter("Not quite. Type what you typed earlier into the input field.\n\n")

# main chatbot function
# chatbot copyright Jxcob-Vfx (c) 2022-2023
def __init__():
  global times
  global CURRENT_ACCOUNT
  userInput = str(input("> ")); print()
  exit = ["exit", "Exit", "e", "E"]
  if userInput in exit:
    main()
  else:
    try:
      if times < 2:
        print(chat[f"{userInput.lower()}"]); print()
        times += 1
        __init__()
      else:
        print(chat[f"{userInput.lower()}"]); print()
        input("Press enter to continue ")
        os.system("clear")
        __init__()
    except:
      times = 0
      print("I don't understand that. How should I respond?"); print()
      exception = str(input("> ")); print()
      chat[f"{userInput}"] = str(exception)
      f = open("chat.py", "w")
      f.write(f"chat = {str(chat)}"); f.close()
      print("Thank you for the feedback!"); print()
      a = open(f"{CURRENT_ACCOUNT}.data", "a")
      a.write(str(f"Input: {userInput}, Response: {exception}\n"))
      a.close()
      b = open(f"{CURRENT_ACCOUNT}.commits", "r")
      commits = int(b.read())
      commits += 1
      b.write(str(commits))
      b.close()
      input("Press enter to continue ")
      os.system("clear")
      __init__()

# account creation subroutine
def newAccount():
  os.system("clear")
  bold("Create Account"); print();
  newUser = str(input("Username > ")); print()
  if len(newUser) > 14:
    print("Please create a username under 15 characters."); print()
    input("Press enter to continue "); main()
  elif newUser in accounts.keys():
    print("This username already exists."); print()
    input("Press enter to continue "); main()
  else:
    newPass = str(input("Password > ")); print()
    if len(newPass) > 19:
      print("Please create a password under 20 characters. "); print()
      input("Press enter to continue"); main()
    else:
      f = open(f"{newUser}.commits", "a+")
      f.write(str("0"))
      f.close()
      d = open(f"{newUser}.data", "a+")
      d.close()
      accounts[f"{newUser}"] = str(newPass)
      e = open("accounts.py", "w")
      e.write(str(f"accounts = {accounts}"))
      e.close()

# login subroutine
def login():
  global LOGGED_IN
  global CURRENT_ACCOUNT
  os.system("clear")
  bold("Login"); print()
  user = str(input("Username > ")); print()
  if user in accounts.keys():
    passwd = str(input("Password > ")); print()
    if accounts[f"{user}"] == str(passwd):
      LOGGED_IN = True
      CURRENT_ACCOUNT = str(user)
      print("Login Successful"); print()
      input("Press enter to continue "); main()
    else:
      print(f"Invalid password for existing user {user}."); print()
      input("Press enter to continue "); main()
  else:
    print("That account does not exist."); print()
    input("Press enter to continue "); main()

# subroutine to allow end user to view their total commits to the AI dataset
def profile():
  global LOGGED_IN
  global CURRENT_ACCOUNT
  if LOGGED_IN == False:
    os.system("clear")
    bold("Error"); print()
    print("You must be logged in to access this feature."); print()
    input("Press enter to continue "); main()
  else:
    os.system("clear")
    bold(f"{CURRENT_ACCOUNT}"); print()
    f = open(f"{CURRENT_ACCOUNT}.commits", "r")
    cmts = str(f.read())
    f.close()
    print(f"Commits: {cmts}"); print()
    input("Press enter to continue "); main()
  

# main menu subroutine
def main():
  global LOGGED_IN
  global CURRENT_ACCOUNT
  os.system("clear")
  bold("SAM Beta"); print()
  if LOGGED_IN == True:
    print(f"Logged in as {CURRENT_ACCOUNT}"); print()
  else:
    pass
  print("1. About"); print("2. Tutorial"); print("3. Open Beta"); print("4. Login"); print("5. Create Account"); print("6. Profile"); print()
  mainInput = str(input("> "))
  if mainInput == str("1") or mainInput == str("1."):
    about()
  elif mainInput == str("2") or mainInput == str("2."):
    tutorial()
  elif mainInput == str("3") or mainInput == str("3."):
    if LOGGED_IN == True:
      os.system("clear")
      print("Type 'exit' at any point to return to the main menu"); print()
      __init__()
    elif LOGGED_IN == False:
      os.system("clear")
      bold("Error"); print()
      print("You must be logged in to access this feature."); print()
      input("Press enter to continue "); main()
    else:
      os.system("clear")
      bold("Error"); print()
      print("Error evaluating login status."); print()
      input("Press enter to continue "); main()
  elif mainInput == str("4") or mainInput == str("4."):
    login()
  elif mainInput == str("5") or mainInput == str("5."):
    newAccount()
  elif mainInput == str("6") or mainInput == str("6."):
    profile()
  else:
    main()


# main loop
while True:
  main()

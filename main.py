import random

def main():
  print("""
  ___________                   __________                    .___              
  \__    ___/______ __ __   ____\______   \_____    ____    __| _/____   _____  
    |    |  \_  __ \  |  \_/ __ \|       _/\__  \  /    \  / __ |/  _ \ /     \ 
    |    |   |  | \/  |  /\  ___/|    |   \ / __ \|   |  \/ /_/ (  <_> )  Y Y  \
    |____|   |__|  |____/  \___  >____|_  /(____  /___|  /\____ |\____/|__|_|  /
                              \/       \/      \/     \/      \/            \/ 
  .__                                                                           
  |__| ________________    ____    ____   ____                                  
  |  |/    \_  __ \__  \  /    \  / ___\_/ __ \                                 
  |  |   |  \  | \// __ \|   |  \/ /_/  >  ___/                                 
  |__|___|  /__|  (____  /___|  /\___  / \___  >                                
          \/           \/     \//_____/      \/                                 
                                                                                
      ______ ___.__.                                                            
      \____ <   |  |                                                            
      |  |_> >___  |                                                            
  /\ |   __// ____|                                                            
  \/ |__|   \/                                                                 


  """)
  print("-----------------------------------------------------------------------------------")
  print("Welcome to the Random Number Generator!")
  min = int(input("Enter the minimum number: "))
  max = int(input("Enter the maximum number: "))
  print("-----------------------------------------------------------------------------------")
  
  while True:
    print("Generating a random number between", min, "and", max)
    print("-----------------------------------------------------------------------------------")
    print("Your random number is:", random.SystemRandom().randint(min, max))
    print("-----------------------------------------------------------------------------------")
    choice = input("Press 'a' to generate another number, or 'q' to quit: ").strip().lower()
    if choice == 'q':
      print("Exiting the Random Number Generator. Goodbye!")
      break
    elif choice != 'a':
      print("Invalid input. Please press 'a' to generate another number or 'q' to quit.")

if __name__ == "__main__":
  main()
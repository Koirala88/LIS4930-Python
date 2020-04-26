from sys import exit
import random
import time

min = 1 
max = 6 
 
x = 0
y = 0

player_name = input("Enter your name please: ")
upper_name = player_name.upper()

virtual_names = ["Virtual P1", "Virtual P2", "Virtual P3", "Virtual P4",
                 "Virtual P5", "Virtual P6", "Virtual P7", "Virtual "]

for name in random.sample(virtual_names, 1):
    virtual_name = name
    virtual_name = virtual_name.upper()
    
    
    roll_again = "yes"
 
while roll_again == "yes": 
   if roll_again == "no":
      exit(0)
   print
   time.sleep(1)
   print ("\nYour Turn")
   time.sleep(1)
   print
   print ("\nDie is rolling...")
      
   time.sleep (2)
 
   x = random.randint(min, max)
   y = random.randint(min, max)
 
   def dice (d):
     if d == 1:
      print (""" 
          _________
         |         |
         |         |  
         |    *    | 
         |         | 
         |_________|  """)
         
     elif d == 2:
      print  ("""
          _________
         |         |
         |     *   |
         |         | 
         |   *     | 
         |_________|  """)
      
     elif d == 3:
      print ("""
          _________
         |         |
         |      *  |  
         |    *    | 
         |  *      | 
         |_________|  """) 
    
     elif d == 4:
      print ("""
          _________
         |         |
         |  *   *  |  
         |         | 
         |  *   *  | 
         |_________|  """) 
    
    
     elif d == 5:
      print (""" 
          _________
         |         |
         |  *   *  |  
         |    *    | 
         |  *   *  | 
         |_________|  """)
    
    
     elif d == 6:
      print ("""   
          _________
         |         |
         |  *   *  |  
         |  *   *  | 
         |  *   *  | 
         |_________|  """)
 
 
   dice (x)
   
   time.sleep(1)
   print
   print ("\n")
   print (virtual_name + "'s", ("Turn"))
   time.sleep(1)
   print
   print ("\nDie is rolling...")
   time.sleep(2)
    
   dice(y)
   
   time.sleep(1)
   
   
   if x == y:
      print
      print ("\nIt's a draw.")
      time.sleep(1)
      print
      print ("\nInput 'yes' to play again or 'no' to stop playing.")
      print
      
   elif x > y:
      print
      print ("\nYou Won, Congratulations!"), upper_name
      time.sleep(1)
      print 
      print ("\nInput 'yes' to keep playing OR 'no' to stop playing.")
      print
      
   elif x < y:
      print
      print (f"\nSorry! You Lost. Try again {upper_name}")
      time.sleep(1)
      print  
      print ("\nInput 'yes' to keep playing OR 'no' to stop playing.")
      print
     
   roll_again = input(f"\nWould you like to roll the die again, {upper_name}? ")

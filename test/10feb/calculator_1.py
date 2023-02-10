#!/usr/bin/python3
#addition
def calculator():
      while True:
          print("Enter operation:")
          
          print("+ for addition")
          
          print("- for subtraction")
          
          print("* for multiplication")
          
          print("/ for division")
          
          print("q for quit")
          

          
          choice = input("Enter choice: ")
          

          
          if choice == 'q':
          
              break
              
          elif choice in ['+', '-', '*', '/']:
          
              num1 = float(input("Enter first number: "))
              
              num2 = float(input("Enter second number: "))
              
              if choice == '+':
              
                  result = num1 + num2
                  
                  print(num1, "+", num2, "=", result)
                  
              elif choice == '-':
              
                  result = num1 - num2
                  
                  print(num1, "-", num2, "=", result)
                  
              elif choice == '*':
              
                  result = num1 * num2
                  
                  print(num1, "*", num2, "=", result)
                  
              elif choice == '/':
            
                  result = num1 / num2
                   
                  print(num1, "/", num2, "=", result)
              else:
              
                                                                                                                                                                                            print("Invalid Input")

calculator()



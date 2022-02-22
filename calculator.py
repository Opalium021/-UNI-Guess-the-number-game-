#python
#Javad Razaz Rahmaty
#Calculator

import math


print("\n\n>>>>>>>>    (Welcome to My Calculator)    <<<<<<<<")


while True:
    
    
    print("\n       ==>     "
          " [ + ] [ - ] [ * ]"
          "      <==   ")
    print("       ==>     "
          " [ / ] [ ^ ] [sqr]"
          "      <==   ")
    print("       ==>     "
          " [sin] [cos] [tan]"
          "      <==   ")
    print("       ==>     "
          " [cot] [fac] [log]"
          "      <==   ")
    print("       ==>     "
          "       [ext]      "
          "      <==   ")


    c = (input("\n\nSelect an Operator That You Need = "))

    try:
        

        if c == "ext":
           print("\n\n        >> Have Fun :D <<        ")
           break

#Get Number(s)---------------------------------------------------------------------------->        

        
        elif c == "sin" or c == "cos" or c == "tan" or c == "cot" or c == "log" or c == "fac" or c == "sqr":
            a = float(input("\nPlease Enter The Number = "))


        else:
            a = float(input("\nPlease Enter The First Number = "))
            b = float(input("\nPlease Enter The Second Number = "))

            
#operations ------------------------------------------------------------------------------->

        if c == "+":
            d = a + b
            print("\n{} + {} = ".format(a , b),d)


        elif c == "-":
            d = a - b
            print("\n{} - {} = ".format(a,b),d)

            
        elif c == "*":
            d = a * b
            print("\n{} * {} = ".format(a,b),d)

            
        elif c == "/":
            if a == 0 or b == 0:
               print("\nCannot Divide by Zero!")
            else:    
                d = a / b
                print("\n{} / {} = ".format(a,b),d)

                
        elif c == "sin":
            d = math.sin
            print("\nSin {} = ".format(a),d)


        elif c == "cos":
            d = math.cos(a)
            print("\nCos {} = ".format(a),d)


        elif c == "tan":
            d = math.tan(a)
            print("\nTan {} = ".format(a),d)


        elif c == "cot":
            d = math.cot(a)
            print("\nCot {} = ".format(a),d)


        elif c == "fac":
            d = math.factorial(a)
            print("\nFactorial {} = ".format(a),d)


        elif c == "log":
            d = math.log(a)
            print("\nLog {} = ".format(a),d)
            

        elif c == "^":
            d = math.pow(a,b)
            print("\n{} ^ {} = ".format(a,b),d)


        elif c == "sqr":
            d = math.sqrt(a)
            print("\nSqrt {} = ".format(a),d)
            

#End of Operations --------------------------------------------------------------------------->        

        
    except ValueError:
        print("\n   !!!!!! Invalid Input !!!!!!   ")

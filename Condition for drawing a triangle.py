#Python
#Javad Razaz Rahmaty
#Condition for Drawing a Triangle


print("\n            ==> Welcome <==            ")

try:
    
    a = int(input("\n\nPlease Enter the First Side of Triangle = "))
    b = int(input("\nPlease Enter the Second Side of Triangle = "))
    c = int(input("\nPlease Enter the Third Side of Triangle = "))

    if a + b > c and a + c > b and b + c > a:
            print("\nThere is No Problem to Drawing This Triangle :D")

    else:
            print("\nThere is no Triangle With These Sides :(")

except ValueError:
            print("\nPlease Enter The Value Number :/")

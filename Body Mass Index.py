#Python
#Javad Razaz Rahmaty
#Body Mass Index

print("\n          ====>> Wellcome To The Body Mass Index <<====          ")


try:

    a = int(input("\n\nPlease Enter Your Weight in 'Kg' = "))
    b = float(input("\nPlease Enter Your Heigh in 'Meter' (like 1.70) = "))
    c = a / (b*b)

    if c < 18.5:
        print("\nYou Are UnderWeight :( Eat SomeThing",c)

    elif 18.5 < c < 24.9:
        print("\nYou Are Normal And Healthy :)")

    elif 25 < c < 29.9:
        print("\nYou Are OverWeight :L Carefull")

    elif 30 < c < 34.9:
        print("\nYou Are Obese :/ Eat Less")

    elif c > 35:
        print("\nYou Are Extremely Obese :0 Please Dont Eat Me!")


except ValueError:
    print("\nPlease Enter a Value Number :\ ")

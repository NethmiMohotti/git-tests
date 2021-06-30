print("Age calculator")
print()
done = False
while not done:
    name = input("What is your name: ")
    try:
        birth_year= int(input("What is your birth year: "))
        age= 2021- birth_year
        print(f'{name} is {age} years old this year')
        option = input("please enter Q to quit or any other key to continue: ")
        if option=='q' or option=='Q':
            done = True
    except ValueError:
        print("Please enter a valid number")


print\
    ("\n\t\t\t\tWONDER CALCULATOR\n\t\t\t\t=================")


def menu():
    print("""
    \t\t\t    Main Menu\n
    \t\t 1.Enter Positive Integers
    \t\t 2.Display Highest Number
    \t\t 3.Display Lowest Number
    \t\t 4.Display Average
    \t\t 5.Display Even Numbers\n
    \t\t 6.Exit
    """)


def function_1():
    try:
        while True:
            selection = int(input("\nInput what you want to do with the numbers : "))

            if selection == 1:
                break

            while (selection < 7) and (selection > 1):
                list1.sort()
                if selection == 2:
                    print("The highest number is:", (list1[len(list1) - 1]))
                    break

                elif selection == 3:
                    print("The lowest number is:", (list1[0]))
                    break

                elif selection == 4:
                    average = sum(list1) / amount
                    print("The average is:", average)
                    break

                elif selection == 5:
                    print("The even numbers are: ")
                    for items in list1:
                        if items % 2 == 0:
                            print(items)
                    break

                elif selection == 6:
                    exit("Exiting! See you again!")

                else:
                    print("Error")

    except ValueError:
        print("Please enter only integers")


while True:
    try:
        amount = 0
        count = 0
        menu()
        x = int(input("Please indicate your option: "))
        if x == 1:
            amount = int(input("How many numbers do you want to input? : "))
            list1 = []
            if amount > 0:
                if amount < 11:
                    while count < amount:
                        num = int(input("Enter a positive number : "))
                        list1.append(num)
                        count += 1
                        if count == amount:
                            print("The number of inputs are over")
                            function_1()
                else:
                    print("Only numbers up to 10")
            else:
                print("Only positive integer numbers")

    except ValueError:
        print("Please enter only integers")


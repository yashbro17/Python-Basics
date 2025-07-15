#Take a number from the user and print whether it’s even or odd.#

def num_oddoreven():
    try:
        number = int(input("Enter the  number  :  "))
        if number%2 == 0: #condition-1#
            print("THE NUMBER IS EVEN")
        else: #condition-2#
            print("THE NUMBER IS ODD.")   
    except ValueError :
        print("TYPE A NUMBER NOT ANY CHARACTER.")
        num_oddoreven()
    finally:
        print("Code executed successfully")
num_oddoreven() #calling the function#



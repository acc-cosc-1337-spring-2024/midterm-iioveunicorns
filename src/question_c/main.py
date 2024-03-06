#add import
from question_c import get_random_number
while True:
    num = get_random_number()
    acceptable = ("y", "n")
    while True:
        answer = int(input("Choose a number 1-5: "))
        if answer == num:
            print("Congratulations you are correct!")
            g = True
            break
        else:
            while True:
                answer = input("Incorrect. Restart?")
                if answer not in acceptable:
                    print("Invalid response. Choose Yes or No: ")
                elif answer == "yes" or answer == "y" or answer == "Yes" or answer == "Y":
                    g = True
                    break
                elif answer == "no" or answer == "n" or answer == "No" or answer == "N":
                    print("The answer was", str(num) + ". Thank you, goodbye.")
                    g = False
                    break
            if g:
                continue
            else:
                exit()

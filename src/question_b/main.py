#add import
from question_b import get_tax_assessed, get_assessment_value

while True:
    value = int(input("What is your home's value?: "))
    assessed_value = get_assessment_value(value)
    property_taxes = get_tax_assessed(assessed_value)
    print(f'The assessed value is ${assessed_value: .2f}.')
    print(f'The tax is ${property_taxes: .2f}. ')

    while True: 
        Acceptable_answer = ["Yes", "No", "Y", "N", "yes", "no", "y", "n"]
        answer = input("Find another home's value?: ")
        if answer not in Acceptable_answer:
            print("Please enter Yes or No: ")
            continue
        elif answer == "Yes" or answer == "Y" or answer == "yes" or answer== "y":
            print("")
            g = True
            break
        elif answer == "No" or answer == "N" or answer == "no" or answer == "n":
            g = False
            break
    if g:
        continue
    else:
        print("Thank you, goodbye.")
        exit()
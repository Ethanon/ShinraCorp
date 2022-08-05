import application

app = application.Application()
valid_choice = False

while(not(valid_choice)):
    try:
        print("1 - Name and age")
        print("2 - Add two numbers")
        print("3 - Exit")
        choice = int(input("Pick an option: "))
        valid_choice = choice >= 1 and choice <= 33        
    except:
        print("Not valid choice, try again.")


match choice:
        case 1:
            app.NameAndAge()
        case 2:
            app.AddingTwoNumber()

print("Thank you for playing, come again!")
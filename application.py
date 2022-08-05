from datetime import datetime

class Application:
    
    def NameAndAge(self):
        age = 20        
        first_name = 'James'
        print(f'my name is {first_name} and my age is {age}')
        first_name = input("What is your name? ")
        
        valid_year = False
        while(not(valid_year)):
            try:
                year_born = int(input("And what year were you born? "))
                current_year = datetime.now().year
                valid_year = year_born >= 1800 and year_born <= current_year
            except:
                pass

            if(not(valid_year)) :
                print(f'That is not a valid year, try something between 1800 and the current year ({current_year}).')
            else:
                age = current_year - year_born

        print(f'So your name is {first_name} and you are {age} years old!')

    def AddingTwoNumber(self):
        
        valid_numbers = False
        while(not(valid_numbers)):
            try:
                first = float(input("First: "))
                second = float(input("Second: "))
                valid_numbers = True
            except:
                print("Not valid numbers, try again.")

        sum = first + second
        print(f'Sum: {sum}')    
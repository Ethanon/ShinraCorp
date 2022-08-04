from datetime import datetime


class Application:
    
    def start(self):
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
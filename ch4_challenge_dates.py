from datetime import datetime
from datetime import date
import calendar

def print_list_of_days() -> str:
    days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    for idx,day in enumerate(days):
        print(idx,":",day)

def day_counter(year,month,day) -> int:
    cout = 0
    cal = calendar.monthcalendar(year, month)
    for week in cal:
        if week[int(day)] != 0:
            cout += 1 
    return cout


  
def main():
    while(True):
        
        print("Which day of the week do you want to count?")
        print_list_of_days()
        print("Or 'exit' to quit")
        
        try:
            day = input("? ")
            if (day == str("exit")):
                break
            # If it's not equal to 'exit', then I convert day to integer and handle the error
            int(day)
            
            year = int(input("Enter the year: "))
            month = int(input("Enter the month: "))
            
            count = day_counter(year,month,int(day))

            print("There are", str(count), "of those days in the month and year specified")
            print("----------------------------------")
            
        except Exception as e:
            print("Invalid literal for int() with base 10 \n")
            print(e)
        
    
if __name__ == "__main__" :
    main()
         
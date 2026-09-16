import datetime


def days_calc():
    try:
        date_text1 = input("Enter First Date In (DD-MM-YYYY) format : ")
        date_value1 = datetime.datetime.strptime(date_text1, "%d-%m-%Y").date()
        date_text2 = input("Enter Second Date In (DD-MM-YYYY) format : ")
        date_value2 = datetime.datetime.strptime(date_text2, "%d-%m-%Y").date()

        if date_value2 < date_value1:
            date_value1, date_value2 = date_value2, date_value1

        total_months = (
            (date_value2.year - date_value1.year) * 12
            + date_value2.month - date_value1.month
        )

        if date_value2.day < date_value1.day:
            total_months -= 1

        years, months = divmod(total_months, 12)

        date_final = date_value2 - date_value1

        print(f"Gap: {date_final.days} days")
        print(f"Gap: {total_months} months")
        print(f"Gap: {years} years and {months} months")
        
    except ValueError:
        print("Please enter a valid date.")


days_calc()
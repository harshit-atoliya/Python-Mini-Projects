# Import the datetime module to work with dates and date parsing.
import datetime

# Define a function that calculates the difference between two dates.
def days_calc():
    try:
        # Ask the user for the first date in the format DD-MM-YYYY.
        date_text1 = input("Enter First Date In (DD-MM-YYYY) format : ")
        # Convert the input string into a Python date object.
        date_value1 = datetime.datetime.strptime(date_text1, "%d-%m-%Y").date()

        # Ask the user for the second date in the format DD-MM-YYYY.
        date_text2 = input("Enter Second Date In (DD-MM-YYYY) format : ")
        # Convert the second input string into a Python date object.
        date_value2 = datetime.datetime.strptime(date_text2, "%d-%m-%Y").date()

        # Ensure the earlier date is always treated as the first date.
        # This makes the calculations consistent regardless of input order.
        if date_value2 < date_value1:
            date_value1, date_value2 = date_value2, date_value1

        # Calculate the total number of months between the two dates.
        # This is done by converting the year difference into months and
        # then adding/subtracting the month difference.
        total_months = (
            (date_value2.year - date_value1.year) * 12
            + date_value2.month - date_value1.month
        )

        # If the day of the second date is earlier than the day of the first date,
        # the month count needs to be adjusted downward by one month.
        if date_value2.day < date_value1.day:
            total_months -= 1

        # Split the total month difference into years and remaining months.
        years, months = divmod(total_months, 12)

        # Calculate the exact day difference between the dates.
        date_final = date_value2 - date_value1

        # Display the results to the user.
        print(f"Gap: {date_final.days} days")
        print(f"Gap: {total_months} months")
        print(f"Gap: {years} years and {months} months")

    # Handle invalid date input gracefully.
    except ValueError:
        print("Please enter a valid date.")


# Run the function when the script is executed.
days_calc()
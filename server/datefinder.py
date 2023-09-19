from datetime import datetime, timedelta

def return_dates():
    # Get today's date
    today = datetime.today()

    # Calculate the date one month ago
    one_month_ago = today - timedelta(days=30)

    # Format the date in YYYY-MM-DD format
    formatted_date_past = one_month_ago.strftime('%Y-%m-%d')
    formatted_date_present = today.strftime('%Y-%m-%d')

    return [formatted_date_past, formatted_date_present]

# Example usage
dates = return_dates()
print('Date one month ago:', dates[0])
print('Today\'s date:', dates[1])

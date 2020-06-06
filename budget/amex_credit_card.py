import datetime

from helpers import should_process_row, determine_category

category_dict = {
    'SPROUTS FARMERS MARK': 'Groceries',
    'WHOLEFDS': 'Groceries',
    'SAFEWAY  STORE': 'Groceries',
    'KING SOOPERS': 'Groceries',
    'WEGMANS FOOD MARKET': 'Groceries'
}

skip_set = {
    'AUTOPAY PAYMENT'
}


def translate(csv_reader, writer, acct_name, acct_type):
    next(csv_reader)
    for row in csv_reader:
        desc = row[4]
        if should_process_row(desc, skip_set):
            date = row[0]
            format_str = '%m/%d/%y'
            date = datetime.datetime.strptime(date, format_str).date()
            amount = row[2]
            category = determine_category(desc, category_dict)
            writer.writerow([date, acct_name, desc, amount, category, acct_type])

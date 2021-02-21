import datetime

from helpers import determine_category

category_dict = {
    'Celeste Jacroux': 'Housing',
    'Deposit from USAA': 'Steven Transfer',
    'Deposit from ALLY': 'Alicia Transfer',
    'Monthly Interest Paid': 'Interest',
    'XCEL ENERGY': 'Utilities',
    'Withdrawal from CAPITAL ONE CRCARDPMT': 'Credit card payment out'
}


def translate(csv_reader, writer, acct_name, acct_type):
    next(csv_reader)
    for row in csv_reader:
        desc = row[4]
        date = row[1]
        format_str = '%m/%d/%y'
        date = datetime.datetime.strptime(date, format_str).date()
        amount = row[2]
        category = determine_category(desc, category_dict)
        writer.writerow([date, acct_name, desc, amount, category, acct_type])

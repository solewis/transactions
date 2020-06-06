import datetime

from helpers import should_process_row, determine_category

category_dict = {
    'Celeste Jacroux': 'Rent',
    'Deposit from USAA': 'Steven Transfer',
    'Deposit from ALLY': 'Alicia Transfer',
    'Monthly Interest Paid': 'Interest',
    'XCEL ENERGY': 'Utilities',

}

skip_set = {
    'CRCARDPMT',
    'Withdrawal from GOLDMAN SACHS BA COLLECTION',
    'Withdrawal to 360 Checking'
}


def translate(csv_reader, writer, acct_name, acct_type):
    next(csv_reader)
    for row in csv_reader:
        desc = row[4]
        if should_process_row(desc, skip_set):
            date = row[1]
            format_str = '%m/%d/%y'
            date = datetime.datetime.strptime(date, format_str).date()
            amount = row[2]
            category = determine_category(desc, category_dict)
            writer.writerow([date, acct_name, desc, amount, category, acct_type])

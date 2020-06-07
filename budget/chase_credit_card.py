import datetime

from helpers import determine_category

category_dict = {
    'SPROUTS FARMERS MAR': 'Groceries'
}


def translate(csv_reader, writer, acct_name, acct_type):
    next(csv_reader)
    for row in csv_reader:
        desc = row[2]
        date = row[0]
        format_str = '%m/%d/%Y'
        date = datetime.datetime.strptime(date, format_str).date()
        amount = row[5]
        category = determine_category(desc, category_dict)
        writer.writerow([date, acct_name, desc, amount, category, acct_type])

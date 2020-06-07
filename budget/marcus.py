from helpers import determine_category

category_dict = {
    'WORLD WIDE TECH DIRECT DEP': 'Paycheck',
    'SAV Increase Int Paid': 'Interest',
    'VANGUARD BUY INVESTMENT': 'Taxable Investment'
}


def translate(csv_reader, writer, acct_name, acct_type):
    next(csv_reader)
    for row in csv_reader:
        desc = row[1]
        date = row[0]
        amount = row[2]
        category = determine_category(desc, category_dict)
        writer.writerow([date, acct_name, desc, amount, category, acct_type])

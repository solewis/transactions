from helpers import determine_category, toFloat

category_dict = {
    'WHOLEFDS': 'Groceries',
    'COMCAST CABLE COMM': 'Utilities',
    'SPROUTS': 'Groceries',
    'DIVINO': 'Alcohol',
    'WASH PERK': 'Restaurants',
    'SAFEWAY': 'Groceries',
    'DENVER WATER': 'Utilities',
    'CHIPOTLE': 'Restaurants',
    'PETSMART': 'Pet Care'
}


def translate(csv_reader, writer, acct_name, acct_type):
    next(csv_reader)
    for row in csv_reader:
        desc = row[3]
        date = row[0]
        debit = toFloat(row[5])
        credit = toFloat(row[6])
        amount = credit - debit
        category = determine_category(desc, category_dict)
        writer.writerow([date, acct_name, desc, amount, category, acct_type])

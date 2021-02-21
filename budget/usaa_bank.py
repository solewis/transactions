import datetime

from helpers import determine_category

category_dict = {
    'ALICIA C RACITI': 'Housing',
    'Asynchrony AP Invoice': 'Business misc',
    'WORLD WIDE TECH  DIRECT DEP': 'Paycheck',
    'VANGUARD BUY     INVESTMENT': 'IRA contribution',
    'INTEREST PAID': 'Interest',
    'To Michael J Lewis Checking': 'Utilities',
    'XCEL ENERGY-PSCO XCELENERGY': 'Utilities',
    'TenantCloud LLC': 'Housing',
    'PAYPAL           INST XFER  ***********TIME': 'Entertainment - goods',
    'Celeste Jacroux': 'Housing'
}


def translate(csv_reader, writer, acct_name, acct_type):
    next(csv_reader)
    for row in csv_reader:
        desc = row[2]
        date = row[0]
        amount = row[4]
        category = determine_category(desc, category_dict)
        writer.writerow([date, acct_name, desc, amount, category, acct_type])

import datetime

from helpers import should_process_row, determine_category

category_dict = {
    'ALICIA C RACITI': 'Housing',
    'Asynchrony AP Invoice': 'Business Misc',
    'WORLD WIDE TECH  DIRECT DEP': 'Paycheck',
    'VANGUARD BUY     INVESTMENT': 'IRA Contribution',
    'INTEREST PAID': 'Interest',
    'To Michael J Lewis Checking': 'Utilities',
    'XCEL ENERGY-PSCO XCELENERGY': 'Utilities',
    'TenantCloud LLC': 'Housing',
    'PAYPAL           INST XFER  ***********TIME': 'Entertainment - goods',
    'Celeste Jacroux': 'Housing',
    'IRS': 'Taxes'
}

skip_set = {
    'AMEX EPAYMENT',
    'CRCARDPMT',
    'CHASE CREDIT CRD AUTOPAY',
    'CAPITAL ONE ONLINE PMT',
    'GOLDMAN SACHS BA COLLECTION',
    'To Steven Lewis Savings #5146'
}


def translate(csv_reader, writer, acct_name, acct_type):
    next(csv_reader)
    for row in csv_reader:
        desc = row[1]
        if should_process_row(desc, skip_set):
            date = row[0]
            format_str = '%m/%d/%y'
            date = datetime.datetime.strptime(date, format_str).date()
            amount = row[3]
            category = determine_category(desc, category_dict)
            writer.writerow([date, acct_name, desc, amount, category, acct_type])

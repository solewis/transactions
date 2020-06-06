import datetime

from helpers import should_process_row, determine_category

category_dict = {
    'ALICIA C RACITI': 'Rent Reimbursement',
    'Asynchrony AP Invoice': 'Business Misc',
    'WORLD WIDE TECH  DIRECT DEP': 'Paycheck',
    'VANGUARD BUY     INVESTMENT': 'IRA Contribution',
    'INTEREST PAID': 'Interest',
    'To Michael J Lewis Checking': 'Cell',
    'XCEL ENERGY-PSCO XCELENERGY': 'Utilities',
    'TenantCloud LLC': 'Rent',
    'PAYPAL           INST XFER  ***********TIME': 'Entertainment - goods',
    'Celeste Jacroux': 'Rent',
    'IRS': 'Taxes'
}

skip_set = {
    'AMEX EPAYMENT',
    'CRCARDPMT',
    'CHASE CREDIT CRD AUTOPAY',
    'GOLDMAN SACHS BA COLLECTION'
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

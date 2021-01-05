import datetime


def translate(csv_reader, writer):
    next(csv_reader)
    for row in csv_reader:
        trade_date = row[0]
        transaction_type = row[1]
        amount = row[2]
        symbol = row[3]
        format_str = '%m/%d/%Y'
        trade_date = datetime.datetime.strptime(trade_date, format_str).date()
        writer.writerow(['', trade_date, symbol, '', transaction_type, '', '', '', amount, 'WWT'])

#          writer.writerow(['Settlement Date', 'Trade Date', 'Symbol', 'Investment Name', 'Transaction Type', 'Shares',
#                          'Share Price', 'Commission fees', 'Net Amount', 'Account Name', 'Account'])

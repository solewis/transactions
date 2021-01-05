import datetime

"in"
"settle, trade, symbol, name, trans type, quantity, price, fees, amount"
"0,      1,     2,      3,    4,          5,        6,     7,    8"

"out"
"Settle, Trade, Symbol, Name, Trans Type, Quantity, Price, Fees, Amount, Account"


def translate(csv_reader, writer, account):
    next(csv_reader)
    for row in csv_reader:
        trade_date = row[1]
        settlement_date = row[0]
        format_str = '%m/%d/%Y'
        trade_date = datetime.datetime.strptime(trade_date, format_str).date()
        settlement_date = datetime.datetime.strptime(settlement_date, format_str).date()
        investment_name = row[3]
        symbol = row[2]
        if 'VANGUARD FEDERAL MONEY MARKET FUND' in investment_name:
            symbol = 'VMFXX'
        if symbol == '--':
            symbol = ''
        amount = row[8]
        amount = amount.replace('$', '').replace(',', '').replace(' ', '').replace('–', '-')
        price = row[6]
        price = price.replace('$', '').replace(',', '').replace(' ', '').replace('–', '-')
        fees = row[7]
        fees = fees.replace('$', '').replace(',', '').replace(' ', '').replace('–', '-')
        trans_type = row[4]
        quantity = row[5]

        # Filter out CASH transactions, as we only care when money entered an investment
        if investment_name != 'CASH':
            writer.writerow(
                [settlement_date, trade_date, symbol, investment_name, trans_type, quantity, price, fees, amount,
                 account])

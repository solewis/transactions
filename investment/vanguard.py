import datetime


def translate(csv_reader, writer):
    next(csv_reader)
    for row in csv_reader:
        trade_date = row[1]
        settlement_date = row[2]
        format_str = '%m/%d/%Y'
        trade_date = datetime.datetime.strptime(trade_date, format_str).date()
        settlement_date = datetime.datetime.strptime(settlement_date, format_str).date()
        investment_name = row[5]
        symbol = row[6]
        if 'VANGUARD FEDERAL MONEY MARKET FUND' in investment_name:
            symbol = 'VMFXX'

        writer.writerow([settlement_date, trade_date, symbol, investment_name, row[3], row[7], row[8], row[10], row[11], row[0]])

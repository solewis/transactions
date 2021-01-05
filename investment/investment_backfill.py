import csv

import vanguard_web


def main():
    with open('data/investment/output_backfill.csv', mode='w') as output_csv, \
            open('data/investment/personalbrokerage.csv') as personal_brokerage_csv, \
            open('data/investment/rollover.csv') as rollover_csv, \
            open('data/investment/roth.csv') as roth_csv, \
            open('data/investment/sharedbrokerage.csv') as shared_brokerage_csv:
        output_writer = csv.writer(output_csv, delimiter=',')
        personal_brokerage_reader = csv.reader(personal_brokerage_csv, delimiter=',')
        rollover_reader = csv.reader(rollover_csv, delimiter=',')
        roth_reader = csv.reader(roth_csv, delimiter=',')
        shared_brokerage_reader = csv.reader(shared_brokerage_csv, delimiter=',')
        output_writer.writerow(
            ['Settlement Date', 'Trade Date', 'Symbol', 'Name', 'Transaction Type', 'Quantity', 'Price',
             'Commissions and fees', 'Amount', 'Account'])
        vanguard_web.translate(personal_brokerage_reader, output_writer, '49579282')
        vanguard_web.translate(rollover_reader, output_writer, '73603013')
        vanguard_web.translate(roth_reader, output_writer, '17456914')
        vanguard_web.translate(shared_brokerage_reader, output_writer, '27144467')

main()

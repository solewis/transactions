import csv

import vanguard
import wwt


def main():
    with open('data/investment/output_pre.csv', mode='w') as output_pre_csv, \
            open('data/investment/vanguard.csv') as vanguard_file, \
            open('data/investment/wwt.csv') as wwt_file:
        output_pre_writer = csv.writer(output_pre_csv, delimiter=',')
        vanguard_reader = csv.reader(vanguard_file, delimiter=',')
        wwt_reader = csv.reader(wwt_file, delimiter=',')
        output_pre_writer.writerow(
            ['Settlement Date', 'Trade Date', 'Symbol', 'Name', 'Transaction Type', 'Quantity', 'Price',
             'Commissions and fees', 'Amount', 'Account'])
        vanguard.translate(vanguard_reader, output_pre_writer)
        wwt.translate(wwt_reader, output_pre_writer)

    # remove already imported transactions
    imported_keys = set()
    with open('data/investment/imported.csv') as imported_csv, \
            open('data/investment/output_pre.csv') as output_pre_csv, \
            open('data/investment/output.csv', mode='w') as output_csv:
        imported_reader = csv.reader(imported_csv, delimiter=',')
        next(imported_reader)
        for row in imported_reader:
            imported_keys.add(toKey(row))

        output_writer = csv.writer(output_csv, delimiter=',')
        output_pre_reader = csv.reader(output_pre_csv, delimiter=',')
        output_writer.writerow(
            ['Settlement Date', 'Trade Date', 'Symbol', 'Name', 'Transaction Type', 'Quantity', 'Price',
             'Commissions and fees', 'Amount', 'Account'])
        next(output_pre_reader)
        for row in output_pre_reader:
            if toKey(row) not in imported_keys:
                output_writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]])


def toKey(row):
    # Key: trade date, symbol, account, amount
    return row[1] + row[2] + row[9] + '%.2f' % float(row[8])


main()

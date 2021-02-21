import csv

import amex_credit_card
import cap_one_bank
import cap_one_credit_card
import chase_credit_card
import marcus
import usaa_bank
from helpers import toFloat


def main():
    with open('data/budget/output_pre.csv', mode='w') as output_csv:
        writer = csv.writer(output_csv, delimiter=',')
        writer.writerow(['Date', 'Account', 'Description', 'Amount', 'Category', 'Type'])
        with open('data/budget/caponesharedchecking.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            cap_one_bank.translate(csv_reader, writer, 'SharedChecking', 'Shared')
        with open('data/budget/savorone.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            cap_one_credit_card.translate(csv_reader, writer, 'SavorOne', 'Shared')
        with open('data/budget/caponestevesavings.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            cap_one_bank.translate(csv_reader, writer, 'CapOneSavings', 'Steven')
        with open('data/budget/caponesharedsavings.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            cap_one_bank.translate(csv_reader, writer, 'CapOne360Savings', 'Shared')
        with open('data/budget/quicksilver.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            cap_one_credit_card.translate(csv_reader, writer, 'Quicksilver', 'Steven')
        with open('data/budget/usaa.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            usaa_bank.translate(csv_reader, writer, 'USAA', 'Steven')
        with open('data/budget/marcus.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            marcus.translate(csv_reader, writer, 'Marcus', 'Steven')
        with open('data/budget/amex.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            amex_credit_card.translate(csv_reader, writer, 'Amex', 'Steven')
        with open('data/budget/chase.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            chase_credit_card.translate(csv_reader, writer, 'Chase', 'Steven')

    # remove already imported transactions
    imported_keys = set()
    with open('data/budget/imported.csv') as imported_csv:
        reader = csv.reader(imported_csv, delimiter=',')
        next(reader)
        for row in reader:
            key = toKey(row)
            if key.startswith('2020-05-01'):
                print(key + str(len(key)))
            imported_keys.add(key)
    with open('data/budget/output.csv', mode='w') as output_csv:
        writer = csv.writer(output_csv, delimiter=',')
        writer.writerow(['Date', 'Account', 'Description', 'Amount', 'Category', 'Type'])
        with open('data/budget/output_pre.csv') as output_pre_csv:
            reader = csv.reader(output_pre_csv, delimiter=',')
            next(reader)
            for row in reader:
                key = toKey(row)
                if key.startswith('2020-05-01'):
                    print(key + str(len(key)))
                if key not in imported_keys:
                    if key.startswith('2020-05-01'):
                        print("Not in imported:")
                        print(key + str(len(key)))
                    writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5]])


def toKey(row):
    amt = toFloat(row[3])
    desc = row[2]
    # usaa gets bad unicode in it
    desc = desc.replace(u'\xa0', u' ')
    return row[0] + row[1] + desc + '%.2f' % amt


main()

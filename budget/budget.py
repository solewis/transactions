import csv

import cap_one_bank
import cap_one_credit_card
import marcus
import usaa_bank
import amex_credit_card
import chase_credit_card


def main():
    with open('data/output.csv', mode='w') as output_csv:
        writer = csv.writer(output_csv, delimiter=',')
        writer.writerow(['Date', 'Account', 'Description', 'Amount', 'Category', 'Type'])
        with open('data/caponechecking.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            cap_one_bank.translate(csv_reader, writer, 'Checking', 'Shared')
        with open('data/savorone.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            cap_one_credit_card.translate(csv_reader, writer, 'SavorOne', 'Shared')
        with open('data/caponesavings.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            cap_one_bank.translate(csv_reader, writer, 'CapOneSavings', 'Steven')
        with open('data/quicksilver.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            cap_one_credit_card.translate(csv_reader, writer, 'Quicksilver', 'Steven')
        with open('data/usaa.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            usaa_bank.translate(csv_reader, writer, 'USAA', 'Steven')
        with open('data/marcus.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            marcus.translate(csv_reader, writer, 'Marcus', 'Steven')
        with open('data/amex.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            amex_credit_card.translate(csv_reader, writer, 'Amex', 'Steven')
        with open('data/chase.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            chase_credit_card.translate(csv_reader, writer, 'Chase', 'Steven')


main()

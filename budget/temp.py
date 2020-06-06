import csv
import datetime

# with open('output2.csv', mode='w') as output_csv:
#     writer = csv.writer(output_csv, delimiter=',')
#     writer.writerow(['Date', 'Account', 'Description', 'Amount', 'Type', 'Category'])
#     with open('output.csv') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         next(csv_reader)
#         for row in csv_reader:
#             date = row[0]
#             acct = row[1]
#             desc = row[2]
#             amt = row[3]
#             typ = row[4]
#             cat = row[5]
#             notes = row[6]
#             if typ == 'expense':
#                 amt = '-' + amt
#             writer.writerow([date, acct, desc, amt, cat, notes])

# sort
with open('amex2.csv', mode='w') as output_csv:
    writer = csv.writer(output_csv, delimiter=',')
    writer.writerow(
        ["Date", "Description", "Amount", "Extended Details", "Appears On Your Statement As", "Address", "City/State",
         "Zip Code", "Country", "Reference", "Category"])
    with open('amex.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        format_str = '%m-%d-%y'
        sortedlist = sorted(reader, key=lambda r: datetime.datetime.strptime(r[0], format_str).date())
        for row in sortedlist:
            writer.writerow(
                [row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip(), row[4].strip(), row[5].strip(),
                 row[6].strip(), row[7].strip(), row[8].strip(), row[9].strip(), row[10].strip()])

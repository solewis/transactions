### Instructions
#### Budget
1. Download transactions. Grab from a few days prior to last recorded
    - Capital One (account services -> download transactions)
    - USAA (download, add headers, delete empty columns)
    - Marcus (manually type for now)
    - Amex (choose custom date range, then can download, check box to show extended details)
    - Chase
    - Notes
        - Negative is money leaving the account (and credit card purchases), positive is money entering (and credit card payments)
        - Delete empty lines at end of csv
1. Export current All Txns tab from google sheets to imported.csv
1. Run budget.py
1. It will output all the new transactions standardized into one file which can be copied to budget tracker in google sheets 

#### Investments
1. Download transactions
    - Vanguard Brokerage - Single
    - Vanguard Rollover IRA
    - Vanguard Roth IRA
    - Vanguard Brokerage - Shared
      - All vanguard can export as one file to csv (download button at top right of balances and holdings)
      - Delete account summary information
    - Merrill Lynch
      - Copy from website to excel, format currency (no commas, no dollar sign), delete details column, delete extra rows/columns, export to csv
      - Contribution should become buy for transaction type
      - All contributions should be negative
      - Dividends should be positive and add a reinvestment that is negative the dividend
        - Split dividends between all investments
      - Recordkeeping fee should be split between investments
1. 
#### TODO
1. Figure out Marcus which copies weird (no export option)
1. Transactions for Investments
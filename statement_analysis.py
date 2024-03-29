import pandas as pd
import os
import matplotlib.pyplot as plt

from open_ai_api import OpenAiApi

folder = 'transactions'
AI = OpenAiApi()

columns_apple = ['Transaction Date', 'Category', 'Amount (USD)']
columns_amex = ['Date', 'Amount', 'Category']

all_transactions = pd.DataFrame()

for filename in os.listdir(folder):
    if filename.endswith('.csv'):
        if 'activity' in filename:
            df = pd.read_csv(os.path.join(folder, filename), usecols=columns_amex)
            df.columns = ['Date', 'Amount', 'Category']
            df['Date'] = pd.to_datetime(df['Date'])
        elif 'Apple' in filename:
            df = pd.read_csv(os.path.join(folder, filename), usecols=columns_apple)
            df.columns = ['Date', 'Category', 'Amount']
            df['Date'] = pd.to_datetime(df['Date'])
        else:
            continue

        all_transactions = pd.concat([all_transactions, df], ignore_index=True)  # Reset the index

monthly_expenditure = all_transactions.groupby([all_transactions['Date'].dt.to_period('M'), 'Category'])['Amount'].sum().unstack()
print("\n\nMonthly Expenditure:")

# Udate category to be consistent across different statements
monthly_expenditure['Category'] = monthly_expenditure['Category'].apply(AI.get_category)

monthly_expenditure.plot(kind='line', title='Expenditure Trend')
plt.show()

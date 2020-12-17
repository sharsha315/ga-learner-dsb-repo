# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
#print(bank.head())

categorical_var = bank.select_dtypes(include='object')
print(categorical_var.head())

numerical_var = bank.select_dtypes(include='number')
print(numerical_var.head())



# code ends here


# --------------
# code starts here
banks = bank.drop(columns='Loan_ID')

# check for null values
print(banks.isnull().sum())

# mode for banks
bank_mode = banks.mode().iloc[0]
print(bank_mode)

# Fill missing (NaN) values of banks with bank_mode
banks.fillna(bank_mode, inplace=True)
#print(banks)

# checking for missing values if any,  after fill
print(banks.isnull().sum())

#code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks, index=['Gender', 'Married', 'Self_Employed'],
                                 values='LoanAmount')
print(avg_loan_amount)


# code ends here



# --------------
# code starts here

# loan_approved self employee count
loan_approved_se = len(banks[(banks['Loan_Status'] == 'Y') & (banks['Self_Employed'] == 'Yes')])
print(loan_approved_se)

# loan approved non self employee count
loan_approved_nse = len(banks[(banks['Loan_Status'] == 'Y') & (banks['Self_Employed'] == 'No')])
print(loan_approved_nse)

# percentage of loan approval for self-employed 
percentage_se = (loan_approved_se / 614) * 100
print(percentage_se)

#percentage of loan approval for not self-employed
percentage_nse = (loan_approved_nse / 614) * 100
print(percentage_nse)

# code ends here


# --------------
# code starts here

# convert months to years
loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x) / 12)
#print(loan_term)

# applicants having loan amount term greater than or equal to 25 years
big_loan_term = len(loan_term[loan_term >= 25])
print(big_loan_term)


# code ends here


# --------------
# code starts here

# groupby Loan_Status and subsetting ApplicantIncome and Credit_History
loan_groupby = banks.groupby('Loan_Status')[['ApplicantIncome', 'Credit_History']]
#print(loan_groupby)

# mean of subsetted dataframe
mean_values = loan_groupby.mean()
print(mean_values)



# code ends here



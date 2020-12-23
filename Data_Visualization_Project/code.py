# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




#Code starts here
data = pd.read_csv(path)


loan_status = data['Loan_Status'].value_counts()
loan_status.plot(kind='bar')
plt.show()


# --------------
#Code starts here

# grouping dataframe by 'Property_Area' and 'Loan_Status'
property_and_loan = data.groupby(['Property_Area', 'Loan_Status'])
property_and_loan = property_and_loan.size().unstack()

# Plotting stacked bar plot of property_and_loan
property_and_loan.plot(kind='bar', stacked=True)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here

# grouping dataframe by 'Education' and 'Loan_Status'
education_and_loan = data.groupby(['Education', 'Loan_Status'])
education_and_loan = education_and_loan.size().unstack()

# plotting stacked bar plot on education_and_loan
education_and_loan.plot(kind='bar', stacked=True)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here
graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']

# plotting density plot
graduate['LoanAmount'].plot(kind='density', label='Graduate')
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')




#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows=3, ncols=1, figsize=(15,10))

# scatter plot for 'ApplicantIncome' and 'LoanAmount'
data.plot(x='ApplicantIncome', y='LoanAmount', kind='scatter', ax=ax_1)
ax_1.set_title('Applicant Income')

# scatter plot for 'CoapplicantIncome' and 'LoanAmount'
data.plot(x='CoapplicantIncome', y='LoanAmount', kind='scatter', ax=ax_2)
ax_2.set_title('Coapplicant Income')

# creating a new column 'TotalIncome'
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
# scatter plot for 'TotalIncome' and 'LoanAmount'
data.plot(x='TotalIncome', y='LoanAmount', kind='scatter', ax=ax_3)
ax_3.set_title('Total Income')





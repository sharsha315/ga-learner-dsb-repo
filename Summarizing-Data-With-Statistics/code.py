# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)

data['Gender'].replace('-', 'Agender', inplace=True)

gender_count = data['Gender'].value_counts()

gender_count.plot.bar()
plt.show()
#Code starts here 




# --------------
#Code starts here
alignment = data['Alignment'].value_counts()

# pie chart for alignment
plt.pie(alignment, labels = alignment.index)
plt.title('Character Alignment')
plt.show()


# --------------
#Code starts here
sc_df = data[['Strength', 'Combat']]

sc_covariance = sc_df.cov().iloc[0,1]
sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()
sc_pearson = sc_covariance / (sc_strength * sc_combat)

# correlation for Intelligence and Combat

ic_df = data[['Intelligence', 'Combat']]

ic_covariance = ic_df.cov().iloc[0,1]
ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()
ic_pearson = ic_covariance / (ic_intelligence * ic_combat)




# --------------
#Code starts here

total_high = data['Total'].quantile(0.99)
super_best = data[data['Total'] > total_high]
super_best_names = super_best['Name'].tolist()
print(super_best_names)



# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(1, 3)

ax_1.boxplot(data['Intelligence'])
ax_1.set_title('Intelligence')

ax_2.boxplot(data['Speed'])
ax_2.set_title('Speed')

ax_3.boxplot(data['Power'])
ax_3.set_title('Power')

plt.show()



# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print("\nData: \n\n", data)
print("\nType of data: \n\n", type(data))

census = np.concatenate((data, new_record))
print(census)


# --------------
#Code starts here

age = census[:,0]
print(age)

max_age = np.max(age)
print(max_age)

min_age = np.min(age)
print(min_age)

age_mean = np.mean(age)
print(age_mean)

age_std = np.std(age)
print(age_std)


# --------------
#Code starts here

race_0 = census[census[:,2]==0]
len_0 = len(race_0)

race_1 = census[census[:,2]==1]
len_1 = len(race_1)
print(len_1)

race_2 = census[census[:,2]==2]
len_2 = len(race_2)

race_3 = census[census[:,2]==3]
len_3 = len(race_3)

race_4 = census[census[:,2]==4]
len_4 = len(race_4)

lens = np.array([len_0,len_1,len_2,len_3, len_4])
mini = np.min(lens)


if len_0 == mini:
    minority_race = 0
elif len_1 == mini:
    minority_race = 1
elif len_2 == mini:
    minority_race = 2
elif len_3 == mini:
    minority_race = 3
elif len_4 == mini:
    minority_race = 4

print(minority_race)
#m = np.where(lens == mini)
#m = m[0]
#print(m)



# --------------
#Code starts here

senior_citizens = census[census[:,0] > 60]
#print(senior_citizens)

working_hours_sum = np.sum(senior_citizens[:,6])
#print(working_hours_sum)

senior_citizens_len = len(senior_citizens)

avg_working_hours = working_hours_sum / senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here

high = census[census[:,1]>10]
low = census[census[:,1]<=10]
#print(high)

avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])
print(avg_pay_high)

if avg_pay_high > avg_pay_low:
    print("Higher Educated people have better pay")
else:
    print("Better Pay has nothing to do with Higher Education")



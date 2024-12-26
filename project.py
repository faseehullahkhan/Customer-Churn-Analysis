import pandas as pa
import numpy as na
import matplotlib.pyplot as plt
import seaborn as sns

data = pa.read_csv(r'C:\Users\DC\Desktop\Python\Fourth_Project\Customer Churn.csv')
print(data.head())
print(data.describe())
# as we know that there are null values in the total charges section thats why the type of Dtype
# of total charges is object instead of float so to change it we can do this

data['TotalCharges'] = data['TotalCharges'].replace(" " , "0")
data['TotalCharges'] = data['TotalCharges'].astype("float")
print(data.info())

# it is here to check the null values in the data
print(data.isnull().sum())

# now we will check the duplicates
print(data.duplicated().sum())

# now if we want to check the duplicates in the specific row we can do this
print(data['customerID'].duplicated().sum())

# now if we want to change the values of senior cetizen from yes to 1 and no to 0 we can do this
def change_senior_citizen(value):
  if value == 1:
    return "Yes"
  elif value == 0:
    return "No"

data['SeniorCitizen'] = data['SeniorCitizen'].apply(change_senior_citizen)
# print(data.head())

# now to check how many customers churn out or not
plt.figure()
churn_counts = data['Churn'].value_counts()
print(churn_counts.values)
plt.bar(churn_counts.index , churn_counts.values)
plt.xlabel('Churn')
plt.ylabel('Count')
plt.title('Churn Counts')
for i, value in enumerate(churn_counts.values):
    plt.text(i, value, str(value), ha='center', va='bottom', fontsize=10)

plt.show()

plt.figure()
gb = data.groupby('Churn').agg({'Churn' : 'count'})
plt.pie(gb['Churn'] , labels= gb.index , autopct= "%1.2f%%")
plt.show()

churn_by_gender = data.groupby(['gender', 'Churn']).size().unstack()
print(churn_by_gender)
churn_by_gender.plot(kind = 'bar' , stacked = False)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Churn Counts by Gender')
plt.xticks(rotation=0)  # Optional: to keep the x-axis labels horizontal
plt.show()

plt.figure()
churn_by_SeniorCitizen = data.groupby(['SeniorCitizen', 'Churn']).size().unstack()
print(churn_by_SeniorCitizen)
churn_by_SeniorCitizen.plot(kind = 'bar' , stacked = False)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Churn Counts by SeniorCitizen')
plt.xticks(rotation=0)  # Optional: to keep the x-axis labels horizontal
plt.show()


plt.figure()
number_of_senior_citizen = data['SeniorCitizen'].value_counts()
plt.bar(number_of_senior_citizen.index , number_of_senior_citizen.values)
plt.xticks([0, 1], ['Young citizen', 'Senior Citizen'])
for i, value in enumerate(number_of_senior_citizen.values):
  plt.text(i, value, str(value), ha='center', va='bottom', fontsize=10)

plt.show()

# Group data by SeniorCitizen and Churn, and get the count of each combination
churn_by_senior_citizen = data.groupby(['SeniorCitizen', 'Churn']).size().unstack()

# Plot the bar chart
churn_by_senior_citizen.plot(kind='bar', stacked=True)

# Add labels and title
plt.xlabel('Senior Citizen Status')
plt.ylabel('Count')
plt.title('Churn by Senior Citizen Status')
plt.xticks([0, 1], ['Young citizen', 'Senior Citizen'], rotation=0)

# Show the plot
plt.show()


# now if i want to check the churn with respect for the tenure
churn_by_tenure = data.groupby(['tenure', 'Churn']).size().unstack
print(churn_by_tenure)
plt.hist(data['tenure'], bins=20, color='blue', edgecolor='black')
plt.xlabel('Tenure')
plt.ylabel('Frequency')
plt.title('Distribution of Tenure')
plt.show()


# now we can count the customer in terms of contract and plot the histogram
contract_counts = data['Contract'].value_counts()
plt.hist(data['Contract'] , bins = 6 , color = 'lightblue' , edgecolor = 'black')
plt.xlabel('Contract Type')
plt.ylabel('Count')
plt.title('Contract Type Counts')
plt.show()

internet_service = data['InternetService'].value_counts()
plt.bar(internet_service.index, internet_service.values, color=['blue', 'orange', 'green'])
plt.xlabel('Internet Service')
plt.ylabel('Count')
plt.title('Churn by Internet Service')

for i, value in enumerate(internet_service.values):
  plt.text(i, value + 5, str(value), ha='center', va='bottom', fontsize=10)

plt.show()


payment_method = data['PaymentMethod'].value_counts()
plt.bar(payment_method.index, payment_method.values, color=['blue', 'orange', 'green' , 'red'])
plt.xlabel('Payment Method')
plt.ylabel('Count')
plt.title('Payment Method Counts')
plt.xticks(rotation=10)
plt.show()
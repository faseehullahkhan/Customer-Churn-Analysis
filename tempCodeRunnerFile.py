gender = data.groupby(['gender', 'Churn']).size().unstack()
# print(churn_by_gender)
# churn_by_gender.plot(kind = 'bar' , stacked = False)
# plt.xlabel('Gender')
# plt.ylabel('Count')
# plt.title('Churn Counts by Gender')
# plt.xticks(rotation=0)  # Optional: to keep the x-axis labels horizontal
# plt.show()
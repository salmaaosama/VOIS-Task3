import pandas as pd

#Load the data inside the provided CSV file into a Data Frame
df = pd.read_csv('C:\Task3\Employees.csv')

#Remove any duplicates in the table
df=df.drop_duplicates()

#Remove any decimal places in the Age column
df['Age'] = df['Age'].astype(int).round()

#Convert the USD salary to EGP
df['Salary(USD)'] = df['Salary(USD)']*47
df=df.rename(columns={"Salary(USD)" : "Salary(EGP)"})
Male_Female_Ratio = df["Gender"].value_counts(normalize=True)

#Print in the console some stats like:- Average age   - Median Salaries   - Ration between males and female employees
print("Average age = ",df['Age'].mean())
print("Median Salaries = ",df["Salary(EGP)"].median())
print("Male_Female_ratio:")
print(Male_Female_Ratio)


df.to_csv('C:\Task3\Employees_Update.csv', index=False)






import pandas as pd
import matplotlib.pyplot as plt #visualisation
import seaborn as sns #visualisation


# Declare where the data sources is located
# and read it as a dataframe saved on "df" variable
url = 'auto2.csv'
df = pd.read_csv(url)

# show the shape of the dataframe

print(df.shape)

# Change your headings names by using the command:
# The array should have same items as your dataframe
# df.columns = ["Column 1 name", "Column 2 name", "etc"]

print("This is the heading in the dataframe:")
print(df.head(15))

# Print the datatypes in your dataframe
print("These are the datatypes of each column in the dataframe:")
print(df.dtypes)


#replace categorical values
df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce') # COerce the invalid parse will be NaN

print(df.info())

print(df.head(15))


#remove name column since does not add value

df = df.drop(['name'], axis=1)
print(df.head())


print(df.info())

print("\n\nVerify null:")

print(df[df.isnull().any(axis=1)])

print("\nRemoving null values...")
df = df.dropna(axis=0)

print("\nnew dataframe: ")
print(df.head(10))
print(df.info())

print("\n\nstatistical analysis:\n")
print(df.describe())

plt.figure(figsize=(10,5))
c= df.corr()
sns.heatmap(c, cmap="BrBG",annot=True)


fig, ax = plt.subplots(figsize=(5,5))
ax.scatter(df['year'], df['weight'])
plt.title('catter plot between year and weight')
ax.set_xlabel('year')
ax.set_ylabel('weight')


fig, ax = plt.subplots(figsize=(5,5))
ax.scatter(df['cylinders'], df['displacement'])
plt.title('catter plot between cylinders and displacement')
ax.set_xlabel('cylinders')
ax.set_ylabel('displacement')

fig, ax = plt.subplots(figsize=(5,5))
ax.scatter(df['weight'], df['displacement'])
plt.title('catter plot between weight and displacement')
ax.set_xlabel('weight')
ax.set_ylabel('displacement')
plt.show()
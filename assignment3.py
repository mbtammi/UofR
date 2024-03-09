import pandas as pd
import numpy as np
import missingno as msno
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import plotly.express as px
import seaborn as sns
import pycountry



print("======== START ========")
# Update the path to the dataset on GitHub
dataset_url = "https://raw.githubusercontent.com/JorgeMiGo/Data-Science-Salaries-2023/main/Dataset/ds_salaries.csv"
data = pd.read_csv(dataset_url)
data.loc[90:94,['work_year','salary_in_usd']]
#data.nunique()

# Transformation of the codes of the categorical variables

data['experience_level'] = data['experience_level'].replace({'SE': 'Expert', 'MI': 'Intermediate', 'EN': 'Junior', 'EX': 'Director'})

data['employment_type'] = data['employment_type'].replace({'FT': 'Full-time', 'CT': 'Contract', 'FL': 'Freelance', 'PT': 'Part-time'})

def country_name(country_code):
    try:
        return pycountry.countries.get(alpha_2=country_code).name
    except:
        return 'other'
    
data['company_location'] = data['company_location'].apply(country_name)
data['employee_residence'] = data['employee_residence'].apply(country_name)
# print(data)

#for column in ['work_year','experience_level','employment_type','company_size','remote_ratio','job_title','company_location']:
#    print(data[column].unique())

#There is no null/NaN values so no need to filter them out.

#Printing how many people earn more than 0.3 Million
print((data['salary_in_usd'] > 300000).sum())

print('Highest salary in dataset:', data['salary_in_usd'].max())



filtered_salary_data = data[data['salary_in_usd'] > 222200]

# Creating a pivot table
pivoted_data = pd.pivot_table(filtered_salary_data, values='salary_in_usd',
                               index=['experience_level', 'employment_type'],
                               columns=['work_year'], aggfunc=np.mean)

# Printing the pivot table
print(pivoted_data)

print("======= BREAK =======")

# Calculate the number of individuals by country but removing US. which is 80% of individuals
filtered_data = data[data['company_location'].str.strip() != 'United States']

level_counts = filtered_data['company_location'].value_counts()

# Let's create a pie chart
plt.figure(figsize=(7,12),dpi=80)
plt.pie(level_counts.values, labels=level_counts.index, autopct='%1.1f%%')
plt.title('Experience Level Distribution')

plt.show()

print("======= BREAK =======")

#Lets do plotting, open the data in fullscreen to also see the year.

pivoted_data = pd.pivot_table(data, values='salary_in_usd',
                               index=['work_year', 'experience_level'],
                               aggfunc=np.mean)

# Plotting
pivoted_data.plot(kind='bar', color='b', alpha=0.7, title='Average Salary (in USD) by Year and Experience Level')
plt.show()


# Uncomment the style and font configurations if needed
# plt.style.use('seaborn-whitegrid')
# plt.rc('text', usetex=True)
# plt.rc('font', family='times')
# plt.rc('xtick', labelsize=10)
# plt.rc('font', size=12)
# plt.rc('ytick', labelsize=10)

print("========= END =========")
# # **Automatidata Project**

# Welcome to the Automatidata Project!
# 
# You have just started as a data professional in a fictional data consulting firm, Automatidata. Their client, the New York City Taxi and Limousine Commission (New York City TLC), has hired the Automatidata team for its reputation in helping their clients develop data-based solutions.
# 
# The team is still in the early stages of the project. Previously, you were asked to complete a project proposal by your supervisor, DeShawn Washington. You have received notice that your project proposal has been approved and that New York City TLC has given the Automatidata team access to their data. To get clear insights, New York TLC's data must be analyzed, key variables identified, and the dataset ensured it is ready for analysis.
# 
# Please complete the following questions.

# # Course 2 End-of-course Project: Inspect and analyze data 
# 
# In this activity, you will examine data provided and prepare it for analysis. This activity will help ensure the information is,
# 
# 1.   Ready to answer questions and yield insights
# 
# 2.   Ready for visualizations
# 
# 3.   Ready for future hypothesis testing and statistical methods
# <br/>   
# 
# **The purpose** of this project is to investigate and understand the data provided.
#   
# **The goal** is to use a dataframe contructed within Python, perform a cursory inspection of the provided dataset, and inform team members of your findings. 
# <br/>  
# *This activity has three parts:*
# 
# **Part 1:** Understand the situation 
# * Prepare to understand and organize the provided taxi cab dataset and information.
# 
# **Part 2:** Understand the data
# 
# * Create a pandas dataframe for data learning, future exploratory data analysis (EDA), and statistical activities.
# 
# * Compile summary information about the data to inform next steps.
# 
# **Part 3:** Understand the variables
# 
# * Use insights from your examination of the summary data to guide deeper investigation into specific variables.

# ### **Task 1. Understand the situation**
# 
# 1.   How can you best prepare to understand and organize the provided taxi cab information? 

# Begin by exploring your dataset and consider reviewing the Data Dictionary. One can prepare to understand the information by reading the taxi cab data fields and understanding the impact of each one. Reviewing the fact sheet could also provide helpful background information. However, the primary goal is to get the data into Python, inspect it, and provide DeShawn with initial observations. The next step would be to learn more about the data and check for any anomalies.

# ## PACE: **Analyze**

# ### **Task 2a. Build dataframe**

# **Code the following,**

# In[1]:


import pandas as pd               #library exercise for buidling dataframes
import numpy as np                #numpy is imported with pandas

df = pd.read_csv('2017_Yellow_Taxi_Trip_Data.csv')
print("done")


# ### **Task 2b. Understand the data - Inspect the data**
# 
# View and inspect summary information about the dataframe by coding the following:
# 
# 1. df.head(10)
# 2. df.info()
# 3. df.describe()
# 
# Consider the following two questions:
# 
# **Question 1:** When reviewing the df.info() output, what do you notice about the different variables? Are there any null values? Are all of the variables numeric? Does anything else stand out?
# Dtypes are non-numeric. Two of which are datetime.
# No null values.
# **Question 2:** When reviewing the df.describe() output, what do you notice about the distributions of each variable? Are there any questionable values?
#Regarding fare amount, the distribution is worth considering. The maximum fare amount is a much larger value ($1000) than the 25-75 percent range of values. Also, it's questionable how there are negative values for fare amount. Regarding trip distance, most rides are between 1-3 miles, but the maximum is over 33 miles.

# In[2]:


df.head(10)


# In[3]:

df.info()


# In[4]:



df.describe()


# ### **Task 2c. Understand the data - Investigate the variables**
# 
# Sort and interpret the data table for two variables:`trip_distance` and `total_amount`.
# 
# **Answer the following three questions:**
# 
# **Question 1:** Sort your first variable (`trip_distance`) from maximum to minimum value, do the values seem normal?
# The values align with our earlier data discovery, where we noticed that t
# **Question 2:** Sort by your second variable (`total_amount`), are any values unusual?
# Yes, the first two values are significantly higher than the others. 
# **Question 3:** Are the resulting rows similar for both sorts? Why or why not?
#The most expensive rides are not necessarily the longest ones. 
# In[5]:

# Sort the data by trip distance from maximum to minimum value

df_sort = df.sort_values(by=['trip_distance'],ascending=False)
df_sort.head(10)


# In[6]:

# Sort the data by total amount and print the top 20 values
total_amount_sorted = df.sort_values(
    ['total_amount'], ascending=False)['total_amount']
total_amount_sorted.head(20)


# In[7]:

# Sort the data by total amount and print the bottom 20 values
total_amount_sorted.tail(20)


# In[8]:

# How many of each payment type are represented in the data?
df['payment_type'].value_counts()


# What is the average tip for trips paid for with credit card?
avg_cc_tip = df[df['payment_type']==1]['tip_amount'].mean()
print('Avg. cc tip:', avg_cc_tip)

# What is the average tip for trips paid for with cash?
avg_cash_tip = df[df['payment_type']==2]['tip_amount'].mean()
print('Avg. cash tip:', avg_cash_tip)


# In[10]:


# How many times is each vendor ID represented in the data?
df['VendorID'].value_counts()


# In[11]:

# What is the mean total amount for each vendor?
df.groupby(['VendorID']).mean(numeric_only=True)[['total_amount']]


# In[12]:

# Filter the data for credit card payments only
credit_card = df[df['payment_type']==1]

# Filter the credit-card-only data for passenger count only
credit_card['passenger_count'].value_counts()


# In[13]:

# Calculate the average tip amount for each passenger count (credit card payments only)
credit_card.groupby(['passenger_count']).mean(numeric_only=True)[['tip_amount']]

 
# After looking at the dataset, the two variables that are most likely to help build a predictive model for taxi ride fares are total_amount and trip_distance because those variables show a picture of a taxi cab ride.



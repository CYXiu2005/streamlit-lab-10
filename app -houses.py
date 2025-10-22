import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')

st.title('California Housing Prices（1990）by Yuxiu Chen')

# Load the data
df = pd.read_csv('housing.csv')

# Price slider
price_filter = st.slider('Median House Value:', 
                          float(df['median_house_value'].min()), 
                          float(df['median_house_value'].max()), 
                          float(df['median_house_value'].median()))

# Sidebar - Multiselect for location type
location_filter = st.sidebar.multiselect(
    'Location Type',
    df['ocean_proximity'].unique(),  # options
    df['ocean_proximity'].unique())  # defaults

# Sidebar - Radio button for income level
income_level = st.sidebar.radio(
    'Income Level',
    ('Low (< 2.5)', 'Medium (2.5 - 4.5)', 'High (>= 4.5)'))

# Filter by price
df = df[df['median_house_value'] <= price_filter]

# Filter by location type
df = df[df['ocean_proximity'].isin(location_filter)]

# Filter by income level using if statement
if income_level == 'Low (< 2.5)':
    df = df[df['median_income'] < 2.5]
elif income_level == 'Medium (2.5 - 4.5)':
    df = df[(df['median_income'] >= 2.5) & (df['median_income'] < 4.5)]
else:  # High (>= 4.5)
    df = df[df['median_income'] >= 4.5]

# Show on map
st.map(df)

# Show histogram of median house value
st.subheader('Median House Value Distribution')
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(df['median_house_value'], bins=30, edgecolor='black')
ax.set_xlabel('Median House Value')
ax.set_ylabel('Frequency')
ax.set_title('Histogram of Median House Value')
st.pyplot(fig)

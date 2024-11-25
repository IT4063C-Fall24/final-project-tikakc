#!/usr/bin/env python
# coding: utf-8

# # Health Access Disparities
# 
# ![Banner](./assets/banner.jpeg)

# ## Topic
# The problem I’m addressing is the disparity in access to healthcare services between different regions, specifically comparing rural areas to urban areas. This topic is important because healthcare access is a key determinant of well-being, and inequities in access can lead to significant differences in health outcomes. Bridging these gaps is crucial to ensuring that all individuals, regardless of where they live, have fair opportunities to access healthcare.
# 
# 

# ## Project Question
# *What specific question are you seeking to answer with this project?*
# *This is not the same as the questions you ask to limit the scope of the project.*
# What factors contribute to disparities in healthcare access between rural and urban areas?
# 
# How does travel distance to healthcare facilities impact healthcare utilization in rural areas?
# 
# What role does socioeconomic status play in healthcare access disparities?
# 
# 

# ## What would an answer look like?
# *What is your hypothesized answer to your question?*
# A bar chart comparing factors like the number of healthcare facilities, transportation availability, and healthcare professional availability between rural and urban areas.
# 
# A line graph showing how utilization rates decrease as travel distances increase, emphasizing how access limitations affect health-seeking behavior.
# 
# A scatter plot to represent the correlation between income levels and proximity to healthcare facilities, illustrating how lower-income areas may have fewer healthcare options.

# ## Data Sources
# *What 3 data sources have you identified for this project?*
# *How are you going to relate these datasets?*
# 
# Healthcare Facilities Data (Type: CSV File)
# Includes information on the location of healthcare facilities, their type (e.g., hospitals, clinics), and the services provided.
# This dataset will help identify where healthcare facilities are located and their distribution between urban and rural areas.
# 
# Demographics Data (Type: API)
# US Census Bureau API
# Provides data on population density, income levels, education, and other demographic factors by geographic area.
# This dataset will be used to assess socioeconomic conditions in different regions and their correlation with healthcare access.
# 
# Healthcare Utilization Data (Type: Database)
# National Health Interview Survey (NHIS) data accessed through a database (e.g., CDC databases).
# Contains data on healthcare visits, frequency of healthcare use, and self-reported barriers to accessing healthcare.
# This dataset will help understand healthcare utilization patterns and assess barriers faced by different regions.
# 
# 

# ## Approach and Analysis
# *What is your approach to answering your project question?*
# *How will you use the identified data to answer your project question?*
# To answer the questions related to health access disparities between rural and urban areas, I will take a multi-step analytical approach using descriptive statistics, comparative analysis, and geospatial analysis.
# 
# Descriptive Statistics:
# 
# I will begin by summarizing the availability of healthcare facilities in both urban and rural regions. This will involve calculating metrics like the number of healthcare facilities per capita, average travel distance to facilities, and the ratio of healthcare providers to residents.
# Comparative Analysis:
# 
# I will perform a comparative analysis to determine how access differs between rural and urban areas. Key variables such as population density, socioeconomic factors (like income and education), and healthcare facility density will be compared using visualizations such as bar charts and scatter plots. This will help to illustrate the disparities clearly and quantify the differences in healthcare access.
# Geospatial Analysis:
# 
# Using the location data from healthcare facilities, I will conduct a geospatial analysis to visualize the geographical distribution of healthcare services. Choropleth maps will be used to show which areas have a shortage of facilities. This will also help to identify regions where travel distances to healthcare services are the longest.
# Correlation Analysis:
# 
# I will also investigate the correlation between socioeconomic indicators and healthcare access by using demographic data from the Census Bureau. For example, I'll analyze if regions with lower average incomes are also the ones that lack sufficient healthcare facilities.
# Data Integration and Aggregation:
# 
# The datasets will be integrated using common identifiers like county codes or zip codes. This integration will enable a comprehensive analysis of healthcare facility availability and utilization relative to population demographics.
# 
# The Healthcare Facilities Data from the Health Resources & Services Administration (HRSA) will be used to understand facility availability in both rural and urban areas. Specifically, this data will allow me to measure the number of facilities available per population unit in each area.
# 
# The Demographics Data from the US Census Bureau will provide essential socioeconomic and geographic data, such as population density, average income, and educational levels, which will be key to understanding how social and economic factors influence healthcare access.
# 
# The Healthcare Utilization Data from the National Health Interview Survey (NHIS) will be used to compare the utilization of healthcare services in rural versus urban areas. By merging this data with demographics and facility data, I can assess whether healthcare utilization correlates with facility availability and the distance to healthcare services.
# 
# Together, these datasets will help build a complete picture of the disparities that exist in healthcare access, focusing on geographic, economic, and social factors that contribute to the issue.

# In[1]:





# ## Resources and References
# *What resources and references have you used for this project?*
# Health Resources & Services Administration (HRSA):
# 
# URL: HRSA Data Downloads
# This resource provides data on healthcare facilities, including their type, location, and services provided. It will be instrumental in determining the availability of healthcare facilities across different regions.
# US Census Bureau:
# 
# API Documentation: Census Bureau Data Sets
# The Census Bureau provides demographic and socioeconomic data that will be used to understand population distribution and socioeconomic conditions in rural and urban areas.
# National Health Interview Survey (NHIS):
# 
# URL: NHIS Overview
# This data provides insights into healthcare utilization rates in various regions, helping to correlate access with the availability of services and socioeconomic factors.
# Academic Articles:
# 
# Articles and papers on healthcare access and rural-urban disparities have been referred to for building an understanding of the existing literature and for defining the project's framework.

# In[1]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')


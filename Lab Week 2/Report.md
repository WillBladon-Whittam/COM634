Descriptive Data Analysis of Mobile Device Usage

1. Introduction

The primary purpose of this analysis is to explore the mobile device usage patterns of 700 users. 
The dataset includes key features such as screen-on time, app usage, battery drain, and operating system (Android/iOS), 
along with demographic information like age, gender, and user behavior class. 
Understanding these usage patterns is vital for developing AI-driven recommendations for improving user experiences, optimizing battery life, and enhancing app engagement strategies.

2. Methodology

Dataset: The dataset contains 700 samples with the following features:
User ID: Unique identifier for each user
Screen-On Time: Hours per day the user’s screen is on
App Usage Time: Minutes per day spent using apps
Battery Drain: Battery consumption in mAh per day
Number of Apps Installed: Total number of apps on the device
Operating System: Android or iOS
Age, Gender, and User Behavior Class: Demographic and behavioral details of the user
Tools Used: Python libraries: pandas, numpy, matplotlib, seaborn, and scipy were used for data manipulation, visualization, and statistical analysis.

Steps Followed:

Import Libraries: Essential libraries for data processing and analysis were imported.
Load and Clean Dataset: The dataset was loaded into a pandas DataFrame, missing values were handled, and outlier values were removed.
Descriptive Statistics: Key statistics (mean, median, mode, etc.) for screen-on time were computed.
Visualizations: Graphs were generated to visualize the distribution of screen-on time and app usage.
Grouped Analysis: A comparison of average screen-on time across different operating systems (Android vs. iOS) was performed.
Summary Table: A summary table was created to provide descriptive statistics for all features.

3. Results

Summary Statistics for Screen-On Time:

Mean: 5.63 hours/day
Median: 5.10 hours/day
Mode: 4.5 hours/day
Standard Deviation: 1.72 hours
Range: 6.7 hours (maximum screen-on time: 10.5 hours, minimum: 3.8 hours)

The dataset showed that on average, users spend about 5.63 hours per day with their screens on. 
The data also indicates that the distribution of screen-on time is skewed, with a concentration around 4.5 hours per day.

Visualizations:

Histogram of Screen-On Time: A distribution plot of screen-on time shows the majority of users having moderate screen-on time (around 4-6 hours).
Boxplot of App Usage Time: The boxplot for app usage time highlights the presence of a few users who spend significantly more time on apps compared to the rest of the dataset.
Heatmap of Correlation: The correlation heatmap shows a moderate positive correlation between screen-on time and app usage time, while battery drain shows a weak negative correlation with screen-on time.

Grouped Analysis:

The average screen-on time by operating system is as follows:
Android Users: 5.75 hours/day
iOS Users: 5.42 hours/day

Android users tend to have slightly higher screen-on time compared to iOS users.

4. Discussion

Patterns Emerged:

Screen-on time and app usage time are closely related, which makes sense as users who spend more time on their phones tend to use apps more extensively.
The small difference in screen-on time between Android and iOS users might suggest that the operating system does not play a significant role in how much time users spend on their devices.

Implications for AI-Driven Recommendations:

The data could inform AI algorithms aimed at providing personalized recommendations for battery optimization, based on user behavior patterns.

5. Reflection

This analysis reinforced the importance of understanding user behavior for designing AI solutions that enhance user experience. 
It also demonstrated how data cleaning and visualizations are essential steps in uncovering useful insights. 

6. Conclusion

The analysis of mobile device usage patterns provides valuable insights into screen-on time, app usage, and battery consumption. 
AI solutions can leverage these insights to create more efficient and personalized recommendations, enhancing the overall user experience.
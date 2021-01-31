# Surfs_up Challenge
Analyzing weather data in Jupyter Notebook using Python and SQLAlchemy to do basic termperature analysis and data exploration of your climate database in Hawaii. All of the following analysis should be completed using SQLAlchemy ORM Queries, Pandas.

## Overview of analysis
'<p>The purpose of our analysis is to see temperature statistics for June and December for Oahu Island to see if running a surf shop is sustainable year around. The way we get the temperature data is by running two seperate queries, one being for June and the other being December across all observation stations. Once we run our queries we store the temperatures in a list then convert them to a dataframe. Once our dataframe is created we are able to get our summary statistics by using the .describe() method. Here is what we found:</p>'
___
# Results
 ## For the Month of *June*  from 2010 to 2017, we determined the following key statistical data:
* Total count of 1,700 data points
* Mean of 74.9  F
* Min temperature of 64.0 F
* Max temperature of 85.0 F
* 75% Max temperature of 85.0 F 
![ ](/Images/June_temp.PNG)
___
 ## For the month of *December* from 2010 to 2016, we determined the following key statistical data:
- Total count of 1,517 data points
- Mean of 71.0  F
- Min temperature of 56 F
- Max temperature of 83.0 F
- 75% Max temperature of 74.0 F
![ ](/Images/December_temp.PNG)

 * Standard deviation is 3.25 for the June months and 3.75 for the December months-- making a .5 difference in the two different seasons
___
*Based on a comparison of precipitation and temperature between June and December from 2010 to 2017 across all observation stations, it’s possible to notice the following statistical information:*


 1. Over 7 years, there are 1574 precipitations occurred and 1700 temperatures  observed in June, higher than 1405 precipitations and 1517 temperatures  observed in December. The different (1700-1517 = 183) between two observations counts that indicate the data of Dec, 2017 not included in database.

 2. Comparing of precipitation, the mean (0.217) and median (0.03) of December are higher than June’s mean (0.136) and median (0.02), respectively. 

 3. For precipitation derivative indicators, December also had higher Standard Deviations and Maximum precipitation. In December, standard deviation (0.541) is higher than June’s standard deviation (0.336). The minimum of both December and June are zero, and December maximum (6.42) is higher than June (4.43).

 4. Comparing of temperatures, it apparently shows that June’s temperature indicators are higher than December.

- **Make variable recommendations for further analysis.**


 1. The lack of data in December, 2017  may cause less reliable of data. The database should generate more recently winter data to compare summer and winter precipitation. 

 2. In addition of statistical summery, various features and plots may help us better analyze the seasonal weather. For example, line plots would be able to  provide quick and easy way to show time-varying. Histogram plots would tell us frequency of precipitation as well as temperature for both December and Jane.

 3. For seasonal analysis, we need filter more detail precipitation and temperatures for Spring and Autumn. 

# Summary 

From the queries required on the challenge, we can tell the temperature behavior for the months of June and July.  However, besides temperature, preciptiation is an important fact for surfers.  On the module we ran a precipitation query
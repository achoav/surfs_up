# Surfs_up Challenge
Analyzing weather data in Jupyter Notebook using Python, SQLAlchemy, Matplotlib and Flask to do visualize climate data as you prepare to open a surf shop. All of the following analysis should be completed using SQLAlchemy ORM (Object Relational Mapper) Queries, Pandas and Flask.  We will use a 'hawaii.sqlite' file that contains data for several (9 *nine*) weather stations.

The 'hawaii.sqlite' table 'Stations':

![](/Images/Stations.PNG)

The 'hawaii.sqlite' table 'Measurments':

![](/Images/Measurement.PNG)
___
## Overview of analysis
The purpose of our analysis is to see temperature statistics for June and December for Oahu Island to see if running a surf shop is sustainable year around. The way we get the temperature data is by running two seperate queries, one being for June and the other being December across all observation stations. Once we run our queries we store the temperatures in a list that is converted to a dataframe. Once our dataframe is created, we are able to get our summary statistics by using the .describe() method.

Further, on our climatte_analysis we created a plot for precipitation.

**Plot of Precipitation Analysis**
![](/Images/Precipitation_analysis.PNG)

___
# Results
 ## For the month of *June*  from 2010 to 2017, we determined the following key statistical data:
* Total count of 1,700 data points
* Mean of 74.9  F
* Min temperature of 64.0 F
* Max temperature of 85.0 F
* 75% Max temperature of 85.0 F 

![](/Images/June_temp.PNG)
___
 ## For the month of *December* from 2010 to 2016, we determined the following key statistical data:
- Total count of 1,517 data points
- Mean of 71.0  F
- Min temperature of 56 F
- Max temperature of 83.0 F
- 75% Max temperature of 74.0 F

![](/Images/December_temp.PNG)

 * Standard deviation is 3.25 for the June months and 3.75 for the December months-- making a .5 difference in the two different seasons
___
### Based on a comparison of precipitation and temperature between June and December from 2010 to 2017 across all observation stations, it’s possible to notice the following statistical information:

1. Over 7 years, there are 1700 temperatures reported in June, higher than 1517 temperatures reported for the monnths in December. The difference of 183 data points (1700-1517 = 183) between two months observations counts can be explained by the fact that the data of Dec, 2017 is not included in SQlite database.
2. Comparing of temperatures, it apparently shows that June’s temperature indicators are higher than December.
3. Comparing of precipitation, the mean (0.217) and median (0.03) of December are higher than June’s mean (0.136) and median (0.02), respectively. 
4. December months are rainier than June months.  As for precipitation derivative indicators, December also had higher Standard Deviations and Maximum precipitation. In December, the standard deviation (0.541) is higher than June’s standard deviation (0.336). The minimum of both December and June are zero, and the December maximum (6.42) is higher than June (4.43).
 
 **June Precipitation**
 ![](/Images/June_prec.PNG)
 
 **December Precipitation**
 !{](/Images/Dec_prec.PNG)
 

## Make variable recommendations for further analysis.
1. The lack of data in December 2017  may cause less reliable data. The database should generate more recent winter data to compare summer and winter precipitation. 
2. Also of statistical summary, various features and plots may help us better analyze the seasonal weather. For example, line plots would be able to provide a quick and easy way to show time-varying. Histogram plots would tell us the frequency of precipitation as well as temperature for both December and June.
3. For seasonal analysis, we need to filter more detailed precipitation and temperatures for Spring and Autumn. 

# Summary 

From the queries required on the challenge, we can tell the temperature behavior for the months of June and December.  However, besides temperature, precipitation is an important fact for surfers.  On the module, we ran a precipitation query so users can have further information on the Winter and Summer months in regards to rain/

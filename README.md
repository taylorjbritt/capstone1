# Capstone 1: Airborne

For this project, I decided to investigate the effect that the COVID-19 epidemic and subsequent quarantines are having on air quality. After seeing numerous claims on social media that implied that the air and water were much cleaner in places that instituted a lockdown, I was curious to see if this effect was real and, if so, how closely the changes tracked the spread of the virus and government measures in responses.

## The Data

The World Air Quality Index Project is a small organization that collects readings from air quality monitoring stations around the world and standardizes them using E.P.A. guidelines into AQI, or Air Quality Index, units. Unfortunately, the type of airborne particle that different stations report is not uniform – all of the stations I looked at report PM<sub>2.5</sub> concentrations (particulate matter 2.5 micrometers or less), but reporting of PM<sub>10</sub> (between 2.5 and 10 micrometers). NO<sub>2</sub> (Nitrogen Dioxide), CO (carbon monoxide), and SO<sub>2</sub> (sulfur dioxide) is sporadic. Many stations have daily values dating back to September 1st, 2014, but quite a few began reporting more recently, and often there are gaps in the reporting, ranging from a day or two to several months. 

I had to download the datasets individually, so I decided to focus on stations that had PM<sub>2.5</sub> and  NO<sub>2</sub> dating back to 2014. The other pollutants were too sporadic to find data for in the range of cities I wanted to look at. Most NO<sub>2</sub> comes from automobile traffic and in burning fossil fuels, so it seemed like a good pollutant to focus on. 

AQI units are not linealy scaled to concentrations of particulate matter, but rather to the relative levels of danger to human health – (cont)

### The cities...


### EDA

I began by converting loading the CSV file for Denver into a dataframe and, after cleaning up the data I was interested in, generated a scatterplot for PM<sub>2.5</sub> and NO<sub>2</sub> concentrations: 

![image](images/scatterplots/scatterdenver.png)

I realized that a major obstacle to discerning if COVID-19 had lead to a significant drop in these pollutants was that they exhibit seasonal variation, especially NO<sub>2</sub> AQI levels, which tend to spike around New Years.  

I subsequently created a pipeline script to clean other datasets and save them as picklefiles, and generated scatterplots for a number of other cities, including in the southern hemisphere where the pattern would likely be reversed if it was driven by weather. 

Cities in Europe and China in the northern hemisphere seemed to generally follow the smame pattern. 

![image](images/scatterplots/scattermadrid.png)

![image](images/scatterplots/scatterparis.png)

![image](images/scatterplots/scatterbeijing.png)

![image](images/scatterplots/scatterwuhan.png)

As I expected, the peaks and valleys were reversed in the southern hemisphere.

![image](images/scatterplots/scattersydney.png)

![image](images/scatterplots/scattersaopaulo.png)

![image](images/scatterplots/scattersantiago.png)

Given the periodicity of the concentrations, I thought it would make the most sense to plot the values for the first three months in different years to get a better sense how the trajectory of PM<sub>2.5</sub> and NO<sub>2</sub> was different. 

While I was working on initial exploration of the data earlier this week, the World Air Quality Project Index released a detailed dataset with hourly values for 380 cities around the world, but because the data only spanned from January 1st 2020 to present and given the seasonal variations I had noticed, I decided to stick with the data I had that spanned several years.

![image](images/screenshots/no2screenshot.png)

![image](images/screenshots/pm25screenshot.png)

To make the graphs easier to interpret, I created a function that would generate variably sized moving window averages to smooth the data, which resulted in something much easier to process. I wrote a script for a plotting function that would generate a graph based on arguments passed in for the picklefile, the type of pollutant in question, the starting year (in case I wanted to plot a dataset that started later). 

I also spent some time researching the spread of COVID in the different U.S. states and countries I had picked monitoring stations for focus on, and created a dictionary to associate these dates with the picklefiles for the dataframes I had cleaned. 

![image](images/quarterly_plots/q1denverno2.png)

![image](images/quarterly_plots/q1wuhanno2.png)

![image](images/quarterly_plots/q1nycno2.png)

![image](images/quarterly_plots/q1parisno2.png)

![image](images/quarterly_plots/q1santiagono2.png)


















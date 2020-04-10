# Capstone 1: Airborne – Quarantine and Air Quality in Cities Around the World

For this project, I decided to investigate the effect that the COVID-19 epidemic and subsequent quarantines are having on air quality. After seeing numerous claims on social media that implied that the air and water were much cleaner in places that instituted a lockdown, I was curious to see if this effect was real and, if so, how closely the changes tracked the spread of the virus and government measures in responses.

These changes in air quality are significant not only as a curiosity or measure of how everyday activities affect the environment: both of the types of air pollution I focused on, NO<sub>2</sub> and PM<sub>2.5</sub> can contribute to chronic lung disease and lead to a lower quality of life and even premature death when present in sufficient quantities. 

This is especially significant during the coronavirus epidemic: <a href="https://projects.iq.harvard.edu/covid-pm" >a study released on April 8th</a>  found a significant link between long term PM<sub>2.5</sub> exposure and increased mortality rates from COVID-19.

## The Data

<a href="https://projects.iq.harvard.edu/covid-pm" >The World Air Quality Index Project </a> is a small organization based in China that collects readings from air quality monitoring stations around the world and standardizes them using E.P.A. guidelines into AQI, or Air Quality Index, units.

Unfortunately, the type of airborne particle that different stations report is not uniform – all of the stations I looked at report PM<sub>2.5</sub> concentrations (particulate matter 2.5 micrometers or less), but reporting of PM<sub>10</sub> (between 2.5 and 10 micrometers). NO<sub>2</sub> (Nitrogen Dioxide), CO (carbon monoxide), and SO<sub>2</sub> (sulfur dioxide) is sporadic. Many stations have daily values dating back to the beginning of 2014, but quite a few began reporting more recently, and often there are gaps in the reporting, ranging from a day or two to several months. 

I had to download the datasets individually, so I decided to focus on stations that had PM<sub>2.5</sub> and  NO<sub>2</sub> dating back to 2014. The other pollutants were too sporadic to find data for in the range of cities I wanted to look at. Most NO<sub>2</sub> comes from automobile traffic and in burning fossil fuels, so it seemed like a good pollutant to focus on in addition to PM<sub>2.5</sub>. 

Both NO<sub>2</sub> and PM<sub>2.5</sub> can contribute to chronic lung disease and lead to a lower quality of life and even premature death when present in sufficient quantities.  This is especially significant during the coronavirus epidemic: a study that was released on April 8th found a significant link between long term PM<sub>2.5</sub> exposure and increased mortality rates from COVID-19. 

The World Air Quality Index Project releases all of its data in AQI units. AQI units are not linearly scaled to concentrations of particulate matter, but rather to the relative levels of danger to human health.

The AQI values correspond to the scale below:


![image](images/misc/aqiscale.png)



<a href="https://www.airnow.gov/index.cfm?action=aqibasics.aqi" >Source: Airnow.gov</a>.

Originally the scale was designed to only go up to 500, but during episodes of extreme air pollution monitoring groups have extrapolated higher values.

For values of less than 100, 1 AQI for NO<sub>2</sub> corresponds to roughly 1 part per billion. Above 100, however, the scale is no longer linear.  

The values for PM<sub>2.5</sub> are scaled to breakpoints that are occasionally revised:

![image](images/misc/aqipm2.5.png)

[Source]("https://www.epa.gov/sites/production/files/2016-04/documents/2012_aqi_factsheet.pdf")

I decided to focus on a range of major cities in the United States along with a few relevant big cities outside of the U.S., including Wuhan, Beijing, and Milan, as well as a number of large cities in the southern hemisphere, for reasons that I will explain shortly. In addition to my local interest in Denver, I wanted to the ten largest all of the largest metropolitan areas in the U.S., but unfortunately many did not report consistent (or any) data to the World Air Quality Index Project for the types of pollution I decided to focus on. 

## Explanatory Data Analysis

I began by loading the CSV file for Denver into a dataframe and, after cleaning up the data I was interested in, generated a scatterplot for PM<sub>2.5</sub> and NO<sub>2</sub> concentrations: 

![image](images/scatterplots/scatterdenver.png)

Clearly, there is a big gap in second half of 2017, which was present accross all of the monitoring stations I checked out in Denver. 

More significantly, I realized that a major obstacle to discerning if COVID-19 had lead to a significant drop in these pollutants was that they exhibit seasonal variation, especially NO<sub>2</sub> AQI levels, which tend to spike in the winter and fall in the summer. I hypothesized that this was due to increases in burning gases that generate NO<sub>2</sub> during the winter, but could also be the result of inversions (which are when cold air is trapped beneath warm air, which happens more commonly in the winter.)

I subsequently created a pipeline script to clean other datasets and save them as picklefiles, and generated scatterplots for a number of other cities, including in the southern hemisphere where the pattern would likely be reversed if it was driven by weather. 

![image](https://upload.wikimedia.org/wikipedia/commons/0/02/Smog_over_Almaty.jpg)

Smog Over Almaty, Kazakhstan 
[Source](https://upload.wikimedia.org/wikipedia/commons/0/02/Smog_over_Almaty.jpg)


Cities in Europe and China in the northern hemisphere seemed to generally follow the same pattern of spiking pollution in the winter, while cities in the southern hemisphere were the opposite. Below I have plotted the readings for PM<sub>2.5</sub> and NO<sub>2</sub> in Madrid and Santiago de Chile, and you can see that their peaks and valleys are opposite. 

![image](images/comparative_scatterplots/scattersantiagomadrid.png)


I also realized that it was important to look back several years because certain events could cause big distortions in the data; for instance, consider the effect of the Austrailian wildfires on PM<sub>2.5</sub> readings in Sydney:

![image](images/scatterplots/scattersydney.png)

Given the periodicity of the concentrations, I thought it would make the most sense to plot the values for the first three months in different years to get a better sense how the trajectory of PM<sub>2.5</sub> and NO<sub>2</sub> was different. 

While I was working on initial exploration of the data earlier this week, the World Air Quality Project Index released a detailed dataset with hourly values for 380 cities around the world, but because the data only spanned from January 1st 2020 to present and given the seasonal variations I had noticed, I decided to stick with the data I had that spanned several years.

## Raw Data for PM<sub>2.5</sub> and NO<sub>2</sub> Daily Values in Denver

![image](images/quarterly_plots_raw/q1rawdenverpm25.png)

![image](images/quarterly_plots_raw/q1rawdenverno2.png)

To make the graphs easier to interpret, I created a function that would generate variably sized moving window averages to smooth the data, which resulted in something much easier to interpret. I wrote a script for a plotting function that would generate a graph based on arguments passed in for the picklefile, the type of pollutant in question, the starting year (in case I wanted to plot a dataset that started later), and the range of the window to be averaged for each data point. 

I also spent some time researching the spread of COVID in the different U.S. states and countries I had picked monitoring stations for focus on, and created a dictionary to associate these dates with the picklefiles for the dataframes I had cleaned. For each city, I added both the date for first COVID case in the state or (country if outside the U.S.) and the date that the government implemented a shelter in place or quarantine. Typically, the first COVID case would prompt a series of increasingly severe shut down measures (banning large events, shutting down schools, limiting meetings to groups of ~10) that culminated in a quarantine, so the time in between the two vertical lines should best be undestood as a gradient of increasing shutdown. 

## COVID and Air Quality EDA Results

## United States

### Denver

![image](images/quarterly_plots/q1denverpm25.png)

![image](images/quarterly_plots/q1denverno2.png)


### New York City

![image](images/quarterly_plots/q1nycpm25.png)

![image](images/quarterly_plots/q1nycno2.png)


### Los Angeles

![image](images/quarterly_plots/q1lapm25.png)

![image](images/quarterly_plots/q1lano2.png)

### Seattle

![image](images/quarterly_plots/q1seattlepm25.png)


![image](images/quarterly_plots/q1seattleno2.png)


### Oakland

![image](images/quarterly_plots/q1oaklandpm25.png)


![image](images/quarterly_plots/q1oaklandno2.png)

## China

### Wuhan

![image](images/quarterly_plots/q1wuhanpm25.png)


![image](images/quarterly_plots/q1wuhanno2.png)

### Beijing

![image](images/quarterly_plots/q1beijingpm25.png)

![image](images/quarterly_plots/q1beijingno2.png)

## Europe

### Milan, Italy
![image](images/quarterly_plots/q1milanpm25.png)


![image](images/quarterly_plots/q1milanno2.png)

### Paris, France

![image](images/quarterly_plots/q1parispm25.png)


![image](images/quarterly_plots/q1parisno2.png)

### Madrid, Spain

![image](images/quarterly_plots/q1madridpm25.png)


![image](images/quarterly_plots/q1madridno2.png)


## Southern Hemisphere

### Santiago, Chile

![image](images/quarterly_plots/q1santiagopm25.png)

![image](images/quarterly_plots/q1santiagono2.png)

### São Paulo, Brazil

![image](images/quarterly_plots/q1saopaulopm25.png)

![image](images/quarterly_plots/q1saopaulono2.png)

### Sydney, Australia

![image](images/quarterly_plots/q1sydneypm25.png)

![image](images/quarterly_plots/q1sydneyno2.png)

# Conclusion

For almost every single city I looked at, the values for NO<sub>2</sub> and PM<sub>2.5</sub> were lower in 2020 after the implementation of shelter in place/quarantine orders than they were in any of the previous years in the data set. However, the difference appeared to be stronger for NO<sub>2</sub> than for PM<sub>2.5</sub>, which makes sense as NO<sub>2</sub> is almost all caused by human activity, whereas high PM<sub>2.5</sub> levels can also arise from natural events like forest fires and dust storms. 

It will be interesting to check on these series in a few weeks or months and see if the low levels persist throughout the quarantine period, and perhaps conduct statistical tests when there is more data for the quarantine periods. 

While the dangers to human health from air pollution are often a result of long term exposure, hopefully the decreases that are taking place across the world will put some downward pressure on the mortality rate from this pandemic. 





















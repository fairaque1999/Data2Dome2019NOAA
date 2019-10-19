
# Data

For this exercise we will be using climate data from the Helsinki-Vantaa airport station.
For these problems, we have daily observations obtained from the [NOAA Global Historical Climatology Network](https://www.ncdc.noaa.gov/cdo-web/search?datasetid=GHCND).
The file was downloaded using the "Custom GHCN-Daily Text" output format, including the geographic location, precipitation (`PRCP`), average temperature (`TAVG`), maximum temperature (`TMAX`), and minimum temperature (`TMIN`).
The file for this problem is exactly as available from the NOAA website. The file is loaded into the Binder Jupyter Notebook Environment you'll be using for this exercise.
Note once again that temperatures in this dataset are given in degrees Fahrenheit, as noted in the [sample data file](ftp://ftp.ncdc.noaa.gov/pub/data/cdo/samples/GHCND_sample_pdf.pdf).

# A Bonus Dataset! (And ways to analyse it)

Download your own data (daily summaries for years **1959-2017 August**) for **Sodankyla Lokka** (notice the place name should be without `ä` letter), from [NOAA Climate Data Online Search](https://www.ncdc.noaa.gov/cdo-web/search?datasetid=GHCND).
Make sure to click on starting day (and ending day) in the date selection panel after changing year!
After you have searched, click “Add to cart” for a selected station, then go to cart. Select the ``Custom GHCN-Daily Text`` -format for the resulting output file and hit continue.

- From ``Station Detail & Data Flag Options`` choose two of the following attributes: Station Name, Geographic Location. **Notice:** Do **NOT** include data flags because it makes the data difficult to read. Use **Standard** units.

- Take also Precipitation and Temperature which are under a separate button below. 
- From the next page, add your own email address where the weather data will be sent after a short moment.

Write your codes into a separate `weather_comparisons.py` file.

After you have downloaded the data. you should first,

- Calculate the average temperature using columns `TMAX` and `TMIN` and insert those values into a new column called `TAVG`.

Next, you should use the approaches learned during the workshop:

- Calculate the temperature anomalies in Sodankyla, i.e. the difference between referenceTemps and the average temperature for each month. 
- Calculate the monthly temperature differences between Sodankyla and Helsinki stations
- How different the summer temperatures (June, July, August) have been between Helsinki and Sodankyla station?
    - Calculate the monthly differences into a DataFrame and save it (as `CSV` file) into your own Exercise repository for this week
    - What were the summer mean temperatures for both of these stations?
    - What were the summer standard deviations for both of these stations?

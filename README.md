# Data Munging using Python

## Objectives:
I will try to make usable a real data source: **NASA's historic measurements of the Earth's surface temperatures**:
1. Download raw data.
1. Write a Python program to clean up (i.e. munge) the data and save it into a standard Comma-Separated Values (CSV) format text file.
1. Write a second Python program to do some simple analysis of the data in the CSV file.

### Data
NASA's [GISS Surface Temperature Analysis web site](https://data.giss.nasa.gov/gistemp/) gives an overview of the data set - they publish recordings in the change of the Earth's surface temperature going back to the year 1880.  
- The numbers do not represent actual temperature readings, but rather represent temperature *anomalies*.


Source: [the raw data in fixed-width column format](https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.txt).
- this is saved in the directory called 'Data'. 


### Munging
Munging will be taken care of in a program called `munge.py`, in which I clean up the raw data and save it into a CSV-formatted file named `clean_data.csv` within the `data` directory of this repository.

Issues I addressed:
- Removed the many lines at the top and bottom of the file that contain notes and not the raw data.
- Removed the column headings are repeated on multiple lines throughout the file, keeping the first one.
- Removed the blank lines in the middle of the data.
- Missing data: there was only 1 piece of missing data which I chose to simply omit since it is a single missing record that I believe will be absorbed in the grand picture. 
- The temperature anomalies in this data are given in 0.01 degrees Celsius.  I converted these to Farenheit, the US standard unit of temperature for greater understandability. I also rounded it to 1 decimal place for ease of readability. 
- This data is in *fixed-width column format*, there are inconsistent numbers of spaces separating the numeric values. **you optionally may want to standardize how many spaces are used as separators**.

All of this data was saved in a new file, `clean_data.csv`.

### Analyzing 
I performed some aggregate statistics on the data in the file named `analyze.py`. This program: 

- Opens up the cleaned up data file, `clean_data.csv` and imports it using Python's `csv` module.
- Outputs the average temperature anomaly in degrees Farenheit for each decade since 1880.  For example, output the average temperature anomaly for the decades:
    - 1880 to 1889
    - 1890 to 1899
    - 1900 to 1909
    - ...and so on.

# Raw Data Munging

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
- there is missing data indicated with `***` - figure out how to **handle missing data so that your analyses are correct**.
- the temperature anomalies in this data are given in 0.01 degrees Celsius.  **Convert temperature anomalies to Farenheit**, the US standard unit of temperature:
    - the formula to do this can be found within the data set
    - format the results so that there's one decimal place (use [format](https://docs.python.org/3/library/functions.html#format) with `.1f` as the second argument)
- since this data is in *fixed-width column format*, there are inconsistent numbers of spaces separating the numeric values... **you optionally may want to standardize how many spaces are used as separators**.
- you are welcome to do **any additional cleanup that helps** you analyze the data in the next step.

Your program must do this cleanup and transformation in a way that is repeatable.  If we were to take the original data file from NASA and run your `munge.py` program on it, these issues would all be resolved in a new file, `clean_data.csv`.

### Part 3: Analyze it
I performed some aggregate statistics on the data.


import csv

#open file
f = open('clean_data.csv', 'r')
csvreader= csv.reader(f)
#add rows to new list
rows = []
for row in csvreader:
    #sorting only digit numbers
    if row[0].isdigit():
        rows.append(row)

#initialize year counter variable 
counter = 0
end_counter = 0
#initialize temporary tot variable
tot = 0
#initialize missing val variable
na_num = 0
#dictionary to store averages:
averages = {}
decade = 1880

#n for 10 decades
n = 10*(len(rows[0])-1)
#go through dataset
for record in rows[:]:
    counter += 1
    end_counter += 1
    
    #going through each year's records, ignoring the year column.
    #12 becuase we are only averaging changes in the 12 months (columns 1-12); +1 because range is not end-inclusive
    for item in record[1:12+1]:
        #print(type(item))
        try: 
            #convert to int
            item = int(item)
            #add to total
            tot += item
        
        #accounting for missing values
        except:
            #In this case there are no actual missing values that we need no account for, but if this is to be 
            #replicable I thought I'd add some contingency code that would just erase it from the dataset. 
            na_num += 1
         
    #once at end of decade:
    if counter == 10:
        #calculate average
        avg = format(tot/(n - na_num), '.3f')
        #creating dictionary key
        temp = str(decade) + ' to ' + record[0]
        #add to dictionary
        averages.update({temp: avg})
        
        #reset items
        decade += 10
        counter = 0
        tot = 0
        temp = ''
        na_num = 0
    
    #at the last rows if len(rows) not divisible by 10.
    if end_counter == len(rows):
        #calculate average
        avg = format(tot/(n - na_num), '.2f')
        temp = str(decade) + ' to ' + str(decade + counter -1)
        #add to dictionary
        averages.update({temp: avg})
        
print(averages)
f.close()
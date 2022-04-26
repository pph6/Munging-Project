import re

f = open("Data.txt", "r")

data = f.readlines()
data2 = ''

#cleaning data, getting rid of extra lines above and below.

#initialize switch variable to help us ignore year + '\n' lines when writing new data
switch = 0

for line in data:
    
    if line[0] == 'Y':
        #"turn on" switch to ignore year lines.
        if switch == 0:
            switch = 1
            data2 += (re.sub(" +", ',', line))
                         
    elif line[0].isdigit():
        data2 += (re.sub(" +", ',', line))

#split data into list where each item in list is a string = 1 year's record.
data3 = data2.split('\n')

#some more data cleaning
for x in range(len(data3)):
    #split each year into list where each line is a string = 1 month's record
    data3[x] = data3[x].split(',')
    
    #get rid of redundant year "column" values at end
    data3[x].pop()
    
    #converting to floats
    for y in range(1, len(data3[x])):
        
        try:
            #put formatted verson into temp variable for transfer; 
            #divide by 100 to find temp in C, formatting to 1 decimal point
            temp = format(float((data3[x][y])/100)*1.8, '.1f')
            data3[x][y] = temp
        
        #to account for missing values that can't be converted
        except:
            continue
            
    
    #turning months back into year record item.      
    data3[x] = ','.join(data3[x])
    data3[x] = data3[x] + '\n'
#turning years into total record item.
data3 = ''.join(data3)


#dropping the last extra \na
data3 = data3[:-2]

#write data to new clean file
output_f = open('clean_data.csv', 'w')
output_f.write('Land-Ocean: Global Means\n')
output_f.write(data3)
output_f.close()
    
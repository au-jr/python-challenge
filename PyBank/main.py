# If I've done it right, the code should run just fine if the budget data is expanded or reduced for further analysis. I've not referenced any static
# values, instead left all variables referring to dynamic rows in the .csv file 

import os
import csv

# buckets to hold our lists and counts
month_count = [] # count of months
net_pl_bucket = [] # profit/loss each month
pl_change = [] # delta of profit/loss each month
average_change = [] # average of the delta


# deifne the csv file for the source data

budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter=",")

    # we don't want to read the header
    
    csv_header = next(csv_file)
    
    # read through each row and add the month (row 1, indexed as row[0]) to the bucket to hold month count
    for row in csv_reader:
    
        # Adding to the bucket to count months
        month_count.append(row[0])
        
        # Adding to the bucket to record the monthly profit/loss
        net_pl_bucket.append(int(row[1]))
        
    
    # Creating a list of our profit/loss bucket, minus the first index to use to create a comparison table to calculate the delta profit/loss each month   
    net_pl_next = net_pl_bucket[1 : len(net_pl_bucket) + 1]
    
    # Source 2 - Last element in a list. Storing the final months p/l as a variable to append our comparison table to calculate delta p/l
    net_pl_last = net_pl_bucket[-1]
    
    # Adding the identical last value of our comparison table, becuse there is no change last month to last month, so should equal 0 in the delta equation
    net_pl_next.append(net_pl_last)
    
    # Zipped together the next month with the previous month to calculate the delta profit/loss, i.e. Jan-10 1088983 --> Feb-10 -354534 was a loss of
    # -1443517, so  in the next line we calculate Feb-10 (-354534) - Jan-10(1088983) to get a loss of -1443517 Jan --> Feb. 
    pl_change = list(zip(net_pl_next, net_pl_bucket))
    
   
    for row in pl_change:
        average_change.append(row[0] - row[1])
        
        # We use the length of the bucket -1 because there's no change to be recorded in the last month (86). This stores the average profit/loss change
        pl_average = sum(average_change) / (len(net_pl_bucket) - 1)
    
    # If next month minus last month is positive, then there was a net increase month to month. We're finding the largest net increase.
    pl_change_inc = average_change.index(max(average_change))
    
    # If next month minus last month is negative, then there was a net decrease month to month. We're finding the largest net increase.
    pl_change_dec = average_change.index(min(average_change))
    

        
# printing the length of the list 'month_count'
    print("================================================================================================================")
    print("The number of months in the data:")
    print(len(month_count))
    
#Prints the sum of the p/l firugre each month   
    print("================================================================================================================")
    print("Total profit/loss over the period:")
    print(f'${sum(net_pl_bucket)}')
    
#Source 1 - Prints the average of the month to month change, rounded to 2 decimal places
    print("================================================================================================================")
    print("The average change to profit/loss each month:")
    print(f'${round(pl_average,2)}')
    
# Prints the greatest increase        
    print("================================================================================================================")
    print("The greatest increase was:")
    print(f'{month_count[pl_change_inc + 1]} ${max(average_change)}')
    
# Prints the greatest decrease    
    print("================================================================================================================")
    print("The greatest decrease was:")
    print(f'{month_count[pl_change_dec + 1]} ${min(average_change)}')
    

mon_length = (f'{len(month_count)}')
total_pl = (f'${sum(net_pl_bucket)}')
avg_pl = (f'${round(pl_average,2)}')
great_inc = (f'{month_count[pl_change_inc + 1]} ${max(average_change)}')
great_dec = (f'{month_count[pl_change_dec + 1]} ${min(average_change)}')

# Source 3. Write to .txt file

file_path = "analysis/PyBank_analysis.txt"

file = open(file_path, 'w')

file.write("==========================================")
file.write("\n" + "The number of months in the data:")
file.write("\n" + mon_length)
file.write("\n" + "")

file.write("==========================================")
file.write("\n" + "Total profit/loss over the period:")
file.write("\n" + total_pl)
file.write("\n" + "")

file.write("==========================================")
file.write("\n" + "The average change to profit/loss each month:")
file.write("\n" + avg_pl)
file.write("\n" + "")

file.write("==========================================")
file.write("\n" + "The greatest increase was:")
file.write("\n" + great_inc)
file.write("\n" + "")

file.write("==========================================")
file.write("\n" + "The greatest decrease was:")
file.write("\n" + great_dec)

file.close() 
# The data we need to retrive
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. The winner of the election based on popular vote

# import datetime as dt
# now = dt.datetime.now()
# print(now)
# print(f'The time right now is {now}. ')

# import csv
# import os

# file_to_load = os.path.join("Resources","election_results.csv")
# with open(file_to_load) as election_data:

#     print(election_data)

# #Create File name
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using with statement to open the file as text file
# with open (file_to_save, 'w') as txt_file:

# # Write data to the file
#     txt_file.write("Counties in the Election\n---------------------------------\nArapahoe\nDenver\nJefferson")

# import csv
# import os

# # Assign a variable to load a file from a path
# file_to_load = os.path.join("Resources", "election_result.csv")

# # Assign a variable to save the file to the path
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Open the election results and read the file
# with open(file_to_load) as election_data:

# # To read and analyze data 
# file_reader = csv.reader(election_data)

# # Print each row of csv file

# for row in file_reader:
#         print(row)


# # txt_file.close()

import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Print the header

    headers = next(file_reader)
    print(headers)

# #Print each row in CSV file
#     for row in file_reader:
#         print(row)



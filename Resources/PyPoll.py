#Add our dependencies
import csv
from email import header
import os
from wsgiref import headers

#Assign a variable for the file to load the path
file_to_load = os.path.join("election_results.csv")

#Create a fiename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:

#To do: read and analyze the data here
    file_reader = csv.reader(election_data)

#Read and print the header row
    headers = next(file_reader)
    print(headers)

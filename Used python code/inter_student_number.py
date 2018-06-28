######################################################################################
# print amount of international students and total amount per university. And also
# calculates the percentage of international students.

######################################################################################
import csv
import pandas as pd
import numpy

data = pd.read_csv("../DATA/ranking_with_country_2016.csv")
counter = 0
for fte in data['fte_students']:
    percentage = data['international_students'][counter]
    international_students_number = fte*percentage
    print(fte, percentage, international_students_number)
    data.set_value(counter, "international_students_number", international_students_number)
    counter += 1
data.to_csv("../DATA/university_ranking_2016.csv", index=False)

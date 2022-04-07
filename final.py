import csv

bright_stars = []
dwarf_stars = []

with open ("bright_stars.csv","r") as f :
    csvreader = csv.reader(f)
    for row in csvreader :
        bright_stars.append(row)
        
with open ("star_data_sorted.csv","r") as f :
    csvreader = csv.reader(f)
    for row in csvreader :
        dwarf_stars.append(row)
        
header1 = bright_stars[0]
star_data1 = bright_stars[1:]

header2 = dwarf_stars[0]
star_data2 = dwarf_stars[1:]

headers = header1 + header2

star_data = []
for index , datarow in enumerate(star_data1):
    star_data.append(star_data1[index]+star_data2[index])

with open ("final_csv","a+") as f :
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)
import csv

with open('user.csv','r',encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['이름'],row['직업'])

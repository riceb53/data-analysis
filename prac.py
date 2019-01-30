# with open("/Users/Apprentice/documents/new-york-city-current-job-postings/nyc-jobs.csv") as f:
#     # print(f.size())
#     index = 0
#     for line in f:
#       print()
#       print(line)
#       index += 1
#     print(index)


import csv

with open('/Users/Apprentice/documents/new-york-city-current-job-postings/nyc-jobs.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    highest_salary = 0
    firstline = True

    for row in readCSV:
        if firstline:
          firstline = False
          continue
        print()
        # print(int(row[11]))
        # print(row[10])
        if highest_salary < float(row[11]):
          highest_salary = float(row[11])
        # print(row[12])
        # print(row[0],row[1],row[2],)
    print(highest_salary)

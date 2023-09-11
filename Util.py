import csv


def get_data_info():
    gpa_group = {}
    hour_group = {}

    # extract data from csv
    with open('gpa_study_hours.csv') as csv_file:
        read = csv.reader(csv_file, delimiter=',')
        read.__next__()     # skip first line. Header row
        for row in read:
            gpa = float(row[0])
            hour = float(row[1])

            # sort by gpa
            if not gpa_group.get(gpa):
                gpa_group[gpa] = [hour]
            else:
                gpa_group[gpa].append(hour)

            # sort by hour
            if not hour_group.get(hour):
                hour_group[hour] = [gpa]
            else:
                hour_group[hour].append(gpa)

    return gpa_group, hour_group

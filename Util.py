import collections
import csv


def dict_to_pairs(dct):
    """
    for each value associated to a key, create a pair

    pairs = {(key i, val j), (key i, val j), (key i+1, val j+1), (key i+1, val j+1)...}

    :return: pairs[]
    """
    pairs = []

    for key in dct:
        for item in dct[key]:
            pairs.append((key, item))

    return pairs


def get_xs(pairs):
    xs = []

    for pair in pairs:
        xs.append(pair[0])
    return xs


def get_ys(pairs):
    ys = []

    for pair in pairs:
        ys.append(pair[1])
    return ys


def get_data_info():
    """
    extract data from csv file into dictionaries

    returns 2 dictionaries respectively sorted by gpa and hours
    dictionaries are sorted in ascending order by key

    :return: gpa_group{}, hour_group{}
    """
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

    return collections.OrderedDict(sorted(gpa_group.items())), collections.OrderedDict(sorted(hour_group.items()))

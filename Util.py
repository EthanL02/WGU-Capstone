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


def sort_by_y(pairs):
    for i, left in enumerate(pairs):
        smallest_val = left
        smallest_i = i
        for j, right in enumerate(pairs[i:], start=i):
            if right[1] < smallest_val[1]:
                smallest_val = right
                smallest_i = j
        if left != smallest_val:
            pairs[i], pairs[smallest_i] = pairs[smallest_i], pairs[i]

    return pairs


def get_pie_chart_from_data(pairs):
    dct = {}

    for pair in pairs:
        item = pair[0]
        if item not in dct.keys():
            dct[item] = 1
        else:
            dct[item] += 1

    total = 0
    out = [["other", 0]]

    for val in dct.values():
        total += val
    for key, val in dct.items():
        perc = val / total

        other_title = 0
        if perc < .015:
            out[0][1] += perc
        else:
            out.append([key, perc])

    return out


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

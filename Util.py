import tkinter as tk
import collections
import csv


def get_dict_keys(dct):
    out = []

    for item in dct.keys():
        val = round(item, 1)
        if val not in out:
            out.append(val)
    return out


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
    """
    sorts an array in ascending order by the y values

    :param pairs: array with format [[x1, y1], [x2, y2],...]
    :return: sorted array
    """
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


def get_pie_chart_from_array(arr, other=False):
    """
    transform array into pie chart readable data
    records each occurrence of data then translates into percentage
    percentages too small for the graph are categorized into an 'other' category optionally

    :param other: boolean to combine small data, False by default
    :param arr: array of pie chart data in the format [val1, val2,...]
    :return: pie chart readable array in the format [[label1, percentage1], [label2, percentage2],...]
    """
    dct = {}

    # extract occurrences
    for a in arr:
        if a not in dct.keys():
            dct[a] = 1
        else:
            dct[a] += 1

    total = 0
    out = [["other", 0]]  # initialize small data grouping

    # get total amount
    for val in dct.values():
        total += val
    for key, val in dct.items():
        perc = val / total

        other_title = 0
        if perc < .015 and other:
            # data grouped together
            out[0][1] += perc
        else:
            out.append([key, perc])

    if out[0][1] == 0:
        del out[0]
    out = sort_by_y(out)

    return out


def get_pie_chart_from_data(pairs, other=False):
    """
    transform array into pie chart readable data
    records each occurrence of data then translates into percentage
    percentages too small for the graph are categorized into an 'other' category optionally

    :param other: boolean to combine small data, False by default
    :param pairs: array of pie chart data in the format [[key1, val1], [key2, val2],...]
    :return: pie chart readable array in the format [[label1, percentage1], [label2, percentage2],...]
    """
    dct = {}

    # extract occurrences
    for pair in pairs:
        item = round(pair[0], 1)  # group by left side
        if item not in dct.keys():
            dct[item] = 1
        else:
            dct[item] += 1

    total = 0
    out = [["other", 0]]    # initialize small data grouping

    # get total amount
    for val in dct.values():
        total += val
    for key, val in dct.items():
        perc = val / total

        other_title = 0
        if perc < .015 and other:
            # data grouped together
            out[0][1] += perc
        else:
            out.append([key, perc])

    if out[0][1] == 0:
        del out[0]
    out = sort_by_y(out)

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
    data = {}

    # extract data from csv
    with open('gpa_study_hours.csv') as csv_file:
        read = csv.reader(csv_file, delimiter=',')
        read.__next__()     # skip first line. Header row
        for row in read:
            gpa = float(row[0])
            hour = float(row[1])

            # sort by gpa
            if not data.get(gpa):
                data[gpa] = [hour]
            else:
                data[gpa].append(hour)

    return collections.OrderedDict(sorted(data.items()))

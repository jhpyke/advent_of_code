import pandas as pd
from pandas import DataFrame


input_data = pd.read_csv('./2024/01/data/input.txt', header=None, sep="   ")


def column_cleaner(input_column: DataFrame) -> DataFrame:
    clean_copy = input_column.copy()
    clean_copy.sort_values(ascending=True, inplace=True, ignore_index=True)
    clean_copy.reset_index(drop=True) # This is here to achieve what ignore_index=True should have done in principle, but hasn't
    return clean_copy

first_list = column_cleaner(input_data[0])
second_list = column_cleaner(input_data[1])
diff = abs(first_list - second_list)
total_diff = diff.sum()

#Part 2

def similarity_scorer(first_list: DataFrame, second_list: DataFrame) -> int:
    frequency_dict = {}
    similarity_score = 0
    # Second list we only care about the frequencies associated with each value
    for value in second_list:
        if value in frequency_dict:
            frequency_dict[value] += 1
        else:
            frequency_dict[value] = 1\
    # First list we care about the value X the frequency of that value in the second list
    for value in first_list:
        if value in frequency_dict:
            similarity_score += (value*frequency_dict[value])
        else:
            continue
    return similarity_score


print("The total difference between the two lists is: ", total_diff, "\nThe similarity score between the two lists is: ", similarity_scorer(first_list, second_list))

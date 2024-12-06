import pandas as pd
from pandas import DataFrame

with open('./2024/02/data/input.txt', 'r') as f:
    reports = f.read().splitlines()


def safety_checker(reports: list) -> dict:
    reports_processed = {"safe_reports": 0, "unsafe_reports": 0}
    for report in reports:
        report_list = report.split(" ")
        current_diff = 0
        last_diff = -999
        for i in range(0, len(report_list)-1):
            current_diff = int(report_list[i+1]) - int(report_list[i])
            if abs(current_diff) > 3 or abs(current_diff) < 1: # This is a condition for an unsafe report
                reports_processed["unsafe_reports"] += 1
                break
            elif last_diff == -999: # This is the first iteration
                last_diff = current_diff
                continue
            else:
                if current_diff * last_diff < 0: # Implies the gradient has changed as the product of the two is negative
                    reports_processed["unsafe_reports"] += 1
                    break
                elif i == len(report_list)-2: #We've hit the final values and none of our failure conditions have been met
                    reports_processed["safe_reports"] += 1
                    break
                else:
                    continue
    return reports_processed
            
        
safety_checker(reports)

def safety_checker_with_dampener(reports: list) -> dict:
    reports_pre_processed = []
    report_number = 0
    for report in reports:
        report_list = report.split(" ")
        current_diff = 0
        current_gradient = 0
        last_gradient = 0
        print(report_list)
        for i in range(0, len(report_list)-1):
            current_diff = int(report_list[i+1]) - int(report_list[i])
            current_gradient = current_diff/(abs(current_diff) + 0.0000000001)
            if abs(current_diff) > 3 or abs(current_diff) < 1:
                try:
                    potential_diff = int(report_list[i+2]) - int(report_list[i])
                    if abs(potential_diff) > 3 or abs(potential_diff) < 1: # Next value must be problem
                        report_list.pop(i+1)
                        break
                    else:
                        report_list.pop(i)
                        break
                except IndexError:
                    potential_diff = int(report_list[i+1]) - int(report_list[i-1])
                    if abs(potential_diff) > 3 or abs(potential_diff) < 1: # Current value must be problem
                        report_list.pop(i+1)
                        break
                    else:
                        report_list.pop(i)
                        break
            elif current_gradient * last_gradient < 0: #Gradient has changed sign
                try:
                    potential_diff = int(report_list[i+2]) - int(report_list[i])
                    potential_gradient = potential_diff/(abs(potential_diff) + 0.0000000001)
                    if potential_gradient * last_gradient > 0: # Next value must be problem
                        report_list.pop(i+1)
                        break
                    else:
                        report_list.pop(i)
                        break
                except IndexError:
                    potential_diff = int(report_list[i+1]) - int(report_list[i-1])
                    potential_gradient = potential_diff/(abs(potential_diff) + 0.0000000001) # To avoid division by zero
                    potential_last_diff = int(report_list[i-1]) - int(report_list[i-2])
                    potential_last_gradient = potential_last_diff/(abs(potential_last_diff)  + 0.0000000001)
                    if potential_gradient * potential_last_gradient > 0: # Current value must be problem
                        report_list.pop(i)
                        break
                    else:
                        report_list.pop(i+1)
                        break
        report_dampened = " ".join(report_list)
        report_number += 1
        print(report_number, "processed")
        reports_pre_processed.append(report_dampened)
        print(len(reports_pre_processed))
    return safety_checker(reports_pre_processed)

safety_checker_with_dampener(reports)
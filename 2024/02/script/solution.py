import pandas as pd
from pandas import DataFrame

with open('./2024/02/data/input.txt', 'r') as f:
    reports = f.read().splitlines()

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
            elif i == len(report_list)-1: #We've hit the final value and none of our failure conditions have been met
                reports_processed["safe_reports"] += 1
                break
            else:
                continue

def safety_checker(reports: list) -> dict:
    reports_processed = {"safe_reports": 0, "unsafe_reports": 0}
    for report in reports:
        report_list = report.split(" ")
        current_diff = 0
        last_diff = -999
        print(report_list)
        for i in range(0, len(report_list)-1):
            current_diff = int(report_list[i+1]) - int(report_list[i])
            if abs(current_diff) > 3 or abs(current_diff) < 1: # This is a condition for an unsafe report
                print("This failed, as the current diff is: ", current_diff, "which is not between 1 and 3")
                reports_processed["unsafe_reports"] += 1
                break
            elif last_diff == -999: # This is the first iteration
                last_diff = current_diff
                continue
            else:
                if current_diff * last_diff < 0: # Implies the gradient has changed as the product of the two is negative
                    print("This failed, as the current diff is: ", current_diff, "and the last diff is: ", last_diff, "which have different signs")
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
    reports_processed = {"safe_reports": 0, "unsafe_reports": 0}
    results_advanced = {}
    report_number = 0
    for report in reports:
        report_list = report.split(" ")
        report_number += 1
        current_diff = 0
        last_diff = -999
        is_dampened = False
        print(report_list)
        for i in range(0, len(report_list)-1):
            current_diff = int(report_list[i+1]) - int(report_list[i])
            if abs(current_diff) > 3 or abs(current_diff) < 1: # This is a condition for an unsafe report
                if i == len(report_list)-2: #we've fallen on the last value, so we can safely dampen this
                    reports_processed["safe_reports"] += 1
                    results_advanced[report_number] = {"dampened": True, "safe": True}
                    break
                elif is_dampened: #We've already dampened this report so it fails
                    reports_processed["unsafe_reports"] += 1
                    results_advanced[report_number] = {"dampened": True, "safe": False}
                    break
                else: #Try dampening the diff
                    potential_diff = int(report_list[i+2]) - int(report_list[i])
                    if abs(potential_diff) > 3 or abs(potential_diff) < 1:
                        reports_processed["unsafe_reports"] += 1
                        results_advanced[report_number] = {"dampened": True, "safe": False}
                        break
                    else:
                        is_dampened = True
                        continue
            elif last_diff == -999: # This is the first iteration
                last_diff = current_diff
                continue
            else:
                if current_diff * last_diff < 0: # Implies the gradient has changed as the product of the two is negative
                    if i == len(report_list)-2: #we've fallen on the last value, so we can safely dampen this
                        reports_processed["safe_reports"] += 1
                        results_advanced[report_number] = {"dampened": True, "safe": True}
                        break
                    elif is_dampened: #We've already dampened this report so it fails
                        reports_processed["unsafe_reports"] += 1
                        break
                    else: #Try dampening
                        potential_diff = int(report_list[i+2]) - int(report_list[i])
                        if potential_diff * last_diff < 0:
                            reports_processed["unsafe_reports"] += 1
                            results_advanced[report_number] = {"dampened": True, "safe": False}
                            break
                        else:
                            is_dampened = True
                            continue
                elif i == len(report_list)-2: #We've hit the final values and none of our failure conditions have been met
                    reports_processed["safe_reports"] += 1
                    results_advanced[report_number] = {"dampened": False, "safe": True}
                    break
                else:
                    continue
    return reports_processed, results_advanced

results, advanced = safety_checker_with_dampener(reports)
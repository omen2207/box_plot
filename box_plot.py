import csv

sepal_length = []
file_path = r'C:\Users\bhilw\OneDrive\Documents\DM\heart.csv' 

with open(file_path, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        sepal_length.append(float(row['chol'])) 

def calculate_quartiles(data):
    data = sorted(data)
    n = len(data)
    Q2 = data[n//2] if n % 2 != 0 else (data[n//2 - 1] + data[n//2]) / 2
    Q1 = data[n//4] if n % 2 != 0 else (data[n//4 - 1] + data[n//4]) / 2
    Q3 = data[(3*n)//4] if n % 2 != 0 else (data[(3*n)//4 - 1] + data[(3*n)//4]) / 2
    return Q1, Q2, Q3

Q1, Q2, Q3 = calculate_quartiles(sepal_length)
IQR_len = Q3 - Q1
lower_bound_len = Q1 - 1.5 * IQR_len
upper_bound_len = Q3 + 1.5 * IQR_len
outliers_len = [x for x in sepal_length if x < lower_bound_len or x > upper_bound_len]
print(f" Q1: {Q1}, Median (Q2): {Q2}, Q3: {Q3}")
print(f"IQR: {IQR_len}")
print(f"Lower Bound whiskers: {lower_bound_len}")
print(f"Upper Bound whiskers: {upper_bound_len}")
print(f"Outliers: {outliers_len}")

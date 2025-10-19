# ================================================================
# Project 1: Python & NumPy Fundamentals
# Student Name: Guga Gagloshvili
# Student ID: 01401148353
# Submission Date: October 19, 2025
#
# Honor Code Statement:
# "I certify that this work is my own and I have not plagiarized."
# ================================================================

# ================================================================
# Table of Contents
# 1. Task 1 – Python Data Structures & Control Flow
# 2. Task 2 – NumPy Arrays & Operations
# 3. Task 3 – Applied Data Analysis
# ================================================================

# -------------------------------
# Task 1 – Python Data Structures & Control Flow
# -------------------------------
students = {
    "S001": {"name": "Guga", "scores": [88, 91, 79, 85], "attendance": 28},
    "S002": {"name": "Giorgi", "scores": [75, 80, 78, 74], "attendance": 26},
    "S003": {"name": "Anita", "scores": [95, 86, 92, 94], "attendance": 11},
    "S004": {"name": "Elene", "scores": [61, 72, 72, 69], "attendance": 23},
    "S005": {"name": "Ilia", "scores": [84, 87, 90, 85], "attendance": 3},
    "S006": {"name": "Daviti", "scores": [5, 85, 88, 7], "attendance": 13},
    "S007": {"name": "Tornike", "scores": [73, 74, 80, 76], "attendance": 25},
    "S008": {"name": "Temuri", "scores": [37, 10, 13, 91], "attendance": 30},
    "S009": {"name": "Mariami", "scores": [21, 79, 85, 88], "attendance": 28},
    "S010": {"name": "Luka", "scores": [73, 68, 48, 75], "attendance": 10}
}

#calculate average
def calculate_avarage(scores: list):
    average = sum(scores) / len(scores)  #formula of average
    return  round(average, 2)  # rounds the number to 2 decimal
#assign Grade
def assign_grade(average: float):
    if average >= 90:
        return "A"
    elif average >=80:
        return "B"
    elif average >=70:
        return "C"
    elif average >=60:
        return "D"
    else:
        return "F"
#failed or passed
def check_eligibility(student_dict: dict, total_classes: int):
    avg = round(calculate_avarage(student_dict['scores']),2)  #calculate avg of student scores
    attendance_rate = round(student_dict['attendance'] / total_classes,2)  # calculate attendance rate based on student attendance and total classes
    if avg >= 60 and attendance_rate >= 0.75:
        return (True, 'Good Job')
    elif avg < 60:
        return (False, f'Not enough score ({avg})')
    else:
        return (False, f'Not enough attendance ({student_dict['attendance']}/{total_classes})')

#top performes
def find_top_performers(students: dict, n: int):
    top_n_students = []
    for a in students:
        top_n_students.append([calculate_avarage(students[a]['scores']), students[a]['name']])
    return sorted(top_n_students)[-n:]   #sort the list and get last n elements as it is sorted ascending
#report
def generate_report(students: dict):
    total_students = len(students)
    passed_count = 0
    failed_count = 0
    all_scores = []
    total_attandance = 0

    for a in students:
        avg = calculate_avarage(students[a]['scores'])
        all_scores.append(avg)
        total_attandance += students[a]['attendance']

        passed, _ = check_eligibility(students[a], 30)
        if passed:
            passed_count += 1
        else:
            failed_count += 1

    class_avarage = round((sum(all_scores) / total_students), 2)
    highest_score = max(all_scores)
    lowest_score = min(all_scores)
    avg_attendance_rate = round((total_attandance * 100 / (total_students * 30)), 2)
    report = {'total_students' : total_students,
              'passed_count' : passed_count,
              'failed_count' : failed_count,
              'class_average' : class_avarage,
              'highest_score' : highest_score,
              'lowest_score' : lowest_score,
              'average_attendance_rate' : avg_attendance_rate
              }
    return report
report = generate_report(students)

top_performers = find_top_performers(students, 5)
grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
failed_students = []

for sid, info in students.items():
    avg = calculate_avarage(info['scores'])
    grade = assign_grade(avg)
    grades[grade] += 1
    passed, reason = check_eligibility(info, 30)
    if not passed:
        failed_students.append((sid, info['name'], reason, grade))

print("=== COURSE STATISTICS ===")
for key, value in report.items():
    print(f'{key.replace('_', ' ').title()}: {value}')


print("\n=== TOP 5 PERFORMERS ===")
for avg, name in reversed(top_performers):
    print(f'{name}: Average = {avg}, Grade = {assign_grade(avg)}')


print("\n=== STUDENTS WHO FAILED ===")
if failed_students:
    for sid, name, reason, grade in failed_students:
        print(f'{sid} - {name}: {reason}')
else:
    print("All students passed!")


print("\n=== GRADE DISTRIBUTION ===")
for grade, count in grades.items():
    print(f'{grade}: {count} students')


# -------------------------------
# Task 2 – NumPy Arrays & Operations
# -------------------------------
import numpy as np
from numpy.ma.extras import median

np.random.seed(42)
#data creation
temperature = np.random.uniform(-10.0, 40.0, size=(365, 5))
print(f'Array Shape: {temperature.shape}')
print(f'Array Dimension: {temperature.ndim}')
print(f'Array Data Type: {temperature.dtype}')
print(f'Array Size: {temperature.size}')

#datacreation
sales = np.random.uniform(1000, 5000, size=(12, 4))

#identity matrix creation
identity_matrix = np.identity(5)

#evelny spaced matrix creation
evenly_spaced_matrix = np.linspace(0, 100, 50)

#extracting specific data
january_data = temperature[0:31, :]  #from 0 element to 31 in terms of rows, and all columns
summer_data = temperature[151:243, :]
weekend_data = temperature[4::7, :]

#hottest and coldest days and number of each
hot_day = temperature[np.any(temperature > 35, axis=1)] #lists all values where at least one city had hot day
number_of_hot_days = hot_day.shape[0]   #total number of hot days in all cities

cold_days = temperature[np.any(temperature < 0, axis=1)] #lists all values where at least one city had cold day
number_of_cold_days = cold_days.shape[0]   #total number of cold days in all cities

comfortable_mask = (temperature > 15) & (temperature < 25)  #True and False values for the days where temperature was between 15 and 25

temperature[temperature < -5] = -5  #find all values with lower degree than -5 and replace with -5


days = [0, 100, 200, 300, 364]  #list all days we want to extract
fancy_indexing_data = temperature[days] #extract the days

quarters = np.array_split(temperature, 4)  # split year into 4 quarters
quarterly_avg = np.array([np.mean(q, axis=0) for q in quarters])  # average in each city

annual_avg = np.mean(temperature, axis=0)  # average over days (rows)
sorted_annual_avg_temperature = np.sort(annual_avg)[::-1]  #sort the list of average temperature descending
sorted_annual_avg_temperature_by_cities = np.argsort(annual_avg)[::-1]   #sort the list of cities by avg temperature descending
sorted_annual_avg_2d = np.column_stack((sorted_annual_avg_temperature_by_cities, sorted_annual_avg_temperature)) #create 2d array of information
mean_per_city = np.mean(temperature, axis=0)   #mean of each city
median_per_city = np.median(temperature, axis=0)   #median of each city
std_per_city = np.std(temperature, axis=0)    #std of each city


daily_max = np.max(temperature, axis=1)  #find to hottest day in all cities in a single day so we have 365 days and their maxs
hottest_temp = np.max(daily_max)   #choose the hottest temp from this 365 temps
hottest_day = np.argmax(daily_max) + 1  #choose the argument of this hottest temp and +1 as first day is indexed as 0


min_max_range = np.max(temperature, axis=0) - np.abs(np.min(temperature, axis=0))  #compute max and min temp for each city and max minus absolute value of min as 12 - -(8) is 20 which is not correct so we get 12 - 8 = 4

correlation = np.corrcoef(temperature.transpose())  #we need .transpose() to transpose so rows are cities and not temps

total_sales_per_category = np.sum(sales, axis=0)  #sales per product axis=0 mean avg of rows

avg_monthly_sales = np.mean(sales, axis= 1)

monthly_sales = np.sum(sales, axis=1)   #sum of each month axis=1 mean avg of columns
best_month_by_sales = np.max(monthly_sales)
best_month = np.argmax(monthly_sales) + 1   #+1 as indexing starts from 0


best_category = np.argmax(total_sales_per_category) + 1  #+1 as indexing starts from 0
best_category_by_sales = np.max(total_sales_per_category)  #max element from best category


window = 7
moving_avg = np.convolve(temperature[:, 0], np.ones(window)/window, mode='valid')  # for one city

moving_avg_all = np.apply_along_axis(
    lambda x: np.convolve(x, np.ones(window)/window, mode='valid'),
    axis=0, arr=temperature
) #for all cities

z_scores = (temperature - np.mean(temperature, axis=0)) / np.std(temperature, axis=0) #function of z_score

percentiles = np.percentile(temperature, [25, 50, 75], axis=0)





# -------------------------------
# Task 3 – Applied Data Analysis
# -------------------------------
import numpy as np
np.random.seed(42)

#data creation
rng = np.random.default_rng(42)
user_ids = np.array([f'u{str(i+1).zfill(3)}' for i in range(100)])  #user ids
ages = rng.integers(18, 71, size=100)  #user ages
genders = rng.integers(0, 2, size=100)  #0 female 1 male

steps = rng.integers(2000, 15001, size=(100, 90)).astype(float)  #daily steps
steps += rng.normal(0, 500, size=(100, 90))  #noise added
steps = np.clip(steps, 0, None)

calories = rng.normal(2300, 300, size=(100, 90))  #daily calories
calories = np.clip(calories, 1000, None)

active_minutes = rng.integers(20, 181, size=(100, 90)).astype(float)  #daily active mins
active_minutes += rng.normal(0, 10, size=(100, 90))
active_minutes = np.clip(active_minutes, 0, None)

avg_hr = rng.normal(75, 8, size=(100, 90))  #avg heart rate
avg_hr = np.clip(avg_hr, 40, 200)

data = np.stack([steps, calories, active_minutes, avg_hr], axis=2)  #combine to array

#add missing and outliers
flat = data.ravel()
nan_count = int(flat.size * 0.05)
flat[rng.choice(flat.size, nan_count, replace=False)] = np.nan  #add nans
out_count = int(flat.size * 0.02)
idx_out = rng.choice(flat.size, out_count, replace=False)
for i in idx_out:
    m = i % 4
    if m == 0:
        flat[i] = 1_000_000
    elif m == 1:
        flat[i] = 50_000
    elif m == 2:
        flat[i] = 10_000
    else:
        flat[i] = 300
data = flat.reshape(data.shape)

#clean missing and outliers
def handle_missing(a):
    b = a.copy()
    means = np.nanmean(b.reshape(-1, 4), axis=0)
    for m in range(4):
        mask = np.isnan(b[..., m])
        b[..., m][mask] = means[m]
    return b

def fix_outliers(a, m):
    b = a.copy()
    x = b[..., m].ravel()
    valid = x[~np.isnan(x)]
    q1, q3 = np.percentile(valid, [25, 75])
    iqr = q3 - q1
    low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    med = np.median(valid)
    vals = b[..., m]
    mask = (vals < low) | (vals > high)
    vals[mask] = med
    b[..., m] = vals
    return b

def clean_data(a):
    b = a.copy()
    for m in range(4):
        b = fix_outliers(b, m)
    b = handle_missing(b)
    return b

cleaned = clean_data(data)  #apply cleaning

#user stats
user_means = cleaned.mean(axis=1)
z = (user_means - user_means.mean(axis=0)) / user_means.std(axis=0)
score = z.sum(axis=1)
top10 = np.argsort(-score)[:10]  #top 10 active users

user_std = cleaned[..., 0].std(axis=1)
most_consistent = np.argsort(user_std)[:10]  #lowest std users

avg_steps = user_means[:, 0]
p25, p75 = np.percentile(avg_steps, [25, 75])
levels = np.array(['low' if s < p25 else 'medium' if s <= p75 else 'high' for s in avg_steps])
unique, count = np.unique(levels, return_counts=True)
activity_counts = dict(zip(unique, count))

#temporal trends
daily_mean = cleaned.mean(axis=0)
days = np.arange(90)
slope, intercept = np.polyfit(days, daily_mean[:, 0], 1)  #trend slope
quarters = np.array_split(daily_mean, 3)
month_means = np.array([q.mean(axis=0) for q in quarters])
growth = (month_means[1:] - month_means[:-1]) / month_means[:-1]  #month growth

#correlation
flat = cleaned.reshape(-1, 4)
corr = np.corrcoef(flat, rowvar=False)
age_corr = np.corrcoef(ages, avg_steps)[0, 1]
mean_m = cleaned[genders == 1].mean(axis=(0, 1))
mean_f = cleaned[genders == 0].mean(axis=(0, 1))

#health score
mins = user_means.min(axis=0)
maxs = user_means.max(axis=0)
norm = (user_means - mins) / (maxs - mins)
norm[:, 3] = 1 - norm[:, 3]
weights = np.array([0.4, 0.25, 0.25, 0.1])
health = norm.dot(weights)
best5 = np.argsort(-health)[:5]

#goal check
goals = {'steps': 8000, 'calories': 2000, 'active': 60}
s_goal = cleaned[..., 0] >= goals['steps']
c_goal = cleaned[..., 1] >= goals['calories']
a_goal = cleaned[..., 2] >= goals['active']
all_goal = s_goal & c_goal & a_goal
rate = all_goal.mean(axis=1) * 100
consistent = np.where(rate > 80)[0]

#print results
print('=== task 3 results ===\n')
print('dataset shape', cleaned.shape)
print('\ntop 10 active users:')
for i in top10:
    print(user_ids[i], round(score[i], 3))
print('\nmost consistent users:')
for i in most_consistent[:5]:
    print(user_ids[i], round(user_std[i], 2))
print('\nactivity counts', activity_counts)
print('\ntrend slope', round(slope, 4))
print('\nmonth growth (%)\n', np.round(growth * 100, 2))
print('\ncorrelation matrix\n', np.round(corr, 3))
print('\nage vs steps corr', round(age_corr, 3))
print('\nmean male', np.round(mean_m, 2))
print('mean female', np.round(mean_f, 2))
print('\ntop 5 health users:')
for i in best5:
    print(user_ids[i], round(health[i], 3))
print('\nusers meeting goals >80%', len(consistent))







#Task2
#Task2
#Task2
#Task2
#Task2
import numpy as np
np.random.seed(42)

#data creation
rng = np.random.default_rng(42)
user_ids = np.array([f'u{str(i+1).zfill(3)}' for i in range(100)])  #user ids
ages = rng.integers(18, 71, size=100)  #user ages
genders = rng.integers(0, 2, size=100)  #0 female 1 male

steps = rng.integers(2000, 15001, size=(100, 90)).astype(float)  #daily steps
steps += rng.normal(0, 500, size=(100, 90))  #noise added
steps = np.clip(steps, 0, None)

calories = rng.normal(2300, 300, size=(100, 90))  #daily calories
calories = np.clip(calories, 1000, None)

active_minutes = rng.integers(20, 181, size=(100, 90)).astype(float)  #daily active mins
active_minutes += rng.normal(0, 10, size=(100, 90))
active_minutes = np.clip(active_minutes, 0, None)

avg_hr = rng.normal(75, 8, size=(100, 90))  #avg heart rate
avg_hr = np.clip(avg_hr, 40, 200)

data = np.stack([steps, calories, active_minutes, avg_hr], axis=2)  #combine to array

#add missing and outliers
flat = data.ravel()
nan_count = int(flat.size * 0.05)
flat[rng.choice(flat.size, nan_count, replace=False)] = np.nan  #add nans
out_count = int(flat.size * 0.02)
idx_out = rng.choice(flat.size, out_count, replace=False)
for i in idx_out:
    m = i % 4
    if m == 0:
        flat[i] = 1_000_000
    elif m == 1:
        flat[i] = 50_000
    elif m == 2:
        flat[i] = 10_000
    else:
        flat[i] = 300
data = flat.reshape(data.shape)

#clean missing and outliers
def handle_missing(a):
    b = a.copy()
    means = np.nanmean(b.reshape(-1, 4), axis=0)
    for m in range(4):
        mask = np.isnan(b[..., m])
        b[..., m][mask] = means[m]
    return b

def fix_outliers(a, m):
    b = a.copy()
    x = b[..., m].ravel()
    valid = x[~np.isnan(x)]
    q1, q3 = np.percentile(valid, [25, 75])
    iqr = q3 - q1
    low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    med = np.median(valid)
    vals = b[..., m]
    mask = (vals < low) | (vals > high)
    vals[mask] = med
    b[..., m] = vals
    return b

def clean_data(a):
    b = a.copy()
    for m in range(4):
        b = fix_outliers(b, m)
    b = handle_missing(b)
    return b

cleaned = clean_data(data)  #apply cleaning

#user stats
user_means = cleaned.mean(axis=1)
z = (user_means - user_means.mean(axis=0)) / user_means.std(axis=0)
score = z.sum(axis=1)
top10 = np.argsort(-score)[:10]  #top 10 active users

user_std = cleaned[..., 0].std(axis=1)
most_consistent = np.argsort(user_std)[:10]  #lowest std users

avg_steps = user_means[:, 0]
p25, p75 = np.percentile(avg_steps, [25, 75])
levels = np.array(['low' if s < p25 else 'medium' if s <= p75 else 'high' for s in avg_steps])
unique, count = np.unique(levels, return_counts=True)
activity_counts = dict(zip(unique, count))

#temporal trends
daily_mean = cleaned.mean(axis=0)
days = np.arange(90)
slope, intercept = np.polyfit(days, daily_mean[:, 0], 1)  #trend slope
quarters = np.array_split(daily_mean, 3)
month_means = np.array([q.mean(axis=0) for q in quarters])
growth = (month_means[1:] - month_means[:-1]) / month_means[:-1]  #month growth

#correlation
flat = cleaned.reshape(-1, 4)
corr = np.corrcoef(flat, rowvar=False)
age_corr = np.corrcoef(ages, avg_steps)[0, 1]
mean_m = cleaned[genders == 1].mean(axis=(0, 1))
mean_f = cleaned[genders == 0].mean(axis=(0, 1))

#health score
mins = user_means.min(axis=0)
maxs = user_means.max(axis=0)
norm = (user_means - mins) / (maxs - mins)
norm[:, 3] = 1 - norm[:, 3]
weights = np.array([0.4, 0.25, 0.25, 0.1])
health = norm.dot(weights)
best5 = np.argsort(-health)[:5]

#goal check
goals = {'steps': 8000, 'calories': 2000, 'active': 60}
s_goal = cleaned[..., 0] >= goals['steps']
c_goal = cleaned[..., 1] >= goals['calories']
a_goal = cleaned[..., 2] >= goals['active']
all_goal = s_goal & c_goal & a_goal
rate = all_goal.mean(axis=1) * 100
consistent = np.where(rate > 80)[0]

#print results
print('=== task 3 results ===\n')
print('dataset shape', cleaned.shape)
print('\ntop 10 active users:')
for i in top10:
    print(user_ids[i], round(score[i], 3))
print('\nmost consistent users:')
for i in most_consistent[:5]:
    print(user_ids[i], round(user_std[i], 2))
print('\nactivity counts', activity_counts)
print('\ntrend slope', round(slope, 4))
print('\nmonth growth (%)\n', np.round(growth * 100, 2))
print('\ncorrelation matrix\n', np.round(corr, 3))
print('\nage vs steps corr', round(age_corr, 3))
print('\nmean male', np.round(mean_m, 2))
print('mean female', np.round(mean_f, 2))
print('\ntop 5 health users:')
for i in best5:
    print(user_ids[i], round(health[i], 3))
print('\nusers meeting goals >80%', len(consistent))




#Task3
#Task3
#Task3
#Task3
#Task3


import numpy as np
import os
np.random.seed(42)

N_USERS = 100
N_DAYS = 90
N_METRICS = 4
METRIC_NAMES = ["daily_steps", "calories", "active_minutes", "avg_heart_rate"]

# Output directory
OUT_DIR = "fitness_outputs"
os.makedirs(OUT_DIR, exist_ok=True)


def generate_data(n_users=N_USERS, n_days=N_DAYS):


    steps = np.random.normal(loc=7000, scale=2500, size=(n_users, n_days))
    steps = np.clip(steps, 2000, 15000).round().astype(float)

    calories = np.random.normal(loc=2300, scale=400, size=(n_users, n_days))
    calories = np.clip(calories, 1500, 3500).round(1).astype(float)

    active_minutes = np.random.normal(loc=60, scale=25, size=(n_users, n_days))
    active_minutes = np.clip(active_minutes, 20, 180).round(1).astype(float)

    avg_hr = np.random.normal(loc=75, scale=8, size=(n_users, n_days))
    avg_hr = np.clip(avg_hr, 60, 120).round(1).astype(float)

    data = np.stack([steps, calories, active_minutes, avg_hr], axis=2)
    return data

def create_metadata(n_users=N_USERS):
    user_id = np.arange(1, n_users + 1)
    ages = np.random.randint(18, 71, size=n_users)
    genders = np.random.choice([0, 1], size=n_users)
    dtype = [("user_id", "i4"), ("age", "i4"), ("gender", "i4")]
    meta = np.zeros(n_users, dtype=dtype)
    meta["user_id"] = user_id
    meta["age"] = ages
    meta["gender"] = genders
    return meta

def insert_nans_and_outliers(data, nan_frac=0.05, outlier_frac=0.02):
    arr = data.copy()
    total = arr.size
    n_nan = int(total * nan_frac)
    n_out = int(total * outlier_frac)

    indices = np.arange(total)
    np.random.shuffle(indices)
    nan_idx = indices[:n_nan]
    out_idx = indices[n_nan:n_nan + n_out]

    # helper to convert flat index to (u, d, m)
    users, days, metrics = arr.shape
    def flat_to_triplet(flat):
        u = flat // (days * metrics)
        rem = flat % (days * metrics)
        d = rem // metrics
        m = rem % metrics
        return u, d, m

    # insert NaNs
    for flat in nan_idx:
        u, d, m = flat_to_triplet(flat)
        arr[u, d, m] = np.nan

    # insert outliers (metric-specific unrealistic values)
    for flat in out_idx:
        u, d, m = flat_to_triplet(flat)
        if m == 0:
            arr[u, d, m] = 100000.0    # unrealistic steps
        elif m == 1:
            arr[u, d, m] = 20000.0     # unrealistic calories
        elif m == 2:
            arr[u, d, m] = 5000.0      # unrealistic active minutes
        elif m == 3:
            arr[u, d, m] = 250.0       # unrealistic heart rate
    return arr, n_nan, n_out

# Generate
raw = generate_data()
metadata = create_metadata()
corrupted, n_nan_inserted, n_out_inserted = insert_nans_and_outliers(raw)

# Save initial stats
np.save(os.path.join(OUT_DIR, "raw_generated.npy"), raw)
np.save(os.path.join(OUT_DIR, "corrupted.npy"), corrupted)
np.save(os.path.join(OUT_DIR, "metadata.npy"), metadata)

print("Part A completed: data generated.")
print(f"Raw shape: {raw.shape}, Corrupted shape: {corrupted.shape}")
print(f"NaNs inserted (approx): {n_nan_inserted}, Outliers inserted (approx): {n_out_inserted}\n")

# -----------------------------
# Part B: Data Cleaning & Validation
# -----------------------------
def handle_missing(arr):
    cleaned = arr.copy()
    users, days, metrics = cleaned.shape
    reshaped = cleaned.reshape(-1, metrics)  # shape (users*days, metrics)
    means = np.nanmean(reshaped, axis=0)     # shape (metrics,)
    # For each metric, fill NaNs
    for m in range(metrics):
        mask = np.isnan(cleaned[:, :, m])
        if np.any(mask):
            cleaned[:, :, m][mask] = means[m]
    return cleaned

def remove_outliers(arr, metric_index):
    cleaned = arr.copy()
    flat = cleaned[:, :, metric_index].reshape(-1)
    # compute Q1, Q3 ignoring NaN
    Q1 = np.nanpercentile(flat, 25)
    Q3 = np.nanpercentile(flat, 75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    median = np.nanmedian(flat)
    # mask outliers (NaNs stay NaN for now)
    m_low = cleaned[:, :, metric_index] < lower
    m_high = cleaned[:, :, metric_index] > upper
    cleaned[:, :, metric_index][m_low | m_high] = median
    return cleaned

# Apply cleaning pipeline: remove outliers for each metric first, then handle missing
cleaned = corrupted.copy()
for m in range(N_METRICS):
    cleaned = remove_outliers(cleaned, m)

cleaned = handle_missing(cleaned)

# Verify no NaNs remain
if np.isnan(cleaned).any():
    raise RuntimeError("Cleaning failed: NaNs remain after handle_missing.")
else:
    print("Part B completed: cleaning pipeline applied. No NaNs remain.\n")

# Save cleaned
np.save(os.path.join(OUT_DIR, "cleaned.npy"), cleaned)

# -----------------------------
# Part C: Comprehensive Analysis
# -----------------------------

# Helper aggregations
def user_averages(data):
    return np.mean(data, axis=1)

def user_stddevs(data):
    return np.std(data, axis=1)

# 1. User Behavior Patterns
user_avg = user_averages(cleaned)  # (100,4)
user_std = user_stddevs(cleaned)   # (100,4)

# a) Top 10 most active users by combined z-score
# compute z-scores across users for each metric using user_avg
means_users = np.mean(user_avg, axis=0)
stds_users = np.std(user_avg, axis=0, ddof=0)
z_users = (user_avg - means_users) / (stds_users + 1e-12)  # avoid div by zero

# Define combined z: for heart rate higher is worse -> subtract hr z
combined_z = z_users[:, 0] + z_users[:, 1] + z_users[:, 2] - z_users[:, 3]
top10_idx = np.argsort(combined_z)[::-1][:10]
top10_users = top10_idx + 1  # user_ids (1-based)

# b) Users with most consistent activity: lowest mean std dev across metrics
consistency_score = np.mean(user_std, axis=1)  # lower is more consistent
most_consistent_idx = np.argsort(consistency_score)[:10]
most_consistent_users = most_consistent_idx + 1

# c) Classify users into activity levels by user_avg steps percentiles
user_steps_avg = user_avg[:, 0]
p25, p75 = np.percentile(user_steps_avg, [25, 75])
activity_level = np.full(user_steps_avg.shape, "Medium", dtype=object)
activity_level[user_steps_avg < p25] = "Low"
activity_level[user_steps_avg > p75] = "High"

# 2. Temporal Trends
# a) 7-day rolling average for population-wide metrics:
# first compute daily population mean for each metric (mean across users)
daily_pop_mean = np.mean(cleaned, axis=0)  # shape (days, metrics)
def rolling_mean_1d(arr, window=7):
    kernel = np.ones(window) / window
    return np.convolve(arr, kernel, mode="valid")

rolling_population = np.stack([rolling_mean_1d(daily_pop_mean[:, m], 7) for m in range(N_METRICS)], axis=1)
# rolling_population shape: (N_DAYS - 7 + 1, N_METRICS)

# b) Weekly patterns: average activity by day of week (assume day 0 = Monday)
days_idx = np.arange(N_DAYS)
dow = days_idx % 7
weekly_pattern = np.zeros((7, N_METRICS))
for wd in range(7):
    mask = (dow == wd)
    # mean across users and only the days in this weekday
    weekly_pattern[wd, :] = np.mean(cleaned[:, mask, :], axis=(0,1))  # mean over (users, days selected)

# c) Trend over time (linear fit) on population daily steps mean
x = np.arange(N_DAYS)
pop_steps_daily = daily_pop_mean[:, 0]
slope, intercept = np.polyfit(x, pop_steps_daily, 1)
trend_direction = "increasing" if slope > 0 else ("decreasing" if slope < 0 else "flat")

# d) Month-over-month growth: assume 3 months of 30 days each
month_totals = []
for m_idx in range(3):
    start = 30 * m_idx
    end = start + 30
    month_totals.append(np.sum(cleaned[:, start:end, 0]))  # sum steps across users & days
month_totals = np.array(month_totals)
mom_growth = 100.0 * (month_totals[1:] - month_totals[:-1]) / (month_totals[:-1] + 1e-12)

# 3. Correlations & Insights
# a) Correlation matrix between metrics (flatten across users & days)
flat_metrics = cleaned.reshape(-1, N_METRICS)
corr_matrix = np.corrcoef(flat_metrics.T)

# b) Relationship between age and activity (user average steps)
ages = metadata["age"]
corr_age_steps = np.corrcoef(ages, user_steps_avg)[0, 1]

# c) Gender-based comparison (mean per gender)
genders = metadata["gender"]
gender_means = {}
for g in np.unique(genders):
    mask = (genders == g)
    gender_means[int(g)] = np.mean(user_avg[mask, :], axis=0)  # per-metric means

# d) Health score: weighted combination of normalized metrics (min-max on user averages)
ua = user_avg.copy()
# min-max scale per metric
ua_min = ua.min(axis=0)
ua_max = ua.max(axis=0)
ua_scaled = (ua - ua_min) / (ua_max - ua_min + 1e-12)
# invert heart rate (lower HR better)
ua_scaled[:, 3] = 1.0 - ua_scaled[:, 3]
weights = np.array([0.4, 0.2, 0.3, 0.1])
health_scores = ua_scaled.dot(weights)
top_health_idx = np.argsort(health_scores)[::-1][:10]

# 4. Goal Achievement
GOALS = {"daily_steps": 8000, "calories": 2000, "active_minutes": 60}
steps_met = cleaned[:, :, 0] >= GOALS["daily_steps"]
cal_met = cleaned[:, :, 1] >= GOALS["calories"]
am_met = cleaned[:, :, 2] >= GOALS["active_minutes"]

steps_rate = np.mean(steps_met, axis=1) * 100  # % of days per user
cal_rate = np.mean(cal_met, axis=1) * 100
am_rate = np.mean(am_met, axis=1) * 100
all_goals_rate = np.mean(steps_met & cal_met & am_met, axis=1) * 100

consistent_users_all_goals = np.where(all_goals_rate > 80)[0] + 1  # user_ids (1-based)

# Percentiles per city (metric)
percentiles_per_metric = np.percentile(flat_metrics, [25, 50, 75], axis=0)  # rows: 25,50,75

# Z-scores per metric (for entire flattened data by metric)
mean_metric = np.mean(flat_metrics, axis=0)
std_metric = np.std(flat_metrics, axis=0, ddof=0)
z_scores_all = (flat_metrics - mean_metric) / (std_metric + 1e-12)

# Save some outputs as CSV-like text files using numpy.savetxt
# - user averages (user_id, metrics...)
user_avg_out = np.column_stack((np.arange(1, N_USERS + 1), user_avg))
np.savetxt(os.path.join(OUT_DIR, "user_averages.csv"),
           user_avg_out,
           header="user_id," + ",".join(METRIC_NAMES),
           delimiter=",", comments="", fmt="%.4f")

# - goal achievement rates
goal_out = np.column_stack((np.arange(1, N_USERS + 1), steps_rate, cal_rate, am_rate, all_goals_rate))
np.savetxt(os.path.join(OUT_DIR, "goal_achievement.csv"),
           goal_out,
           header="user_id,steps_rate_pct,calories_rate_pct,active_minutes_rate_pct,all_goals_pct",
           delimiter=",", comments="", fmt="%.4f")








import numpy as np
studentebi = {
    'S001': {
        'name' : 'Const',
        'scores' : [70,80,46,80],
        'attended' : [22,29,30,14]
    },
'S002': {
        'name' : 'Gigi',
        'scores' : [72,18,66,55],
        'attended' : [7,8,9,10]
    },
'S003': {
        'name' : 'Lia',
        'scores' : [66,77,50,71],
        'attended' : [12,12,23,29]
    },
'S004': {
        'name' : 'Lile',
        'scores' : [70,80,46,80],
        'attended' : [25,25,25,21]
    },
'S005': {
        'name' : 'Nini',
        'scores' : [55,51,77,61],
        'attended' : [18,17,16,20]
    },
'S006': {
        'name' : 'Vaso',
        'scores' : [64,63,62,88],
        'attended' : [7,9,11,14]
    },
'S007': {
        'name' : 'Shota',
        'scores' : [97,77,81,73],
        'attended' : [20,20,19,21]
    },
'S008': {
        'name' : 'Taso',
        'scores' : [70,80,46,80],
        'attended' : [12,4,7,11]
    },
'S009': {
        'name' : 'Gio',
        'scores' : [70,80,46,80],
        'attended' : [25,26,27,28]
    },
'S010': {
        'name' : 'Dachi',
        'scores' : [70,80,46,80],
        'attended' : [15,16,17,8]
    },
'S011': {
        'name' : 'Dima',
        'scores' : [70,80,46,80],
        'attended' : [14,14,14,18]
    },
'S012': {
        'name' : 'Maka',
        'scores' : [97,89,96,100],
        'attended' : [29,29,30,28]
    }
}

def calculate_average(scores : list):
    return round(sum(scores)/len(scores),2)

def assign_grades(grades):
    if grades > 100 or grades < 0 :
        return "Invalid"
    elif grades >= 90 :
            return "A"
    elif grades >= 80 :
            return "B"
    elif grades >= 70:
            return "C"
    elif grades >= 60:
            return "D"
    else:
            return "F"

def check_eligibility(student_dict, total_classes):
    avg = calculate_average(student_dict["scores"])

    attendance_rate = (sum(student_dict["attended"]) / (total_classes * len(student_dict["attended"]))) * 100 if \
student_dict["attended"] else 0

    if avg >= 60 and attendance_rate >= 75:
        return True, "Passed"
    elif avg < 60:
        return False, "Failed due to low average"
    else:
        return False, "Failed due to low attendance"

def find_top_performers(students, n):
    averages = [(sid, calculate_average(data["scores"])) for sid, data in students.items()]
    sorted_avg = sorted(averages, key=lambda x: x[1], reverse=True)
    return sorted_avg[:n]

def generate_report(students):
    total = len(students)
    all_scores = [s for data in students.values() for s in data["scores"]]
    passed, failed, total_att = 0, 0, 0
    for data in students.values():
        eligible, _ = check_eligibility(data, 30)
        if eligible: passed += 1
        else: failed += 1
        total_att += len(data["attended"])

    return {
        "total_students": total,
        "passed_count": passed,
        "failed_count": failed,
        "class_average":calculate_average(all_scores),
        "highest_score": max(all_scores),
        "lowest_score": min(all_scores),
        "average_attendance_rate": round((total_att/(total*30))*100, 2)
    }


def final_report():
    report = generate_report(studentebi)
    print("=== COURSE REPORT ===")
    for k, v in report.items():
        print(f"{k.replace('_', ' ').title()}: {v}")

    print("\n=== TOP 5 PERFORMERS ===")
    top5 = find_top_performers(studentebi, 5)
    for sid, avg in top5:
        grade = assign_grades(avg)
        print(f"{sid} - {studentebi[sid]['name']}: Avg={avg}, Grade={grade}")

    # Failed students
    print("\n=== FAILED STUDENTS ===")
    for sid, data in studentebi.items():
        passed, reason = check_eligibility(data, 30)
        if not passed:
            print(f"{sid} - {data['name']}: {reason}")

    # Grade distribution
    print("\n=== GRADE DISTRIBUTION ===")
    grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for data in studentebi.values():
        g = assign_grades(calculate_average(data["scores"]))
        grades[g] += 1
    for g, count in grades.items():
        print(f"{g}: {count}")


############################################################
#part2

temperatures = np.random.uniform(-10.0, 40.0, (365, 5))
print("Shape:", temperatures.shape)
print("Dimensions:", temperatures.ndim)
print("Data type:", temperatures.dtype)
print("Size:", temperatures.size)

#  Sales matrix: 12 months × 4 product categories
sales = np.random.randint(1000, 5001, (12, 4))

identity_matrix = np.eye(5)
evenly_spaced = np.linspace(0, 100, 50)

january = temperatures[:31, :]
summer = temperatures[151:243, :]
weekends = temperatures[5::7, :]

hot_days = temperatures[np.any(temperatures > 35, axis=1)]
freezing_days = np.sum(temperatures < 0, axis=0)
mask_comfort = (temperatures >= 15) & (temperatures <= 25)
temperatures[temperatures < -5] = -5

specific_days = temperatures[[0, 100, 200, 300, 364], :]
quarters = np.array_split(temperatures, 4)         # Quarterly data
quarterly_avg = np.array([q.mean(axis=0) for q in quarters])
annual_avg = temperatures.mean(axis=0)
city_order = np.argsort(-annual_avg)               # Descending
rearranged = temperatures[:, city_order]

#temperatires
mean_temp = np.mean(temperatures, axis=0)
median_temp = np.median(temperatures, axis=0)
std_temp = np.std(temperatures, axis=0)

# coldest and hottest
max_day, max_city = np.unravel_index(np.argmax(temperatures), temperatures.shape)
min_day, min_city = np.unravel_index(np.argmin(temperatures), temperatures.shape)
hottest = (max_day, temperatures[max_day, max_city])
coldest = (min_day, temperatures[min_day, min_city])

temp_range = np.ptp(temperatures, axis=0)
corr_matrix = np.corrcoef(temperatures.T)

#sales
total_sales = np.sum(sales, axis=0)
avg_monthly_sales = np.mean(sales, axis=0)
best_month = np.argmax(np.sum(sales, axis=1))
best_category = np.argmax(total_sales)

window = 7
moving_avg = np.array([
    np.convolve(temperatures[:, i], np.ones(window)/window, mode='valid')
    for i in range(temperatures.shape[1])
]).T

# z-scores per city
z_scores = (temperatures - mean_temp) / std_temp

# Percentiles
percentiles = np.percentile(temperatures, [25, 50, 75], axis=0)






if __name__ == '__main__':
    final_report()
    print()
    print("Mean temp per city:", mean_temp)
    print("Hottest day:", hottest)
    print("Coldest day:", coldest)
    print("Total sales per category:", total_sales)
    print("Best month index:", best_month)
    print("Best category index:", best_category)


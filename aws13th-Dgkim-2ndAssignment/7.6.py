import csv
import json


# 1
with open('users.csv','r',encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['이름'],row['직업'])


# 2
with open('users.csv','r',encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if int(row['나이']) >= 30:
            print(row['이름'],row['나이'])


# 3
students = [
    {'학번': 'S001', '이름': '김민수', '학과': '컴퓨터공학'},
    {'학번': 'S002', '이름': '이수진', '학과': '전자공학'},
    {'학번': 'S003', '이름': '박영호', '학과': '기계공학'},
]

with open('students.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['학번', '이름', '학과']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

# 4
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

print(f"앱 이름: {config['app_name']}")
print(f"버전: {config['version']}")
print(f"DB 호스트: {config['database']['host']}")

# 5
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
config['debug'] = True
config['features'].append('notifications')
with open('config_updated.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=2)


# 6
with open('users.csv', 'r', encoding='utf-8') as f:
    users = list(csv.DictReader(f))
with open('users.json', 'w', encoding='utf-8') as f:
    json.dump(users, f, ensure_ascii=False, indent=2)


# 7
with open('logs.json', 'r', encoding='utf-8') as f:
    logs = json.load(f)

errors = [log for log in logs if log['level'] == 'ERROR']

print(errors)

with open('errors.json', 'w', encoding='utf-8') as f:
    json.dump(errors, f, ensure_ascii=False, indent=2)

print(f"에러 {errors}건을 errors.json에 저장했습니다.")
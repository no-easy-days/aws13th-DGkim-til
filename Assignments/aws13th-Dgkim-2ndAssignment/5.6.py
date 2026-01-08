# 1
cities = [
    {"name": "서울", "population": 9700000},
    {"name": "부산", "population": 3400000},
    {"name": "인천", "population": 2900000},
    {"name": "대구", "population": 2400000}
]

sorted_cities = sorted(cities, key=lambda x: x["population"])

for city in sorted_cities:
    print(f"{city['name']}")
    print(f"{city['population']}")

# 2
str_numbers = ["10", "20", "30", "40", "50"]

result = list(map(lambda x: x + 100, map(int, str_numbers)))
print(result)


# 3
products = [
    {"name": "노트북", "discount": 15},
    {"name": "마우스", "discount": 25},
    {"name": "키보드", "discount": 30},
    {"name": "모니터", "discount": 10}
]

discounted = list(filter(lambda p: p["discount"] >= 20, products))
print(discounted)
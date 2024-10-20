# Используя map() и reduce() посчитать площадь квартиры, 
# имея на входе характеристики комнат квартиры. 
# Пример входных данных:
# rooms = [
#     {"name": ”Kitchen", "length": 6, "width": 4},
#     {"name": ”Room 1", "length": 5.5, "width": 4.5},
#     {"name": ”Room 2", "length": 5, "width": 4},
#     {"name": ”Room 3", "length": 7, "width": 6.3},
# ]

from functools import reduce

rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3},
]

room_areas = list(map(lambda room: room["length"] * room["width"], rooms))
print(room_areas)

total_area = reduce(lambda x, y : x + y, room_areas)
print(total_area)
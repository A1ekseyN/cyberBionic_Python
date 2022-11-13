import calendar
import heapq
import bisect


print(calendar.Calendar)
print(calendar.firstweekday())

list = [7, 5, 2, 10, 8, 29, 15, 13]
print(list)
heapq.heapify(list)
print(list)

bisect.insort(list, 9)
bisect.insort(list, 3)
bisect.insort(list, 12)
print(list)

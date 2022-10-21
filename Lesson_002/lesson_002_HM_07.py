# Ready
length = 700
velocity = 90

time_h = length // velocity
time_m = int(((length % velocity) / velocity) * 60)
time_s = round(((length / velocity) - time_h - int(time_m) / 60) * 3600)


print(f"Время прибытия через: {time_h} часов {time_m} минут {time_s} секунд.")

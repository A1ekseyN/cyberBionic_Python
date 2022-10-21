# Ready
pc = 27862
lcd = 7499
keyboard = 867
mouse = 437
printer = 10124
switch = 6253

calc = (pc*15) + (lcd*20) + (keyboard*15) + (mouse*15) + (printer*5) + switch

print(f"Для запуска IT компании нужен бюджет: {calc:,.0f} грн.")

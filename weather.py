temperatures = [-3, 2, 8, 15, 22, 27, 31]
day = 1
for temp in temperatures:
 if temp < 0:
    weather = "Saxta"
 elif temp <= 9:
    weather = "Soyuq"
 elif temp <= 19:
    weather = "Mulayim"
 elif temp <= 29:
    weather = "Isti"
else:
    weather = "Cox isti"
    print (day, "-ci gun:", temp, "derece ->", weather)
    day = day + 1

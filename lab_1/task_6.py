print ("Enter the pressure(Па), Volume(м^3), Temprature(celsius)")
R = 8.314
p = float(input())
V = float(input())
T = 273.15 + float(input())
answ = (p * V) / (R * T)
print (answ)

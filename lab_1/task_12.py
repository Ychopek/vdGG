base_price = 24.99
included_minutes = 60
included_sms = 30
included_mb = 1024

price_per_minute = 0.89
price_per_sms = 0.59
price_per_mb = 0.79

tax_rate = 0.02

minutes = int(input("Введите количество минут за месяц: "))
sms = int(input("Введите количество SMS за месяц: "))
mb = int(input("Введите количество МБ интернет-трафика за месяц: "))

extra_minutes = max(0, minutes - included_minutes)
extra_sms = max(0, sms - included_sms)
extra_mb = max(0, mb - included_mb)

cost_extra_minutes = extra_minutes * price_per_minute
cost_extra_sms = extra_sms * price_per_sms
cost_extra_mb = extra_mb * price_per_mb

subtotal = base_price + cost_extra_minutes + cost_extra_sms + cost_extra_mb
tax = subtotal * tax_rate
total = subtotal + tax

print("\nОтчет по вашему тарифу:")
print(f"Базовая плата: {base_price:.2f} руб.")
if extra_minutes > 0:
    print(f"Дополнительные минуты ({extra_minutes} мин): {cost_extra_minutes:.2f} руб.")
if extra_sms > 0:
    print(f"Дополнительные SMS ({extra_sms} шт): {cost_extra_sms:.2f} руб.")
if extra_mb > 0:
    print(f"Дополнительный интернет ({extra_mb} МБ): {cost_extra_mb:.2f} руб.")
print(f"Налог (2%): {tax:.2f} руб.")
print(f"Итого к оплате: {total:.2f} руб.")

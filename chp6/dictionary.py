country_codes = {'Finland': 'fi', 'South Africa': 'za', 'Nepal': 'np'}
print(country_codes)
print(len(country_codes))
if country_codes:
    print("country_code is not empty")
else:
    print("country_code is empty")
print(country_codes)
print()

days_per_month = {'January': 31, 'February': 28, 'March': 31}
print(days_per_month)
for month, days in days_per_month.items():
    print(f'{month} has {days} days')
print()

roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}
print(roman_numerals)
print(roman_numerals["V"])
roman_numerals['X'] = 10
print(roman_numerals)
roman_numerals['L'] = 50
print(roman_numerals)

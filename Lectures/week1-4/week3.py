happy = True
if happy is True:
    print("I am happy")

print("This will print regardless of the value of happy")


happy = True
very_happy = True
if happy is True:
    print("I am happy")
    if very_happy is True:
        print("Actually, I'm really happy!")


less_than_test = "That" < "This"
print(f'"That" < "This" yields {less_than_test}')
greater_than_test = "That" > "This"
print(f'"That" > "This" yields {greater_than_test}')


a = -1
b = True
if a != 0:
    print("a is non-zero")
elif b is True:
    print("b is True")
elif a < 0 and b is True:
    print("a is negative and b is True")
else:
    print("None of the conditions above hold")

x=1
y=2
if x > 0 and y is True:
 # Write code for this case later
    pass
elif x <= 0 and y is True:
 # Write code for this case later
    pass
else:
 # Write code for this case later
    pass


#practice
hours = input('Enter number of hours you worked this week: ')

hours = int(hours)
normal_rate = 51.45
overload_rate = 88.9

if hours > 35 :
    pay = (35 * normal_rate) + ((hours - 35) * overload_rate)
else :
    pay = hours * normal_rate
    print(f'This weekly payment is: {pay}')


import yfinance
start = '2020-01-01'
end = None
tickers = ["QAN.AX", "WES.AX"]
for tic in tickers:
    df = yfinance.download(tic, start, end)
    print(df)
    tic_base = tic.lower().split('.')[0]
    df.to_csv(f'{tic_base}_stk_prc.csv')



d = {
 "beauty": True,
 "truth": True,
 "red wheelbarrow": 100000,
 5: "fingers",
 }
for key, value in d.items():
    print(f'KEY: {key} VALUE: {value}')



numbers = [3,9,1,5,7,2,11,0,3,12,3,15]
temp_largest = None
print('Before', temp_largest)
for number in numbers:
    if temp_largest is None:
        temp_largest = number
    elif number > temp_largest:
        temp_largest = number
    print(number, temp_largest)
print(f'The largest value is {temp_largest}')


years = [2018, 2019, 2020]
months = [
 "Jan",
 "Feb",
 "Mar",
 "Apr",
 "May",
 "Jun",
 "Jul",
 "Aug",
 "Sep",
 "Oct",
 "Nov",
 "Dec",
 ]
for year in years:
    for month in months:
        print("Year: {}, Month: {}".format(year, month))



the_sum = 0
for i in range(1,101):
    if i % 2 == 0:
        continue
    if i % 3 == 0:
        continue
    if i % 7 == 0:
        continue
    if i % 13 == 0:
        continue
    print(f' the_sum is {the_sum}')
    the_sum = the_sum + i
print(f'Sum is {the_sum}')



for x in range(0, 4):
    print(f"Outer loop: x = {x}")
    for y in range(0,4):
        print(f" Start of Inner loop: y = {y}")
    if x + y >= 4:
        print(f" x = {x} and y ={y} have sum >= 4, continuing to next y value")
        continue
    elif (x + y) % 2 != 0:
        print(f" x = {x} and y = {y} have non-even sum, continuing to next y value")
        continue
    print(f" x = {x} and y = {y} have even sum less than 4")


for even in range(0, 10, 2):
    print(even)
    if even > 2:
        break




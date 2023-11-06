# Less-than and less-than or eqaul tests
1 < 2 # --> `True`
2 < 2 # --> `False`
2 <= 2 # --> `True`



# Greater-than or greater-than or equal tests
1 > 2 # --> `False`
2 > 2 # --> `False`
2 >= 2 # --> `True`


# Downloads Qantas share price beginning 1 January 2020
import yfinance
tic = "QAN.AX"
start = '2020-01-01'
end = None
df = yfinance.download(tic, start, end) # (5)
print(df)
df.to_csv(' .csv')



x = str('abc')
xup = str.upper(x)
print(xup)

#practice
length = 65
width = 36.2
height = 28.5
volume = length * width * height
print(f"the volume of the box is {volume} cubic centimeters.")


lst = [1, 2, 3]
print(lst)
t = type(lst) # --> <class 'list'>
print(t)



lst = []
lst = list()


lst = ["a", "b", "c", "d", "e", "f"]
print(f"lst[:3] gives {lst[:3]}")
print(f"lst[0:1000] gives {lst[0:1000]}")


lst_a = [1] # lst_a is [1]
list.append(lst_a,2)
print(lst_a)

lst_a = [1]
lst_b = [2, 3]
lst_a.extend(lst_b)
print(lst_a)

lst = [1, "string", True, None, True]
no_of_items =len(lst)
print(f"lst has {no_of_items} items"


a, b, c = 1, True, "word"
a, b, c = (1, True, "word")
(a, b, c) = 1, True, "word"
(a, b, c) = (1, True, "word")


s = set()
s.add("QAN.AX")
s.add("WES.AX")
s.add("CBA.AX")
s.add("CBA.AX")
print(f"After adding objects, s is {s}")
s.remove("CBA.AX")
print(f"After removing 'CBA.AX', s is {s}")

line = 'From nickname.surname@unsw.edu.au Tue Oct 06 10:10:15 2020'
domain = line.split()[1].split('@')[1]
print(domain)
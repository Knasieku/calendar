# import calendar

# yy= int(input("Enter year to display: "))
# mm= int(input("Enter month to display: "))
# dd= int(input("Enter day to display: "))

# print(calendar.month(yy,mm,dd))

# fu

# random=input().capitalize()
# print(random)

# random="          any word       "
# text=random.strip()

# print(text)
# def password():
#     word=input().strip()
#     print(word)
# password()

# def password():
#     random="person"
#     text=random.strip("pn")
#     print(text)
# password()

# def fruits():
#     basket="I like bananas. bananas grow in the forest bananas.bananas"
#     b=basket.replace("bananas","apples")
#     print(b)
# fruits()
    
age=[11,7,32,45,5]
def age_check(a):
    if a<10:
        return False
    else:
        return True
adult=filter(age_check,age)
for a in adult:
    print(a)
    
    
   

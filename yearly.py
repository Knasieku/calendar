import calendar

yy= int(input("Enter year to display: "))
mm= int(input("Enter month to display: "))
dd= int(input("Enter day to display: "))

print(calendar.month(yy,mm,dd))
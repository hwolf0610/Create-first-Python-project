import re
from datetime import datetime
from datetime import timedelta
import calendar

a="Guru"
b=99
print (a[1])
print ( "u"  in a )
print (a*2)


def some():
    global b
    print(b)
    b=100
some()
print(b)

oldstring="I love Guru99"
newstring=oldstring.replace("love", "like")
print(newstring)
print(newstring.upper())
print(newstring.capitalize())
print(newstring.lower())
print(newstring.split(" "))
mylist=[1,2,3]
for x in mylist:
    print(x)
string="12345"
print(":".join("python"))
print('666'.join(reversed(string)))
tup1=(1,2,3,4,5,6)
print(tup1[0])
print(tup1[1:4])
x=("asdf","asdgivbdfb","askdfhsuhf1234")
(asd1,asd2,asd3)=x
print(asd1)
print(asd2)
print(asd3)

a1=(5,6)
a2=(6,4)
if(a1>a2):print("a1 is bigger")
else:print("b is bigger")

a={'a':50,'x':100, 'y':200,'z':300,'yy':400}
b=a.items()
c=list(a.keys())
d=list(a.values())
print(d)
print(c)
print(b)
print(a['yy'])

studentx=a.copy()
print(studentx)

a.update({'yy':567})
print(a)

del a['yy']
print(a)


x=20
y=20
if(x is y):
    print("x & y SAME identity")
z=(x+y)*x/y
print("Vlaue of (x+y) * x/y is" ,z)

def square(x):
    print(x*x)

print(square(4))

def multiply(x, y=0):
    return x*y
print(multiply(4, y=2))

def use():
    x,y=12,8
    if (x<y):
        st="x is less than y"
    elif(x ==y):
        st="x is same as y"
    else:
        st="x is less grester than y"
    print(st)
if use == "__use__":
    use()
x=0
while(x<4):
    print(x)
    x=x+1
for x in range(2,7):
    print(x)

class myClass():
    def method1(self):
        print("Guru99")
    # def method2(self, someString):
    #     print("Software Testing:"+someString)

class childclass(myClass):
    #def method1(self):
        #myClass.method1(self):
        #print("childClss Method1")
    def method2(self):
        print("childClass method2")
def main():
    c2=childclass()
    c2.method1()
    c2.method2()
if __name__=="__main__":
    main()
class User:
    name=""
    def __init__(self,name):
        self.name=name
    def sayHello(self):
        print("welcome to ,"+self.name)
user1=User("Alex")
user1.sayHello()

xx="asd,guru99, education is fun"
r1=re.findall(r"^\w+",xx)
r2=re.findall(r"^\w+",xx,re.MULTILINE)
print(r1)
print(r2)
print((re.split(r'\s','we are splitting the words')))
print((re.split(r's','we are splitting the words')))

list = ["guru99 get", "guru99 give","guru seleni"]
for element in list:
    z=re.match("(g\w+)\W(g\w+)", element)
    if z:
        print((z.group()))

abc="guru99@google.com, careerguru99@hotmail.com, users@yahomail.com"
emails=re.findall(r'[\w\.-]+@[\w\.-]+',abc)
for email in emails:
    print(email)

today=datetime.now()
print("Today's Weekday:", today)

t=datetime.time(datetime.now())
print("The current time is ", t)

wd=datetime.weekday(today)

days=["monday","Tuesday","Wednesday","thursday", "friday","saturday","sunday"]
print("which is a "+days[wd])

now=datetime.now()
print(now.strftime("%Y, %B,  %d, %a, %A,  %y"))
print(now.strftime("%c"))
print(now.strftime("%x"))
print(now.strftime("%X"))
print(now.strftime("%I:%M:%S %p"))
print(now.strftime("%H:%M"))


print(timedelta(days=365, hours=8, minutes=15))

c=calendar.TextCalendar(calendar.SUNDAY)
str=c.formatmonth(2019,12)
print(str)

hc=calendar.HTMLCalendar(calendar.THURSDAY)
str=hc.formatmonthname(2019,12)
print(str)

for name in calendar.month_name:
    print(name)
print("\n")
for day in calendar.day_name:
    print(day)









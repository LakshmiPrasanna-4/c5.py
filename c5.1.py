# Write a program to generate salary bill for employee.

class Employee():
    def getdata(self,emno,empname,des,basic,hra,da,ta):
        self.emno=emno
        self.empname=empname
        self.des=des
        self.basic=basic
        self.hra=hra
        self.da=da
        self.ta=ta
    def putdata(self):
        print('Employee number:',self.emno)
        print('Employee name:',self.empname)
        print('Enter designation:',self.des)
        print('Enter basic salary:',self.basic)
        print('Enter hra:',self.hra)
        print('Enter da:',self.da)
        print('Enter ta:',self.ta)
        ntsal=self.basic+self.da+self.ta+self.hra
        if ntsal>50000:
            a=ntsal*(5/100)
            sal=ntsal-a
            print('Salary:',sal)
        elif ntsal>35000:
            b=ntsal*(3/100)
            sal=ntsal-b
            print('Salary',sal)
        elif ntsal>20000:
            c=ntsal*(1/100)
            sal=ntsal-c
            print('Salary',sal)
        else:
            d=ntsal*0
            sal=ntsal-d
            print('Salary',sal)
    
s=Employee()
emno=int(input('Enter employee number:'))
empname=input('Enter employee name:')
des=input('Enter employee designation:')
basic=int(input('Enter basic salary:'))
hra=int(input('Enter hra:'))
da=int(input('Enter da:'))
ta=int(input('Enter ta:'))
s.getdata(emno,empname,des,basic,hra,da,ta)
s.putdata()

# Write a program to print given year is a leap year or not.

class Solution:
    def leap_year(self,n):
        if n%4==0 or n%100!=0 and n%400==0:
            return True
        else:
            return False
n=int(input())
s=Solution()
if s.leap_year(n):
    print('Leap Year')
else:
    print('Not a Leap Year')

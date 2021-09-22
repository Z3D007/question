import os
import time 

user=input("Enter Username : ")
if user=="David":
     time.sleep(2)
     os.system ("clear")
     print ("Script By David Khant")
     time.sleep(2)
     os.system ("clear")
     print ("start" , time.ctime())
     print ("")
     mark=0
     que=str(input("Do You Want Question Y/N : "))
     if que=="Y" or que=="y":
          time.sleep(4)
          os.system ("clear")
          print ("Question 1 ")
          print("")
          q1=str(input("Python is Programming Language Y/N : "))
          if q1=="Y" or q1=="y":
               print ("correct")
               mark=mark+10
               os.system("clear")
          else:
               print("incorrect")
               os.system ("clear")
          print ("Question 2 ")
          print ("")
          q2=str(input("Facebook is Social Media Y/N : "))
          if q2=="Y" or q2=="y":
               print ("correct")
               mark=mark+10
               os.system ("clear")
          else:
               print ("incorrect")
               os.system ("clear")
          print ("Question 3 ")
          print ("")
          q3=str(input("Google is Game Y/N : "))
          if q3=="N" or q3=="n":
               print ("correct")
               mark=mark+10
               os.system("clear")
          else:
               print ("incorrect")
               os.system ("clear")
          print ("Question 4 ")
          print ("")
          q4=str(input("Html is Programming Language Y/N : "))
          if q4=="N" or q4=="n":
               print ("correct")
               mark=mark+10
               os.system ("clear")
          else:
               print ("incorrect")
               os.system ("clear")
          print ("Question 5 ")
          print ("")
          q5=str(input("Nethunter is OS Y/N : "))
          if q5=="Y" or q5=="y":
               print ("correct")
               mark=mark+10
               os.system ("clear")
               time.sleep(3)
               print ("")
               print ("Full Mark is 50")
               print ("Your Mark is " ,mark )
               print ("End" , time.ctime())
          else:
               print("incorrect")
               os.system ("clear")
     else:
          print("Question is very easy let try bro!! ")
else:
     print ("Wrong Username")
     

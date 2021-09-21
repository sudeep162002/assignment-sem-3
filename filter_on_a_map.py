import sys
import csv


def verify(n):
    if n[30]=="1":
        return n
    


counter=0

if len(sys.argv)<2:
    print("not a valid argument")
else:

    with open('phd-test-anon.csv',"r") as f:
        csv_reader=csv.reader(f)
        result=map(verify,csv_reader )
    
        for i in list(result):
           if i!=None:
                print(i)
                counter+=1

 
print(len(result))
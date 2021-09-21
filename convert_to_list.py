import sys
import csv







if len(sys.argv)<2:
    print("not a valid argument")
else:

    with open('phd-test-anon.csv',"r") as f:
        csv_reader=csv.reader(f)
    
    
        for i in csv_reader:
           if i[0].isdigit():
                print(i)
      



          

import sys
j=0;
if len(sys.argv)<2:
    print("not a valid argument")
else:
    f = open(sys.argv[1],"r")
   
    content = f.read()
    
    for i in open(sys.argv[1],"r"):
        print(i)
    
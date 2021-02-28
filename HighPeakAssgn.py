infl=open("input.txt","r")#open input file in read mode
out=open("Output.txt","w")#open output file in write mode
for i in infl:
  NoEm=int(i.split(":")[1]) #taking Number of employees
  infl.readline() #leaving unwanted lines
  infl.readline()
  infl.readline()
  goodie={} #intializing dictonary
  for j in infl:
    if(j=="\n"): #conditon statement for end of testcase
      break
    x=j.split(":")  
    goodie[x[0]]=int(x[1]) #appending name and values of goodies to dictonary
    #sorting dictonary based on values
  goodie={k: v for k, v in sorted(goodie.items(), key=lambda item: item[1])}
  l=[]
  for key in goodie:
    l.append(goodie[key]) #taking values to list
  low=l[len(l)-1]
  for j in range(len(l)-NoEm+1):
    x=l[j+NoEm-1]-l[j]
    if(x<low):
      low=x # taking lowest difference.
      res=j #taking index of that ggodie
  out.write("The goodies selected for distribution are:\n\n")
  for key in goodie:
    if(res<=0):
      x=str(key)+": "+str(goodie[key])+"\n" 
      out.write(x)# writing the selected goodies to output file in given format
      NoEm-=1
      if(NoEm==0):
        break
    res-=1
  x="\nAnd the difference between the chosen goodie with highest price and the lowest price is "+str(low)+"\n\n" 
  out.write(x)
infl.close()
out.close()

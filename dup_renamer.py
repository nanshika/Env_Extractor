#dup_renamer.py
f2=open(r"C:\Users\works\yet\IC\aaaaa02.txt","w")
f1=open(r"C:\Users\works\yet\IC\aaaaa01.txt","r")
l_dict = {}
for l in f1.readlines():
  if l in l_dict:
    l_dict[l]+=1
    f2.write("_dup_" + str(l_dict[l]) + l)
  else:
    f2.write(l)
    l_dict[l] = 0


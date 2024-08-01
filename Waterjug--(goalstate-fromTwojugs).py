jicap=int(input("Enter jug1 capacity"))
jicap2=int(input("Enter jug2 capacity"))
goal=int(input("Enter goal"))
def check( j1 , j2):
   if j1==goal:
    return True
   else:
    return False

def rules():
  print("1.Fill jug1")
  print("2.Fill jug2")
  print("3.Empty jug1")
  print("4.Empty jug2")
  print("5.Transfer jug1 to jug2 until jug2 is full")
  print("6.Transfer jug2 to jug1 until jug1 is full")
def choice( i, j1, j2):
  if i==1:
    j1=jicap
  elif i==2:
    j2=jicap2
  elif i==3:
    j1=0
  elif i==4:
    j2=0
  elif i==5:
    if j1+j2>jicap2:
      temp=jicap2-j2
      j1-=temp
      j2+=temp
    else:
      j2+=j1
      j1=0
  elif i==6:
    if j2+j1>jicap:
      temp1=jicap-j1
      j2-=temp1
      j1+=temp1
    else:
      j1+=j2
      j2=0 
  elif i==7:
    return 0,0
  else:
    print("Enter correct choice")  

      
  return j1,j2          
jug1=0
jug2=0
rules()
while check(jug1,jug2)!=True:
  
  x=int(input("Enter your choice"))
  jug1,jug2=choice(x,jug1,jug2)
  print("jug1:",jug1)
  print("jug2:",jug2)
print("successfully done")  

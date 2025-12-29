#finding odd or even number

num=7
if num%2==0:
  print("even number")
else:
  print("odd number")


# printing only odd numbers
a=int(input("enter a number"))
if(a>0 and a%2==0):
    for i in range(0,a+1):
        if(i%2==0):
            print(i,end=" ")
        else:
            continue
elif(a>0 and a%2!=0):
    for i in range(0,a+1):
        if(i%2!=0):
            if(i%5==0):
                continue
            else:
                print(i,end=" ")
elif(a<0):
    print("negative num not allowed")
elif(a==0):
    print("zero entered")
else:
    pass

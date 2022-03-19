i=0
a=int(input("Max:"))
while i<a:
 i=i+1
 if i%4==0 and i%6!=0:
  print("Fizz")
 elif i%6==0 and i%4!=0:
  print("Buzz")
 elif i%4==0 and i%6==0:
  print("FizzBuzz")
 else:
  print(i)
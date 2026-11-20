number = int(input("Eded daxil edin:"))

factorial = 1

if number < 0:
 print("Menfi ededin faktoriali yoxdu")

else:
 for i in range (1, number + 1):
  factorial = factorial * i
  print ("Faktorial:", factorial)
  
text = input ("Soz ve ya cumle daxil edin:")
saitler = "a, e, ə, ı, i, o, ö, u, ü"
count = 0
for letter in text:
    if letter in saitler:
        count = count + 1
        print ("Saitlerin sayi" , count)
        
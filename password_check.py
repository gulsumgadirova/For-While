password = input("Sifre daxil edin:")
boyuk = 0
kicik = 0
reqem = 0
diger = 0

for herf in password:
    if herf >= "A" and herf <= "Z":
        boyuk = boyuk + 1
    elif herf >= "a" and herf <= "z":
        kicik = kicik + 1
    elif herf >= "0" and herf <= "9":
        reqem = reqem + 1
    else:
        diger = diger + 1
print ("Boyuk herf:", boyuk)
print ("kicik herf:", kicik)
print ("Reqem:", reqem)
print ("Diger:", diger)

if len(password) >= 8 and boyuk >= 1 and kicik >= 1 and reqem >= 1 and diger >= 1:
    print ("Guclu sifre:")
else:
    print("Zeif sifre")
        

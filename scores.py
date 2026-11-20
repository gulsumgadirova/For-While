scores = [78, 92, 65, 88, 100, 54, 91, 73]
cem = 0
count = 0
bal = scores[0]

for score in scores:
    cem = cem + score

    if score >= 90:
        count = count + 1
        if score > bal:
            bal = score
average = cem / len(scores)
print("Ballarin cemi:", cem)
print ("Orta bal:", average)
print ("90 ve yuxari:", count)
print ("En yuksek bal:" , bal)

            
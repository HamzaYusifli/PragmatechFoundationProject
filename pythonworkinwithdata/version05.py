# version 05
telebeler={
     "adlar":['Ehmed','Memmed','Sabir'],
     "soyadlar":['Ehmedov','Salehov','Quliyev']
 }

print("while:")

i=0
while i<len(telebeler["adlar"]):
    print(f"Ad:{telebeler['adlar'][i]}, Soyad:{telebeler['soyadlar'][i]}")
    i+=1
    
print("for:")

for i in range(len(telebeler["adlar"])):
    print(f"Ad:{telebeler['adlar'][i]}, Soyad:{telebeler['soyadlar'][i]}")
# version 03
telebe01={
    "ad":"Ehmed",
     "soyad":"Ehmedov"
}

telebe02={
     "ad":"Memmed",
     "soyad":"Salehov"
 }

telebe03={
     "ad":"Sabir",
     "soyad":"Quliyev"
 }

telebeler=[telebe01,telebe02,telebe03]

print("while:")

i=0
while i<len(telebeler):
    print(f"Ad:{telebeler[i]['ad']}, Soyad:{telebeler[i]['soyad']}")
    i+=1
    
print("for:")

for i in range(len(telebeler)):
    print(f"Ad:{telebeler[i]['ad']}, Soyad:{telebeler[i]['soyad']}")
# version 04
telebeler=[
 {
     "ad":"Ehmed",
     "soyad":"Ehmedov"
 },
 {
     "ad":"Memmed",
     "soyad":"Salehov"
 },
 {
     "ad":"Sabir",
     "soyad":"Quliyev"
 }
]

print("while:")

i=0
while i<len(telebeler):
    print(f"Ad:{telebeler[i]['ad']}, Soyad:{telebeler[i]['soyad']}")
    i+=1
    
print("for:")

for i in range(len(telebeler)):
    print(f"Ad:{telebeler[i]['ad']}, Soyad:{telebeler[i]['soyad']}")
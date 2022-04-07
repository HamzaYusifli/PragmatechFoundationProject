# version 01
adlar=['Ehmed','Memmed','Sabir','Ekrem','Namiq']
soyadlar=['Ehmedov','Salehov','Quliyev','Tahirov','Rustemov']
telebeler=[adlar,soyadlar]

print("while:")

i=0
while i<len(adlar):
    print(f"Ad:{telebeler[0][i]}, Soyad:{telebeler[1][i]}")
    i+=1

print("for:")

for i in range(len(adlar)):
    print(f"Ad:{telebeler[0][i]}, Soyad:{telebeler[1][i]}")
# version 02
telebeler=[
    ['Ehmed','Memmed','Sabir'],
    ['Ehmedov','Salehov','Quliyev']
]

print("while:")

i=0
while i<len(telebeler[0]):
    print(f"Ad:{telebeler[0][i]}, Soyad:{telebeler[1][i]}")
    i+=1

print("for:")

for i in range(len(telebeler[0])):
    print(f"Ad:{telebeler[0][i]}, Soyad:{telebeler[1][i]}")
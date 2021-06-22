# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# CONTOH HASIL NILAI LATIHAN SOAL MAHASISWA

#Mhs 1 - 80 88 89 90
#Mhs 2 - 90 89 88
#Mhs 3 - 88 80 90 89
#Mhs 4 - 89 80 90 88

Nilai = [[80, 88, 89, 90], [90, 89, 88], [88, 80, 90, 89], [89, 80, 90, 88]]
 #Mengisi data array 2 dimensi, perhatikan cara berikut ini :
print(Nilai[0])
print(Nilai[2])
print(Nilai[0][2])
print(Nilai[2][0])

print("Menampilkan Array dalam bentuk tabel atau matrix")
for a in Nilai:
    for b in a:
        print(b, end = " ")
    print()

print("Menambahkan Data Baru di Array")
Nilai.insert(3,(90, 99, 98, 97))
for a in Nilai:
    for b in a:
        print(b, end = " ")
    print()

print("Mengupdet Data didalam Array")
Nilai[3] = [80, 90]
Nilai[0][3] = 98
for a in Nilai:
    for b in a:
        print(b, end = " ")
    print()

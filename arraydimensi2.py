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

print("Menghapus Data didalam Array")
del Nilai[3]
for a in Nilai:
    for b in a:
        print(b, end = " ")
    print()

#Bagaimana menggukan format input user?
#Studi kasus input nilai diatas

#Deklarasi Variabel
Nilai_mahasiswa=[ ]
stop1 = False
i=0

print("Mengisi data Nilai Mahasiswa melalui input user")
while(not stop1):
    jumlah=int(input("Berapa Nilai akan diinput, pada array ke- {}:".format(i)))
    a = 0
    tampung = [ ]
    for a in range(jumlah):
        Nilai_baru = int(input("Input Hasil Nilai ke-{}".format(a)))
        tampung.append(Nilai_baru)
    Nilai_mahasiswa.insert(i,tampung)
    i+=1
    tanya = input("Mau isi data mahsiswa selanjutnya???(y/t):")
    if(tanya == "t"):
        stop1 = True
        #cetak semua data nilai
print("===========================")
print("Cetak Hasil Nilai Dalam data asli array 2 Dimensi", Nilai_mahasiswa)
print()
print("===========================")
print("Hasil Array 2 Dimensi dalam bentuk Tabel")
for x in Nilai_mahasiswa:
    for b in x:
        print(b, end = " ")
    print()
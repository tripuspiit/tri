print("Array Dimensi Satu")
buah=[ ]
stop =  False
i = 0

# Mengisi data buah melalui input user
while(not stop):
    buah_baru = input("Input Nama Buah-buahan yang ke- {} :".format(i))
    buah.append(buah_baru)
    #Updet nilai i
    i+=1
    tanya = input("Mau isi data lagi??? (y/t):")
    if(tanya=="t"):
        stop = True
        #Cetak Semua Data Buah
        print("===========================================")
        print("Hasil input nama buat dalam format array : ", buah)

print("=======================================")



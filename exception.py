try:
    x = 10/2
    hasil = x
    print (hasil)
    
except Exception as e:
    print ("Kesalahan : Tidak boleh dibagi 0")

else:
    print ("Kode berjalan")

finally:
    print ("Kode selesai dijalankan")   


#Contoh Type error
try:
    hasil = "5" + 5
    print(hasil)
    
except TypeError as e:
    print("Terjadi kesalahan: Tidak boleh memasukkan huruf!")

else:
    print("Berhasil")

finally:
    print("Kode berjalan")    
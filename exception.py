def pembagian (a, b):
    if b==0:
        raise Exception("Angka pembagi tidak boleh nol.")
    return a/b

try:
    hasil=pembagian (10, 2)
    print (hasil)
    
except Exception as e:
    print (f"Kesalahan : {e}")

else:
    print ("Kode berjalan")

finally:
    print ("Kode selesai dijalankan")   
    
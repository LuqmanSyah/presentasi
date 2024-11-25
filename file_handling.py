# Membuka file dalam mode 'r'
with open("contoh.txt", "r") as file:
  a = file.read()
  print(a)

# Membaca per baris
with open("contoh.txt", "r") as file:
  for baris in file:
    print(baris)

with open("contoh.txt", "r") as file:
  print(file.readline())

# Overwrite ke file
with open("contoh.txt", "w") as file:
  file.write("Hello, World\n")
  file.write("file handling in ptyhon.")

# Menambahkan tulisan diakhir
with open("contoh.txt", "a") as file:
  file.write("\nini akan ditambahkan diakhir")


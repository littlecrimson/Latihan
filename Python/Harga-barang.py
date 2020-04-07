# Buatlah program yang menghitung harga barang setelah diskon
# program menerima 3 inputan : kode,jenis,harga
# kode A : 10% B : 15% C : 20%

def harga(kode,jenis,harga):
  total = 0
  if kode.lower() == 'a':
    total = harga * 10/100
  elif kode.lower() == 'b':
    total = harga * 15/100
  elif kode.lower() == 'c':
    total = harga * 20/100
  
  print("Total harga : %d" %total)

harga('A','Pacul',12000)
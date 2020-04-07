# Buatlah program yang menghitung lama bekerja seorang pegawai
def lamaKerja(masuk,pulang):
  if pulang < masuk:
    pulang += 12
	
  print(pulang - masuk)
  
lamaKerja(10,11)
lamaKerja(10,2)
lamaKerja(10,7)
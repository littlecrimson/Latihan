# Buatlah program yang menghitung gaji karyawan
# program menerima 2 inputan : golongan, jamkerja
# gol 1 = 3000/jam
# gol 2 = 3500/jam
# gol 3 = 4000/jam
# gol 4 = 5000/jam
# jika bekerja <= 40 jam/minggu gaji seperti diatas
# jika lebih maka dianggap lembur dengan upah 1.5 gaji

def upah(gol,jamkerja):
  upah = 0
  if gol == 1:
    upah = 3000
  elif gol == 2:
    upah = 3500
  elif gol == 3:
    upah = 4000
  elif gol == 4:
    upah = 5000
  
  if jamkerja <= 40:
    print("Gaji : %d" %(upah*jamkerja))
  else:
    gaji = upah * (jamkerja - (jamkerja%40))
    lembur = (jamkerja%40) * 1.5 * upah
    total = gaji + lembur
    print("Gaji : {g}, Lembur : {l}, Total : {t}".format(g=gaji,l=lembur,t=total))
  

upah(1,40)  
upah(1,41)
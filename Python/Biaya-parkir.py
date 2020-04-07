# Buatlah program yang menghitung biaya parkir.
# biaya parkir 2 jam pertama 2000, perjam selanjutnya 500

def parkir(masuk,keluar):
  if keluar < masuk:
    keluar += 12
  
  lamaParkir = keluar - masuk
  biaya = 0
  
  if lamaParkir < 2:
    biaya += 2000
  elif lamaParkir > 2:
    biaya += 2000 + ((lamaParkir - 2) * 500)
  
  print("Lama parkir : {l} jam, biaya : {b}".format(l=lamaParkir,b=biaya))
  
parkir(10,11)
parkir(10,2)
print ("Nama   : Louis Ferry Setyawan Putra")
print ("NIM    : 04119013")
print ("Prodi  : Sistem Komputer")
print ("*******************")
print ("APLIKASI TOKENISASI")
print ("*******************")
print ("")
print ("Silahkan masukkan Kalimat :")

#input
L = input()
#rumus
print(L.split())
for kata in L.split():
 print(kata)
#hasil
print ("     ")  
print("Terdeksi Ada {} kata".format(len(L.split())))

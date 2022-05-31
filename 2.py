
x  = input('Masukkan Nilai permintaan = ' )
y = input ('Masukkan Nilai persediaan = ')

permintaan  = float(x)
persediaan = float(y)


if  permintaan<= 1000:
    pmt_turun = 1
    pmt_naik = 0
    
if permintaan>=1000 and permintaan<=5000 :
    pmt_turun = (5000-permintaan)/4000
    pmt_naik = (permintaan-1000)/4000
   
if permintaan>=5000:
    pmt_turun = 0
    pmt_naik = 1


if persediaan<=100:
   psd_sedikit= 1
   psd_banyak = 0
   
if persediaan>=100 and persediaan <=600:
    psd_sedikit= (600-persediaan)/500
    psd_banyak = (persediaan-100)/500
   
if persediaan>=600:
   psd_sedikit= 0
   psd_banyak = 1


print('')
print('Hasil Proses Fuzzifikasi') 
print('Hasil derajat keanggotaan pada setiap variabel Linguistik "Permintaan"')
print('Nilai Permintaan Turun =', pmt_turun)
print('Nilai Permintaan Naik  =', pmt_naik)
print('')
print('Hasil derajat keanggotaan pada setiap variabel Linguistik "Persediaan"' )
print('Nilai Persediaan Sedikit =', psd_sedikit)
print('Nilai Persediaan Banyak  =', psd_banyak)

print('Sistem Inferensi / Menyesuaikan sesuai aturan yang dibuat')
p1 = min(pmt_turun, psd_banyak)
z1 = 7000 - (p1 * 5000)

p2 = min(pmt_turun, psd_sedikit)
z2 = 7000 - (p2 * 5000)

p3 = min(pmt_naik, psd_banyak)
z3 = (p3 * 5000) +  2000

p4 = min(pmt_naik, psd_sedikit)
z4 = (p4 * 5000) + 2000

z = ((p1*z1) + (p2*z2) + (p3*z3) + (p4 *z4)) / (p1+p2+p3+p4)


print('')
print('Nilai z1 = ', z1)
print('Nilai z2 = ', z2)
print('Nilai z3 = ', z3)
print('Nilai z4 = ', z4)
print('Nilai z = ', z)


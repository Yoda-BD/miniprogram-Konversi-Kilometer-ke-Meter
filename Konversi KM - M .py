print('Pilih konversi \n 1. KM ke M \n 2. M ke KM')
pilihan = int(input('Masukkan nomor Pilihan: '))
satuan = int(input('Masukkan yang ingin dikonversikan: '))
if pilihan == 1:
    konversi = satuan*1000
    print('{} M'.format(konversi))
elif  pilihan == 2:
    konversi = satuan/1000
    print('{} KM'.format(konversi))
else:
    print('pilihan tidak tersedia')
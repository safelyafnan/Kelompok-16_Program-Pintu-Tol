import random
daftar_tgl = ("1", "2", "3", "4", "5", "06", "7", "8", "9" "10", "11", "12", "13", "14", "15", "16", "17",
              "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30")
bulan = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")

rand = random.randint(0, 13)
rando = random.randint(0, 31)

today = daftar_tgl[rando]
month = bulan[rand]
tanggal = today + "-" + month + "-2021"

print('--------------------------------------------')
print('Selamat datang di pintu masuk toll Jasawarga')
print('--------------------------------------------')
print('Lokasi anda saat ini adalah')
print('A. Semarang')
print('B. Surakarta')
print('C. Bandung')
print('D. Jakarta')
print('E. Surabaya')
lokasi =input('Silakan pilih lokasi anda saat ini(pilih A/B/C/D/E: ')
print("\n")

if lokasi == 'A':
    print('Daftar tujuan:')
    print('1. Jakarta')
    print('2. Bandung')
    print('3. Surakarta')
    print('4. Surabaya')
    Tujuan = input('Masukkan tujuan Anda: ')
    if Tujuan == 'Surabaya':
        harga = 320000
        print('Jenis kendaraan yang diperkenankan memasuki toll adalah: Roda 4, Roda 6, dan Roda 8')
        jenis_kendaraan = input('Apakah kendaraan yang anda pakai? ')
        if jenis_kendaraan == 'Roda 4':
            tarif = 11000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 6':
            tarif = 16500
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 8':
            tarif = 16500
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
    elif Tujuan == 'Jakarta':
        harga = 330000
        print('Jenis kendaraan yang diperkenankan memasuki toll adalah: Roda 4, Roda 6, dan Roda 8')
        jenis_kendaraan = input('Apakah kendaraan yang anda pakai? ')
        if jenis_kendaraan == 'Roda 4':
            tarif = 11000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 6':
            tarif = 16500
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 8':
            tarif = 22000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
    elif Tujuan == 'Bandung':
        harga = 300000
        print('Jenis kendaraan yang diperkenankan memasuki toll adalah: Roda 4, Roda 6, dan Roda 8')
        jenis_kendaraan = input('Apakah kendaraan yang anda pakai? ')
        if jenis_kendaraan == 'Roda 4':
            tarif = 11000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 6':
            tarif = 16500
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 8':
            tarif = 22000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
    elif Tujuan == 'Surakarta':
        harga = 55000
        print('Jenis kendaraan yang diperkenankan memasuki toll adalah: Roda 4, Roda 6, dan Roda 8')
        jenis_kendaraan = input('Apakah kendaraan yang anda pakai? ')
        if jenis_kendaraan == 'Roda 4':
            tarif = 11000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 6':
            tarif = 16500
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 8':
            tarif = 22000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)

elif lokasi =='B':
    print('Daftar tujuan:')
    print('1. Jakarta')
    print('2. Bandung')
    print('3. Semarang')
    print('4. Surabaya')
    Tujuan = input('Masukkan tujuan Anda: ')
    if Tujuan == 'Surabaya':
        harga = 210000
        print('Jenis kendaraan yang diperkenankan memasuki toll adalah: Roda 4, Roda 6, dan Roda 8')
        jenis_kendaraan = input('Apakah kendaraan yang anda pakai? ')
        if jenis_kendaraan == 'Roda 4':
            tarif = 11000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 6':
            tarif = 16500
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 8':
            tarif = 22000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
    elif Tujuan == 'Semarang':
        harga = 55000
        print('Jenis kendaraan yang diperkenankan memasuki toll adalah: Roda 4, Roda 6, dan Roda 8')
        jenis_kendaraan = input('Apakah kendaraan yang anda pakai? ')
        if jenis_kendaraan == 'Roda 4':
            tarif = 11000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 6':
            tarif = 16500
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 8':
            tarif = 22000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
    elif Tujuan == 'Bandung':
        harga = 370000
        print('Jenis kendaraan yang diperkenankan memasuki toll adalah: Roda 4, Roda 6, dan Roda 8')
        jenis_kendaraan = input('Apakah kendaraan yang anda pakai? ')
        if jenis_kendaraan == 'Roda 4':
            tarif = 11000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 6':
            tarif = 16500
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 8':
            tarif = 22000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
    elif Tujuan == 'Jakarta':
        harga = 400000
        print('Jenis kendaraan yang diperkenankan memasuki toll adalah: Roda 4, Roda 6, dan Roda 8')
        jenis_kendaraan = input('Apakah kendaraan yang anda pakai? ')
        if jenis_kendaraan == 'Roda 4':
            tarif = 11000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 6':
            tarif = 16500
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 8':
            tarif = 22000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
elif lokasi =='C':
    print('Daftar tujuan:')
    print('1. Jakarta')
    print('2. Semarang')
    print('3. Surakarta')
    print('4. Surabaya')
    Tujuan = input('Masukkan tujuan Anda: ')
    if Tujuan == 'Surabaya':
        harga = 500000
        print('Jenis kendaraan yang diperkenankan memasuki toll adalah: Roda 4, Roda 6, dan Roda 8')
        jenis_kendaraan = input('Apakah kendaraan yang anda pakai? ')
        if jenis_kendaraan == 'Roda 4':
            tarif = 11000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 6':
            tarif = 16500
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 8':
            tarif = 22000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
    elif Tujuan == 'Surakarta':
        harga = 370000
        print('Jenis kendaraan yang diperkenankan memasuki toll adalah: Roda 4, Roda 6, dan Roda 8')
        jenis_kendaraan = input('Apakah kendaraan yang anda pakai? ')
        if jenis_kendaraan == 'Roda 4':
            tarif = 11000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 6':
            tarif = 16500
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 8':
            tarif = 22000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
    elif Tujuan == 'Semarang':
        harga = 300000
        print('Jenis kendaraan yang diperkenankan memasuki toll adalah: Roda 4, Roda 6, dan Roda 8')
        jenis_kendaraan = input('Apakah kendaraan yang anda pakai? ')
        if jenis_kendaraan == 'Roda 4':
            tarif = 11000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 6':
            tarif = 16500
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 8':
            tarif = 22000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
    elif Tujuan == 'Jakarta':
        harga = 60000
        print('Jenis kendaraan yang diperkenankan memasuki toll adalah: Roda 4, Roda 6, dan Roda 8')
        jenis_kendaraan = input('Apakah kendaraan yang anda pakai? ')
        if jenis_kendaraan == 'Roda 4':
            tarif = 11000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 6':
            tarif = 16500
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 8':
            tarif = 22000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
elif lokasi == 'D':
    print('Daftar tujuan:')
    print('1. Bandung')
    print('2. Semarang')
    print('3. Surakarta')
    print('4. Surabaya')
    Tujuan = input('Masukkan tujuan Anda: ')
    if Tujuan == 'Surabaya':
        harga = 660000
        print('Jenis kendaraan yang diperkenankan memasuki toll adalah: Roda 4, Roda 6, dan Roda 8')
        jenis_kendaraan = input('Apakah kendaraan yang anda pakai? ')
        if jenis_kendaraan == 'Roda 4':
            tarif = 11000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 6':
            tarif = 16500
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 8':
            tarif = 22000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
    elif Tujuan == 'Surakarta':
        harga = 400000
        print('Jenis kendaraan yang diperkenankan memasuki toll adalah: Roda 4, Roda 6, dan Roda 8')
        jenis_kendaraan = input('Apakah kendaraan yang anda pakai? ')
        if jenis_kendaraan == 'Roda 4':
            tarif = 11000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 6':
            tarif = 16500
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 8':
            tarif = 22000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
    elif Tujuan == 'Semarang':
        harga = 330000
        print('Jenis kendaraan yang diperkenankan memasuki toll adalah: Roda 4, Roda 6, dan Roda 8')
        jenis_kendaraan = input('Apakah kendaraan yang anda pakai? ')
        if jenis_kendaraan == 'Roda 4':
            tarif = 11000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 6':
            tarif = 16500
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 8':
            tarif = 22000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
    elif Tujuan == 'Bandung':
        harga = 60000
        print('Jenis kendaraan yang diperkenankan memasuki toll adalah: Roda 4, Roda 6, dan Roda 8')
        jenis_kendaraan = input('Apakah kendaraan yang anda pakai? ')
        if jenis_kendaraan == 'Roda 4':
            tarif = 11000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 6':
            tarif = 16500
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
        elif jenis_kendaraan == 'Roda 8':
            tarif = 22000
            harga1 = harga + tarif
            print('Harga yang anda harus bayarkan adalah')
            print(harga1)
print('\n')
if tanggal == '6-5-2021':
    harga1 = harga1 + 5000
    print('========================================================================================================')
    print('Dikarenakan sudah memasuki H-7 lebaran maka ada tambahan tarif sebesar 7000 sehingga menjadi IDR', harga1)
    print('========================================================================================================')
elif tanggal == '10-5-2021':
    harga1 = harga1 + 7000
    print('========================================================================================================')
    print('Dikarenakan sudah memasuki H-3 lebaran maka ada tambahan tarif sebesar 7000 sehingga menjadi IDR', harga1)
    print('========================================================================================================')
elif tanggal == '13-5-2021':
    harga1 = harga1 + 10000
    print('===========================================================================================================')
    print('Dikarenakan sudah memasuki hari H lebaran maka ada tambahan tarif sebesar 7000 sehingga menjadi IDR', harga1)
    print('===========================================================================================================')
elif tanggal == '16-5-2021':
    print('========================================================================================================')
    harga1 = harga1 + 7000
    print('Dikarenakan sudah memasuki H+3 lebaran maka ada tambahan tarif sebesar 7000 sehingga menjadi IDR', harga1)
    print('========================================================================================================')
elif tanggal == '20-5-2021':
    harga1 = harga1 + 5000
    print('========================================================================================================')
    print('Dikarenakan sudah memasuki H+7 lebaran maka ada tambahan tarif sebesar 7000 sehingga menjadi IDR', harga1)
    print('========================================================================================================')

print("\n")
print('------------------------------------------------------------------')
print('                       Gerbang Tol Jasawarga', lokasi)
print('Terima kasih telah menggunakan layanan kami')
print('Semoga selamat sampai tujuan. Berikut adalah struk transaksi anda:')
print('')
print('Kota tujuan                              :', Tujuan)
print('Jenis kendaraan anda adalah              :', jenis_kendaraan)
if tanggal == '6-5-2021':
    print('Tarif tambahan                       :IDR 5000')
elif tanggal == '10-5-2021':
    print('Tarif tambahan                       :IDR 7000')
elif tanggal == '13-5-2021':
    print('Tarif tambahan                       :IDR 10000')
elif tanggal == '16-5-2021':
    print('Tarif tambahan                       :IDR 7000')
elif tanggal == '20-5-2021':
    print('Tarif tambahan                       :IDR 5000')
print('Harga yang harus anda bayarkan adalah    : IDR', harga1)
print('')
print('WWW.Jasa-Warga.com\tCall Center:777\t', tanggal)
print('------------------------------------------------------------------')


list_karyawan = [[1001,'Asep hidayat', 'Tangerang 20/08/1987','Laki-laki',
                'Jalan raya jelupang','S1','Informatika',9000000,'Staff'],
                 [1002,'Anggi anipar','Jakarta 31/01/1968','Laki-laki',
                'Perumahan Perum 4 Tangerang kota','S1','Informatika',11000000,'Staff'],
                 [1003,'Komarudin','Jakarta 12/02/1994','Laki-Laki',
                'Cibodas raya Kota Tangerang','S1','Informatika',20000000,'Staff'],
                [1004,'Siska fauziah','Medan 12/09/1998','Perempuan','Jalan raya Mt Haryono',
                'S1','Keuangan',9000000,'Staff'],[1005,'Amanda geraldin','Medan 21/09/1980','Perempuan',
                'Jalan raya st','SMA','Keuangan',4500000,'Staff'],
                [1006,'Cornelius','Tangerang 25/04/1995','Laki-laki','Jalan Raya BSD','S1','Multimedia',9000000,'Staff']
                ]

divisi  = []
nomor_id = []
nama = []
list_gaji = []
gender =[]
list_kategori_tabel = ['NOMOR ID','NAMA','TEMPAT & TANGGAL LAHIR','JENIS KELAMIN','ALAMAT','PND','DIVISI','GAJI','JABATAN']

def menampilkan_menu_1():
     print('Daftar Karyawan\n')
     print(f'Index{(" " * 1)} || Nomor id {(" " * 1)} || Nama{(" " * 8)} '
          f'|| Tempat & Tanngal Lahir{(" " * 1)} || Jenis Kelamin{(" " * 1)}'
          f'|| Alamat{(" " * 26)} || Pnd{(" " * 1)} || Divisi{(" " * 5)}'
          f'|| Gaji{(" " * 5)}||Jabatan{(" " * 1)}||')

     for item in range(len(list_karyawan)):
          print(f'{item}{(" " * 6)}|'
               f'{list_karyawan[item][0]}{(" " * 10)}|'
               f'{list_karyawan[item][1]}{(" " * (15 - len(list_karyawan[item][1])))}|'
               f'{list_karyawan[item][2]}{(" " * (25 - len(list_karyawan[item][2])))}|'
               f'{list_karyawan[item][3]}{(" " * (16 - len(list_karyawan[item][3])))}|'
               f'{list_karyawan[item][4]}{(" " * (35 - len(list_karyawan[item][4])))}|'
               f'{list_karyawan[item][5]}{(" " * (7 - len(list_karyawan[item][5])))}|'
               f'{list_karyawan[item][6]}{(" " * (14 - len(list_karyawan[item][6])))}|'
               f'{list_karyawan[item][7]}{(" " * 2)}|'
               f'{list_karyawan[item][8]}{(" " * (2 - len(list_karyawan[item][8])))}\n')

def Read_Data():
     read = True
     while read != '2':
          print('''Read Data Sub Menu :

                   1. Report seluruh data!
                   2. Report data with primary key!
                   3. Kembali ke menu utama !\n''')

          read = input('Silakan masukan pilihan sub menu!\t:')
          if read == '1':
               if len(list_karyawan) != 0:
                    menampilkan_menu_1()
               else:
                print('Tdidak ada data karyyawan')
               continue
          elif read == '2':
           menampilkan_menu_2()
          elif read == '3':
           break

def cerate_data():
     create = True
     while create != '3':
          print('''Report Sub Menu :

                1. Create data baru
                2. sorting data divisi
                3. sorting data gender
                4. Kembali ke menu utama !\n''')

          create = input('Silakan masukan pilihan sub menu!\t:')
          if create == '1' :
               if len(list_karyawan)!= 0:
                    menampilkan_menu_3()
               else:
                continue
          elif create == '2':
           menampilkan_menu_5()
          elif create == '3':
           menampilkan_menu_6()
          elif create == '4':
           break

def update_data():
    update = True
    while update != '4':
        print('''List Sub Menu Update :

              1.Update Data List Karyawan
              2.Kembali ke Menu utama\n''')

        update = input('Silakan masukan pilahan Sub Menu !\t:')
        menampilkan_menu_1()

        if update == '1':
            if len(list_karyawan)!=0:
                menampilkan_menu_4()
            else:
                continue
        elif update == '2':
            break

def delete_data():
    delete = True
    while delete != '5':
        print(''' List Sub Menu Delete :

              1. Delete Data List Karyawan
              2. Kembali ke Menu Utama\n ''')

        delete = input('Silakan masukan pilihan Sub Menu!\t:')
        if delete == '1':
            if len(list_karyawan) != 0:
                menampilkan_menu_7()
            else:
                continue
        elif delete == '2':
            break



def menampilkan_menu_2():
    nomor_id = []
    nomor_id_2 = []


    while True:
        xy = int(input('Masukan Nomor id\t:'))
        for cek_nomor_id_1 in range(len(list_karyawan)):
            for y in range(len(list_karyawan[cek_nomor_id_1])-8):
                if list_karyawan [cek_nomor_id_1][y] == xy:
                    nomor_id.append(list_karyawan[cek_nomor_id_1][y])
                    nomor_id_2.append(list_karyawan[cek_nomor_id_1])
                    if nomor_id == [xy]:
                        print('Data')
                        print('Daftar Karyawan\n')
                        print(f'Index{(" " * 1)} || Nomor ID {(" " * 1)} || Nama{(" " * 8)} '
                        f'|| Tempat & Tanngal Lahir{(" " * 1)} || Jenis Kelamin{(" " * 1)}'
                        f'|| Alamat{(" " * 26)} || Pnd{(" " * 1)} || Divisi{(" " * 5)}'
                        f'|| Gaji{(" " * 5)}||Jabatan{(" " * 1)}||')

                        for item in range(len(nomor_id)):
                          print(f'{item}{(" " * 6)}|'
                          f'{nomor_id_2[item][0]}{(" " * 10)}|'
                          f'{nomor_id_2[item][1]}{(" " * (15 - len(nomor_id_2[item][1])))}|'
                          f'{nomor_id_2[item][2]}{(" " * (25 - len(nomor_id_2[item][2])))}|'
                          f'{nomor_id_2[item][3]}{(" " * (16 - len(nomor_id_2[item][3])))}|'
                          f'{nomor_id_2[item][4]}{(" " * (35 - len(nomor_id_2[item][4])))}|'
                          f'{nomor_id_2[item][5]}{(" " * (7 - len(nomor_id_2[item][5])))}|'
                          f'{nomor_id_2[item][6]}{(" " * (14 - len(nomor_id_2[item][6])))}|'
                          f'{nomor_id_2[item][7]}{(" " * 2)}|'
                          f'{nomor_id_2[item][8]}{(" " * (2 - len(nomor_id_2[item][8])))}\n')
                          return()

        else:
         print('Data Belum ada, silakan masukan nomor id lain\t!')
         break




def menampilkan_menu_3():

    #x =[]
    xy = []

    while True:
        cek_nomor_id = int(input('Masukan Nomor Id!\t:'))
        for cek_nomor_id_1 in range(len(list_karyawan)):
            for y in range(len(list_karyawan[cek_nomor_id_1])-8):
                    if list_karyawan[cek_nomor_id_1][y] == cek_nomor_id:
                            print('Nomor ID sudah ada Masukan Nomor Lain!\t:')
                            return

        else:
          print('Nomor id belum terdaftar silakan masukan data!')
          nomor_id   = int(input(f'Masukan Nomor id baru !{(" " * 49)}:'))
          name       = str(input(F'Masukan nama karyawan !{(" " * 49)}:'))
          ttl        = str(input('Masukan tempat dan tanggal lahir dengan format tempat /01/01/2000!\t:'))
          gender     = str(input(F'Masukan jenis kelamin karyawan!{(" " * 41)}:'))
          alamat     = str(input(F'Masukan alamat karyawan !{(" " * 47)}:'))
          pendidikan = str(input(F'Masukan Pedidikan Terakhir Karyawan !{(" " * 35)}:'))
          divis_1    = str(input(F'Masukan Divis Karyawan !{(" " * 48)}:'))
          gaji       = int(input(F'Masukan Gaji Karyawan !{(" " * 49)}:'))
          jabatan    = str(input(f'Masukan Jabatan Karyawan !{(" " * 46)}:'))

          list_karyawan.append ([nomor_id,name,ttl,gender,alamat,pendidikan,divis_1,gaji,jabatan])
          menampilkan_menu_1()
          return()

def menampilkan_menu_4():
            menampilkan_menu_1
            update_colum         = str(input('Masukan colum Yang Ingin Di Update ?\t'))
            update_colum_capital = update_colum.upper()
            update_nama_2        = int(input('Masukan nomor Id yang ingin di update !\t'))
            update               = str(input('Masukan data yang ingin di update\t'))

            for nama_karyawan_2 in range (len(list_kategori_tabel)):
                if list_kategori_tabel[nama_karyawan_2] == update_colum_capital:
                     colum = [nama_karyawan_2]
                     for x in range(len(list_karyawan)):
                         for y in range(len(list_karyawan[x])):
                            if list_karyawan [x][y] == update_nama_2:
                                list_karyawan [x][nama_karyawan_2] = update

            menampilkan_menu_1()

def menampilkan_menu_5():
        divisi.clear()
        nama_divisi = str(input('Tuliskan Nama Divisi Yang Ingin di ambil ?\t'))
        nama_divisi_capital = nama_divisi.capitalize()


        for divisi_karyawan_1 in range(len(list_karyawan)):
             for x in range(len(list_karyawan[divisi_karyawan_1])):
                     if list_karyawan[divisi_karyawan_1][x] == nama_divisi_capital:
                         divisi.append (list_karyawan[divisi_karyawan_1])

        print('Daftar Karyawan\n')
        print(f'Nomor ID {(" " * 1)} || Nama{(" " * 8)} '
              f'|| Tempat & Tanngal Lahir{(" " * 1)} || Jenis Kelamin{(" " * 1)}'
              f'|| Alamat{(" " * 26)} || Pnd{(" " * 1)} || Divisi{(" " * 5)}'
              f'|| Gaji{(" " * 5)}||Jabatan{(" " * 1)}||')

        for item in range(len(divisi)):
            print(
            f'{divisi[item][0]}{(" " * 10)}|'
            f'{divisi[item][1]}{(" " * (15 - len(divisi[item][1])))}|'
            f'{divisi[item][2]}{(" " * (25 - len(divisi[item][2])))}|'
            f'{divisi[item][3]}{(" " * (16 - len(divisi[item][3])))}|'
            f'{divisi[item][4]}{(" " * (35 - len(divisi[item][4])))}|'
            f'{divisi[item][5]}{(" " * (7 - len(divisi[item][5])))}|'
            f'{divisi[item][6]}{(" " * (14 - len(divisi[item][6])))}|'
            f'{divisi[item][7]}{(" " * 2)}|'
            f'{divisi[item][8]}{(" " * (2 - len(divisi[item][8])))}\n')

def menampilkan_menu_6():
        gender.clear()
        gender_yang_ingin_input = str(input('Tuliskan gender Yang Ingin di ambil ?\t'))
        nama_gender = gender_yang_ingin_input.capitalize()


        for gender_karywan_1 in range(len(list_karyawan)):
             for x in range(len(list_karyawan[gender_karywan_1])):
                     if list_karyawan[gender_karywan_1][x] == nama_gender:
                         gender.append (list_karyawan[gender_karywan_1])

        print('Daftar Karyawan\n')
        print(f'Nomor ID {(" " * 1)} || Nama{(" " * 8)} '
              f'|| Tempat & Tanngal Lahir{(" " * 1)} || Jenis Kelamin{(" " * 1)}'
              f'|| Alamat{(" " * 26)} || Pnd{(" " * 1)} || Divisi{(" " * 5)}'
              f'|| Gaji{(" " * 5)}||Jabatan{(" " * 1)}||')

        for item in range(len(gender)):
            print(
            f'{gender[item][0]}{(" " * 10)}|'
            f'{gender[item][1]}{(" " * (15 - len(gender[item][1])))}|'
            f'{gender[item][2]}{(" " * (25 - len(gender[item][2])))}|'
            f'{gender[item][3]}{(" " * (16 - len(gender[item][3])))}|'
            f'{gender[item][4]}{(" " * (35 - len(gender[item][4])))}|'
            f'{gender[item][5]}{(" " * (7 - len(gender[item][5])))}|'
            f'{gender[item][6]}{(" " * (14 - len(gender[item][6])))}|'
            f'{gender[item][7]}{(" " * 2)}|'
            f'{gender[item][8]}{(" " * (2 - len(gender[item][8])))}\n')

def menampilkan_menu_7():

    menampilkan_menu_1()

    nomor_id = []
    nomor_id_2 = []

    while True:
        xyz = int(input('Masukan Nomor id:\t'))
        for cek_nomor_id_1 in range(len(list_karyawan)):
            for y in range(len(list_karyawan[cek_nomor_id_1])-8):
                if list_karyawan [cek_nomor_id_1][y] == xyz:
                    nomor_id.append(list_karyawan[cek_nomor_id_1][y])
                    nomor_id_2.append(list_karyawan[cek_nomor_id_1])
                    print('Nomor id ada')
                    delete_nomor = int(input('Masukan kembali nomor id yang akan di hapus !'))
                    del list_karyawan [cek_nomor_id_1]
                    menampilkan_menu_1()
                    return()
        else:
             break


while True:
     pilihan_menu = input('''
     Program Report Data  Karyawan

          List Menu Utama :

          1. READ DATA
          2. CREATE DATA
          3. UPDATE DATA
          4. DELETE DATA
          5. EXIT MENU

     Pilih Sala Satu Menu \t''')

     if (pilihan_menu == '1'):
          Read_Data()
     elif(pilihan_menu == '2'):
          cerate_data()
     elif(pilihan_menu == '3'):
          update_data()
     elif(pilihan_menu == '4'):
         delete_data()
     else:
      print('Opsi tidak valid masukan ulang opsi!')
      break

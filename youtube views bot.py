import time
import os
import string
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import ctypes
import sys
##################################### // Başlangıç
ctypes.windll.kernel32.SetConsoleTitleW("Made by Shixy#8000 Youtube Views Bot")
clear = lambda: os.system('cls')
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)
        ####################### // Printler fln
slowprint("Made by Shixy#8000 Youtube Views Bot")
time.sleep(2)
clear()
slowprint("Starting..")
time.sleep(2)
clear()
slowprint("Youtube Link")
ytlink = input()
time.sleep(2)
clear()
slowprint("ok ok ok...")
time.sleep(1)
clear()
proxy_ip_port = '213.108.5.224:3128' # your proxy pls / sizin proxynizi girin lütfen
time.sleep(1)
clear()
############################################### // Proxy Kısmı
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port
############################################### //Webdriver Kısmı
capabilities = webdriver.DesiredCapabilities.FIREFOX
proxy.add_to_capabilities(capabilities)
driver = webdriver.Firefox()
driver.get(ytlink)
print("Views Completed " + ''.join(proxy_ip_port))
time.sleep(70)

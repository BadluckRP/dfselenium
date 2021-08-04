from sel import ws
import time

debug = True

web = 'C:\webdrivers\geckodriver.exe'
l = 'insidesales@dryve.com.br'
s = 'Inside@100'

def encerra(b):
    print('fechando')
    time.sleep(10)
    b.fechaGuia()
    time.sleep(5)
    print('fechado')

auto = ws(web)

auto.navegaPara('https://accounts.rdstation.com.br/')
time.sleep(1)

auto.procura_xpath_escreve('//*[@id="email"]', l)
auto.procura_xpath_escreve('//*[@id="password"]', s)
auto.procura_xpath_clica('/html/body/div/div/div/div/div[2]/div/form/button')
if debug == True: time.sleep(1)
print('logon OK')
time.sleep(1)

auto.procura_xpath_clica('/html/body/div/div[2]/div/table/tbody/tr[3]/td[2]/div/button')
if debug == True: time.sleep(1)
auto.procura_xpath_clica('/html/body/div/div[2]/div/table/tbody/tr[3]/td[2]/div/ul/li[2]/a')
print('instancia OK')
if debug == True: time.sleep(1)

auto.navegaPara('https://plugcrm.net/app#/deals/open')
time.sleep(1)
print('listagem OK')
if debug == True: time.sleep(1)

auto.procura_xpath_clica('/html/body/div[2]/div[2]/div[1]/div/div[1]/md-toolbar/div[2]/div[1]/gselect[2]/md-menu/button')
if debug == True: time.sleep(1)
auto.procura_xpath_escreve('//*[@id="input_19"]', 'Todas as Oportunidades')
if debug == True: time.sleep(1)
auto.procura_xpath_clica('/html/body/div[8]/md-menu-content/md-list/md-content/div/md-list-item/div/button')
if debug == True: time.sleep(1)
print('Todas as Oportunidades OK')
if debug == True: time.sleep(1)


auto.procura_xpath_clica('/html/body/div[2]/div[2]/div[1]/div/div[1]/md-toolbar/div[2]/div[1]/gselect[2]/md-menu/button')
if debug == True: time.sleep(1)
auto.procura_xpath_escreve('//*[@id="input_19"]', 'Todas as Oportunidades')
if debug == True: time.sleep(1)
print('Todas as Etapas OK')
if debug == True: time.sleep(1)


print('Status da oportunidade')
if debug == True: time.sleep(1)


# encerra(auto.__driver)


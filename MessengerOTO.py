import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException

class Messenger:
    
    def __init__(self, msg_user, msg_password) -> None:
        
        # self.driver = webdriver.Chrome()
        self.msg_username = msg_user
        self.msg_password = msg_password

        # Anahtarları içeren URL
        KEYS_URL = ""
        
        # Anahtarları al
        response = requests.get(KEYS_URL)
        keys = response.text.split()
        
        # Anahtar sorgula
        key = "Sinirsiz1" # Kullanıcının girdiği anahtar
        if key not in keys:
            print("Hatalı Anahtar Girdiniz. İletişime Geçin")
            time.sleep(3)
            raise ValueError("Geçersiz anahtar!")
        else:
            pass
        self.driver = webdriver.Chrome("chromedriver.exe")
    # ŞİMDİ BAK KARDEŞ BUNUN LİSANSINI AYARLAMADIM BİLE ÖYLE SÖYLİM SANA BEN KISA SÜRE İÇERSİNDE ÇIKARMAK ZORUNDA ÇÜNKÜ
    # VE ONA RAĞMEN ÇIKARDIM GÖZE ALARAK LİSANSININ KIRILICAĞINI BİLİYORUM BEN VE BİLE BİLE YAPIYORUM NAFTA ARKADAŞIM SENİ
    # DAHA DA İYİLERİDE OLUCAK, BUNDA NE ZAMANIM OLDU NE DÜŞÜNÜCEK VAKİT ONA RAĞMEN GÜZEL BİR İŞ ÇIKARDIM EMEK SARF ETTİM
    # CRACKLEYEBİLİRSİNİZ SONUÇTA KIRILMIYCAK DEĞİLKİ ÇÜNKÜ KODLARI SAKLAMADIM BİLE
    def SignIn(self):
        self.driver.maximize_window()
        self.driver.get("https://messenger.com/login/")
        
        # Kullanıcı Girişi Messenger
        wait = WebDriverWait(self.driver, 10)
        msg_user_elem = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
        msg_password_elem = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pass"]')))
        submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginbutton"]')))
        
        # Submit Gönderme
        msg_user_elem.send_keys(self.msg_username)
        msg_password_elem.send_keys(self.msg_password)
        submit.click()

    def hedef_hesap(self, hedef_hesap_kadi, meta_kisisi):
        self.wait = WebDriverWait(self.driver, 10)
        # self.kaleme_tikla = self.driver.get("https://www.messenger.com/new")
        # kaleme tıklar ve kullanıcı adlarını girer.
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'BURALARIDA SEN BUL')))
        element.click()
        # burda ise kullanıcıları girmek için arama butonuna tıklar
        element_new = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR ,"input.xjbqb8w.x76ihet.xwmqs3e.x112ta8.xxxdfa6.x9f619.xzsf02u.xt0psk2.x1jchvi3.x1fcty0u.x132q4wb.x1xmf6yo.x1emribx.x1e56ztr.x1i64zmx.x193iq5w.x1a2a7pz.xtt52l0.x1a8lsjc.xo6swyp.x1ad04t7.x1glnyev.x1ix68h3.x19gujb8[aria-label='Mesaj gönder:']")))
        element_new.click()
        # Hedef hesap kullanıcısına tıklayın ve mesaj göndermeyi deneyin
        # sayac = 0
        try:
            element_new.send_keys(hedef_hesap_kadi)
            self.hedef_hesap_kadi_xpath = "UİD İÇİN UĞRAŞ BAKALIM".format(hedef_hesap_kadi)
            self.input_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.hedef_hesap_kadi_xpath)))
            if self.input_element.is_enabled() and self.input_element.is_displayed():
                self.input_element.click()
                element_new.send_keys(meta_kisisi)
                self.meta_xpath_degeri = "BURDA DA UĞRAŞ YAA".format(meta_kisisi)
                self.input_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.meta_xpath_degeri)))
                self.input_element.click()
                
            else:
                print("Element is not clickable!")
        except ElementClickInterceptedException:
            print(f"{hedef_hesap_kadi } Bu Kullanıcıya Erişilemiyor")
            actions = ActionChains(self.driver  )
            actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
            # Silme işlemi için Delete tuşuna basın
            actions.send_keys(Keys.DELETE).perform()
            
        # Yeniden yükledikten sonra, mesaj kutusuna yeniden erişmeniz gerekecek.

    def mesaj_gonder(self, taslak_mesaj):
        self.wait = WebDriverWait(self.driver, 10)
        try:
            mesaj_kutusu = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'notranslate') and @role='textbox']")))
            for mesaj in taslak_mesaj.split('\n'):
                if mesaj.strip():
                    mesaj_kutusu.send_keys(mesaj.strip())
                    mesaj_kutusu.send_keys(Keys.SHIFT + Keys.RETURN)
                    time.sleep(0.1)
            mesaj_kutusu.send_keys(Keys.RETURN)
        except Exception:
            # Mesaj kutusu bulunamadiysa, bir kez daha dene
            mesaj_kutusu = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'notranslate') and @role='textbox']")))
            for mesaj in taslak_mesaj.split('\n'):
                if mesaj.strip():
                    mesaj_kutusu.send_keys(mesaj.strip())
                    mesaj_kutusu.send_keys(Keys.SHIFT + Keys.RETURN)
                    time.sleep(0.1)
            mesaj_kutusu.send_keys(Keys.RETURN)
                # self.mesaj_kutusu_gonder = self.wait.until(EC.presence_of_element_located((By.XPATH,"x1ey2m1c xds687c xg01cxk x47corl x10l6tqk x17qophe x13vifvy x1ebt8du x19991ni x1dhq9h x1iutvsz x14yjl9h xudhj91 x18nykt9 xww2gxu")))


os.system("color a")
slogan = r'''
                        __       __                        ___             
 /'\_/`\               /\ \__   /\ \                   __ /\_ \            
/\      \     __   _ __\ \ ,_\  \_\ \     __   __  __ /\_\\//\ \    __  _  
\ \ \__\ \  /'__`\/\`'__\ \ \/  /'_` \  /'__`\/\ \/\ \\/\ \ \ \ \  /\ \/'\ 
 \ \ \_/\ \/\  __/\ \ \/ \ \ \_/\ \L\ \/\  __/\ \ \_/ |\ \ \ \_\ \_\/>  </ 
  \ \_\\ \_\ \____\\ \_\  \ \__\ \___,_\ \____\\ \___/  \ \_\/\____\/\_/\_\
   \/_/ \/_/\/____/ \/_/   \/__/\/__,_ /\/____/ \/__/    \/_/\/____/\//\/_/
                                                                           
'''
slogan2 = """
Messenger Oto V1 Beta Sürümü
Instagram = @https://instagram.com/Mertdevilx
Telegram = @https://t.me/SpyWare_x
"""
print(slogan)
time.sleep(1)
print(slogan2)

# Örnek kullanım
msg_user = input("E-Posta Giriniz: ")
msg_password = input("Şifre Giriniz: ")
# key = input("Keyi Giriniz: ")

messenger = Messenger(msg_user=msg_user,msg_password=msg_password)
os.system("cls")
messenger.SignIn()


with open('telif.txt', 'r',encoding="utf-8") as file:
    taslak_mesaj = file.readlines()

taslak_mesaj = ''.join(taslak_mesaj)


sayac = 0

with open('hesaplar.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines() if line.strip()]
    
    for line in lines:
        try:
            messenger.hedef_hesap(line.strip(), "facebook")
            messenger.mesaj_gonder(taslak_mesaj),
            sayac += 1 # increase counter only when message is sent successfully
        except (TimeoutException, Exception, ElementClickInterceptedException) as e:
            print(f"{line.strip()} kullanıcısına ulaşılamadı.")
            messenger.driver.get("https://messenger.com/new")
            continue
        finally:
            actions = ActionChains(messenger.driver)    
            actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
            # Silme işlemi için Delete tuşuna basın
            actions.send_keys(Keys.DELETE).perform()
            # check if "Geçersiz İşlem" text is present
            try:
                element = WebDriverWait(messenger.driver, 3).until(EC.presence_of_element_located((By.XPATH,'//span[text()="Geçersiz İşlem"]')))
                # skip the current user and proceed to the next one
                print(f"{line.strip()} kullanıcısına mesaj gönderilemedi: Geçersiz İşlem.")
                messenger.driver.get("https://messenger.com/new/")
                continue
            except:
                pass
            hedef_hesap_kadi = line.strip()
            print("{} Tane Basıldı Gönderilen Kullanıcı >>> {}".format(sayac,hedef_hesap_kadi))

print("İyi Vuruşlar.")
messenger.driver.quit()

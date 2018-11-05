import os
import glob
import shutil
import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from tkinter import messagebox

def removeCharacter(string, illegalchar = "\\"):
    newstring = string[:string.find('/')] + '\\/' + string[string.find('/')+1:]
    return newstring


chromedriver = r"C:\Users\JHanlon\Desktop\chromedriver_win32\chromedriver.exe"
url = 'https://books.goalkicker.com/'

r = requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')
links = soup.findAll('div',{'class':'bookContainer grow'})

refs = []

for link in links:
    a = link.findAll('a')
    for hrf in a:
        refs.append(hrf.get('href'))
        
browser = webdriver.Chrome(chromedriver)
browser.get(url)
main_window = browser.current_window_handle

for i in range(len(refs)):
    slct = "a[href*="+str(refs[i])+"]"
    slct = removeCharacter(slct)
    sleep(1) # Time in seconds.
    browser.find_element_by_css_selector(slct).click()
    sleep(1) # Time in seconds.
    browser.switch_to_window(browser.window_handles[-1])
    sleep(1) # Time in seconds.
    browser.find_element_by_class_name('download').click()
    sleep(1) # Time in seconds.
    browser.close()
    sleep(1) # Time in seconds.
    browser.switch_to_window(main_window)
    sleep(1) # Time in seconds.
    
    folder = r'C:\Users\JHanlon\Downloads\\'
    downloads = os.path.join(folder,'*')
    files = sorted(glob.iglob(downloads), key=os.path.getctime, reverse=True)
    src = files[0]
    ext = os.path.splitext(src)[1]
    while ext == '.crdownload' :
        sleep(1)
        files = sorted(glob.iglob(downloads), key=os.path.getctime, reverse=True)
        src = files[0]
        ext = os.path.splitext(src)[1]

    files = sorted(glob.iglob(downloads), key=os.path.getctime, reverse=True)
    src = files[0]
    head, tail = os.path.split(src)
    dst = r'C:\Users\JHanlon\Desktop\Programming_Books'
    
    sleep(1)
    shutil.copy2(src,dst)

messagebox.showinfo("Downloads Complete", "You downloaded "+str(len(refs))+" Programming Books from : "+url) 

#browser.close()
#shutil.copyfile(src, dst)
#print(files[0:len(links)])
#print(browser.current_url)
#print(len(browser.window_handles))
#browser.switch_to.window(windows[1])
#browser.execute_script("window.history.go(-1)")

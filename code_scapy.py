from bs4 import BeautifulSoup
import os
from urllib.request import urlopen
from selenium import webdriver
import time


#  1. Khai báo browser
browser = webdriver.Chrome(executable_path ="chromedriver.exe")
#browser = webdriver.chrome(executable_path = "/.Chromedriver.exe")

# 2. Thử mở một trang web
browser.get("http:/google.com")

# 3. Dừng chương trình vài giây
time.sleep(35)

# 4. Đóng trình duyệt
browser.close()

# 5. Sau khi vào web copy url cần craw rồi dán vào đây
a = input('paste url :')

url = a
soup = BeautifulSoup(url,"html.parser")
print(soup)

n = input("""nhập tên file : 
        """)
file = n + '.txt'
f = open(file, 'w')

html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])

        f.write(url)  # Nhập nội dung file
        f.write('\n')
        f.write(link.attrs['href'])
f.close()

#h = 'C:\\Users\\ADMIN\\Desktop'+'\\'+file


#os.rename(file,h)   #lưu file
link=os.getcwd()
print("""LINK :
""",link)


list1 = [1, 2, 4, 20, "chào"]
print('CHuỗi trước khi edit:',list1)
x = list1.pop(0)
print('Phần tử đầu tiên:',x)
print('Chuỗi sau khi edit:',list1)
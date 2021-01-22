from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# 1.1 nhập username fb
username = input('nhập tài khoản Fb :')
pass_fb = input('nhập mật khẩu fb :')

# 2. Thử mở một trang web
#  2.1. Khai báo browser
browser = webdriver.Chrome(executable_path ="chromedriver.exe")
browser.get("https://vi-vn.facebook.com/")

# 2.2 Gửi dữ liệu vào ô username và pass
username_fb = browser.find_element_by_id("email") # tìm kiếm ib có tên email, tài khoản có id là email
username_fb.send_keys(username) #gửi ký tự đến id
pass_work_fb = browser.find_element_by_id("pass")
pass_work_fb.send_keys(pass_fb)

pass_work_fb.send_keys(Keys.ENTER) # login
time.sleep(20) # dừng 20 giây
# 4. Đóng trình duyệt
browser.close()
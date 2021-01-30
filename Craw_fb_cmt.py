from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys
from time import sleep
from easygui import passwordbox

# Lưu ý: Cần đặt file chromedriver chung bên cạnh để có thể chạy chương trình
x = 'yes'
while x == 'yes' :
    # 1.1 nhập username fb
    username = input("USERNAME :")
    pass_fb = passwordbox("PASSWORD:")

    #  1.2 Giả lập chrome
    browser = webdriver.Chrome(executable_path="chromedriver.exe")
    browser.get("https://vi-vn.facebook.com/")

    #  1.3 Gửi dữ liệu vào ô username và pass
    username_fb = browser.find_element_by_id("email")  # tìm kiếm ib có tên email, tài khoản có id là email
    username_fb.send_keys(username)  # gửi ký tự đến id
    pass_work_fb = browser.find_element_by_id("pass")
    pass_work_fb.send_keys(pass_fb)
    sleep(random.randint(2,5))

    pass_work_fb.send_keys(Keys.ENTER)  # login : auto nhấn ENTER

    sleep(random.randint(3,5))
    # dùng lệnh dưới để dừng chương trình đến khi thực hiện xg thao tác trên browser
    start = input('press any to countinute :')

    comment_list = browser.find_elements_by_xpath("//div[@class='b3i9ofy5 e72ty7fz qlfml3jp inkptoze qmr60zad rq0escxv oo9gr5id q9uorilb kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x d2edcug0 jm1wdb64 l9j0dhe7 l3itjdph qv66sw1b']")
    print(comment_list)

     # 2. Lặp trong tất cả các comment và hiển thị nội dung comment ra màn hình
    for comment in comment_list:
     # hiển thị tên người và nội dung, cách nhau bởi dấu :
        poster = comment.find_element_by_class_name("nc684nl6")
        content = comment.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/ul/li[2]/div[1]/div/div[2]/div/div[1]/div/div/div/div/div/span/div")
        print("<>", poster.text, ":", content.text)

    x = input('Bạn muốn tiếp tục craw ?..')
# đóng trình duyệt
    browser.close()

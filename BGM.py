from selenium import webdriver
import time
import json

url = "https://www.mewpot.com/users/sign_in"

emotion = "잔잔"

options = webdriver.ChromeOptions()
options.headless = True   # headless Chrome 구현(브라우저 키지 않아도 알아서 내부적으로 돌아감)
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
prefs = {'download.default_directory': 'C:\\Users\\박규한\\Desktop\\MusicCrawling\\{}'.format(emotion)}
options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(options=options)
browser.maximize_window()

browser.get(url)

with open("information.json") as json_file:
    json_data = json.load(json_file)
    # 로그인 정보 입력
    browser.find_element_by_class_name("login_input_email").send_keys(json_data["id"])
    browser.find_element_by_class_name("login_input_password").send_keys(json_data["password"])
    browser.find_element_by_class_name("login_btn").click()

# 각각의 버튼 식별하는 요소 찾기
free_down_selector = "#simple-modal > div.modal-dialog > div > div.modal-body > div > div > a:nth-child(2)"
down_selector = "#simple-modal > div.modal-dialog > div > div.modal-body > a.button.blue.mb-5.medium.tag-button.pay_catnip"
close_selector = "#simple-modal > div.modal-dialog > div > div.modal-footer > button"

# emotions = ["Smile", "잔잔", "Surprise", "Sad", "Fear"]

for page in range(1, 3):
    url = "https://www.mewpot.com/search/song?page={0}&situation%5B%5D={1}".format(page, emotion)
    browser.get(url)
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, 720)")
    downloads = browser.find_elements_by_css_selector('td.function_cell > div > div:nth-child(3) > a > i')
    print("현재 페이지 :", page)
    for download in downloads:
        download.click()  # 다운로드(구름) 버튼
        time.sleep(1)
        try:
            browser.find_element_by_css_selector(free_down_selector).click()  # 무료 음원 다운로드 버튼
        except(Exception):
            browser.find_element_by_css_selector(down_selector).click()  # 곡 구매 버튼
        finally:
            time.sleep(1)
            browser.find_element_by_css_selector(close_selector).click()  # close 버튼
            time.sleep(1)
            print("download !")

print("download clear !")
browser.quit()  # 실행종료








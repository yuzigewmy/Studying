from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
def main():
    options=webdriver.ChromeOptions()
    location=r"C:\Users\25708\PycharmProjects\pythonProject\chrome-win\chrome.exe"
    options.binary_location=location
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    #设置代理，前期测试发现豆瓣封IP
    proxy = "socks5://127.0.0.1:7890"
    options.add_argument(f"--proxy-server={proxy}")
    driver=webdriver.Chrome(r"C:\Users\25708\PycharmProjects\pythonProject\chromedriver.exe",options=options)
    #电影部分
    driver.get('https://movie.douban.com/tag/#/')
    num1=1
    num2=20
    while True:
        for i in range(num1,num2):
            name = driver.find_element('xpath',f'//div/a[{i}]/p')
            print(name.text)
        num1+=20
        num2+=20
        js = "document.documentElement.scrollTop=10000"
        driver.execute_script(js)
        # time.sleep(1)
        action=ActionChains(driver)
        next=driver.find_element("xpath",'//*[@id="app"]/div/div[1]/a')
        action.click(next)
        action.perform()
        #若网页响应速度较慢，建议打开
        # time.sleep(2)
    driver.quit()
if __name__=="__main__":
    main()

import sys
import time
from selenium import webdriver

def user_chat():

    chat_new = browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    chat_new.click()

    user_chat = browser.find_element_by_xpath('//div[@class="_3u328 copyable-text-selectable-text')
    user_chat.send_keys(name_user)

    time.sleep(2)

    try:
        user= browser.find_element_by_xpath('//span[@title="{}"]' , format(name_user))
        use.click()

    except Exception as e:
        print(f"User {user_name} is not in the contacts")

    except Exception as e:
        browser.close()
        print(e)
        sys.exit()


if __name__ == '__main__':

    my_options = webdriver.ChromeOptions()
    browser = webdriver.Chrome('chromedriver.exe',options=my_options)
    browser.get('http://web.whatsapp.com')

    time.sleep(20)

    name_List = ['shalini']

    for name_user in name_List:
        try:
            user = browser.find_element_by_xpath('//*[@id="main"]/header/div[2]/div/div/span')
            user.click()

        except Exception as e:
            print(e)
            # chat_new(name_user)

            box_message = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]')
            box_message.send_keys("Hi ........")

            box_message = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]/button')
            box_message.click()
            time.sleep(20)

        browser.close()






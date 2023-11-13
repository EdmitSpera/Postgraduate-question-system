from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver  
from selenium.webdriver.edge.service import Service  
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import ElementClickInterceptedException
import time
import re

def scrape_questions(url, num_questions=1000, file_name="question.doc"):
    wb = webdriver.Edge()
    wb.get(url)
    ans = 0
    counter = 0

    while ans < num_questions:
        try:
            time.sleep(1)
            question = wb.find_element(By.TAG_NAME, "h4").text
            p_elements = wb.find_elements(By.TAG_NAME, "p")  
            selection = ""

            for p_element in p_elements:
                if counter > 50:
                    break
                if re.match("^D", p_element.text):
                    selection += p_element.text
                    break
                if re.search("D", selection):
                    break
                if re.search("A", p_element.text) or re.search("B", p_element.text) or re.search("C", p_element.text) or re.search("D", p_element.text):
                    selection += p_element.text
                counter += 1    

            correct_answer_element = "答案:" + wb.find_element(By.XPATH, '//div[@onclick="answer_ok(this)"]').text + "\n"
            
            with open(file_name, "a", encoding="utf-8") as f:
                f.write(question + "\n")
                f.write(selection + "\n")
                f.write(correct_answer_element + "\n")

            next_button = wb.find_elements(By.CLASS_NAME, "timu")
            next_button[1].click()
            ans += 1

        except NoSuchElementException:
            next_button = wb.find_elements(By.CLASS_NAME, "timu")
            next_button[1].click()
            ans += 1

    wb.quit()

def scrape_and_save(url, file_name):
    scrape_questions(url, file_name=file_name)

#爬取数据结构
data_structure_url = "https://noobdream.com/Practice/article/120/"
data_structure_file_name = "data_structure.doc"

#爬取操作系统
opera_sys_url = "https://noobdream.com/Practice/article/372/"
opera_sys_file_name = "opera_sys.doc"

#爬取计算机组成原理
computer_sys_url = "https://noobdream.com/Practice/article/874/"
computer_sys_file_name = "computer_sys.doc"

#爬取计算机网络
web_url = "https://noobdream.com/Practice/article/754/"
web_file_name = "web.doc"


#爬取数据库
database_url = "https://noobdream.com/Practice/article/968/"
database_file_name = "database.doc"

# 使用ThreadPoolExecutor创建线程池
with ThreadPoolExecutor(max_workers=5) as executor:
    # executor.submit(scrape_and_save, data_structure_url, data_structure_file_name)
    executor.submit(scrape_and_save, opera_sys_url, opera_sys_file_name)
    executor.submit(scrape_and_save, computer_sys_url, computer_sys_file_name)
    # executor.submit(scrape_and_save, web_url, web_file_name)
    # executor.submit(scrape_and_save, database_url, database_file_name)

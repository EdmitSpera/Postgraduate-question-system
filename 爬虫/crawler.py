import requests
from bs4 import BeautifulSoup
import re
import os
from urllib.parse import urljoin
from tqdm import tqdm  # 导入tqdm模块

# # 设置代理
# proxies = {
#     'http': 'http://127.0.0.1:7890',    # 再例如  "http":  "http://127.0.0.1:7890",
#     'https': 'http://127.0.0.1:7890',
# }

def visit_web(question_nums, sum=10):
    base_url = 'https://noobdream.com/Practice/article/'
    ans_question_num = 0

    # 使用tqdm显示进度条
    with tqdm(total=sum) as pbar:
        while ans_question_num < sum:
            code_flag = 0
            url = f"{base_url}{question_nums}/"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    soup = BeautifulSoup(response.text, 'html.parser')

                    # 获取题目信息
                    question = soup.find('h4').text

                    # 获取代码框（如果存在）
                    code_element = soup.find('code')
                    if code_element:
                        code = code_element.text
                    else:
                        code_flag = 1

                    # 获取选项
                    selection = ""
                    p_elements = soup.find_all('p')
                    counter = 0
                    for p_element in p_elements:
                        if counter > 10:
                            break
                        if re.match("^D", p_element.text):
                            selection += p_element.text
                            break
                        if re.search("D", selection):
                            break
                        if re.search("[ABCD]", p_element.text):
                            selection += p_element.text
                        counter += 1

                    # 获取图片（如果存在）
                    for p_element in p_elements:
                        img_tags = p_element.find_all('img')
                        if len(img_tags) != 0:
                            for img_tag in img_tags:
                                if img_tag:
                                    match = re.search(r'\[(.*?)\]', question)
                                    image_name = match.group(1)
                                    image_src = img_tag.get('src')

                                    # 检查图片链接是否包含协议部分，如果没有，则补全链接
                                    if not image_src.startswith('http'):
                                        image_src = urljoin(url, image_src)

                                    if image_src.startswith('http'):
                                        # 创建文件夹来保存图片
                                        if not os.path.exists('images'):
                                            os.makedirs('images')
                                        # 下载图片并保存到本地，使用标题中方括号内的内容作为图片的一部分命名
                                        img_data = requests.get(image_src).content
                                        with open(f'images/{image_name}.png', 'wb') as handler:
                                            handler.write(img_data)

                    # 获取答案
                    answer_element = soup.find('div', onclick="answer_ok(this)")
                    correct_answer_element = "答案:" + answer_element.text.strip() + "\n"

                    # 写入文件
                    with open("oj.doc", "a", encoding="utf-8") as f:
                        f.write(question + "\n")
                        f.write(selection + "\n")
                        f.write(correct_answer_element + "\n")

                    question_nums += 1
                    ans_question_num += 1
                    pbar.update(1)  # 更新进度条

                except Exception as e:
                    print(f"Exception occurred: {e}")
                    print("Moving to the next page...")
                    question_nums += 1
                    ans_question_num += 1
                    pbar.update(1)  # 更新进度条
            else:
                print("Failed to fetch page")
                

def main():
    num = 2774               #defalut=16
    sum_question = 2200      #defalut=4973
    visit_web(num, sum_question)

if __name__ == "__main__":
    main()

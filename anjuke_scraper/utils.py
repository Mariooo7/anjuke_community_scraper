import pandas as pd
import requests
from bs4 import BeautifulSoup

# 获取小区具体信息页面链接
def get_url(city, region, page_num, headers, cookies):
    community_links = []
    base_url = f'https://{city}.anjuke.com/community/{region}/'
    link_num = 0
    page = 1
    while(True):
        # 获取对应region的页面
        response = requests.get(f'{base_url}p{page}/', headers=headers, cookies=cookies)
        if response.status_code == 200:
            print("请求成功！")
            page_content = response.text
            soup = BeautifulSoup(page_content, "html.parser")
            # 获取所有小区的链接
            a_tags = soup.find_all('a', class_='li-row')
            for a_tag in a_tags:
                # 提取每个 <a> 标签的 href 属性
                href = a_tag.get('href')
                if href:
                    community_links.append(href)
            new_num = len(community_links) - link_num
            print(f"第{page}页找到 {new_num} 个链接")
            link_num += new_num
            page += 1
            if page - 1 == page_num:
                print(f"爬取完毕，总共爬取{link_num}个链接")
                break
        else:
            print(f"请求失败，状态码：{response.status_code}")
    return(community_links)

# 获取小区具体信息
def get_community_details(url, headers, cookies):
    response = requests.get(url, headers=headers, cookies=cookies)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # 解析详细信息
        # 可根据实际标签增改这些查询条件
        name = soup.find('h1', class_='title').get_text(strip=True)
        address = soup.find('p', class_='sub-title').get_text(strip=True)
        price = soup.find('span', class_='average').get_text(strip=True)
        green_rate = soup.find('div', class_='value value_7').get_text(strip=True)
        property_fee = soup.find('div', class_='value value_13').get_text(strip=True)
        property_type = soup.find('div', class_='value value_0').get_text(strip=True)

        # 输出或返回数据
        return {
            '小区名字': name,
            '小区地址': address,
            '均价': price,
            '绿化率': green_rate,
            '物业费': property_fee,
            '物业类型': property_type
        }

    else:
        print(f"请求失败，状态码：{response.status_code}")
        return None

def save_to_csv(list,filename):
    df = pd.DataFrame(list)
    df.to_csv(filename,index=False, header=True)
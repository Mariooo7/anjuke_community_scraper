from .utils import get_url, get_community_details ,save_to_csv

def get_communities( city, region, page_num, headers, cookies):
    community_links = get_url(city, region, page_num, headers, cookies)
    community_data = []
    # 获取所有小区的详细信息
    for link in community_links:
        try:
            details = get_community_details(link, headers, cookies)
            print(f'处理链接{link}成功')
            if details:
                community_data.append(details)
                print(f'获取{link}详细信息成功')

        except Exception as e:
            print(f"处理链接 {link} 时发生错误: {e}")
            continue  # 发生错误时跳过当前迭代
    save_to_csv(community_data, f'{city}_{region}_{page_num}.csv')
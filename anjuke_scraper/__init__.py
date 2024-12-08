from .utils import get_url, get_community_details, save_to_csv
from .anjuke_scraper import get_communities
from .config import city, region, page_num, headers, cookies

print(f"加载配置：城市={city}, 区域={region}, 页数={page_num}, 请求头 = {headers}, cookies= {cookies}")
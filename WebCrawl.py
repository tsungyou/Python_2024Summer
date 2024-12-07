#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 13:01:46 2024

@author: chihhsuanlin
"""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 目標 URL
url = 'https://swipe.mystrikingly.com/8'  

# 設置 headers 來模擬瀏覽器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 發送 GET 請求以獲取網頁內容
response = requests.get(url, headers=headers)

# 確認請求是否成功
if response.status_code == 200:
    # 使用 BeautifulSoup 解析網頁
    soup = BeautifulSoup(response.content, 'html.parser')

    # 創建保存圖片的文件夾
    if not os.path.exists('images'):
        os.makedirs('images')

    # 找到所有圖片標籤 <img>
    for img_tag in soup.find_all('img'):
        img_url = img_tag.get('src')

        # 如果圖片的 URL 是相對路徑，將其轉換為完整 URL
        img_url = urljoin(url, img_url)

        # 過濾出 JPEG 圖片（以 .jpg 或 .jpeg 結尾）
        if img_url.endswith('.jpg') or img_url.endswith('.jpeg'):
            # 獲取圖片名稱
            img_name = img_url.split('/')[-1]

            try:
                # 下載圖片並保存到本地
                img_response = requests.get(img_url)
                if img_response.status_code == 200:
                    with open(f'images/{img_name}', 'wb') as img_file:
                        img_file.write(img_response.content)
                    print(f'Saved {img_name}')
                else:
                    print(f'Failed to retrieve image from {img_url}')
            except requests.exceptions.RequestException as e:
                print(f'Error downloading {img_url}: {e}')
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')




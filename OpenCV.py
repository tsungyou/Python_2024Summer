#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 15:09:02 2024

@author: chihhsuanlin
"""

import cv2

# 讀取圖片
image_path = "/Users/chihhsuanlin/Desktop/202370_568025.jpeg"
image = cv2.imread(image_path)

if image is None:
    print("無法讀取圖片，請檢查文件是否損壞或路徑是否正確。")
else:
        # 獲取圖片的高度和寬度
    height, width, _ = image.shape
    print(f"圖片大小：{width}x{height}")
    
# 檢查是否正確讀取圖片
if image is None:
    print("無法讀取圖片，請檢查文件路徑是否正確。")
else:
    # 獲取圖片的高度和寬度
    height, width, _ = image.shape
    print(f"圖片大小：{width}x{height}")

    # 設定每列的x坐標範圍（根據圖片的實際情況調整）
    columns = {
        "MON": (300, 385),
        "TUE": (385, 470),
        "WED": (470, 555),
        "THU": (555, 640),
        "FRI": (640, 725),
        "SAT": (815, 900),
        "SUN": (900, 985)
    }

    # 設定每行的y坐標範圍（根據時間段劃分，這些是示例數據，請根據您的圖片調整）
    rows = [
        (205, 280),    # 第一行
        (285, 360),  # 第二行
        (365, 440),  # 第三行
        (445, 520),  # 第四行
        (525, 600),  # 第五行
        (605, 680),  # 第六行
        (685, 760),  # 第七行
        (765, 840),  # 第八行
        (845, 920),  # 第九行
        (930, 1005),  # 第十行
        (1005, 1085),  # 第十一行
        (1090, 1165),  # 第十二行
        (1175, 1250),  # 第十三行
        (1255, 1330),  # 第十四行
        (1335, 1410),  # 第十五行
        (1415, 1490),  # 第十六行
        (1495, 1570),  # 第十七行
    ]

    # 遍歷每一列和每一行，進行裁剪並保存
    for day, (start_x, end_x) in columns.items():
        for idx, (start_y, end_y) in enumerate(rows):
            # 使用高度範圍 [start_y:end_y] 和指定的 x 範圍來裁剪出每一小格
            block_image = image[start_y:end_y, start_x:end_x]

            # 保存每一小格為獨立的圖片
            
            output_path = f"/Users/chihhsuanlin/Desktop/Python Block/{day}_block_{idx + 1:02}.jpeg"
            cv2.imwrite(output_path, block_image)
            print(f"{day} 的區塊 {idx + 1} 已保存為 {output_path}")

    print("圖片裁剪完成！")

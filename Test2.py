from google.cloud import vision
import os
import pandas as pd
import re

# 建立 Vision API 客戶端
client = vision.ImageAnnotatorClient()

# 定義要讀取的圖片文件夾
folder_path = "/Users/chihhsuanlin/Desktop/Python Block/"

# 遍歷文件夾中的所有圖片文件
results = []
for file_name in os.listdir(folder_path):
    if file_name.endswith(".jpeg") or file_name.endswith(".jpg") or file_name.endswith(".png"):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "rb") as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        # 使用文字檢測功能
        response = client.text_detection(image=image)
        texts = response.text_annotations

	# 保存檢測到的文字到 CSV
        first_detected_text = texts[0].description if len(texts) > 0 else ""
        first_text_lines = first_detected_text.split('\n')
        dance_style = first_text_lines[0] if len(first_text_lines) > 0 else ""
        teacher = first_text_lines[1] if len(first_text_lines) > 1 else ""


        # 根據檔案名判斷時間範圍
        time = ""
        block_number = int(re.search(r'_(\d+)', file_name).group(1))
        if file_name.startswith(('MON', 'TUE', 'WED', 'THU', 'FRI')):
            if block_number == 1:
                time = "12:20-13:20"
            elif block_number in [2, 3]:
                time = "13:30-14:30"
            elif block_number in [4, 5, 6]:
                time = "18:30-19:30"
            elif block_number in [7, 8, 9]:
                time = "19:40-20:40"
            elif block_number in [10, 11, 12]:
                time = "20:50-21:50"
        elif file_name.startswith(('SAT', 'SUN')):
            if block_number in [1, 2, 3]:
                time = "13:30-14:30"
            elif block_number in [4, 5, 6]:
                time = "14:40-15:40"
            elif block_number in [7, 8, 9]:
                time = "15:50-16:50"
            elif block_number in [10, 11, 12]:
                time = "17:00-18:00"
            elif block_number in [13, 14, 15]:
                time = "18:10-19:10"
            elif block_number in [16, 17]:
                time = "19:20-20:20"

        # 將結果保存到列表中
        results.append([file_name, dance_style, teacher, time])

# 將結果保存為 CSV
df = pd.DataFrame(results, columns=["檔案名", "舞風", "教師", "時間"])
output_csv_path = "detected_texts_with_time.csv"

        # 如果 CSV 文件不存在，創建並寫入表頭
if not os.path.exists(output_csv_path):
	df.to_csv(output_csv_path, index=False)
else:
        # 如果 CSV 文件已存在，追加寫入
        df.to_csv(output_csv_path, mode='a', header=False, index=False)

print(f"Saved detected text from {file_name} to CSV")


import csv
import json
import os
from tqdm import tqdm
from collections import Counter

# 定义输入文件路径和输出 JSON 文件路径
csv_file_path = '/storage/ScientificPrograms/LMM/inference_fjh/ChestXray14/train_11_1.csv'
json_file_path = '/storage/ScientificPrograms/Diffusion/data/ChestXray14/styleGAN-ChestXRay14/dataset.json'

# 初始化用于存储标签的列表
labels = []

# 读取 CSV 文件
with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # 读取表头（跳过第一行）
    headers = next(csv_reader)
    count = []
    # 遍历每一行数据
    for row in tqdm(csv_reader):
        # 获取图像文件名（去掉文件扩展名）
        image_name = row[1]

        # 查找类别标签
        label_index = next((index for index, value in enumerate(row[2:], start=1) if int(value.strip()) == 1), None)

        # 如果存在有效标签，将其格式化为所需格式
        if label_index is not None:
            label_index -= 1
        elif label_index is None:
            label_index = 14

        # 创建图像路径，格式化为 "val_data/imgXXXXXX.png"
        image_path = f"train/{image_name}"
        # 将路径和标签追加到 labels 列表中
        labels.append([image_path, label_index])
        # count.append(label_index)
# print(Counter(count))

# 创建 JSON 结构
data = {
    "labels": labels
}

# 将数据写入 JSON 文件
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"转换成功！JSON 文件已保存到 {json_file_path}")

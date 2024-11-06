import csv
import json
import os

# 定义输入文件路径和输出 JSON 文件路径
csv_file_path = '/storage/ScientificPrograms/Conditional_Diffusion/ISIC_data/ISIC2019/ISIC_2019_Training_GroundTruth.csv'
json_file_path = '/storage/ScientificPrograms/Conditional_Diffusion/ISIC_data/ISIC2019/dataset.json'

# 初始化用于存储标签的列表
labels = []

# 读取 CSV 文件
with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # 读取表头（跳过第一行）
    headers = next(csv_reader)

    # 遍历每一行数据
    for row in csv_reader:
        # 获取图像文件名（去掉文件扩展名）
        image_name = row[0]

        # 查找类别标签
        label_index = next((index for index, value in enumerate(row[1:], start=1) if int(float(value.strip())) == 1), None) - 1

        # 如果存在有效标签，将其格式化为所需格式
        if label_index is not None:
            # 创建图像路径，格式化为 "val_data/imgXXXXXX.png"
            image_path = f"train_data/{image_name}.jpg"
            # 将路径和标签追加到 labels 列表中
            labels.append([image_path, label_index])

# 创建 JSON 结构
data = {
    "labels": labels
}

# 将数据写入 JSON 文件
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"转换成功！JSON 文件已保存到 {json_file_path}")

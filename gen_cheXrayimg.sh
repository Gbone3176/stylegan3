#!/bin/bash

# 设置CUDA设备
export CUDA_VISIBLE_DEVICES=0,1

# 循环执行 class 从 0 到 14
for class in {0..14}
do
    # 设置输出目录，根据 class 动态调整
    outdir="out-imgs/chestXray-trunc0.1/$class"
    
    # 执行 Python 脚本
    python gen_images.py \
        --network=/cpfs01/projects-SSD/cfff-906dc71fafda_SSD/gbw_21307130160/Downstream/stylegan3/training-runs/chestXray14-train/00007-stylegan3-t-chestXray14-train-gpus2-batch32-gamma2/network-snapshot-000800.pkl \
        --outdir="$outdir" \
        --seeds=0-7 \
        --trunc=0.1 \
        --class="$class" \
        --img_mode=L

    # 检查上一个命令的状态，如果失败则退出循环
    if [ $? -ne 0 ]; then
        echo "Error: gen_images.py failed for class $class"
        exit 1
    fi
done

echo "All images generated successfully."

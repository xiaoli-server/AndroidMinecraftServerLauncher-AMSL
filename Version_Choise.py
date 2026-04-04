import os

target_dir = "/storage/emulated/0/mcserver/"
output_file = "version_list.txt"

# 获取子文件夹列表
folders = [f for f in os.listdir(target_dir) if os.path.isdir(os.path.join(target_dir, f))]

# 写入文件
with open(output_file, "w", encoding="utf-8") as f:
    for folder in folders:
        f.write(folder + "\n")

print(f"已生成 {output_file}，共 {len(folders)} 个文件夹。")

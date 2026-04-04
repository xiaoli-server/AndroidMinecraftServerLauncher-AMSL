print ("欢迎使用AMSL，请输入您想进行的操作（启动服务端/重新下载依赖/下载游戏版本/开启联机(暂时尚未完成)/关于")
num = input()
num_set = {
"启动服务端", "下载Java", "下载游戏版本"
}

if num in num_set:
    print ("输入有效，正在执行")
else:
   print ("请重新输入")

if num =="开启联机":
    print ("联机仍在测试阶段，敬请期待")
    
import os

# 每次运行脚本时，先删除再创建 AMSL.sh
def reset_AMSL_sh():
    file_path = "Service.sh"
    # 如果文件存在，先删除
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"已删除旧文件: {file_path}")
    # 创建新文件
    with open(file_path, "w", encoding="utf-8") as f:
        # 可以在这里写入初始内容，比如一个空的shebang行
        f.write("#!/bin/bash\n")
    print(f"已创建新文件: {file_path}")


if num == "启动服务端":
    # 1. 读取文件所有行
    with open("Service.sh", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 2. 确保文件至少有2行，不足则补空行
    while len(lines) < 2:
        lines.append("\n")

    # 3. 覆盖第二行（索引为1）
    lines[1] = "bash ServerLuncher.sh\n"

    # 4. 写回文件
    with open("Service.sh", "w", encoding="utf-8") as f:
        f.writelines(lines)

if num == "重新下载依赖":
    # 1. 读取文件所有行
    with open("Service.sh", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 2. 确保文件至少有2行，不足则补空行
    while len(lines) < 2:
        lines.append("\n")

    # 3. 覆盖第二行（索引为1）
    lines[1] = "apt install openjdk-21\n"

    # 4. 写回文件
    with open("Service.sh", "w", encoding="utf-8") as f:
        f.writelines(lines)
        
if num == "下载游戏版本":
    # 1. 读取文件所有行
    with open("Service.sh", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 2. 确保文件至少有2行，不足则补空行
    while len(lines) < 2:
        lines.append("\n")

    # 3. 覆盖第二行（索引为1）
    lines[1] = "bash ServerDownload.sh\n"

    # 4. 写回文件
    with open("Service.sh", "w", encoding="utf-8") as f:
        f.writelines(lines)
        
if num == "关于":
    # 1. 读取文件所有行
    with open("Service.sh", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 2. 确保文件至少有2行，不足则补空行
    while len(lines) < 2:
        lines.append("\n")

    # 3. 覆盖第二行（索引为1）
    lines[1] = "bash about.sh\n"

    # 4. 写回文件
    with open("Service.sh", "w", encoding="utf-8") as f:
        f.writelines(lines)
        


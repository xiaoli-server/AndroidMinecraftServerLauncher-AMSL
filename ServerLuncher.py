import sys
# 1. 输入
with open("version_list.txt", "r", encoding="utf-8") as f:
    content = f.read()
user_input = input("请输入想要启动的版本："+content)

# 2. 读取文件
with open("Version_list.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]  # strip() 去除换行符
    
# 3. 核心判断语句
if user_input in lines:
    print("识别到该版本，正在运行")
else:
    print("未识别到输入的版本，请重新输入")
    sys.exit(1)
    
# 4.替换逻辑

file_path = 'ServerLuncher.sh'

lines = []
with open(file_path, 'r', encoding='utf-8') as f:
    for line_num, line_content in enumerate(f, 1): # 枚举行号
        # 判断当前行是否包含关键词
        if "1.21.11" in line_content:
            print(f"正在执行替换")
            # 替换该行
            new_line = line_content.replace("1.21.11", user_input)
            lines.append(new_line)
        else:
            # 不包含则原样保留
            lines.append(line_content)

# 写入修改后的内容
with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
    
    

    

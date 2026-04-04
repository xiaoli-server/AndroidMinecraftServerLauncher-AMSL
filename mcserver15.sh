apt update #更新镜像源
termux-setup-storage #获取访问文件权限
chmod +x mcserver15.sh
cp "$0" /storage/emulated/0/Download/
apt install openjdk-21 #下载java21
apt install git #安装git工具
apt install python #安装python
#下载版本选择库
touch Service.sh
touch ServerLuncher.py
python Version_selection15.py  #运行版本选择库
cd /storage/emulated/0/
mkdir -p mcserver/1.21.11 #创建服务器文件夹
cd /storage/emulated/0/mcserver/1.21.11
curl -O https://raw.githubusercontent.com/xiaoli-server/Minecraft-server-in-android-phone/refs/heads/main/eula.txt #下载配置好的eula协议
curl -O https://raw.githubusercontent.com/xiaoli-server/Minecraft-server-in-android-phone/refs/heads/main/server.properties #下载配置好的服务器配置文件
curl -OJ https://meta.fabricmc.net/v2/versions/loader/1.21.11/0.18.4/1.1.1/server/jar
java -jar fabric-server-mc.1.21.11-loader.0.18.4-launcher.1.1.1.jar #运行启动脚本
cd /storage/emulated/0/mcserver/1.21.11/.fabric/server/
cd /storage/emulated/0/mcserver/1.21.11
java -jar fabric-server-mc.1.21.11-loader.0.18.4-launcher.1.1.1.jar #开服



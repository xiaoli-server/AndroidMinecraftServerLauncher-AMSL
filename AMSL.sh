rm ServerLuncher.sh
curl -O http://154.37.220.137:50800/download/ServerLuncher.sh #下载配置好的服务器配置文件
python AMSL.py
python Version_Choise.py
bash Service.sh
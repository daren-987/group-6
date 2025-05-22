# dockerhub 上的 python image
FROM python:3

# 建立工作目錄 /APP
WORKDIR /APP

# 將當前路徑所有檔案複製到 /APP 內以供容器執行
COPY . /APP

# python 的執行指令
CMD ["python", "main.py"]
from python:3.9-slim
workdir /app
copy requirements.txt ./
run pip install -r requirements.txt 
copy app.py ./
expose 5070
cmd ["python3","app.py"]

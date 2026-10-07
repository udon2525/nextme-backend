# Pythonの軽量イメージを使用
FROM python:3.11-slim

# 作業ディレクティブを設定
WORKDIR /app

# 必要なパッケージ情報をコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリのソースコードをコピー
COPY . .

# Cloud Runのポート(8080)でFastAPI(uvicorn)を起動
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

# Pythonの軽量イメージを使用
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# 依存パッケージ情報をコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリのソースコードをコピー
COPY . .

# ポートの明示 (Cloud Run等のデフォルト 8080)
EXPOSE 8080

# FastAPI (uvicorn) の起動命令
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

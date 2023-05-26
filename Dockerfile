FROM python:3.10-slim
WORKDIR /app
COPY main.py .
#COPY config.json .
RUN pip install requests cloudflare
CMD ["python", "-u", "main.py"]



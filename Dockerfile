FROM python:3.7-slim
RUN apt-get update && apt-get install -y libpython3.7 libcrypt1 && apt-get clean
WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app.py"]

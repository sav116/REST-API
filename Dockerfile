FROM python:3.8-alpine
WORKDIR /app
ADD ./ /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python main.py
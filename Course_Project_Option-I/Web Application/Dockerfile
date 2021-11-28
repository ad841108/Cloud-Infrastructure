FROM python:latest
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","webapplication.py"]
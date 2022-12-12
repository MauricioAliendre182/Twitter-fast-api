FROM python:3.9

WORKDIR /usr/src/app
COPY . /usr/src/app/

RUN pip install --no-cache-dir --upgrade -r /usr/src/app/requirements.txt
# RUN service postgresql start && sudo -u postgres psql -h db -U root -d DataBase -a -f create_tables.sql

CMD ["uvicorn" , "main:app" , "--host" , "0.0.0.0" , "--port" , "8000", "--reload"]
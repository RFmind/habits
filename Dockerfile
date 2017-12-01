FROM tiangolo/uwsgi-nginx-flask:python3.6

WORKDIR /flaskapp

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

COPY habits/ ./

RUN ls ./

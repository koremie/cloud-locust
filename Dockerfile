FROM locustio/locust

EXPOSE 8090

COPY ./locustfile.py /home

FROM locustio/locust

EXPOSE 8090

PORT = 8090

COPY ./locustfile.py /home

FROM bde2020/spark-base:2.4.5-hadoop2.7

LABEL maintainer="Gezim Sejdiu <g.sejdiu@gmail.com>, Giannis Mouchakis <gmouchakis@gmail.com>"

COPY master.sh /

RUN chmod +x /master.sh

ENV SPARK_MASTER_PORT 7077
ENV SPARK_MASTER_WEBUI_PORT 8080
ENV SPARK_MASTER_LOG /spark/logs

EXPOSE 8080 7077 6066 50010 50020 50070 50075 50090 8020 9000 8032 8088 9870 18080

CMD ["/bin/bash", "/master.sh"]

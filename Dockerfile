FROM apache/spark:3.5.1

USER root

# Install Python
RUN apt-get update --allow-releaseinfo-change && \
    apt-get install -y python3 python3-pip

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

# Install tzdata to set the timezone
RUN apt-get install -y tzdata && \
    ln -sf /usr/share/zoneinfo/UTC /etc/localtime && \
    echo "UTC" > /etc/timezone

# Install MySQL JDBC
RUN wget -qO /opt/spark/jars/mysql-connector-java-8.0.30.jar https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.30/mysql-connector-java-8.0.30.jar

# mkdir checkpoint and chmod
RUN mkdir -p /app/checkpoint && \
    chmod -R 777 /app/checkpoint

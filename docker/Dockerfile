FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y \
    build-essential=12.9ubuntu3 \
    cmake=3.22.1-1ubuntu1.22.04.1 \
    git=1:2.34.1-1ubuntu1.10 \
    python3=3.10.6-1~22.04 \
    python3-pip=22.0.2+dfsg-1ubuntu0.4 \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install pytest==8.0

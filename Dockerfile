FROM python:3.8

# update
RUN apt-get -y update && apt-get install -y \
sudo \
wget \
vim \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
&& unzip awscliv2.zip \
&& sudo ./aws/install

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN mkdir /work
WORKDIR /work
FROM ubuntu:latest


RUN apt update && apt -y update
RUN apt install -y build-essential python3.8 python3-pip python3-dev
RUN pip3 -q install pip --upgrade

RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata

RUN apt install ffmpeg libsm6 libxext6  -y
RUN apt install -y libgl1-mesa-glx
RUN apt install -y supervisor

# ssh
RUN apt update && apt install  openssh-server sudo -y
RUN useradd -rm -d /home/pfe -s /bin/bash -g root -G sudo -u 1000 pfe 
RUN echo 'pfe:pfe' | chpasswd
RUN service ssh start
EXPOSE 22

# requirements
RUN mkdir src
WORKDIR /src
ADD ./requirements.txt /src/requirements.txt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Authorize SSH Host
RUN mkdir -p /src/.ssh && \
    chmod 0700 /src/.ssh
    # ssh-keyscan github.com > /src/.ssh/known_hosts

# Add the keys and set permissions
RUN echo "~/.ssh/01_id" > /src/.ssh/01_id && \
    echo "~/.ssh/01_id.pub" > /src/.ssh/01_id.pub && \
    echo "~/.ssh/authorized_keys" > /src/.ssh/authorized_keys && \
    chmod 600 /src/.ssh/01_id && \
    chmod 600 /src/.ssh/01_id.pub && \
    chmod 600 /src/.ssh/authorized_keys 

# tini
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

RUN pip install aiofiles
COPY . /src

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
# ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["supervisord","-c","/src/supervisord.conf"]

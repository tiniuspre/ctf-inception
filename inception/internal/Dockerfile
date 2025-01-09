FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y openssh-server sudo && \
    mkdir /var/run/sshd

RUN useradd -m -s /bin/bash ctfuser && \
    echo 'ctfuser:password' | chpasswd && \
    adduser ctfuser sudo

RUN sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config

RUN sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config

EXPOSE 22

COPY set_password.sh /usr/local/bin/set_password.sh
COPY home/ /home/ctfuser/

RUN chmod +x /usr/local/bin/set_password.sh

ENTRYPOINT ["/usr/local/bin/set_password.sh"]

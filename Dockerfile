FROM docker:dind

RUN apk update && apk add socat


COPY inception/ /inception/

COPY entrypoint.sh /entrypoint.sh
COPY . .

RUN chmod 777 /entrypoint.sh

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN apk add --no-cache python3 py3-pip


EXPOSE 5000
EXPOSE 30000-30150

ENTRYPOINT ["/entrypoint.sh"]

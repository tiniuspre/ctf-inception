FROM docker:dind

RUN apk update && apk add socat

COPY internal/ /internal/

COPY entrypoint.sh /entrypoint.sh
COPY flag.txt /flag.txt

RUN chmod 777 /entrypoint.sh

EXPOSE 22

ENTRYPOINT ["/entrypoint.sh"]

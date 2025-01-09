# CTF Manager
###### Author : Tinius
Warning, super slow when starting and stopping.
Give it time when shutting down or it will fuck upp stuff if you force stop it.

## RUN
```shell
docker compose up --build --remove-orphans --force-recreate
```

## Ports
Default ports are
- 5000
- 40000 to 42000

Increase/decrease in Dockerfile and manager.py
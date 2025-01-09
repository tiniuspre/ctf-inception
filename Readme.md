# CTF Challenge
###### Author: Tinius
###### [@tiniuspre](https://github.com/tiniuspre)

### Level:
Medium / Hard

### Categories:
Docker, docker escape

### Source handout:
No

### Note
[Manager/instance handler](ManagerReadme.md) is not reliable, it was made in one afternoon and is not tested properly. But it works.


## Inception
Inception is inspired by the movie Inception. You are inside a docker, inside a docker, inside a docker. You need to escape the current docker and get the flag.txt on the "system" (First docker level) (But actually second level if you count CTF manager (docker in a docker in a docker)).


## Starting
1. Change flag in docker-compose.yaml.
2. Run `docker-compose up --build -d` in the root directory.
3. Visit `localhost:5000` in your browser.
4. Enter nick name and connect to your instance.

### [Intended Solve](solve.md)
from __future__ import annotations

import os
import subprocess
from time import sleep
from typing import Dict
import random


class Container:
    def __init__(self, participant: str, container_name: str, password: str, port: int):
        self.port = port
        self.container_name = container_name
        self.participant = participant
        self.password = password

    def start(self):
        subprocess.run([
            "docker", "run", "-d",
            "-p", f"{self.port}:22",
            "--name", self.container_name,
            "-e", f"SSH_PASSWORD={self.password}",
            "--privileged",
            "ctf_inception:latest"
        ])

    def stop(self):
        subprocess.run([
            "docker", "stop", self.container_name
        ])
        subprocess.run([
            "docker", "rm", self.container_name
        ])


class CTFManager:
    def __init__(self, port_range_start: int | None = None, port_range_stop: int | None = None):
        self.used_ports = []
        if port_range_start is None:
            port_range_start = os.getenv("PORT_RANGE_START", 40000)
        if port_range_stop is None:
            port_range_stop = os.getenv("PORT_RANGE_STOP", 42000)

        self.port_range_start, self.port_range_stop = int(port_range_start), int(port_range_stop)
        self.running_containers: Dict[str, Container] = {}
        self._build_image()

    def _build_image(self):
        subprocess.run([
            "docker", "build", "-t", "ctf_inception:latest", "inception/"
        ])

    def _get_port(self, count=0):
        if count > 500:
            raise Exception("No available ports")

        port = random.randint(self.port_range_start, self.port_range_stop)
        if port not in self.used_ports:
            self.used_ports.append(port)
            return port
        return self._get_port(count + 1)

    def _release_port(self, port):
        self.used_ports.remove(port)

    def _create_password(self):
        return ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=16))

    def _validate_participant(self, participant) -> Container | None:
        if participant in self.running_containers:
            return self.running_containers[participant]
        return

    def create_container(self, participant: str) -> Container:
        valid = self._validate_participant(participant)
        if valid is not None:
            return valid

        port = self._get_port()
        container_name = f"ctf_inception_{participant}_{port}"
        container = Container(participant=participant, container_name=container_name, password=self._create_password(), port=port)
        container.start()

        self.running_containers.setdefault(participant, container)

        return container

    def stop_all(self):
        for container_name, container in self.running_containers.items():
            container.stop()
            self._release_port(container.port)
            self.running_containers.pop(container_name)


if __name__ == '__main__':
    manager = CTFManager()
    a = manager.create_container("alv")
    b = manager.create_container("brage")

    sleep(5)
    manager.stop_all()

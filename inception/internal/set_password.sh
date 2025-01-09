#!/bin/bash

if [ -z "$SSH_PASSWORD" ]; then
    echo "SSH_PASSWORD not set. Using default password."
else
    echo "ctfuser:${SSH_PASSWORD}" | chpasswd
    echo "Password for ctfuser set."
fi

/usr/sbin/sshd -D

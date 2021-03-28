#!/bin/bash

pip install \
    --trusted-host pypi.org \
    --trusted-host pypi.python.org \
    --trusted-host=files.pythonhosted.org \
    --no-cache-dir \
    -r /usr/local/src/tests/requirements.txt

apt-get update
apt-get install -y firefox-esr

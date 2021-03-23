#!/bin/bash

apt-get update
apt-get install -y firefox-esr
export PATH=$PATH:/usr/local/src/test/features/geckodriver/linux
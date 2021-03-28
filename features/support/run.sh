#!/bin/bash

apt-get update && apt-get install -y firefox-esr
./features/support/requirements.sh

export PATH=$PATH:/usr/local/src/features/support/geckodriver/linux
behave
  
#!/bin/bash

export PATH=$PATH:/usr/local/src/features/support/webdriver
chmod +x /usr/local/src/features/support/webdriver/geckodriver
behave

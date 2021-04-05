FROM python:3

RUN apt-get update && \
    apt-get install -y firefox-esr

COPY features /usr/local/src/features/
RUN pip install \
    --trusted-host pypi.org \
    --trusted-host pypi.python.org \
    --trusted-host=files.pythonhosted.org \
    --no-cache-dir \
    -r /usr/local/src/features/support/requirements.txt
WORKDIR /usr/local/src

CMD ["/usr/local/src/features/support/start.sh"]

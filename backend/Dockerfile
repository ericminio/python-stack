FROM python:3

RUN apt-get update && apt-get install -y postgresql-client

COPY requirements* /usr/local/src/backend/
RUN pip install \
    --trusted-host pypi.org \
    --trusted-host pypi.python.org \
    --trusted-host=files.pythonhosted.org \
    --no-cache-dir \
    -r /usr/local/src/backend/requirements-prod.txt

WORKDIR /usr/local/src

CMD ["/usr/local/src/backend/start.sh"]

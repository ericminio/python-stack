FROM python:3

COPY . /usr/local/src/backend
RUN pip install \
    --trusted-host pypi.org \
    --trusted-host pypi.python.org \
    --trusted-host=files.pythonhosted.org \
    --no-cache-dir \
    -r /usr/local/src/backend/requirements-prod.txt

WORKDIR /usr/local/src
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "backend:app"]

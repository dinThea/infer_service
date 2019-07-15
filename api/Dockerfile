FROM iagoeli/opencv:4.1
WORKDIR /api
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
# ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--log-level", "warning", "example:app"]
FROM iagoeli/opencv:4.1
WORKDIR /api
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
# RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV FLASK_ENV development
COPY . .
CMD ["flask", "run"]
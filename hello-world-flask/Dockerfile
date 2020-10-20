FROM python:3.7-alpine AS base
WORKDIR /src
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt && rm /tmp/requirements.txt

FROM base AS test
COPY requirements-dev.txt /tmp/requirements-dev.txt
RUN pip3 install -r /tmp/requirements-dev.txt && rm /tmp/requirements-dev.txt
CMD ["nosetests", "--with-timer", "--with-randomly"]

FROM test AS localdev
ENV FLASK_APP /src/helloworld/app.py
ENV FLASK_DEBUG 1
CMD ["flask", "run", "--host", "0.0.0.0"]

FROM base AS final
COPY . /src
CMD ["gunicorn", "-b", "0.0.0.0:5000", "helloworld.app:app"]

FROM node:current-alpine3.17
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python && \
    python3 -m ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools && \
    pip3 install pipenv
RUN apk add --no-cache bash build-base zlib-dev
COPY ./ /PineSAM
WORKDIR /PineSAM
RUN chmod +x setup-dev.sh && ./setup-dev.sh
RUN chmod +x run-dev.sh

ENTRYPOINT ["./run-dev.sh"]

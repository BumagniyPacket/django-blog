FROM alpine:3.7

RUN addgroup -S -g 777 django && adduser -D -S -G django -u 777 django

RUN apk -U upgrade && echo http://nl.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories && \
    apk -U --no-cache add git python3 ca-certificates musl-dev gcc python3-dev postgresql-dev \
    gettext libffi-dev openjpeg openjpeg-tools openjpeg-dev libjpeg-turbo \
    libjpeg-turbo-utils libjpeg-turbo-dev musl freetype freetype-dev \
    libwebp lcms2 tiff zlib zlib-dev libmagic cabextract fontconfig cups-dev && \
    update-ca-certificates && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache && \
    ln -s /usr/bin/python3 /usr/bin/python

RUN mkdir -p /code && chown -R django /code
WORKDIR /code
ADD . /code/

RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./scripts/entrypoint.sh /entrypoint.sh
COPY ./scripts/gunicorn.sh /gunicorn.sh
COPY ./scripts/start_dev.sh /start_dev.sh
RUN sed -i 's/\r//' /entrypoint.sh \
    && sed -i 's/\r//' /gunicorn.sh \
    && sed -i 's/\r//' /start_dev.sh \
    && chmod +x /entrypoint.sh \
    && chown django /entrypoint.sh \
    && chmod +x /gunicorn.sh \
    && chown django /gunicorn.sh \
    && chmod +x /start_dev.sh \
    && chown django /start_dev.sh

RUN mkdir -p /code/public
RUN chown -R django /code/public
RUN mkdir -p /code/public/badges
RUN chown -R django /code/public/badges
VOLUME ["/code/public"]

HEALTHCHECK --interval=10s --timeout=10s CMD python /code/manage.py watchman || exit 1
EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]

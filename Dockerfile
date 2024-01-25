FROM  python:3.11-slim-bullseye
LABEL mantainer="tengobilt@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./djangoapp /djangoapp
COPY ./scripts /scripts

RUN apt update && \
    apt install -y netcat

WORKDIR /djangoapp


RUN pip install -r requirements.txt

RUN adduser --disabled-password --no-create-home duser

RUN mkdir -p /data/web/static && \
    mkdir -p /data/web/media

RUN chown -R duser:duser /data/web/static && \
    chown -R duser:duser /data/web/media && \
    chmod -R 755 /data/web/static && \
    chmod -R 755 /data/web/media && \
    chmod -R +x /scripts

ENV PATH="$PATH:/scripts"

USER duser

CMD ["commands.sh"]
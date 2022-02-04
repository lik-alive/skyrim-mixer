FROM python:3.10-alpine

RUN adduser -D worker
USER worker

WORKDIR /home/worker
COPY --chown=worker:worker ./src .

CMD [ "python3", "-m", "http.server", "--cgi" ]
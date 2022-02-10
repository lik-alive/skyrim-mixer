FROM python:3.10-alpine

# RUN adduser -D worker
# USER worker

WORKDIR /home/worker
COPY ./src .
COPY --chown=33:33 ./src .

CMD [ "python3", "-m", "http.server", "--cgi" ]
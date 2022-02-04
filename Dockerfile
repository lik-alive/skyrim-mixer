FROM python:3.10-alpine
WORKDIR /app
COPY ./src .
CMD [ "python3", "-m", "http.server", "--cgi" ]
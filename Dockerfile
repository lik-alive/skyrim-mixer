FROM python:3.10-alpine
WORKDIR /app
CMD [ "python3", "-m", "http.server", "--cgi" ]
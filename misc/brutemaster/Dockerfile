FROM ubuntu
RUN apt-get -y update && apt-get install -y netcat python
HEALTHCHECK CMD nc -z -n -v 127.0.0.1 50001 || exit 1
ADD app /app
WORKDIR /app
EXPOSE 50001
CMD ["python2", "/app/service.py"]

FROM python:3
COPY static/ /root
RUN apt-get -y update && apt-get -yqq install locales; \
	locale-gen ru_RU.UTF-8
EXPOSE 31265
HEALTHCHECK CMD nc -z -n -v 127.0.0.1 31265 || exit 1

WORKDIR /root
CMD [ "python3", "server.py" ]

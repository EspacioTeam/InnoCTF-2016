FROM fedora

RUN dnf upgrade -y && dnf install -y rust cargo && mkdir -p /srv/rustyserver

EXPOSE 8765
WORKDIR /srv/rustyserver/
ADD rustyserver /srv/rustyserver
RUN cargo build --release

HEALTHCHECK CMD curl http://localhost:8765 -s || exit 1

CMD ["cargo", "run", "--release"]

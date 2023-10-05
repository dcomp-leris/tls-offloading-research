
FROM debian:latest
ARG KTLS_ENABLED="true"

RUN apt update; apt install procps zlib1g-dev libpcre3-dev build-essential make wget net-tools tmux curl vim -y
RUN wget https://www.openssl.org/source/openssl-3.0.0.tar.gz
ADD "./nginx-1.21.4.tar.gz" .
RUN tar xzf openssl-3.0.0.tar.gz
WORKDIR /nginx-1.21.4
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt -subj "/C=BR/ST=Sao Paulo/L=Sao Paulo/O=.../OU=.../CN=.../emailAddress=..."

# Conditionally copy the appropriate nginx.conf file
RUN mkdir -p /etc/nginx
COPY ./nginx_ktls.conf /etc/nginx/nginx_ktls.conf
COPY ./nginx_noktls.conf /etc/nginx/nginx_noktls.conf
RUN echo "$KTLS_ENABLED"
RUN if [ "$KTLS_ENABLED" = "true" ]; then \
    echo "Compiling nginx+kTLS image"; \
    cp /etc/nginx/nginx_ktls.conf /etc/nginx/nginx.conf; \
    ./configure --with-openssl=../openssl-3.0.0 --with-openssl-opt=enable-ktls; \
    else \
    echo "Compiling nginx without kTLS image"; \
    cp /etc/nginx/nginx_noktls.conf /etc/nginx/nginx.conf; \
    ./configure; \
    fi
RUN cat /etc/nginx/nginx.conf ; echo 1

RUN make -j4
RUN make install
RUN find /usr/local/ -type f -name nginx
RUN mkdir /var/cache/nginx
RUN useradd -r nginx
RUN mkdir /data
RUN truncate --size 1G /data/1G
RUN truncate --size 30G /data/30G
RUN truncate --size 1M /data/1M
RUN truncate --size 100M /data/100M
WORKDIR /
ADD entrypoint.sh .
RUN chmod +x entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
EXPOSE 8383

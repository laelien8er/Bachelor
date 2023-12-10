FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

# install java version
RUN apt update
RUN apt install -y testdisk wget gnupg

RUN wget -q -O - https://download.bell-sw.com/pki/GPG-KEY-bellsoft | apt-key add -
RUN echo "deb [arch=amd64] https://apt.bell-sw.com/ stable main" > /etc/apt/sources.list.d/bellsoft.list
RUN apt update
RUN apt install -y bellsoft-java8

ENV JAVA_HOME=/usr/lib/jvm/bellsoft-java8-amd64

RUN apt update && apt install -y \
        apt-utils \
        curl \
		dnsutils \
        libafflib0v5 \
        libafflib-dev \
        libboost-all-dev \
        libboost-dev \
        libc3p0-java \ 
        libewf2 \
        libewf-dev \
        libpostgresql-jdbc-java \
        libpq5 \
        libsqlite3-dev \
        libvhdi1 \
        libvhdi-dev \
        libvmdk1 \
        libvmdk-dev \
        openjfx \
        testdisk \
        unzip \
        xauth \
        x11-apps \
        x11-utils \
        x11proto-core-dev \
        x11proto-dev \
        xkb-data \
        xorg-sgml-doctools \
        xtrans-dev \
        libcanberra-gtk-module \
	squashfs-tools \ 
	git \
	make \
	gcc \
	libbz2-dev \
	libclang-dev \
	liblinear \
	&& rm -rf /var/lib/apt/lists/*

# install sceadan

RUN mkdir -p /opt \
    && cd /opt \
	&& curl -L https://github.com/UTSA-cyber/sceadan/archive/refs/tags/v1.2.1.tar.gz > v1.2.1.tar.gz \
	&& tar -xf v1.2.1.tar.gz \
	&& rm v1.2.1.tar.gz \
	&& cd /opt/sceadan-1.2.1/src \
	&& chmod 744 configure \ 
	&& ./configure && make && make install 

# install liblinear


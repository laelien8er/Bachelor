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


RUN apt-get update && apt-get install -y \
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
	sudo \
	openjdk-17-jdk openjdk-17-jre \
    build-essential autoconf libtool automake git zip wget ant \
    libde265-dev libheif-dev \
    libpq-dev \
    testdisk libafflib-dev libewf-dev libvhdi-dev libvmdk-dev \
    libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x \
    gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio \
    && rm -rf /var/lib/apt/lists/*

# install scalpel
RUN cd /opt \
	&& git clone https://github.com/sleuthkit/scalpel.git \
	&& apt-get update -y && apt-get install -y gettext autopoint\
	&& git clone https://github.com/laurikari/tre.git \
	&& cd /opt/tre \
	&& ./utils/autogen.sh \
	&& ./configure && make && make check && make install \
	&& ./configure && make dist \
	&& cd /opt/scalpel && ./bootstrap && ./configure && make 
	
# install bulk_extractor
RUN cd /opt \
	&& git clone --recurse-submodules https://github.com/simsong/bulk_extractor.git \
	&& cd /opt/bulk_extractor/etc \
	&& bash CONFIGURE_UBUNTU20LTS.bash \
	&& cd .. \
	&& ./bootstrap.sh && ./configure && make && make install
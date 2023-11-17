#  --add-opens=java.base/java.lang=ALL-UNNAMED

# run autopsy with bin/autopsy

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
	openjdk-17-jdk openjdk-17-jre \
    build-essential autoconf libtool automake git zip wget ant \
    libde265-dev libheif-dev \
    libpq-dev \
    testdisk libafflib-dev libewf-dev libvhdi-dev libvmdk-dev \
    libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x \
    gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio \
    && rm -rf /var/lib/apt/lists/*

# install autopsy
RUN mkdir -p /opt \
    && cd /opt \
    && curl -L https://github.com/sleuthkit/autopsy/releases/download/autopsy-4.21.0/autopsy-4.21.0.zip > autopsy-4.21.0.zip \
    && unzip autopsy-4.21.0.zip \
    && rm autopsy-4.21.0.zip \
	&& cd /opt \
    && curl -L https://github.com/sleuthkit/sleuthkit/releases/download/sleuthkit-4.12.1/sleuthkit-java_4.12.1-1_amd64.deb > sleuthkit-java_4.12.1-1_amd64.deb \
    && dpkg -i sleuthkit-java_4.12.1-1_amd64.deb \
        || apt-get install -fy \
	&& cd /opt/autopsy-4.21.0/ \
	&& chmod 744 unix_setup.sh \
	&& ./unix_setup.sh
	
# install sleuthkit
RUN git clone https://github.com/sleuthkit/sleuthkit.git \
 && cd /sleuthkit && ./bootstrap && ./configure && make && make install

# install foremost
RUN cd /opt \
	&& curl -L http://foremost.sourceforge.net/pkg/foremost-1.5.7.tar.gz > foremost-1.5.7.tar.gz \
	&& tar -xf foremost-1.5.7.tar.gz && cd /opt/foremost-1.5.7 && make && make install \
	&& cd /opt \
	&& rm foremost-1.5.7.tar.gz

# install scalpel
RUN cd /opt \
	&& git clone https://github.com/sleuthkit/scalpel.git \
	&& apt-get update -y && apt-get install -y gettext \
	&& git clone https://github.com/laurikari/tre.git \
	&& cd /opt/tre \
	&& ./utils/autogen.sh \
	&& ./configure && make && make check && make install \
	&& cd /opt/scalpel && ./bootstrap && ./configure && make 

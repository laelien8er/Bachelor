FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

ENV JAVA_HOME /opt/jdk1.8.0_201
ENV PATH /opt/autopsy/bin:${JAVA_HOME}/bin:$PATH

COPY --from=bannsec/autopwn-stage-j8 /tmp/jdk* /opt/.

RUN apt-get update && apt-get install -y \
        apt-utils \
		build-essential \
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
        wget \
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
	
# install autopsy, sleuthkit
RUN mkdir -p /opt \
    && cd /opt \
    && curl -L https://github.com/sleuthkit/autopsy/releases/download/autopsy-4.21.0/autopsy-4.21.0.zip > autopsy.zip \
    && mkdir autopsy \
    && unzip -d autopsy autopsy.zip \
    && mv autopsy/autopsy*/* autopsy/. \
    && rm autopsy.zip \
    && curl -L https://github.com/sleuthkit/sleuthkit/releases/download/sleuthkit-4.12.1/sleuthkit-java_4.12.1-1_amd64.deb > tsk_java.deb \
    && dpkg -i tsk_java.deb \
        || apt-get install -fy \
    && cd /opt \
    && unzip -P AcceptEULA jdk*.zip \
    && rm jdk*.zip \
    && cd /opt/autopsy*/ \
	&& ["chmod", "+x", "./unix_setup.sh"]


# install foremost
RUN cd /opt \
	&& curl -L http://foremost.sourceforge.net/pkg/foremost-1.5.7.tar.gz > foremost-1.5.7.tar.gz \
	&& tar -xf foremost-1.5.7.tar.gz && cd/foremost-1.5.7 && make && make install 

# install scalpel
RUN cd /opt \
	&& git clone https://github.com/sleuthkit/scalpel.git \
	&& cd /scalpel && ./bootstrap && ./configure && make \

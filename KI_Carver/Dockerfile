# run container:
# docker run -d -it -v /c/Bachelorarbeit/KI_Carver/case:/case <containername>
# docker exec -it <containerid> /bin/bash		

# validate data
# cd tools && python3 sceadan_train.py --validate --data=/case/DATA --exp=<outputfolder>

# train data 
# cd tools && python3 sceadan_train.py --data=/case/DATA --exp=<outputfolder>

FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

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
	gcc \
	libbz2-dev \
	libclang-dev \
	python3 python3-dev python3-pip python3-setuptools \
	liblinear-tools liblinear-dev python3-liblinear \
	libtool libtool-bin libtool-doc\
	&& rm -rf /var/lib/apt/lists/*

# create directory for Dataset
RUN mkdir -p /case

# install sceadan
RUN mkdir -p /opt \
    && cd /opt \
	&& git clone --recursive https://github.com/UTSA-cyber/sceadan.git \
	&& cd sceadan \
	&& autoreconf --force --install \
	&& sh bootstrap.sh && ./configure && make
	



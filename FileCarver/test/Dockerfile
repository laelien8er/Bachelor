FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

ENV JAVA_HOME /opt/jdk1.8.0_201
ENV PATH /opt/autopsy/bin:${JAVA_HOME}/bin:$PATH

RUN apt-get update && apt-get install -y \
	testdisk \
	wget \
	gnupg \
	p7zip-full \
	openjfx \
	squashfs-tools \
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
	exiftool && \
   	apt-get clean && \
    	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


WORKDIR /tmp

RUN wget https://github.com/sleuthkit/autopsy/releases/download/autopsy-4.19.0/autopsy-4.19.0.zip
RUN wget https://github.com/sleuthkit/sleuthkit/releases/download/sleuthkit-4.11.0/sleuthkit-java_4.11.0-1_amd64.deb

RUN apt install -y ./sleuthkit-java_4.11.0-1_amd64.deb

WORKDIR /opt
RUN 7z x /tmp/autopsy-4.19.0.zip

WORKDIR /opt/autopsy-4.19.0
RUN bash unix_setup.sh
RUN chmod +x /opt/autopsy-4.19.0/bin/autopsy
RUN ln -s /opt/autopsy-4.19.0/bin/autopsy /bin/
CMD ["/bin/autopsy", "--nosplash"]
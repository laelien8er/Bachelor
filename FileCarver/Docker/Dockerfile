FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y testdisk wget gnupg

RUN wget -q -O - https://download.bell-sw.com/pki/GPG-KEY-bellsoft | apt-key add -
RUN echo "deb [arch=amd64] https://apt.bell-sw.com/ stable main" > /etc/apt/sources.list.d/bellsoft.list
RUN apt-get update
RUN apt-get install -y bellsoft-java8

ENV JAVA_HOME=/usr/lib/jvm/bellsoft-java8-amd64

WORKDIR /tmp

RUN wget https://github.com/sleuthkit/autopsy/releases/download/autopsy-4.19.0/autopsy-4.19.0.zip
RUN wget https://github.com/sleuthkit/sleuthkit/releases/download/sleuthkit-4.11.0/sleuthkit-java_4.11.0-1_amd64.deb

RUN apt install -y ./sleuthkit-java_4.11.0-1_amd64.deb

WORKDIR /opt
RUN apt-get install -y p7zip-full openjfx
RUN 7z x /tmp/autopsy-4.19.0.zip

WORKDIR /opt/autopsy-4.19.0
RUN bash unix_setup.sh
RUN chmod +x /opt/autopsy-4.19.0/bin/autopsy
RUN ln -s /opt/autopsy-4.19.0/bin/autopsy /bin/
CMD ["/bin/autopsy", "--nosplash"]

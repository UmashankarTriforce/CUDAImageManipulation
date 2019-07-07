FROM nvidia/cuda
MAINTAINER Umashankar Sivakumar <umashankarsivakumar@gmail.com>

ENV UNAME nvidiacuda


RUN cp /etc/apt/sources.list /etc/apt/sources.list~ && \
    sed -Ei 's/^# deb-src /deb-src /' /etc/apt/sources.list

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt install --yes pulseaudio-util \
    build-essential libgl1-mesa-dev libassimp-dev libfontconfig1 libdbus-1-3 libasound* libgtk2.0-dev python3-pip \
    sudo lsb-release bash-completion git vim wget curl \
    ccache perl python build-dep qtbase5-dev \
    "^libxcb.*" libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev \
    "libatspi2*" libdbus-1-dev \
    flex bison gperf libicu-dev libxslt-dev ruby \
    libssl-dev libxcursor-dev libxcomposite-dev libxdamage-dev libxrandr-dev libfontconfig1-dev libcap-dev libbz2-dev \
    libgcrypt11-dev libpci-dev libnss3-dev libxcursor-dev libxcomposite-dev libxdamage-dev libxrandr-dev libdrm-dev    \
    libfontconfig1-dev libxtst-dev libasound2-dev libcups2-dev libpulse-dev libudev-dev libssl-dev \
    libasound2-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev


RUN wget https://download.qt.io/archive/qt/5.9/5.9.4/qt-opensource-linux-x64-5.9.4.run && chmod +x qt-opensource-linux-x64-$5.9.4.run 
COPY qt-installer-noninteractive.qs /qt-installer-noninteractive.qs
RUN ./qt-opensource-linux-x64-5.9.4.run --script qt-installer-noninteractive.qs \
 --verbose --platform minimal && \

    pip3 install PyQt5 pycuda numpy opencv-python scikit-cuda && \
    export UNAME=$UNAME UID=1000 GID=1000 && \
    mkdir -p "/home/${UNAME}" && \
    echo "${UNAME}:x:${UID}:${GID}:${UNAME} User,,,:/home/${UNAME}:/bin/bash" >> /etc/passwd && \
    echo "${UNAME}:x:${UID}:" >> /etc/group && \
    mkdir -p /etc/sudoers.d && \
    echo "${UNAME} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/${UNAME} && \
    chmod 0440 /etc/sudoers.d/${UNAME} && \
    chown ${UID}:${GID} -R /home/${UNAME} && \
    gpasswd -a ${UNAME} audio &&\
    usermod -aG sudo nvidiacuda

COPY pulse-client.conf /etc/pulse/client.conf

USER $UNAME
ENV HOME /home/nvidiacuda
RUN cd && git clone https://github.com/UmashankarTriforce/CUDAImageManipulation.git
CMD ["bash"]

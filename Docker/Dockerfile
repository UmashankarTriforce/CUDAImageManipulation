FROM nvidia/cuda
MAINTAINER Umashankar Sivakumar <umashankarsivakumar@gmail.com>

ENV UNAME nvidiacuda

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt install --yes pulseaudio-utils sudo \
 build-essential libgl1-mesa-dev libassimp-dev libfontconfig1 libdbus-1-3 wget libasound* libgtk2.0-dev python3-pip \
 libxcb*

#pip files
RUN sudo pip3 install PyQt5

# Set up the user
RUN export UNAME=$UNAME UID=1000 GID=1000 && \
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

ENV QT_VERSION_A=5.9
ENV QT_VERSION_B=5.9.4
ENV QT_VERSION_SCRIPT=594

RUN sudo wget https://download.qt.io/archive/qt/${QT_VERSION_A}/${QT_VERSION_B}/qt-opensource-linux-x64-${QT_VERSION_B}.run
RUN sudo chmod +x qt-opensource-linux-x64-${QT_VERSION_B}.run 
COPY qt-installer-noninteractive.qs /qt-installer-noninteractive.qs
RUN sudo ./qt-opensource-linux-x64-${QT_VERSION_B}.run --script qt-installer-noninteractive.qs \
 --verbose --platform minimal

# run
CMD ["bash"]

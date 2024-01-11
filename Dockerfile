# This is a sample Dockerfile you can modify to deploy your own app based on face_recognition

FROM python:3.8-slim-buster

RUN apt-get -y update
RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN git clone -b 'v19.16' --single-branch https://github.com/davisking/dlib.git && \
    mkdir -p /dlib/build && \
    cmake -H/dlib -B/dlib/build -DDLIB_USE_CUDA=1 -DUSE_AVX_INSTRUCTIONS=1 && \
    cmake --build /dlib/build && \
    cd /dlib && \
    python3 /dlib/setup.py install
    git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python3 setup.py install --yes USE_AVX_INSTRUCTIONS


# The rest of this file just runs an example script.

# If you wanted to use this Dockerfile to run your own app instead, maybe you would do this:
# COPY . /root/your_app_or_whatever
# RUN cd /root/your_app_or_whatever && \
#     pip3 install -r requirements.txt
# RUN whatever_command_you_run_to_start_your_app

COPY requirements.txt /root/face_recognition/
COPY . /root/face_recognition
COPY requirements.txt /root/face_recognition/
COPY . /root/face_recognition
RUN pip install -r /root/face_recognition/requirements.txt

CMD cd /root/face_recognition/examples && \
    python3 recognize_faces_in_pictures.py

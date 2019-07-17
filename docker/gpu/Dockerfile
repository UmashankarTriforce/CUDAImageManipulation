FROM nvcr.io/nvidia/cuda:10.1-devel-ubuntu18.04

RUN apt-get update && \
    apt-get install -y python3-pip 
COPY gpu_requirements.txt /gpu/gpu_requirements.txt
RUN pip3 install -r /gpu/gpu_requirements.txt
EXPOSE 5000
CMD ["python3", "/gpu/server.py"]


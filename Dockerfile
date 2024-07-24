FROM python:3.10.13

RUN apt-get update -y && \
    apt-get install -y python3-opencv \
                       libgl1-mesa-glx \
                       libglib2.0-0 \
                       libsm6 \
                       libxrender1 \
                       libxext6 \
                       xvfb

WORKDIR /home/src

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

ENV DISPLAY=host.docker.internal:0.0

CMD ["python", "main.py"]

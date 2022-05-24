# CPU
# FROM gcr.io/kaggle-images/python:latest

# GPU
FROM gcr.io/kaggle-gpu-images/python:v115


RUN pip install autopep8 japanize_matplotlib hydra
RUN sudo apt install -y fonts-ipafont
RUN fc-cache -fv

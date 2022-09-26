sudo docker build -t project .
sudo docker run \
    -v `pwd`/:/app \
    -p 8501:8501 \
    project
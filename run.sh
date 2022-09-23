sudo docker volume create --name projectVolume
sudo docker run \
    -v `pwd`/:/app \
    -p 8501:8501 \
    project
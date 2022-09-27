sudo docker build -t project .
sudo docker run -v `pwd`/:/app -p 80:80 wce-github-enterprise
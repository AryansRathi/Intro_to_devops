## For testing IS_READY=true
```
docker build -t start --build-arg IS_READY=true .
docker run --name start -p 8080:80 -t start
```

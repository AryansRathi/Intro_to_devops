## For testing IS_READY=true
```
docker build -t start --build-arg IS_READY=true .
docker run --name start -p 8080:80 -t start
```
## For testing IS_READY=False
```
docker build -t not_start --build-arg IS_READY=false .
docker run --name not_start -p 8080:80 -t not_start
```

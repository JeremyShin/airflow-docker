colima , docker-compose 설치
- https://smallsharpsoftwaretools.com/tutorials/use-colima-to-run-docker-containers-on-macos/

```shell
sudo chown -R $(whoami) ~/.docker

docker-compose up --build
```

- 이미지 삭제하고 싶을 땐
```shell
docker-compose down --volumes --rmi all
```
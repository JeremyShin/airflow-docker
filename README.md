colima , docker-compose 설치
- https://smallsharpsoftwaretools.com/tutorials/use-colima-to-run-docker-containers-on-macos/

```shell
# 콜리마 설치 후 커스터마이즈 실행
colima start --cpu 4 --memory 8

sudo chown -R $(whoami) ~/.docker
docker-compose up --build
```

- 이미지 삭제하고 싶을 땐
```shell
docker-compose down --volumes --rmi all
```
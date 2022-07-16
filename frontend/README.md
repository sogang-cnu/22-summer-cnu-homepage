## 프로젝트 실행 방법

### 릴리즈용

1. `cp env .env `
   - .env 파일 생성 
   - 로컬 실행 포트 설정
2. `docker-compose --profile release up -d`
   - release 프로파일로 Docker 실행

### 개발용

1. node 설치
2. `npm install -g yarn`
3. `yarn`
4. `yarn start`
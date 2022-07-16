## 프로젝트 실행 방법
프로젝트 루트 폴더 : /frontend/
프로젝트 실행 전 `cp env .env`를 통하여 `.env` 파일을 만들고 환경 변수를 설정해주시기 바랍니다.

### 릴리즈용
2. `docker-compose --profile release up -d`

### 개발용
1. node 설치
2. `npm install -g yarn`
3. `yarn`
4. `yarn start`
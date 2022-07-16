## 프로젝트 실행 방법
- 프로젝트 루트 폴더 : /backend/
- 프로젝트 실행 전 `cp env .env`를 통하여 `.env` 파일을 만들고 환경 변수를 설정해주시기 바랍니다.

### 릴리즈용
1. `./runserver`

### 개발용
1. Python 3 설치
2. `pip install virtualenv `
3. `python -m venv venv`
4. `source ./venv/Scripts/activate`
5. `pip install -r requirements.txt`
6. `docker-compose --profile dev up -d`
7. `python manage.py migrate`
8. `python manage.py runserver`

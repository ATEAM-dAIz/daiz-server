# daiz-server

## 1. 준비🛠
### reuirements.txt 설치
``` C
pip install -r requirements.txt
```
### kobert 설치
- Windows
``` C
pip install git+https://git@github.com/Jsgithubchannel/KoBERT.git@master
```
### 마이그레이션 적용 
``` C
python manage.py makemigrations
```
- TypeError: __init__() got an unexpected keyword argument 'return_dict' 오류 발생시
  ``` C
  pip install transformers==4.15.0
  ```
``` C
python manage.py migrate
```
- 테이블 생성이 안될 시 https://stackoverflow.com/a/62454561



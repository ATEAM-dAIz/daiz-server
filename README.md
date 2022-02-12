# daiz-server

## 준비🛠
### 1. 인공지능 모델 학습
- [situation.pt](https://github.com/ATEAM-dAIz/daiz-training-situation)

- [emotion.pt](https://github.com/ATEAM-dAIz/daiz-training-emotion)

- [comment.pt](https://github.com/ATEAM-dAIz/daiz-training-comment)

### 2. reuirements.txt 설치
``` C
pip install -r requirements.txt
```
### 3. kobert 설치
``` C
pip install git+https://git@github.com/Jsgithubchannel/KoBERT.git@master
```
### 4. 마이그레이션 적용 
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



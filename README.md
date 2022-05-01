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
### 3. kobert 설치(Windows 환경에 적합하도록 requirements.txt 수정한 KoBERT 입니다.)
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

# 📝 dAIz (데이즈)

## 프로젝트 소개
- AI를 통해 일기를 분석하여 심리 상태를 알려주고 공감하는 웹입니다.

## 기술 스택
- React | Redux
- TypeScript
- HTML, SCSS Modules
- Django Rest API
- Korean BERT pre-trained cased API


##  기능 / 소개
- 자연어 처리 기법을 사용하여 사용자의 감정을 분석하고 의견을 제시합니다.
- PyTorch 기반 딥러닝 API를 사용했습니다. (KoBERT)
- 약 75,000개의 상황 데이터 세트와 100,000개의 감정 데이터 세트를 처리했습니다.
- 다양한 장치에 따라 프로토타입을 설계하고 반응형 웹 페이지를 구현했습니다.
- RESTful API와 통합된 웹 페이지입니다.


## 레파지토리
- Client: https://github.com/ATEAM-dAIz/daiz-front
- Server: https://github.com/ATEAM-dAIz/daiz-server
- Emotion Training: https://github.com/ATEAM-dAIz/daiz-training-emotion
- Situation Training: https://github.com/ATEAM-dAIz/daiz-training-situation
- Comment Training: https://github.com/ATEAM-dAIz/daiz-training-comment


## 미리보기
### [로그인/회원가입]
- 아이디와 비밀번호를 입력하여 간편하게 로그인 할 수 있습니다.
- 아이디는 이메일 형식이어야 하며 닉네임을 별도로 입력해야 가입이 가능합니다.

![image](https://user-images.githubusercontent.com/66022264/164190399-53db124e-f0cd-4d33-b6e4-04a31c89c888.png)
![image](https://user-images.githubusercontent.com/66022264/164190458-947a3d0c-40cd-4176-a695-9c86ce53eb47.png)

### [메인-모바일 버전/PC 버전]
- 사용자가 일기를 작성한 날짜가 달력에 표시가 됩니다.
- 작성한 일기 목록을 슬라이딩하여 확인할 수 있고, 클릭 시 작성된 일기가 보입니다.

![img](https://user-images.githubusercontent.com/66022264/164190943-406e6de2-6a2d-48b6-8aae-65fd0b3364c3.png)
![img](https://user-images.githubusercontent.com/66022264/164190955-57fdab8f-a1c7-493d-9e51-09e6f90786f3.png)

- 달력 없이 일기 목록만 보고 싶다면, 전체 보기 버튼을 눌려 한눈에 더 많은 목록을 볼 수 있습니다.

![img](https://user-images.githubusercontent.com/66022264/164191387-02d9971c-9292-4524-8661-b545d840950b.png)


### [글 작성 페이지]
- 제목과 내용을 적고 작성 완료 버튼을 누릅니다.
- 일기는 AI를 통해 분석되며 수정할 수 없습니다.

![img](https://user-images.githubusercontent.com/66022264/164193996-7f7a5c81-6b77-4351-9f9e-3ee01021a197.png)
![img](https://user-images.githubusercontent.com/66022264/164194002-0495caf0-37e0-4b4a-82cc-014b76fa4952.png)
![img](https://user-images.githubusercontent.com/66022264/164194006-02975cbe-0652-42f3-9185-2f8b702f3616.png)

### [결과창]
- 사용자가 일기를 작성한 날짜와 제목, 글이 보입니다.
- AI가 일기를 분석하여 남긴 코멘트를 확인할 수 있습니다.

![img](https://user-images.githubusercontent.com/66022264/164247276-5486c0f7-67c6-4615-b687-2c7e175964ad.png)
![img](https://user-images.githubusercontent.com/66022264/164247258-e5de5594-c3fb-41d9-9ec0-257944920881.png)


### [비밀번호 변경]
![img](https://user-images.githubusercontent.com/66022264/164247749-343d21ab-81b6-4271-8bff-e200aa9b5fec.png)

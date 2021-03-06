# daiz-server

## ์ค๋น๐ 
### 1. ์ธ๊ณต์ง๋ฅ ๋ชจ๋ธ ํ์ต
- [situation.pt](https://github.com/ATEAM-dAIz/daiz-training-situation)

- [emotion.pt](https://github.com/ATEAM-dAIz/daiz-training-emotion)

- [comment.pt](https://github.com/ATEAM-dAIz/daiz-training-comment)

### 2. reuirements.txt ์ค์น
``` C
pip install -r requirements.txt
```
### 3. KoBERT ์ค์น(Windows ํ๊ฒฝ์ ์ ํฉํ๋๋ก requirements.txt ์์ ํ KoBERT ์๋๋ค.)
``` C
pip install git+https://git@github.com/Jsgithubchannel/KoBERT.git@master
```
### 4. ๋ง์ด๊ทธ๋ ์ด์ ์ ์ฉ 
``` C
python manage.py makemigrations
```
- TypeError: __init__() got an unexpected keyword argument 'return_dict' ์ค๋ฅ ๋ฐ์์
  ``` C
  pip install transformers==4.15.0
  ```
``` C
python manage.py migrate
```
- ํ์ด๋ธ ์์ฑ์ด ์๋  ์ https://stackoverflow.com/a/62454561




# ๐ dAIz (๋ฐ์ด์ฆ)

## ํ๋ก์ ํธ ์๊ฐ
- AI๋ฅผ ํตํด ์ผ๊ธฐ๋ฅผ ๋ถ์ํ์ฌ ์ฌ๋ฆฌ ์ํ๋ฅผ ์๋ ค์ฃผ๊ณ  ๊ณต๊ฐํ๋ ์น์๋๋ค.

## ๊ธฐ์  ์คํ
- React | Redux
- TypeScript
- HTML, SCSS Modules
- Django Rest API
- Korean BERT pre-trained cased API


##  ๊ธฐ๋ฅ / ์๊ฐ
- ์์ฐ์ด ์ฒ๋ฆฌ ๊ธฐ๋ฒ์ ์ฌ์ฉํ์ฌ ์ฌ์ฉ์์ ๊ฐ์ ์ ๋ถ์ํ๊ณ  ์๊ฒฌ์ ์ ์ํฉ๋๋ค.
- PyTorch ๊ธฐ๋ฐ ๋ฅ๋ฌ๋ API๋ฅผ ์ฌ์ฉํ์ต๋๋ค. (KoBERT)
- ์ฝ 75,000๊ฐ์ ์ํฉ ๋ฐ์ดํฐ ์ธํธ์ 100,000๊ฐ์ ๊ฐ์  ๋ฐ์ดํฐ ์ธํธ๋ฅผ ์ฒ๋ฆฌํ์ต๋๋ค.
- ๋ค์ํ ์ฅ์น์ ๋ฐ๋ผ ํ๋กํ ํ์์ ์ค๊ณํ๊ณ  ๋ฐ์ํ ์น ํ์ด์ง๋ฅผ ๊ตฌํํ์ต๋๋ค.
- RESTful API์ ํตํฉ๋ ์น ํ์ด์ง์๋๋ค.


## ๋ ํ์งํ ๋ฆฌ
- Client: https://github.com/ATEAM-dAIz/daiz-front
- Server: https://github.com/ATEAM-dAIz/daiz-server
- Emotion Training: https://github.com/ATEAM-dAIz/daiz-training-emotion
- Situation Training: https://github.com/ATEAM-dAIz/daiz-training-situation
- Comment Training: https://github.com/ATEAM-dAIz/daiz-training-comment


## ๋ฏธ๋ฆฌ๋ณด๊ธฐ
### [๋ก๊ทธ์ธ/ํ์๊ฐ์]
- ์์ด๋์ ๋น๋ฐ๋ฒํธ๋ฅผ ์๋ ฅํ์ฌ ๊ฐํธํ๊ฒ ๋ก๊ทธ์ธ ํ  ์ ์์ต๋๋ค.
- ์์ด๋๋ ์ด๋ฉ์ผ ํ์์ด์ด์ผ ํ๋ฉฐ ๋๋ค์์ ๋ณ๋๋ก ์๋ ฅํด์ผ ๊ฐ์์ด ๊ฐ๋ฅํฉ๋๋ค.

![image](https://user-images.githubusercontent.com/66022264/164190399-53db124e-f0cd-4d33-b6e4-04a31c89c888.png)
![image](https://user-images.githubusercontent.com/66022264/164190458-947a3d0c-40cd-4176-a695-9c86ce53eb47.png)

### [๋ฉ์ธ-๋ชจ๋ฐ์ผ ๋ฒ์ /PC ๋ฒ์ ]
- ์ฌ์ฉ์๊ฐ ์ผ๊ธฐ๋ฅผ ์์ฑํ ๋ ์ง๊ฐ ๋ฌ๋ ฅ์ ํ์๊ฐ ๋ฉ๋๋ค.
- ์์ฑํ ์ผ๊ธฐ ๋ชฉ๋ก์ ์ฌ๋ผ์ด๋ฉํ์ฌ ํ์ธํ  ์ ์๊ณ , ํด๋ฆญ ์ ์์ฑ๋ ์ผ๊ธฐ๊ฐ ๋ณด์๋๋ค.

![img](https://user-images.githubusercontent.com/66022264/164190943-406e6de2-6a2d-48b6-8aae-65fd0b3364c3.png)
![img](https://user-images.githubusercontent.com/66022264/164190955-57fdab8f-a1c7-493d-9e51-09e6f90786f3.png)

- ๋ฌ๋ ฅ ์์ด ์ผ๊ธฐ ๋ชฉ๋ก๋ง ๋ณด๊ณ  ์ถ๋ค๋ฉด, ์ ์ฒด ๋ณด๊ธฐ ๋ฒํผ์ ๋๋ ค ํ๋์ ๋ ๋ง์ ๋ชฉ๋ก์ ๋ณผ ์ ์์ต๋๋ค.

![img](https://user-images.githubusercontent.com/66022264/164191387-02d9971c-9292-4524-8661-b545d840950b.png)


### [๊ธ ์์ฑ ํ์ด์ง]
- ์ ๋ชฉ๊ณผ ๋ด์ฉ์ ์ ๊ณ  ์์ฑ ์๋ฃ ๋ฒํผ์ ๋๋ฆ๋๋ค.
- ์ผ๊ธฐ๋ AI๋ฅผ ํตํด ๋ถ์๋๋ฉฐ ์์ ํ  ์ ์์ต๋๋ค.

![img](https://user-images.githubusercontent.com/66022264/164193996-7f7a5c81-6b77-4351-9f9e-3ee01021a197.png)
![img](https://user-images.githubusercontent.com/66022264/164194002-0495caf0-37e0-4b4a-82cc-014b76fa4952.png)
![img](https://user-images.githubusercontent.com/66022264/164194006-02975cbe-0652-42f3-9185-2f8b702f3616.png)

### [๊ฒฐ๊ณผ์ฐฝ]
- ์ฌ์ฉ์๊ฐ ์ผ๊ธฐ๋ฅผ ์์ฑํ ๋ ์ง์ ์ ๋ชฉ, ๊ธ์ด ๋ณด์๋๋ค.
- AI๊ฐ ์ผ๊ธฐ๋ฅผ ๋ถ์ํ์ฌ ๋จ๊ธด ์ฝ๋ฉํธ๋ฅผ ํ์ธํ  ์ ์์ต๋๋ค.

![img](https://user-images.githubusercontent.com/66022264/164247276-5486c0f7-67c6-4615-b687-2c7e175964ad.png)
![img](https://user-images.githubusercontent.com/66022264/164247258-e5de5594-c3fb-41d9-9ec0-257944920881.png)


### [๋น๋ฐ๋ฒํธ ๋ณ๊ฒฝ]
![img](https://user-images.githubusercontent.com/66022264/164247749-343d21ab-81b6-4271-8bff-e200aa9b5fec.png)

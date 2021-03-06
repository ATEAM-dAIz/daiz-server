# pip install git+https://git@github.com/Jsgithubchannel/KoBERT.git@master
# pip install transformers==4.15.0

from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import torch
import gluonnlp as nlp
import numpy as np
import random
import json

#kobert
from kobert.utils import get_tokenizer
from kobert.pytorch_kobert import get_pytorch_kobert_model

from .model.daizBERT import BERTDataset, BERTClassifier

device = torch.device("cpu")

batch_size = 16
max_len = 200

bertmodel, vocab = get_pytorch_kobert_model() # BERT 모델, Vocabulary 불러오기
tokenizer = get_tokenizer()
tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)

# 상황 모델
def Situation(predict_sentence):
    data = [predict_sentence, '0']
    dataset_another = [data]

    another_test = BERTDataset(dataset_another, 0, 1, tok, vocab, max_len, True, False)
    test_dataloader = torch.utils.data.DataLoader(another_test, batch_size=batch_size, num_workers=5)
    
    model = BERTClassifier(bertmodel, num_classes=12, dr_rate=0.5).to(device)
    model.load_state_dict(torch.load('C:\\Users\\Server\\Desktop\\daiz-server\\dAIzProject\\dAIzApp\\ai\\model\\situation.pt', map_location=device)) # GPU 저장 모델 CPU에서 불러오기
    model.eval()

    result = ["가족관계", "학업 및 진로", "학교폭력/따돌림", 
    "대인관계(부부, 자녀)", "대인관계", "연애, 결혼, 출산", 
    "진로, 취업, 직장", "재정, 은퇴, 노후준비", "건강, 죽음", "건강",
    "직장, 업무 스트레스", "재정"]

    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_dataloader):
        token_ids = token_ids.long().to(device)
        segment_ids = segment_ids.long().to(device)

        valid_length= valid_length
        label = label.long().to(device)

        out = model(token_ids, valid_length, segment_ids)

        for i in out:
            logits=i
            logits = logits.detach().cpu().numpy()

            return result[np.argmax(logits)]


# 감정 모델
def Emotion(predict_sentence):
    data = [predict_sentence, '0']
    dataset_another = [data]

    another_test = BERTDataset(dataset_another, 0, 1, tok, vocab, max_len, True, False)
    test_dataloader = torch.utils.data.DataLoader(another_test, batch_size=batch_size, num_workers=5)
    
    model = BERTClassifier(bertmodel, num_classes=7, dr_rate=0.5).to(device)
    model.load_state_dict(torch.load('C:\\Users\\Server\\Desktop\\daiz-server\\dAIzProject\\dAIzApp\\ai\\model\\emotion.pt', map_location=device)) # GPU 저장 모델 CPU에서 불러오기
    model.eval()

    result = ["기쁨을", "당황을", "분노를", "불안을", "상처를", "슬픔을", "중립을"]

    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_dataloader):
        token_ids = token_ids.long().to(device)
        segment_ids = segment_ids.long().to(device)
        valid_length = valid_length
        label = label.long().to(device)

        out = model(token_ids, valid_length, segment_ids) # forward pass: compute predicted outputs by passing inputs to the model

        for i in out:
            logits=i
            logits = logits.detach().cpu().numpy()

            return result[np.argmax(logits)]


# 코멘트 모델
def Comment(predict_sentence):
    data = [predict_sentence, '0']
    dataset_another = [data]

    another_test = BERTDataset(dataset_another, 0, 1, tok, vocab, max_len, True, False)
    test_dataloader = torch.utils.data.DataLoader(another_test, batch_size=batch_size, num_workers=5)
    
    model = BERTClassifier(bertmodel, num_classes=359, dr_rate=0.5).to(device)
    model.load_state_dict(torch.load('C:\\Users\\Server\\Desktop\\daiz-server\\dAIzProject\\dAIzApp\\ai\\model\\comment.pt', map_location=device)) # GPU 저장 모델 CPU에서 불러오기
    
    model.eval()

    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_dataloader):
        token_ids = token_ids.long().to(device)
        segment_ids = segment_ids.long().to(device)
        valid_length = valid_length
        label = label.long().to(device)

        out = model(token_ids, valid_length, segment_ids) # forward pass: compute predicted outputs by passing inputs to the model

        for i in out:
            logits = i
            
            softmax_logit = torch.softmax(logits, dim=-1)
            softmax_logit = softmax_logit.squeeze()

            max_index = torch.argmax(softmax_logit).item()
            max_index_value = softmax_logit[torch.argmax(softmax_logit)].item()
            
            with open(r'C:\Users\Server\Desktop\daiz-server\dAIzProject\dAIzApp\ai\data\wellness_dialog_system.json', 'r') as f:
                wellness_dialog_system = json.load(f, encoding='cp949')

            with open(r'C:\Users\Server\Desktop\daiz-server\dAIzProject\dAIzApp\ai\data\wellness_dialog_category.json', 'r') as f:
                wellness_dialog_category = json.load(f, encoding='cp949')

            index = wellness_dialog_category[max_index][0] # 카테고리
            comment_list = wellness_dialog_system[index] # 코멘트 후보

            comment_len = len(comment_list) - 1
            comment_index = random.randint(0, comment_len)
            result = comment_list[comment_index] # 코멘트
    return result
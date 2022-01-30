import pandas as pd
from collections import defaultdict
import json

# 데이터셋 파일 읽어오기
test_data = pd.read_excel(r'C:\daiz-server\dAIzProject\dAIzApp\ai\data\웰니스_챗봇_말뭉치_데이터셋.xlsx')

# 대답 데이터만 뽑기
wellness_dialog_system = defaultdict(list)
nullcheck = test_data['챗봇'].isnull()

for emo, sen, check in zip(test_data['구분'], test_data['챗봇'], nullcheck):
  keys = wellness_dialog_system.keys()
  if check:
    continue
  else:
      wellness_dialog_system[emo].append(sen)

with open(r'C:\daiz-server\dAIzProject\dAIzApp\ai\data\wellness_dialog_system.json', 'w') as f:
    json.dump(wellness_dialog_system, f)
    

# 카테고리 데이터만 뽑기
wellness_dialog_category = []
cate_dict = []
category_count = 0

for emo in zip(test_data['구분']):
  if emo[0] not in cate_dict:
    cate_dict.append(emo[0])
    
    data = []
    data.append(emo[0])
    data.append(str(category_count))
    category_count += 1
    wellness_dialog_category.append(data)

with open(r'C:\daiz-server\dAIzProject\dAIzApp\ai\data\wellness_dialog_category.json', 'w') as f:
    json.dump(wellness_dialog_category, f)
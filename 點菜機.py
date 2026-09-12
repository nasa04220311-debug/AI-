#!/usr/bin/env python
# coding: utf-8

# In[44]:


import requests
import pandas as pd
from bs4 import BeautifulSoup
from openai import OpenAI
f=pd.read_excel(r"d:\交易行情查詢_115_09_12_蔬菜.xls",header=None)[4:]
f
client=OpenAI(
    api_key="",
    base_url="",
)
def api_ai(user_input_text):

    pmotmp=f"""
    貴賓：美國川普、柯文哲、黃國昌
    任務：請以晶華酒店特級廚師身份，依據以下提供的當令蔬菜行情資料，設計 5 道融合該食材的頂級主菜。
    實際材料和烹飪方法。
    價格請依據食材成本與五星級飯店定位合理訂價（約新台幣 1,200 至 3,800 元之間），格式必須為 Markdown 表格。
    加入20%利潤，是美國人買單，算貴議點。
    算出總價格，包跨服務費30%
    不要有HTML語法、不要程式碼
當令蔬菜行情：
    {f}
    """
    resplace=client.chat.completions.create(
        model="",
        messages=[
            {"role":"system","content":"你是晶華酒店特級廚師"},
            {"role":"user","content":pmotmp}
        ],
        temperature=0.7
    )
    return resplace.choices[0].message.content
r=api_ai(f)
print(r)


import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from keras.src.utils.dataset_utils import labels_to_dataset

themes = []
fake_news_counts = []
true_news_counts = []

#遍历每个csv文件
for filename in os.listdir('output_files'):
    if filename.endswith('.csv'):
        filepath = os.path.join('output_files',filename)

        #读取csv文件
        df = pd.read_csv(filepath)

        #统计真假新闻数量
        if 'label' in df.columns:
            fake_news_count = df[df['label'] == 0].shape[0]
            true_news_count = df[df['label'] == 1].shape[0]

        #打印统计结果
        print(f"Theme: {filename.split('_')[0]}\n")
        print(f"Fake News Count: {fake_news_count}\n")
        print(f"True News Count: {true_news_count}\n")

        themes.append(filename.split('_')[0])
        fake_news_counts.append(fake_news_count)
        true_news_counts.append(true_news_count)

'''
#绘制柱状图
plt.figure(figsize=(10,6))   #图形大小
bar_width = 0.4              #柱状图宽度
index_pos = range(len(themes)) #x轴位置
mid_position = [i + bar_width / 2 for i in index_pos]

#绘制假新闻的柱状图
plt.bar(index_pos, fake_news_counts, bar_width, label='Fake News', color='orange')
#绘制真新闻的柱状图
plt.bar([i + bar_width for i in index_pos], true_news_counts, bar_width, label='True News', color='blue')
#设置x轴标签
plt.xticks(mid_position, themes, rotation='vertical')
#设置图形的标题和标签
plt.title('Fake and True News Counts by Theme')
plt.xlabel('Theme')
plt.ylabel('Count')
#显示图例
plt.legend()
#显示图形
plt.tight_layout()
plt.show()

'''
'''
        #绘制饼状图
        labels = ['Fake News', 'True News']
        sizes = [fake_news_count, true_news_count]


        fig, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        # 设置数值标签的格式
        for i, autotext in enumerate(autotexts):
            autotext.set_text(f'{sizes[i]} ({autotext.get_text()})')  # 显示数值和百分比
        # 显示图例
        ax.legend()
        # 设置图表标题
        ax.set_title(f'Ratio of True to False News for Topic {filename.split('_')[0]}')

        plt.axis('equal')  # 使饼状图保持圆形
        plt.show()
'''




'''
true_news = [0] * 40
false_news = [0] * 40
with (open("gossipcop_doc_topics.txt","r",encoding="UTF-8") as news_topic_file,
      open("gossipcop_label-0 for fake and 1 for true.txt","r",encoding="UTF-8") as news_true_or_false_file):
    for line1,line2 in zip(news_topic_file,news_true_or_false_file):
        line1 = int(line1.strip())
        line2 = int(line2.strip())
        if line2 == 1 :
            true_news[line1] += 1
        else:
            false_news[line1] += 1

print(true_news)
print(false_news)

for j in range(16):
  news=[]
  news.append(true_news[j])
  news.append(false_news[j])

  labels = ['true','false']
  # 绘制饼状图
  fig, ax = plt.subplots()
  wedges, texts, autotexts = ax.pie(news, labels=labels, autopct='%1.1f%%', startangle=90)
  # 设置数值标签的格式
  for i, autotext in enumerate(autotexts):
    autotext.set_text(f'{news[i]} ({autotext.get_text()})')  # 显示数值和百分比
  #显示图例
  ax.legend()
  # 设置图表标题
  ax.set_title(f'Ratio of True to False News for Topic {j}')
  # 显示图表
  plt.axis('equal')  # 使饼状图保持圆形
  plt.show()'''
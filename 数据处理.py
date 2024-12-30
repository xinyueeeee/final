import csv

import pandas as pd
import os
import csv

from tensorflow.tools.docs.doc_controls import header

#对数据集Twitter中的新闻进行主题分类
'''
#读取文件
df = pd.read_csv('twitter.csv')

#提取image_id前缀写入主题列
df['theme'] = df['image_id'].apply(lambda x:x.split('_')[0])

#对label列进行处理(fake->0,true->1,其他->None)
df['label'] = df['label'].apply(lambda x: 0 if x == 'fake' else (1 if x == 'real' else ''))

#过滤掉label列为空的数据
df_filtered = df[df['label'] != '']

#提取需要的列
df_final = df_filtered[['theme','post_text','label']]

#分组
grouped_data = df_final.groupby('theme')

#为每个前缀创建一个输出文件，并写入数据
output_dir = 'output_files'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for theme, data in grouped_data:
    output_file = os.path.join(output_dir, f'{theme}_output.csv')
    data.to_csv(output_file, index=False)
'''




#选取主题为Boston（波士顿）、fuji（富士山）、eclipse（日食），bowie（David Bowie），refugees（难民）的新闻数据，分成train和test两类
'''
def extract_and_write_csv(input_file_path,output_file_path,row_ranges):
    #读取文件
    with open(input_file_path, 'r', encoding='utf-8') as infile,open(output_file_path, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        #读取表头
        header = next(reader)
        #写入表头
        writer.writerow(header)
        for current_row,row in enumerate(reader,start=2):
            for start,end in row_ranges:
                if start <= current_row <= end:
                    writer.writerow(row)
            if all(current_row > end for _, end in row_ranges):
                break


#选取部分真假信息作为宏观新闻环境的基本元素，剩余的作为待测新闻
#boston
input_file_path = 'output_files/boston_output.csv'
output_file_path = 'train_files/boston_train.csv'
row_ranges = [(2,73),(93,338)]
extract_and_write_csv(input_file_path,output_file_path,row_ranges)
input_file_path = 'output_files/boston_output.csv'
output_file_path = 'test_answer_files/boston_test.csv'
row_ranges = [(74,92),(339,399)]
extract_and_write_csv(input_file_path,output_file_path,row_ranges)

#fuji
input_file_path = 'output_files/fuji_output.csv'
output_file_path = 'train_files/fuji_train.csv'
row_ranges = [(2,88),(111,144)]
extract_and_write_csv(input_file_path,output_file_path,row_ranges)
input_file_path = 'output_files/fuji_output.csv'
output_file_path = 'test_answer_files/fuji_test.csv'
row_ranges = [(89,110),(145,157)]
extract_and_write_csv(input_file_path,output_file_path,row_ranges)

#eclipse
input_file_path = 'output_files/eclipse_output.csv'
output_file_path = 'train_files/eclipse_train.csv'
row_ranges = [(2,62),(77,95)]
extract_and_write_csv(input_file_path,output_file_path,row_ranges)
input_file_path = 'output_files/eclipse_output.csv'
output_file_path = 'test_answer_files/eclipse_test.csv'
row_ranges = [(63,76),(96,106)]
extract_and_write_csv(input_file_path,output_file_path,row_ranges)

#bowie
input_file_path = 'output_files/bowie_output.csv'
output_file_path = 'train_files/bowie_train.csv'
row_ranges = [(2,17),(26,60)]
extract_and_write_csv(input_file_path,output_file_path,row_ranges)
input_file_path = 'output_files/bowie_output.csv'
output_file_path = 'test_answer_files/bowie_test.csv'
row_ranges = [(18,25),(61,75)]
extract_and_write_csv(input_file_path,output_file_path,row_ranges)

#refugees
input_file_path = 'output_files/refugees_output.csv'
output_file_path = 'train_files/refugees_train.csv'
row_ranges = [(2,27),(37,46)]
extract_and_write_csv(input_file_path,output_file_path,row_ranges)
input_file_path = 'output_files/refugees_output.csv'
output_file_path = 'test_answer_files/refugees_test.csv'
row_ranges = [(28,36),(47,68)]
extract_and_write_csv(input_file_path,output_file_path,row_ranges)


'''


#整合各主题选取的用于train和test的新闻数据

for filename in os.listdir('test_answer_files'):
    if filename.endswith('.csv'):
        filepath = os.path.join('test_answer_files',filename)
        with open(filepath, 'r', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            if os.path.basename(filepath) == os.listdir('test_answer_files')[0]:
                header = next(reader)
                with open('test_answer.csv', 'a', newline='',encoding='utf-8') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow(header)
            with open('test_answer.csv', 'a', newline='',encoding='utf-8') as outfile:
                writer = csv.writer(outfile)
                for row in reader:
                    writer.writerow(row)
'''

#除去标签列
#读取文件
df = pd.read_csv('test_answer.csv')
#提取需要的列
df_final = df[['theme','post_text']]
df_final.to_csv('test.csv', index=False)
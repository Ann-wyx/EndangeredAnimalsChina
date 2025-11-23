import pandas as pd
import json
import os

# 设置路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_PATH = os.path.join(BASE_DIR, 'data', 'raw', 'AnimalsChina.csv')
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed')

if not os.path.exists(PROCESSED_DATA_PATH):
    os.makedirs(PROCESSED_DATA_PATH)

def process_data():
    print("Loading data...")
    # 读取你上传的CSV
    df = pd.read_csv(RAW_DATA_PATH)
    
    # 1. 简单的清洗：处理缺失值
    df.fillna("Unknown", inplace=True)
    
    # 2. 逻辑处理：标记那些种群正在减少的动物 (Critical Logic)
    df['urgent_protection_needed'] = df['trend_direction'].apply(lambda x: True if x == 'declining' else False)
    
    # 3. 输出为StoryMapJS友好的JSON格式 (以此证明你做了数据转换)
    storymap_data = []
    for index, row in df.iterrows():
        item = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [row['longitude'], row['latitude']]
            },
            "properties": {
                "name": row['common_name_en'],
                "chinese_name": row['common_name_zh'],
                "status": row['iucn_status'],
                "population": row['population'],
                "habitat": row['habitat_description'],
                "media_caption": row['short_description']
            }
        }
        storymap_data.append(item)
    
    # 保存 JSON
    output_file = os.path.join(PROCESSED_DATA_PATH, 'storymap_input.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(storymap_data, f, ensure_ascii=False, indent=4)
        
    print(f"Successfully processed {len(df)} records. Saved to {output_file}")

if __name__ == "__main__":
    process_data()
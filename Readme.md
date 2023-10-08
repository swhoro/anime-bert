## 基于 Bert 的视频名提取模型

基于模型 [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased)

## 1.获取数据

example:
```
# file: 1.txt
[Airota&Nekomoe kissaten&VCB-Studio] Yagate Kimi ni Naru [01][Ma10p_1080p][x265_flac_aac].mkv
[Airota&Nekomoe kissaten&VCB-Studio] Yagate Kimi ni Naru [02][Ma10p_1080p][x265_flac].mkv
[Airota&Nekomoe kissaten&VCB-Studio] Yagate Kimi ni Naru [03][Ma10p_1080p][x265_flac_aac].mkv
[Airota&Nekomoe kissaten&VCB-Studio] Yagate Kimi ni Naru [04][Ma10p_1080p][x265_flac_aac].mkv
[Airota&Nekomoe kissaten&VCB-Studio] Yagate Kimi ni Naru [05][Ma10p_1080p][x265_flac].mkv
[Airota&Nekomoe kissaten&VCB-Studio] Yagate Kimi ni Naru [06][Ma10p_1080p][x265_flac_aac].mkv
[Airota&Nekomoe kissaten&VCB-Studio] Yagate Kimi ni Naru [07][Ma10p_1080p][x265_flac_aac].mkv
[Airota&Nekomoe kissaten&VCB-Studio] Yagate Kimi ni Naru [08][Ma10p_1080p][x265_flac].mkv
[Airota&Nekomoe kissaten&VCB-Studio] Yagate Kimi ni Naru [09][Ma10p_1080p][x265_flac_aac].mkv
[Airota&Nekomoe kissaten&VCB-Studio] Yagate Kimi ni Naru [10][Ma10p_1080p][x265_flac].mkv
[Airota&Nekomoe kissaten&VCB-Studio] Yagate Kimi ni Naru [11][Ma10p_1080p][x265_flac].mkv
[Airota&Nekomoe kissaten&VCB-Studio] Yagate Kimi ni Naru [12][Ma10p_1080p][x265_flac_aac].mkv
[Airota&Nekomoe kissaten&VCB-Studio] Yagate Kimi ni Naru [13][Ma10p_1080p][x265_flac_aac].mkv
```

## 2.标注数据

使用 [doccano](https://github.com/doccano/doccano) 标注数据，导出 .jsonl 格式

example: 
```
# file: data.jsonl
{"id": 3, "text": "[Airota&Nekomoe kissaten&VCB-Studio] Yagate Kimi ni Naru [01][Ma10p_1080p][x265_flac_aac].mkv", "Comments": [], "label": [[1, 7, "字幕组"], [8, 24, "字幕组"], [25, 35, "字幕组"], [37, 56, "视频名"], [58, 60, "集数"], [68, 73, "分辨率"], [75, 79, "视频编码"], [80, 84, "音频编码"], [85, 88, "音频编码"]]}
{"id": 4, "text": "[Airota&Nekomoe kissaten&VCB-Studio] Yagate Kimi ni Naru [02][Ma10p_1080p][x265_flac].mkv", "Comments": [], "label": [[1, 7, "字幕组"], [8, 24, "字幕组"], [25, 35, "字幕组"], [37, 56, "视频名"], [58, 60, "集数"], [68, 73, "分辨率"], [75, 79, "视频编码"], [80, 84, "音频编码"]]}
{"id": 5, "text": "[Airota&Nekomoe kissaten&VCB-Studio] Yagate Kimi ni Naru [03][Ma10p_1080p][x265_flac_aac].mkv", "Comments": [], "label": [[1, 7, "字幕组"], [8, 24, "字幕组"], [25, 35, "字幕组"], [37, 56, "视频名"], [58, 60, "集数"], [68, 73, "分辨率"], [75, 79, "视频编码"], [80, 84, "音频编码"], [85, 88, "音频编码"]]}
{"id": 6, "text": "[Airota&Nekomoe kissaten&VCB-Studio] Yagate Kimi ni Naru [04][Ma10p_1080p][x265_flac_aac].mkv", "Comments": [], "label": [[1, 7, "字幕组"], [8, 24, "字幕组"], [25, 35, "字幕组"], [37, 56, "视频名"], [58, 60, "集数"], [68, 73, "分辨率"], [75, 79, "视频编码"], [80, 84, "音频编码"], [85, 88, "音频编码"]]}
{"id": 7, "text": "[Airota&Nekomoe kissaten&VCB-Studio] Yagate Kimi ni Naru [05][Ma10p_1080p][x265_flac].mkv", "Comments": [], "label": [[1, 7, "字幕组"], [8, 24, "字幕组"], [25, 35, "字幕组"], [37, 56, "视频名"], [58, 60, "集数"], [68, 73, "分辨率"], [75, 79, "视频编码"], [80, 84, "音频编码"]]}
```

## 3.数据预处理

example:
```
python preprocess.py data.jsonl
```

同目录下的 `${dataname}.new.json` 是最终训练需要的数据

## 4.训练

example:
```
python train.py data.jsonl.new.json
```
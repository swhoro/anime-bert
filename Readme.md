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

由于不支持下划线，因此需要替换: `make replace dataname=1.txt`

## 2.标注数据

使用 [label-studio](https://labelstud.io/) 标注数据，导出 .conll 格式

example: 
```
# file: data.conll
# 第一行额外数据需手动删除
[ -X- _ O
Airota -X- _ B-字幕组
& -X- _ O
Nekomoe -X- _ B-字幕组
kissaten -X- _ I-字幕组
& -X- _ O
VCB-Studio -X- _ B-字幕组
] -X- _ O
Yagate -X- _ B-视频名
Kimi -X- _ I-视频名
ni -X- _ I-视频名
Naru -X- _ I-视频名
[ -X- _ O
01 -X- _ B-集数
] -X- _ O
[ -X- _ O
Ma10p -X- _ O
1080p -X- _ B-分辨率
] -X- _ O
[ -X- _ O
x265 -X- _ B-视频编码
flac -X- _ B-音频编码
aac -X- _ B-音频编码
] -X- _ O
.mkv -X- _ O
```

## 3.数据预处理

example:
```makefile
make preprocess dataname=data.conll
```

同目录下的 `${dataname}.txt.json` 是最终训练需要的数据

## 4.训练

example:
```makefile
make train dataname=data.conll.txt.json
```
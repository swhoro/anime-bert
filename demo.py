from transformers import BertTokenizerFast
import json

datas = []

with open("data/admin.jsonl") as f:
    for line in f:
        datas.append(json.loads(line))
# print(datas)

max_length = 64
tokenizer: BertTokenizerFast = BertTokenizerFast.from_pretrained("bert-base-multilingual-cased")
i = tokenizer.tokenize(
    datas[0]["text"], max_length=max_length, truncation=True, padding="max_length"
)
encoding = tokenizer(datas[0]["text"], max_length=max_length, truncation=True, padding="max_length")

print(len(i), i)
# print(encoding)
print(len(encoding.word_ids()), encoding.word_ids())

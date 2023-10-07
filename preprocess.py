import json
import sys

from label2id import label2id

if len(sys.argv) < 2:
    print("no data given")
    sys.exit(1)

dataname = sys.argv[1]


# 读取CoNLL格式的数据文件
def read_conll_file(file_path):
    sentences = []
    labels = []
    with open(file_path, "r", encoding="utf-8") as file:
        sentence = []
        label = []
        for line in file:
            line = line.strip()
            if line == "":
                if len(sentence) > 0:
                    sentences.append(sentence)
                    labels.append(label)
                    sentence = []
                    label = []
            else:
                parts = line.split(" ")
                word = parts[0]
                tag = parts[1]
                sentence.append(word)
                label.append(tag)
    return sentences, labels


# 转换为Transformers可以接受的格式
def convert_to_json(sentences, labels):
    input_tokens = []
    input_labels = []

    for sentence, label in zip(sentences, labels):
        this_sentence_token = []
        this_sentence_label = []
        for word, tag in zip(sentence, label):
            this_sentence_token.append(word)
            this_sentence_label.append(label2id[tag])
        input_tokens.append(this_sentence_token)
        input_labels.append(this_sentence_label)

    all_values = []
    for i, _ in enumerate(input_tokens):
        all_values.append({"id": i, "ner_tags": input_labels[i], "tokens": input_tokens[i]})
    return all_values


if __name__ == "__main__":
    sentences, labels = read_conll_file(dataname)
    j = convert_to_json(sentences, labels)
    with open(f"{dataname}.json", "wt") as f:
        newj = []
        j_len = len(j)
        for i in range(100):
            for template_json in j:
                newj.append(
                    {
                        "id": str(i * j_len + template_json["id"]),
                        "ner_tags": template_json["ner_tags"],
                        "tokens": template_json["tokens"],
                    }
                )
        json.dump(newj, f)

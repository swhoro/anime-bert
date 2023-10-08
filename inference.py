from transformers import pipeline
import json


input_str = (
    "[Airota&Nekomoe kissaten&VCB-Studio] Yagate Kimi ni Naru [01][Ma10p_1080p][x265_flac_aac].mkv"
)

p = pipeline("ner", model="outdir/checkpoint-336")
result = str(p(input_str))
result = json.loads(result.replace("'", '"'))

# ner_struct: {
#     "label_name": label_word_location
# }
ner_struct = {}
# label_word_location: {
#     "label": str,
#     "from": int,
#     "to": int,
# }
label_word_location = {}
for res in result:
    if res["entity"].startswith("B-"):
        if not res["word"].startswith("##"):
            if "label" in label_word_location:
                if label_word_location["label"] in ner_struct:
                    ner_struct[label_word_location["label"]].append(
                        {"from": label_word_location["from"], "to": label_word_location["to"]}
                    )
                else:
                    ner_struct[label_word_location["label"]] = [
                        {"from": label_word_location["from"], "to": label_word_location["to"]}
                    ]

            label_word_location["label"] = res["entity"].split("-")[1]
            label_word_location["from"] = res["start"]
            label_word_location["to"] = res["end"]
        else:
            if res["entity"].split("-")[1] == label_word_location["label"]:
                label_word_location["to"] = res["end"]
    else:
        # start with I-
        label_word_location["to"] = res["end"]

# add the last result
if label_word_location["label"] in ner_struct:
    ner_struct[label_word_location["label"]].append(
        {"from": label_word_location["from"], "to": label_word_location["to"]}
    )
else:
    ner_struct[label_word_location["label"]] = [
        {"from": label_word_location["from"], "to": label_word_location["to"]}
    ]

for label, value_list in ner_struct.items():
    vs = []
    for value in value_list:
        vs.append(input_str[value["from"] : value["to"]])
    ner_struct[label] = vs

print(ner_struct)

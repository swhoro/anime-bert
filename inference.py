from transformers import pipeline
import json


input_str = "[Nekomoe kissaten&LoliHouse] Migi to Dali - 01 [WebRip 1080p HEVC-10bit AAC ASSx2].mkv"

p = pipeline("ner", model="outdir/checkpoint-60")
result = str(p(input_str))
print(result)
result = json.loads(result.replace("'", '"'))

ner_struct = {}
tr = {}
for res in result:
    if res["entity"].startswith("B-"):
        if not res["word"].startswith("##"):
            if "label" in tr:
                if tr["label"] in ner_struct:
                    ner_struct[tr["label"]].append({"from": tr["from"], "to": tr["to"]})
                else:
                    ner_struct[tr["label"]] = [{"from": tr["from"], "to": tr["to"]}]

            tr["label"] = res["entity"].split("-")[1]
            tr["from"] = res["start"]
            tr["to"] = res["end"]
        else:
            if res["entity"].split("-")[1] == tr["label"]:
                tr["to"] = res["end"]
    else:
        # start with I-
        tr["to"] = res["end"]

if tr["label"] in ner_struct:
    ner_struct[tr["label"]].append({"from": tr["from"], "to": tr["to"]})
else:
    ner_struct[tr["label"]] = [{"from": tr["from"], "to": tr["to"]}]

print(ner_struct)

for k, value_list in ner_struct.items():
    vs = []
    for value in value_list:
        vs.append(input_str[value["from"] : value["to"]])
    ner_struct[k] = vs

print(ner_struct)

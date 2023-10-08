import json
import sys
import re

from labels import label2id


def should_break_here(str: str):
    if re.match("\w", str):
        if re.match("_", str):
            return True
        else:
            return False
    else:
        return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("no data given")
        sys.exit(1)

    datapath = sys.argv[1]

    # examples: [
    #     {
    #          "id": int,
    #          "text": str,
    #          "label": [
    #               [int, int, str],
    #          ]
    #     }
    # ]
    examples = []
    with open(datapath, "r", encoding="utf-8") as f:
        for line in f:
            examples.append(json.loads(line))

    # word_with_location_list: [
    #     this_sentence_words
    # ]
    word_with_location_list = []
    for example in examples:
        from_loc = -1
        sentence_end_loc = -1
        last_break = 0
        this_sentence_words = []
        # this_sentence_words: [
        #     {
        #       "word": str,
        #       "from": int,
        #       "to": int
        #     }
        # ]
        for i, v in enumerate(example["text"]):
            if should_break_here(v):
                if sentence_end_loc + 1 == i and sentence_end_loc != -1:
                    # [sentence][special]
                    this_sentence_words.append(
                        {"word": example["text"][from_loc:i], "from": from_loc, "to": i}
                    )
                if v == " ":
                    from_loc = i + 1
                    continue
                this_sentence_words.append(
                    {"word": example["text"][i : i + 1], "from": i, "to": i + 1}
                )
                last_break = i
                from_loc = i + 1
            else:
                sentence_end_loc = i

        if last_break + 1 != len(example["text"]):
            this_sentence_words.append(
                {
                    "word": example["text"][last_break + 1 :],
                    "from": last_break + 1,
                    "to": len(example["text"]),
                }
            )

        # organize label
        labels = example["label"]
        for label in labels:
            label_from = label[0]
            label_to = label[1]
            label_name = label[2]
            for word in this_sentence_words:
                if word["from"] >= label_to:
                    break
                if "label" in word:
                    continue
                if word["from"] > label_from:
                    word["label"] = f"I-{label_name}"
                if word["from"] == label_from:
                    word["label"] = f"B-{label_name}"
        for word in this_sentence_words:
            if not "label" in word:
                word["label"] = "O"

        word_with_location_list.append(this_sentence_words)

    # json_val: [
    #     {
    #         "id": int
    #         "tokens": [str],
    #         "ner_tags": [str]
    #     }
    # ]
    json_val = []
    count = 0
    for this_sentence_words in word_with_location_list:
        this_val = {"id": count, "tokens": [], "ner_tags": []}
        for word in this_sentence_words:
            this_val["tokens"].append(word["word"])
            this_val["ner_tags"].append(label2id[word["label"]])
        json_val.append(this_val)
        count += 1

    with open(f"{datapath}.new.json", "w", encoding="utf-8") as f:
        json.dump(json_val, f, ensure_ascii=False)

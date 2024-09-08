import os
import json

def formalize(value):
    # round to 1 decimal places
    try:
        return round(float(value), 1)
    except:
        return value


def extract_import_values(meta, obj):
    out = {}
    out['Model'] = ""                  # We need Model to be the first column
    out['Method'] = meta['Method']
    out['Source'] = meta['Source']
    out['Date'] = meta['Date']
    out['ALL'] = formalize(obj['average']['accuracy'])
    out['FQA'] = formalize(obj['task']['figure question answering']['accuracy'])
    out['GPS'] = formalize(obj['task']['geometry problem solving']['accuracy'])
    out['MWP'] = formalize(obj['task']['math word problem']['accuracy'])
    out['TQA'] = formalize(obj['task']['textbook question answering']['accuracy'])
    out['VQA'] = formalize(obj['task']['visual question answering']['accuracy'])
    out['ALG'] = formalize(obj['skills']['algebraic reasoning']['accuracy'])
    out['ARI'] = formalize(obj['skills']['arithmetic reasoning']['accuracy'])
    out['GEO'] = formalize(obj['skills']['geometry reasoning']['accuracy'])
    out['LOG'] = formalize(obj['skills']['logical reasoning']['accuracy'])
    out['NUM'] = formalize(obj['skills']['numeric commonsense']['accuracy'])
    out['SCI'] = formalize(obj['skills']['scientific reasoning']['accuracy'])
    out['STA'] = formalize(obj['skills']['statistical reasoning']['accuracy'])
    return out


## process scores
models = [d for d in os.listdir() if os.path.isdir(d)]
table = []
for model in models:
    files = os.listdir(f'./{model}')
    print(model)
    print(files)
    file = [f for f in files if f.startswith("scores_")][0]

    # load score file
    score_file = os.path.join(model, file)
    with open(score_file, 'r') as f:
        obj = json.load(f)

    # load meta file
    meta_file = os.path.join(model, 'meta.json')
    with open(meta_file, 'r') as f:
        meta = json.load(f)

    out = extract_import_values(meta, obj)
    out['Model'] = model
    table.append(out)

    new_obj = {
        "average": {"accuracy": obj['average']['accuracy']},
        "task": {
            "figure question answering": {"accuracy": obj['task']['figure question answering']['accuracy']},
            "geometry problem solving": {"accuracy": obj['task']['geometry problem solving']['accuracy']},
            "math word problem": {"accuracy": obj['task']['math word problem']['accuracy']},
            "textbook question answering": {"accuracy": obj['task']['textbook question answering']['accuracy']},
            "visual question answering": {"accuracy": obj['task']['visual question answering']['accuracy']},
        },
        "skills": {
            "algebraic reasoning": {"accuracy": obj['skills']['algebraic reasoning']['accuracy']},
            "arithmetic reasoning": {"accuracy": obj['skills']['arithmetic reasoning']['accuracy']},
            "geometry reasoning": {"accuracy": obj['skills']['geometry reasoning']['accuracy']},
            "logical reasoning": {"accuracy": obj['skills']['logical reasoning']['accuracy']},
            "numeric commonsense": {"accuracy": obj['skills']['numeric commonsense']['accuracy']},
            "scientific reasoning": {"accuracy": obj['skills']['scientific reasoning']['accuracy']},
            "statistical reasoning": {"accuracy": obj['skills']['statistical reasoning']['accuracy']},
        }
    }
    # print(new_obj)
    with open(score_file, 'w') as f:
        json.dump(new_obj, f, indent=2)

## sort by ALL and adjust score_table to ensure "Human Performance*" is the first row
# the model to be removed
model_to_remove = 'Human Performance*'

# find the index of the element with Model 'Human Performance'
index_to_remove = next((i for i, item in enumerate(table) if item['Model'] == model_to_remove), None)

# remove the element
human = table.pop(index_to_remove)
human = {"-": human}

# sort the table
sorted_table = sorted(table, key=lambda x: x['ALL'], reverse=True)
sorted_table = {str(i+1): sorted_table[i] for i in range(len(sorted_table))}

# add the human performance back
score_table = {**human, **sorted_table}


# rename the top 3 models by adding 🥇, 🥈, and 🥉, respectively
score_table['1']['Model'] = score_table['1']['Model'] + ' 🥇'
score_table['2']['Model'] = score_table['2']['Model'] + ' 🥈'
score_table['3']['Model'] = score_table['3']['Model'] + ' 🥉'

# print to file
with open('model_scores.js', 'w+') as f:
    f.write("score_table = " + json.dumps(score_table, indent=2))



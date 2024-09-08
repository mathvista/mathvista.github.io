import os
import json


## [1] Initiate output_folders.js
# list all directories that contain output_xx.json in the current folder
models = sorted([d for d in os.listdir() if os.path.isdir(d)])

output_models = {}
for model in models:
    files = os.listdir(f'./{model}')
    file = [f for f in files if f.startswith("output")]
    if len(file) > 0:
        output_models[model] = model

# remove "Random Chance"
to_remove = ["Random Chance"]
for model in to_remove:
    if model in output_models:
        del output_models[model]

s = 'model_output_folder_list = ' + json.dumps(output_models, indent=2)
with open('output_folders.js', 'w+') as f:
    f.write(s)


## [2] create a data.js file for the explorer
for model in output_models:
    files = os.listdir(f'./{model}')
    file = [f for f in files if f.startswith("output")][0]
    with open(os.path.join(model, file), 'r') as f:
        obj = json.load(f)
    keys_needed = ['response']
    new_obj = {}
    for i in range(1, 1001):
        if str(i) not in obj: continue
        new_obj[str(i)] = {k:v for k,v in obj[str(i)].items() if k in keys_needed}

    outstr = f"cache['{model}'] = {json.dumps(new_obj, indent=2)}"
    with open(os.path.join(model, 'data.js'), 'w') as f:
        f.write(outstr)


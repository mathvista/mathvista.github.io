import os, sys
import json

input_root = "../../data_final"
output_root = "data"

os.makedirs(output_root, exist_ok=True)

# # cuttoff = 1000 (data version: 0824)
# total = 10057

# cuttoff = 400 (data version: 0901)
total = 6141

# generate all filters
# try:
input_file = os.path.join(input_root, "private/data.json")
output_file = os.path.join(output_root, "filters.json")
output_num_file = os.path.join(output_root, "filters_num.json")

names = ["question_type", "answer_type", "language", "source", "category", "task", "context", "grade", "skills"]
test_data = json.load(open(input_file, "r"))

filters = {}
filtes_nums = {}


for name in names:
    values = []
    filtes_nums[name] = {"All": 0}  # "All" is the total number of problems

    for pid, problem in test_data.items():
        value = problem[name] if name in problem else problem["metadata"][name]
        if isinstance(value, list):
            for v in value:
                values.append(v)
                # print("name: {}, value: {}".format(name, value))
                if v not in filtes_nums[name]:
                    filtes_nums[name][v] = 1
                else:
                    filtes_nums[name][v] += 1
                # add to "All"
                filtes_nums[name]["All"] += 1
        else:
            values.append(value)
            # print("name: {}, value: {}".format(name, value))
            if value not in filtes_nums[name]:
                filtes_nums[name][value] = 1
            else:
                filtes_nums[name][value] += 1 
            # add to "All"
            filtes_nums[name]["All"] += 1

    # add "All" to the beginning of the list
    filters[name] = ["All"] + sorted(list(set(values)))

    # add the number of problems for each attribute value
    if name != "skills":
        assert filtes_nums[name]["All"] == total
        assert sum(list(filtes_nums[name].values())) == total * 2 
        
    filtes_nums[name] = [f"{value} ({filtes_nums[name][value]})" for value in filters[name]]

with open(output_file, "w+") as f:
    json.dump(filters, f)
    
with open(output_num_file, "w+") as f:
    json.dump(filtes_nums, f)

# except Exception as e:
#     print(f"Error with {output_file}")


# testmini data
try:
    input_file = os.path.join(input_root, "testmini.json")
    output_file = os.path.join(output_root, "testmini.js")
    with open(input_file, "r") as f:
        lns = f.readlines()
    lns = ["test_data = "] + lns
    with open(output_file, "w+") as f:
        f.writelines(lns)
except Exception as e:
    print(f"Error with {output_file}")


# test data
try:
    input_file = os.path.join(input_root, "test.json")
    output_file = os.path.join(output_root, "test.js")
    with open(input_file, "r") as f:
        lns = f.readlines()
    lns = ["test_data = "] + lns
    with open(output_file, "w+") as f:
        f.writelines(lns)
except Exception as e:
    print(f"Error with {output_file}")


# test data for private
try:
    input_file = os.path.join(input_root, "private/data.json")
    output_file = os.path.join(output_root, "data_private.js")
    with open(input_file, "r") as f:
        lns = f.readlines()
    lns = ["test_data = "] + lns
    with open(output_file, "w+") as f:
        f.writelines(lns)
except Exception as e:
    print(f"Error with {output_file}")



# test data for public
try:
    input_file_mini = os.path.join(input_root, "testmini.json")
    with open(input_file_mini, "r") as f:
        data_mini = json.load(f)

    input_file_test = os.path.join(input_root, "test.json")
    with open(input_file_test, "r") as f:
        data_test = json.load(f)

    combined_data = {**data_mini, **data_test}
    # convert to f.readlines()
    combined_data = [json.dumps(combined_data, indent=4)]
    lns = ["test_data = "] + combined_data

    output_file = os.path.join(output_root, "data_public.js")
    with open(output_file, "w+") as f:
        f.writelines(lns)

except Exception as e:
    print(f"Error with {output_file}")

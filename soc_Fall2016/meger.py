import sys
def merge_values(cat_info1, cat_info2):
    str_values = cat_info1.split("&")
    final_info = {}
    for x in str_values:
        cat_name = x.split(":")[0].strip()
        cat_val =  x.split(":")[1].strip()
        final_info[cat_name] = int(cat_val)
    str_values2 = cat_info2.split("&")
    for x in str_values2:
        cat_name = x.split(":")[0].strip()
        cal_val = int(x.split(":")[1].strip())
        if cat_name in final_info:
            final_info[cat_name] += cal_val
    final_str = ""
    for key in final_info:
        final_str = final_str+key+":"+str(final_info[key])
        final_str = final_str+"&"
    return final_str[:-1]

file1 = sys.argv[1]
file2 = sys.argv[2]
result_file = sys.argv[3]

file1_obj = open(file1, "r")
file1_info = {}
for e, line in enumerate(file1_obj):
    str_values = line.split(",")
    customer_id = str_values[0].strip()
    category_id = str_values[1].strip()
    file1_info[customer_id] = category_id
file1_obj.close()

file2_obj = open(file2)
for e, line in enumerate(file2_obj):
    str_values = line.split(",")
    customer_id = str_values[0].strip()
    category_id = str_values[1].strip()
    if not (customer_id in file1_info):
        val1 = file1_info[customer_id]
        merge_values(category_id, val1)
    else:
        file1_info[customer_id] = category_id
file2_obj.close()

file3_obj = open(result_file,"w")
for key in file1_info:
    final_str = key+","+file1_info[key]+"\n"
    file3_obj.write(final_str)
file3_obj.close()

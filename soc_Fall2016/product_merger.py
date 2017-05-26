import sys
file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]
file1_obj = open(file1,"r")
file2_obj = open(file2, "r")
file1_info = {}
for e, line in enumerate(file1_obj):
    str_value = line.split(",")
    product_info = str_value[0].strip()
    product_id = str_value[1].strip()
    file1_info[product_info] = product_id
file1_obj.close()
file2_info = {}
for e, line in enumerate(file2_obj):
    str_value = line.split(",")
    product_info = str_value[0].strip()
    product_id  = str_value[1].strip()
    if not (product_info in file1_info):
        file1_info[product_info] = product_id
file2_obj.close()
file3_obj = open(file3,"w")
for pro in file1_info:
    line_str = pro + "," + file1_info[pro]+"\n"
    file3_obj.write(line_str)
file3_obj.close()
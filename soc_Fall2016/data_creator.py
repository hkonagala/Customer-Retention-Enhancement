import sys
file1 = sys.argv[1]
output_file = sys.argv[2]
#id	chain	dept	category	company	brand	date	productsize	productmeasure	purchasequantity	purchaseamount
file1_obj = open(file1,"r")
final_info = {}
def write_to_file(filename,obj):
    output_file_obj = open(filename,"w")
    for custId in obj:
        str_value = get_string(obj[custId])
        final_str = custId +","+str_value+"\n"
        output_file_obj.write(final_str)
    output_file_obj.close()

def get_string(cust_info):
    final_str = ""
    for cat in cust_info:
        final_str = final_str+cat+":"+str(cust_info[cat])
        final_str = final_str+"&"
    return final_str[:-1]

for e, line in enumerate(file1_obj):
    str_values = line.split(",")
    customer_id = str_values[0].strip()
    category = str_values[3].strip()
    if not (customer_id in final_info):
        final_info[customer_id] = {}
        final_info[customer_id][category] = 1
    else:
        if category in final_info[customer_id]:
            final_info[customer_id][category] += 1
        else:
            final_info[customer_id][category] = 1
write_to_file(output_file, final_info)
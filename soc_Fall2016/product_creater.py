#id	chain	dept	category	company	brand	date	productsize	productmeasure	purchasequantity	purchaseamount
import sys
def get_constant_chars(num):
    my_list = ['0']*total_chars
    index = total_chars-1
    while num != 0:
        char = num%10
        my_list[index] = char
        index -= 1
        num = num/10
    return to_str(my_list)
def to_str(my_list):
    final_str = ""
    for i in range(0,len(my_list)):
        final_str += str(my_list[i])
    return  final_str

file_loc = sys.argv[1]
output_file = sys.argv[2]
file_obj = open(file_loc, "r")
total_chars = 10
count = 1
product_data = dict()
line_count = 0
for e, line in enumerate(file_obj):
    if(line_count%50000 == 0):
        print str(line_count)+" lines read.."
    line_count += 1
    try:
        str_values = line.split(",")
        chain = str_values[1]
        dept = str_values[2]
        category = str_values[3]
        company = str_values[4]
        brand = str_values[5]
        final_id = chain+"-"+dept+"-"+category+"-"+company+"-"+brand
        product_data[final_id] = get_constant_chars(count)
        count += 1
    except Exception as e:
        print 'Got exception '+str(e)
file_obj.close()
out_file_obj = open(output_file,"w")
for pro in product_data:
    line_str = pro + "," + product_data[pro]+"\n"
    out_file_obj.write(line_str)
out_file_obj.close()
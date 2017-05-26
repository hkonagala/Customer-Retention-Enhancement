# market, repeat, repeattrips, chain, same_company, same_brand, same_category
file_obj = open('F:\\soc\\train_data','r')
lines = file_obj.readlines()
same_category_min = 100000
same_brand_min = 100000
same_company_min = 100000
same_category_sum = 0
same_brand_sum = 0
same_company_sum = 0
for line_num in range(0,len(lines)):
    curr_line = lines[line_num]
    str_values = curr_line.split(',')
    is_repeat  = int(str_values[1])
    if is_repeat == 1:
        num_category = int(str_values[6])
        num_brand = int(str_values[5])
        num_company = int(str_values[4])
        same_category_min = min(same_category_min, num_category)
        same_brand_min = min(same_brand_min, num_brand)
        same_company_min = min(same_company_min, num_category)
        same_category_sum =  same_category_sum + num_category
        same_brand_sum = same_brand_sum + num_brand
        same_company_sum = same_company_sum + num_company

print "minimum category -->> "+str(same_category_min)
print 'minimum brand -->>'+str(same_brand_min)
print 'minimum company -->>'+str(same_company_min)
print '---------------------------------------'
print 'mean category -->> '+str(same_category_sum/len(lines))
print 'mean brand -->> '+str(same_brand_sum/len(lines))
print 'mean company -->> '+str(same_company_sum/len(lines))


def min(a, b):
    if a < b:
        return a
    return b

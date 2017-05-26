fob = open('F:\\soc\\data\\brand\\brand.csv')
new_file = open('F:\\soc\\data\\brand\\brand_new.csv',"w")
new_file.write("cust_id,info\n")
for e, line in enumerate(fob):
    new_file.write(line)

print 'Finally done'


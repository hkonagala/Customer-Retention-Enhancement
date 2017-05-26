# offer category quantity company offervalue brand
#id chain offer market repeattrips repeater offerdate
#id	chain	dept	category	company	brand	date	productsize	productmeasure	purchasequantity	purchaseamount
transactions_file = "F:\\soc\\transactions_reduced.csv"
offers_file = "F:\\soc\\offers.csv"
trainHistory_file = "F:\\soc\\trainHistory.csv"
features_file = "F:\\soc\\features_info.csv"
offers_file_obj = open(offers_file,"r")
offers = dict()
for e, line in enumerate(offers_file_obj):
    str_values = line.split(",")
    particular_offer = dict()
    offers[str_values[0].strip()] = particular_offer
    particular_offer["category"] = str_values[1].strip()
    particular_offer["company"] = str_values[3].strip()
    particular_offer["offervalue"] = str_values[4].strip()
    particular_offer["brand"] = str_values[5].strip()
offers_file_obj.close()
print 'read offers file'
trainHistory_file_obj = open(trainHistory_file,"r")
trainHistory = {}
for e, line in enumerate(trainHistory_file_obj):
    str_values = line.split(",")
    particular_train = dict()
    trainHistory[str_values[0].strip()] = particular_train
    particular_train["chain"] = str_values[1].strip()
    particular_train["offer"] = str_values[2].strip()
    particular_train["market"] = str_values[3].strip()
    particular_train["repeattrips"] = str_values[4].strip()
    particular_train["repeat"] = str_values[5].strip()
    particular_train["offerdate"] = str_values[6].strip()
trainHistory_file_obj.close()
print 'read train file'
transactions_file_obj = open(transactions_file,"r")
for e, line in enumerate(transactions_file_obj):
    try:
        str_values = line.split(",")
        if(e%50000 == 0):
            print 'read num line'+str(e)
        cust_id = str_values[0]
        if(cust_id in trainHistory):
            offer_id = trainHistory[cust_id]["offer"]
            offer_info = offers[offer_id]
            if str_values[3].strip() == offer_info["category"]:
                if "same_category" in trainHistory[cust_id]:
                    trainHistory[cust_id]["same_category"] += 1
                else:
                    trainHistory[cust_id]["same_category"] = 1
            if str_values[4].strip() == offer_info["company"]:
                if "same_company" in trainHistory[cust_id]:
                    trainHistory[cust_id]["same_company"] += 1
                else:
                    trainHistory[cust_id]["same_company"] = 1
            if str_values[5].strip() == offer_info["brand"]:
                if "same_brand" in trainHistory[cust_id]:
                    trainHistory[cust_id]["same_brand"] += 1
                else:
                    trainHistory[cust_id]["same_brand"] = 1
    except Exception as e:
        print "Got error "+str(e)
transactions_file_obj.close()
features_info_file_obj = open(features_file,"w")
for cust_id in trainHistory:
    final_str = ""
    if "same_category" in trainHistory[cust_id]:
        final_str += str(trainHistory[cust_id]["same_category"])
    else:
        final_str += "0"
    final_str += ","
    if "same_company" in trainHistory[cust_id]:
        final_str += str(trainHistory[cust_id]["same_company"])
    else:
        final_str += "0"
    final_str += ","
    if "same_brand" in trainHistory[cust_id]:
        final_str += str(trainHistory[cust_id]["same_brand"])
    else:
        final_str += "0"
    final_str += ","
    final_str+=trainHistory[cust_id]["repeat"]
    final_str += "\n"
    features_info_file_obj.write(final_str)
features_info_file_obj.close()
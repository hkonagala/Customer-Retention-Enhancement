from pymongo import MongoClient
from bson.objectid import ObjectId
def getParticularInfo(key,info):
    str_values = info.split("&")
    for item in str_values:
        key_val = item.split(":")
        if key_val[0].strip() == key:
            return int(key_val[1])
    return 0
def search_over_element_prod(product, count, machine_learn_instance, machine_learn_model):
    connection = MongoClient("localhost")
    collection = connection.soc.products
    docs = collection.find({"product_id":{"$eq":int(product)}})
    for _doc in docs:
        doc = _doc
    product_info = doc["product_info"]
    category = product_info.split("-")[2].strip()
    company = product_info.split("-")[3].strip()
    brand = product_info.split("-")[4].strip()
    return search_over_element(category, brand, company, count, machine_learn_instance, machine_learn_model)

def search_over_element(category,brand,company, count, machine_learn_instance, machine_learn_model):
    connection = MongoClient("localhost")
    collection = connection.soc.category_info
    greatest_val = GreatestVal(int(count))
    doc_count = 0
    for doc in collection.find().batch_size(1000):
        doc_count += 1
        if doc_count%1000 == 0:
            print str(doc_count)+" customers read.."
        if doc_count > 5000:
            break
        comp_val = get_company(doc["cust_id"], company, connection)
        brand_val = get_brand(doc["cust_id"], brand, connection)
        category_val = getParticularInfo(category,doc["info"])
        predict_val = machine_learn_instance.predict(machine_learn_model,[comp_val, brand_val, category_val])
        greatest_val.add((predict_val[0],doc["cust_id"]))
    print str(greatest_val.heap)
    result = []
    for item in greatest_val.heap:
        result.append(item[1])
    return result

def get_company(cust_id, company, connection):
    collection = connection.soc.company_info
    customer_info = collection.find({"cust_id":{"$eq":cust_id}})
    _doc = None
    for doc in customer_info:
        _doc = doc
    if _doc != None:
        return getParticularInfo(company,_doc["info"])
    return 0

def get_brand(cust_id,brand,connection):
    collection = connection.soc.brand_info
    customer_info = collection.find({"cust_id":{"$eq":cust_id}})
    _doc = None
    for doc in customer_info:
        _doc = doc
    if _doc != None:
        return getParticularInfo(brand,_doc["info"])
'''Maintaing the greatest elements using the heap
'''
class GreatestVal:
    def __init__(self,num):
        self.max_size = num
        self.size = 0
        self.heap = []
    def get_min(self):
        return self.heap[0]
    def add(self, ele):
        if self.size < self.max_size:
            self.heap.append(ele)
            self.fix_up();
            self.size += 1
        else:
            if(ele > self.get_min()):
                self.heap[0] = ele
                self.fix_down()
    def fix_down(self):
        index = 0
        while index < len(self.heap):
            left_child = self.get_left_child(index)
            right_child = self.get_right_child(index)
            which_child = self.get_minimum(index,left_child, right_child)
            '''your are done'''
            if which_child == -1:
                return
            else:
                temp = self.heap[which_child]
                self.heap[which_child] = self.heap[index]
                self.heap[index] = temp
                index = which_child
    def get_minimum(self, index, left_index, right_index):
        if( left_index >= len(self.heap) and right_index >= len(self.heap)):
            return -1
        elif right_index >= len(self.heap):
            if self.heap[index][0] > self.heap[left_index][0]:
                return left_index
            else:
                return -1
        else:
            if self.heap[index][0] <= self.heap[left_index][0] and self.heap[index][0] <= self.heap[right_index][0]:
                return -1
            else:
                if self.heap[left_index][0] < self.heap[right_index][0]:
                    return left_index
                else:
                    return right_index
    def fix_up(self):
        index = len(self.heap)-1
        while index > 0:
            parent_index= self.get_parent(index)
            if self.heap[parent_index][0] > self.heap[index][0]:
                temp = self.heap[parent_index]
                self.heap[parent_index] = self.heap[index]
                self.heap[index] = temp
            else:
                return
            index = parent_index
        return
    def get_parent(self, index):
        return (index - 1) / 2

    def get_left_child(self, index):
        return index * 2 + 1

    def get_right_child(self, index):
        return index * 2 + 2

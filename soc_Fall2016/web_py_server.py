#mongod --port 27017 --dbpath C:\Program%20Files\MongoDB\data\db
import web
import db_connector as db
import logreg_class as lr
import json;
urls = (
    '/customers', 'Customers',
)
machine_learn_model = None
machine_learn_instance = None
class Customers:
    def GET(self):
        data = web.input()
        count = data.count
        product = data.product
        print 'product is '+product
        print 'count is '+count
        global machine_learn_instance, machine_learn_model
        machine_learn_instance = lr.logreg_class()
        machine_learn_model = machine_learn_instance.initialize()
        result = db.search_over_element_prod(product,count,machine_learn_instance,machine_learn_model)
        web.header("Access-Control-Allow-Origin","*")
        return json.dumps(result)
if __name__ == "__main__":
    
    global machine_learn_model
    global machine_learn_instance
    machine_learn_instance = lr.logreg_class()
    machine_learn_model = machine_learn_instance.initialize()
    app = web.application(urls, globals())
    app.run()



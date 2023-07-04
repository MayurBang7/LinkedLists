class ModelNode:
    def __init__(self,name, code, quantity, price):
        self.name = name
        self.code = code
        self.quantity = quantity
        self.price = price
        self.next = None
    
    def __str__(self):
        return "[" + ",".join((self.name,self.code,str(self.quantity),str(self.price))) + "]"

class ModelList:
    def __init__(self):
        self.head = ModelNode("dummy", "0000", -1, 0.0) #dummy node to indicate empty list
    
    def insert(self,name, code, quantity, price):
        temp = ModelNode(name, code, quantity, price)
        temp.next = self.head
        self.head = temp
    
    def search(self,name=None,code=None):
        curr = self.head
        while curr!=None:
            if curr.name == name or curr.code == code : return curr
            curr = curr.next
        return curr
    
    def update(self,name=None,code=None,quantity=None):
        curr = self.search(name,code)
        if not curr: raise Exception("Model type does not exist, cannot update!")
        curr.quantity = quantity
        return curr

    def delete(self,name=None,code=None):
        curr = self.head
        if curr.name==name or curr.code==code : #delete head node
            self.head = curr.next
            del(curr)
            return
        while curr!=None:
            if curr.next.code==code or curr.next.name==name: break
            curr = curr.next
        if curr==None : raise Exception("mentioned code/name of Model not available, cannot delete")
        temp = curr.next
        curr.next = curr.next.next
        del(temp)
        return curr

    def show(self):
        curr = self.head
        while curr != None:
            print(curr)
            curr = curr.next
    
    def __del__(self): #clear the entire inner list if the product type is dropped
        curr = self.head
        while curr !=None :
            temp = curr
            curr = curr.next
            del(temp)

class ProductNode:
    def __init__(self, type, code):
        self.type = type
        self.code = code
        self.models = None
        self.next = None
    
    def __str__(self):
        return "(" + self.type + "," + self.code +")"
    
    def __del__(self):
        del(self.models)


class ProductList:
    def __init__(self):
        self.head = ProductNode("dummy","0000") #dummy node to indicate empty list
    
    def insert(self,type,code):
        temp = ProductNode(type,code)
        temp.next = self.head
        self.head = temp
    
    def search(self,type=None,code=None):
        curr = self.head
        while curr!=None:
            if curr.code==code or curr.type==type: return curr
            curr = curr.next
        return curr
    
    def delete(self,type=None,code=None):
        curr = self.head
        if curr.type==type or curr.code==code : #deleting the head node
            self.head = curr.next
            del(curr)
            return
        
        while curr!=None:
            if curr.next.code==code or curr.next.type==type: break
            curr = curr.next
        if curr==None : raise Exception("mentioned code/type of Product not available, cannot delete")
        temp = curr.next
        curr.next = curr.next.next
        del(temp)
        return curr
    
    def show(self):
        curr = self.head
        while curr != None:
            print(curr)
            curr = curr.next

x = ProductList()
x.show() #will show dummy node indicating empty list
x.insert("LED TV","1001")
x.head.models = ModelList()
x.head.models.show() #will show dummy node indicating empty list
x.head.models.insert("Samsung LED TV 55 inch","1001001",11,556677.88)
x.head.models.insert("Sony Bravia LED TV 45 inch","1001002",55,16000.44)
x.head.models.insert("TCL LED TV 43 inch","1001003",22,26080.33)

x.insert("Pulse Oximeter","1002")
x.head.models = ModelList()
x.head.models.insert("3M pulse oximeter","1002001",776,2503.66)
x.head.models.insert("Medcalplus pulse oximeter","1002002",0,1400.88)

x.insert("Umbrella","1003")
x.head.models = ModelList()
x.head.models.insert("Cheetah brand","1003001",3223,88.33)
x.head.models.insert("Poppy brand","1003002",4325,44.67)
x.head.models.insert("Thomas brand","1003003",6677,34.67)
x.head.models.insert("Jason brand","1003004",7634,32.67)

x.show()

print(x.search(code="10022"))
x.head.models.show() #umbrellas
x.head.next.models.show() #oximeters
x.head.next.next.models.show() #TV

x.head.models.delete(code="1003002")
x.head.models.show() #umbrellas

x.show()
x.delete(code="1003") #delete the umbrella product category
x.show()

print(x.head.next.models.search(name="TCL LED TV 43 inch")) #notice we are using head.next only, compare with Line 140
print(x.head.next.models.update(name="TCL LED TV 43 inch",quantity=33))
print(x.head.next.models.update(name="TCL Laser TV 43 inch",quantity=33)) #product does not exist
import datetime.datetime
class Discountcode:
    time:datetime.datetime
    customers:list["Customer"]
    product:"Product"=None 
    limit:int=0
    def __init__(self,time,customer,product,limit):
        self.time=time
        self.customer=customer
        self.product=product
        self.limit=limit
    def __str__(self):
        return f"time:{self.time},customer:{self.customer},product:{self.product},limit:{self.limit}"
class Shoppingbasket:
    item:"Item"=None
    seller:"Seller"=None
    time:datetime.datetime
    discount_codes:list[Discountcode]
    def __init__(self,item,seller,time,discount_codes):
        self.item=item
        self.seller=seller
        self.time=time
        self.discount_code=discount_codes
    def __str__(self):
        return f"item:{self.item},seller:{self.seller},time:{self.time},discount_code:{self.discount_code}"
class Transaction:
    time:datetime.datetime
    tracking_number:int=0
    amount:int=0
    def __init__(self,time,tracking_number,amount):
        self.time=time
        self.tracking_number=tracking_number
        self.amount=amount
    def __str__(self):
        return f"time:{self.time},tracking_number:{self.tracking_number},amount:{self.amount}"
class Wallet:
    code:int=0
    transactions:list[Transaction]
    def __init__(self,code,transactions):
        self.code=code
        self.transactions=transactions
    def __str__(self):
        return f"code:{self.code},transactions:{self.transactions}"
class Customer:
    name:str=""
    family:str=""
    id:str=""
    shopping_basket:list[Shoppingbasket]
    wallet:Wallet=None
    def __init__(self,name,family,id,shopping_basket,wallet):
        self.name=name
        self.family=family
        self.id=id
        self.shopping_basket=shopping_basket
        self.wallet=wallet
    def __str__(self):
        return f"name:{self.name},family:{self.family},id:{self.id},shopping_basket:{self.shopping_basket},wallet:{self.wallet}"
class Comment:
    context:str=""
    time:datetime.datetime
    user:Customer
    def __init__(self,context,time,user):
        self.context=context
        self.time=time
        self.user=user
    def __str__(self):
        return f"time:{self.time},user:{self.user},context:{self.context}"
class Product:
    id:str=""
    comments:list[Comment]
    def __init__(self,id,comments):
        self.id=id
        self.comments=comments
    def __str__(self):
        return f"id:{self.id},comments:{self.comments}"
class Item:
    number:int=0
    type:Product
    price:int=0
    def __init__(self,number,type,price):
        self.number=number
        self.type=type
        self.price=price
    def __str__(self):
        return f"number:{self.number},type:{self.type},price:{self.price}"
class Orderlist:
    id:str=""
    sellers:"Seller"=None
    item:Item=None
    order_time=datetime.datetime
    discount_code:Discountcode=None
    def __init__(self,id,sellers,item,order_time,discount_code):
        self.id=id
        self.sellers=sellers
        self.item=item
        self.order_time=order_time
        self.discount_code=discount_code
    def __str__(self):
        return f"id:{self.id},sellers:{self.sellers},item:{self.item},order_time:{self.order_time},discount_code:{self.discount_code}"
class Seller:
    products:list[Item]
    place:str=""
    score:int=0
    order_list:list[Orderlist]
    wallet:int=0
    satistics:int=0
    user_number:str=""
    def __init__(self,products,place,score,order_list,wallet,satistics,user_number):
        self.products=products
        self.place=place
        self.score=score
        self.order_list=order_list
        self.wallet=wallet
        self.satistics=satistics
        self.user_number=user_number
    def __str__(self):
        return f"products:{self.products},place:{self.place},score:{self.score},order_list:{self.order_list},wallet:{self.wallet},satistics:{self.satistics},user_number:{self.user_number}"
class Shop:
    sellers:list[Seller]
    products:list[Product]
    customers:list[Customer]
    discount_codes:list[Discountcode]
    def __init__(self,sellers,products,customers,discount_codes):
        self.sellers=sellers
        self.products=products
        self.customers=customers
        self.discount_codes=discount_codes
    def __str__(self):
        return f"sellers:{self.sellers},products:{self.products},customers:{self.customers},discount_codes:{self.discount_codes}"
    
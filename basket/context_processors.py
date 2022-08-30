from .basket import Basket


def basket(request):
# here we are assessing the Basket class from the basket.py file in other to ustilize the session inside the basket.
    return {'basket': Basket(request)}
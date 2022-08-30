from store.models import Product
from decimal import Decimal


class Basket():
    """
    A base Basket class, the provides a default attribute which can be overwritten or inherited
    """
    def __init__(self, request):
        self.session = request.session
# if we have an existing session go ahead and run the session, if not, create a new one
        basket = self.session.get('skey')
# if we have a new user session go ahead and create a new session instance and store the session in the basket.
        if 'skey' not in request.session:
            basket= self.session['skey'] = {}
        self.basket = basket


    def add(self, product, qty):
        """
        Adding and updating the users basket session data
        """
        product_id = str(product.id)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        else:
            self.basket[product_id] = {'price':str(product.price), 'qty':qty}

        self.save()

# we are using __iter__ function to make the basket iterable so that when we iterate through the basket, we can spit out some data or values
    def __iter__(self):
        """
        Collect the product_id in the session data to query the database and return products
        """
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket= self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item


    def __len__(self):
        """
        get the basket data and count the qty of items
        """
        return sum(item['qty'] for item in self.basket.values())
    

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())


    def delete(self, product):
        """
        Delete item from session data
        """
        product_id = str(product)

        if product_id in self.basket:
            del self.basket[product_id]
            self.save()


    def update(self, product, qty):
        """
        update values in session data
        """
        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty

        self.save()

    def save(self):
        self.session.modified = True
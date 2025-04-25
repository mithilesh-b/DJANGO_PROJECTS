from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .cart import Cart
from product.models import Product
# Create your views here.


def add_cart (request):
    #initializes a blank cart or get an existing cart
    mycart = Cart(request)
    
    if request.method == "POST":
        prod_id = int(request.POST['product_id'])
        qty = int(request.POST['product_qty'])
        select_product = get_object_or_404 (Product, product_id = prod_id)
        mycart.add_item(added_product = select_product, prod_qty=qty)
        cart_quantity = len(mycart)
        print(cart_quantity)
        response = JsonResponse({'qty':cart_quantity})
        return response
    

def cart_page(request):
    cart = Cart(request)         #object(request) --> retrieve from session
    cart_products = cart.get_prod_list()
    cart_quantity = cart.get_prod_qnty()
    return render(request, 'cart.html', {'cart_products':cart_products, 'cart_qnty':cart_quantity})    


def cart_updte (request):
    if request.method == "POST":
        prod_qty = int(request.POST.get("product_qty"))
        prod_id = str(request.POST.get("product_id"))
        my_cart = Cart(request)
        my_cart.update_cart_qunatity(product_id=prod_id, product_quantity=prod_qty)
        cart_quantity = len(my_cart)
        response = JsonResponse({'cqty':cart_quantity})
        return response
def cart_delete (request):
    if request.method == "POST":
        prod_id = str(request.POST.get("product_id"))
        my_cart = Cart(request)
        my_cart.delete_item(product_id=prod_id)
        response = JsonResponse({'quantity':len(my_cart)})
        return response
from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerSignup, CusstomerprofileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse


# Create your views here.
class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        return render(request, 'index.html', {'topwears': topwears, 'bottomwears': bottomwears, 'mobiles': mobiles})


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        if request.user.is_authenticated:
            return render(request, 'product_details.html', {'product': product})
        else:
            return redirect('login')


def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'Asus' or data == 'Samsung' or data == 'Apple':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(
            category='M').filter(selling_price__lt=100000)
    elif data == 'above':
        mobiles = Product.objects.filter(
            category='M').filter(selling_price__gt=100000)
    return render(request, 'mobiles.html', {'mobiles': mobiles})


def topwear(request, data=None):
    if data == None:
        topwears = Product.objects.filter(category='TW')
    elif data == 'below':
        topwears = Product.objects.filter(
            category='TW').filter(selling_price__lt=1000)
    elif data == 'above':
        topwears = Product.objects.filter(
            category='TW').filter(selling_price__gt=1000)
    return render(request, 'topwear.html', {'topwears': topwears})


def bottomwear(request, data=None):
    if data == None:
        bottomwears = Product.objects.filter(category='BW')
    elif data == 'below':
        bottomwears = Product.objects.filter(
            category='BW').filter(selling_price__lt=1000)
    elif data == 'above':
        bottomwears = Product.objects.filter(
            category='BW').filter(selling_price__gt=1000)
    return render(request, 'bottomwear.html', {'bottomwears': bottomwears})


# def index(request):
#     return render(request, 'index.html')


# def product_details(request):
#     return render(request, 'product_details.html')

# def signup(request):
#     return render(request, 'signup.html')


class CustomerReg(View):
    def get(self, request):
        form = CustomerSignup()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = CustomerSignup(request.POST)
        if form.is_valid():
            messages.success(
                request, 'Congratulations! Registered Successfully')
            form.save()
            return redirect('login')
        return render(request, 'signup.html', {'form': form})


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_pro = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_pro:
            tempamount = (p.quantity * p.product.selling_price)
            amount += tempamount
        print(amount + shipping_amount, '-----')
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount,
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_pro = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_pro:
            tempamount = (p.quantity * p.product.selling_price)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount':  amount + shipping_amount,
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        cart_pro = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_pro:
            tempamount = (p.quantity * p.product.selling_price)
            amount += tempamount

        data = {
            'amount': amount,
            'totalamount':  amount + shipping_amount,
        }
        return JsonResponse(data)


def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_pro = [p for p in Cart.objects.all() if p.user == user]

        if cart_pro:
            for p in cart_pro:
                tempamount = (p.quantity * p.product.selling_price)
                amount += tempamount
                totalamount = amount + shipping_amount
            return render(request, 'add_to_cart.html', {'carts': cart, 'totalamount': totalamount, 'amount': amount})
        else:
            return render(request, 'emptycart.html')
    return redirect('login')


def buy_now(request):
    return render(request, 'buy_now.html')


class ProflieView(View):
    def get(self, request):
        form = CusstomerprofileForm()
        return render(request, 'profile.html', {'form': form, 'active': 'btn-primary'})

    def post(self, request):
        form = CusstomerprofileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, locality=locality,
                           city=city, state=state, zipcode=zipcode)
            messages.success(
                request, 'Congratulations! Registered Successfully')
            reg.save()

        return render(request, 'profile.html', {'form': form, 'active': 'btn-primary'})


#
def admin(request):
    return render(request, 'admin.html')


def orders(request):
    return render(request, 'orders.html')


def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'address.html', {'add': add, 'active': 'btn-primary'})


#
# def change_password(request):
#     return render(request, 'change_password.html')
#

# def login(request):
#     return render(request, 'login.html')


def customer_registration(request):
    return render(request, 'customer_registration.html')


def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_itm = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    total_amount = 0
    cart_pro = [p for p in Cart.objects.all() if p.user == user]

    if cart_pro:
        for p in cart_pro:
            tempamount = (p.quantity * p.product.selling_price)
            amount += tempamount
        totalamount = amount + shipping_amount
    print(totalamount)  
    return render(request, 'checkout.html', {'add': add, 'tempamount': tempamount, 'cart_itm': cart_itm})

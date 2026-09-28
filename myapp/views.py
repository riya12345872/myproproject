from django.shortcuts import render , redirect 
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def index_view (request):

    if not request.user.is_authenticated:
        return redirect('login_page')

    product = Products.objects.all()

    context = {
        'productdata': product,
    }

    return render (request,'pages/index.html',context)



    
def about_view(request):
    return render(request,'pages/about.html')

def login_view(request):
    if request.method== 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

      

def register_view(request):

    if request.method == 'POST':
        # Process the form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            messages.error(request,'please fill in all fields.')
            return redirect('register_page')


    user_data = User.objects.create_user(username=email,first_name=username, email=email, password=password)

    user_data.save()
    messages.success(request,'registeration successful.Please login.')
    return redirect('login_page')

def add_to_cart_view(request, product_id):

    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to add items to the cart.')
        return redirect('login_page')

    productis = Products.objects.filter(id=product_id).first()

if products is None:
    messages.error(request,'Product not found.')
    return redirect('index_page')
user_cart, created = UserCart.objects.get_or_create(user=request.user)

cart_item, created = CartItems.objects.get_or_create(cart=user_cart,product=productis)

if not created:
    cart_item.quantity += 1
    cart_item.save()

    messages.success(request, f'Added {productis.name} to your cart')
    return redirect('index_page')


def cart_count(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in ')
        return redirect('login_page')

    user_cart, created = UserCart.objects.get
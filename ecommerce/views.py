from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Product, ProductImage, Section, Banner, Shop, ShopTheme, Brand, Tag, Customer,ProductVariant, Page, Menu, MenuItem, Contact, Order, Order_status, Review, Plugin, ShopPlugin, Seo
from .models import Leads
from .decorators import get_shop2
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from core.notification.notif import notify
from core.models import Account, Notification
# Create your views here.

@get_shop2
def home(request, shop, theme):
    qs = Product.objects.filter(shop=shop)
    sections = Section.objects.filter(shop=shop)
    banners = Banner.objects.filter(shop=shop)
    brands = Brand.objects.filter(shop=shop)
    payment_methods = ShopPlugin.objects.filter(shop=shop, plugin__type='payment', activated=True)
    active = ShopTheme.objects.filter(shop=shop, activated=True).first()
    context = {
        'feature_products': qs[:6],
        'all_products': qs,
        'banners': banners,
        'brands': brands,
        'payment_methods': payment_methods,
        'active': active
    }
    return render(request, theme + 'home.html', context)

@get_shop2
def details(request, shop, theme, id):
    product = Product.objects.filter(id=id, shop=shop).first()
    images = ProductImage.objects.filter(product = product)
    productvarient = ProductVariant.objects.filter(id=id, product=product)
    sections = Section.objects.filter(shop=shop)

    if not product:
        return redirect('not_found')
    if request.method == 'POST':
        data = request.POST
        print(data)
        # {'csrfmiddlewaretoken': ['gUsG6CR5oa7248Pncn0ZDKmwA27qNZ7xe0LQzwVFELmwtHyVN3Pym1i1XnC83ED1'], 'rating': ['5'], 'review': ['asdfasdfasdf']}
        if 'rating' in data:
            customer = request.user.customer
            review = Review.objects.create(
                customer=customer,
                product=product,
                rating=data['rating'], 
            )
            review.save()
            revList = list(customer.reviewables)
            revList.remove(id)
            print(customer.reviewables, revList, 8888)
            customer.reviewables = revList
            customer.save()
    reviews = Review.objects.filter(product=product)
    qs = Product.objects.filter(shop=shop)
    user = request.user
    context = {
        'product': product,
        'images': images,
        'productvarient': productvarient,
        'feature_products': qs,
        'all_products': qs,
        'reviews': reviews,
        'sections': sections,
    }
    if user.is_authenticated and user.customer.reviewables and id in user.customer.reviewables:
        context['reviewable'] = True
    return render(request, theme + 'details.html', context)

@get_shop2
def checkout(request, shop, theme):
    payment_methods = ShopPlugin.objects.filter(shop=shop, plugin__type='payment', activated=True)
    # qs = Product.objects.filter(shop=shop)

    print(payment_methods)
    context = {
        'payment_methods': payment_methods,
    }
    return render(request, 'commons/checkout.html', context)
@get_shop2
def cart(request, shop, theme):
    sections = Section.objects.filter(shop=shop)
    qs = Product.objects.filter(shop=shop)
    context = {
        'feature_products': qs,
    }
    return render(request, theme + 'cart.html', context)
@get_shop2
def wishlist(request, shop, theme):
    sections = Section.objects.filter(shop=shop)
    products = Product.objects.filter(shop=shop)

    context = {
        'product': products
    }
    return render(request, theme + 'wishlist.html', context)
@csrf_exempt
@get_shop2
def signin(request, shop, theme):
    sections = Section.objects.filter(shop=shop)
    context = {
        'action': 'signin'
    }
    
    if request.method == 'POST':
        data = request.POST
        if 'confirm-password' in data:
            print(data, 'register')
            context['action'] = 'signup'
            if not data['password'] == data['confirm-password']:
                messages.warning(request, "Password not match")
                context['error'] = 'Password not match'
            elif Customer.objects.filter(shop=shop, email=data['email']).first():
                messages.warning(request, "Email already exists")
                context['error'] = 'Email already exists'
            else:
                new_user = User.objects.create_user(data['email']+shop.name, data['email'], data['password'])
                new_user.save()
                new_customer = Customer.objects.create(
                    user=new_user,
                    shop=shop,
                    email=data['email'],
                )
                user = authenticate(request, username=new_user.username, password=data['password'])
                messages.success(request, "Registration successful")
                login(request, user)
                if request.GET.get("next"):
                    return HttpResponseRedirect(request.GET.get("next"))
                else:
                    return render(request, theme + 'my_account.html', context)
        else:
            print(data, 'login')
            user = authenticate(request, username=data['email']+shop.name, password=data['password'])
            if user:
                login(request, user)
                messages.success(request, "Login successful")
                if request.GET.get("next"):
                    return HttpResponseRedirect(request.GET.get("next"))
                else:
                    return render(request, theme + 'my_account.html', context)
            else:
                context['error'] = 'Invalid username or password'
            context['error'] = 'Invalid username or password'
            messages.error(request, "Invalid username or password")
    if request.user.is_authenticated:
        if request.GET.get('logout', None):
            messages.success(request, "Logout successful")
            logout(request)
        else:
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            else:
                return HttpResponseRedirect('/my_account')
    return render(request, theme + 'login_signup.html', context)
@get_shop2
def search_page(request, shop, theme):
    products = Product.objects.filter(shop=shop)
    qs = Product.objects.filter(shop=shop)

    search = request.GET.get('search', None)
    if search:
        tag, ct = Tag.objects.get_or_create(shop=shop, name=search)
        tag.qty += 1
        tag.save()
        products = Product.objects.filter(shop=shop, name__icontains=search)
        products = products | Product.objects.filter(shop=shop, tags__id=tag.id)
    category_id = request.GET.get('category', None) 
    if category_id:
        products = products.filter(categories__id=category_id)
    section = request.GET.get('section', None)
    if section:
        products = products.filter(categories__section__id=section)
    brand = request.GET.get('brand', None)
    if brand:
        products = products.filter(brand__id=brand)
    # ?min=666&max=1000
    min_price = request.GET.get('min', None)
    max_price = request.GET.get('max', None)
    if min_price and max_price:
        products = products.filter(sale_price__gte=min_price, sale_price__lte=max_price)
    
    perpage = request.GET.get('perpage', 16)
    paginator = Paginator(products, perpage)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj,
        'feature_products': qs,
    }
    return render(request, theme + 'search_page.html', context)
@get_shop2
def my_account(request, shop, theme):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/signin')
    if request.method == 'POST':
        data = request.POST
        print(data)
        # 'name': ['adsgasdf'], 'phone': ['2352352'], 'email': ['shimul929@gmail.com'], 'pass': [''], 'pass1': [''], 'pass2': ['']
        if 'name' in data:
            customer = request.user.customer
            customer.name = data['name']
            customer.phone = data['phone']
            customer.email = data['email']
            customer.save()
            messages.success(request, "Profile details updated.")
        if 'pass' in data and data['pass']:
            if not request.user.check_password(data['pass']):
                messages.error(request, "Invalid password.")
            elif not data['pass1'] == data['pass2']:
                messages.error(request, "Password not match.")
            else:
                request.user.set_password(data['pass1'])
                request.user.save()
                messages.success(request, "Password updated.")
    orders = Order.objects.filter(customer=request.user.customer)
    context = {
        'orders': orders,
    }
    return render(request, theme + 'my_account.html', context)
@get_shop2
def contact_us(request, shop, theme):
    context = {}
    if request.method == "POST":
        data = request.POST
        print(data)
        Contact.objects.create(
            shop=shop,
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            message=data['message'],
        )
        context['success'] = 'Your message has been sent successfully'
        notify(shop.account,None,None,4)
    return render(request, theme + 'contact_us.html', context)
@get_shop2
def tracking(request, shop, theme):
    id = request.GET.get('tracking', None)
    if id:
        order = Order.objects.filter(id=id).first()
        if order:
            items = order.items
            for item in items:
                item['details'] = Product.objects.get(id=item['id'])
            statuses = Order_status.objects.filter(order=order)
            context = {
                'order': order,
                'items': items,
                'statuses': statuses,
            }
        else:
            context = {
                'error': 'Order not found!',
            }
    else:
        context = {}
    return render(request, theme + 'tracking.html', context)
@get_shop2
def page(request, shop, theme, name):
    if name == 'privacy':
        page,ct = Page.objects.get_or_create(title='Privacy Policy', shop=shop)
    elif name == 'terms':
        page,ct = Page.objects.get_or_create(title='Terms and Conditions', shop=shop)
    elif name == 'refund':
        page,ct = Page.objects.get_or_create(title='Refund Policy', shop=shop)
    else:
        page = Page.objects.get(shop = shop, slug=name)
    context = {
        'shop': shop,
        'page': page,
    }
    return render(request, theme + 'page.html', context)

@get_shop2
def pages(request, shop, theme, name):
    context = {
        'shop': shop,
    }
    if request.method == "POST":
        data = request.POST
        print(data)
        Contact.objects.create(
            shop=shop,
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            message=data['message'],
        )
        context['success'] = 'Your message has been sent successfully'
    return render(request, theme + 'pages/' +name+ '.html', context)



# other 
def activateNextoxyTheme(request):
    return render(request, 'other/activateNextoxyTheme.html')

@get_shop2
def sitemap(request, shop, theme):
    plugin = ShopPlugin.objects.filter(shop=shop, plugin__code = 'sitemap', activated = True)
    if not plugin:
        return HttpResponse('Page not found!')    
    date = datetime.now().strftime('%Y-%m-%d')
    base_url = request.build_absolute_uri('/')[:-1]
    pages = Page.objects.filter(shop=shop)
    products = Product.objects.filter(shop=shop)
    context = {
        "shop" : shop,
        "base_url" : base_url,
        "date" : date,
        "pages" : pages,
        "products" : products,
    }
    return render(request, 'other/sitemap.xml', context, content_type='text/xml')

@get_shop2
def robots(request, shop, theme):
    seo, ct = Seo.objects.get_or_create(shop=shop)
    plugin = ShopPlugin.objects.filter(shop=shop, plugin__code = 'robots', activated = True)
    print(plugin)
    if not plugin:
        return HttpResponse('Page not found!')
    context = {
        "content" : seo.robots
    }
    return render(request, 'other/robots.txt', context, content_type='text/plain')

@get_shop2
def not_found(request, shop, theme):
    return render(request, theme + '404.html')



def blogDetails(request):
    return render(request, 'blog2/blog_details.html')
def category(request):
    return render(request, 'blog2/categories.html')
def contact(request):
    return render(request, 'blog2/contact.html')
def about(request):
    return render(request, 'blog2/about.html')


# landing page 

@get_shop2
def submitLeadForm(request, shop, theme):
    if request.method == 'POST':
        data = request.POST
        print(data)
        new_ld = Leads.objects.create(shop=shop)
        if data['name']:
            new_ld.name = data['name']
        if 'phone' in data:
            new_ld.phone = data['phone']
        if 'email' in data:
            new_ld.email = data['email']
        if 'whatsapp' in data:
            new_ld.whatsapp = data['whatsapp']
        if 'skype' in data:
            new_ld.skype = data['skype']
        if 'website' in data:
            new_ld.website = data['website']
        if 'facebook' in data:
            new_ld.facebook = data['facebook']
        if 'message' in data:
            new_ld.message = data['message']
        if 'note' in data:
            new_ld.note = data['note']
        if 'label' in data:
            new_ld.label = data['label']
        if 'extra' in data:
            new_ld.extra = data['extra']
        new_ld.save()
    return render(request, theme + 'submit-lead-form.html')






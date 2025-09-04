from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request,"index.html",{})

def fake(request):
    return render(request,"calendar_appointment-booking.html",{})

def about(request):
    return render(request,"about.html",{})


def services(request):
    service=Service.objects.all()
    return render(request,"services.html",{"services":service})

def contact(request):
    return render(request,"contact.html",{})

def contact_page(request):
    if request.method == 'POST':
        print("hii")
        contact = ContactForm(request.POST)
        print(contact.errors)
        print("hii")
        if contact.is_valid():
            print("hii")
            print(contact.errors)
            contact.save()
            return render(request,"contact.html",{"msg":"send message"})
    return render(request,"contact.html",{"msg":"send fail"})


def client(request):
    return render(request,"client.html",{})


def customer_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, "", password)
        customer = Client.objects.filter(email=email, password=password)
        if customer.exists():
            request.session['email'] = email
            print(email)
            client = Client.objects.get(email=email)
            return render(request, "client_profile.html", {"msg": client.firstname})
        else:
            return render(request, "client.html", {"msg": "does not exist"})
    return render(request, "client.html", {})


def client_reg(request):
    return render(request,"client_reg.html",{})



def client_profile(request):
    return render(request,"client_profile.html",{})


def client_register(request):
    if request.method == "POST":
        email = request.POST["email"]
        
        if Client.objects.filter(email=email).exists():
            print("email already taken")
            return render(request, "client_reg.html", {"msg": "email already taken"})
        else:
            form = ClientForm(request.POST)
            print("error:", form.errors)
            if form.is_valid():
                try:
                    form.save()
                    return render(request, "client.html", {"msg": "REGISTER SUCCESS"})
                except Exception as e:
                    print(e)
                    
            return render(request, "client_reg.html", {"msg": "REGISTER FAILED"})


def client_details(request):
    email=request.session['email']
    client=Client.objects.get(email=email)
    return render(request,"client_details.html",{"client":client})


def client_logout(request):
    request.session["email"] = ""
    del request.session["email"]
    return render(request,"client.html",{})



def is_client(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def client_changepassword(request):
    if is_client(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]
            try:
                user = Client.objects.get(email=email, password=password)
                user.password = newpassword
                user.save()
                msg = 'password update successfully'
                return render(request, "client.html", {"msg": msg})
            except:
                msg = 'Password is Wrong'
                return render(request, "client_password.html", {"msg": msg})
        return render(request, "client_password.html", {})
    else:
        return render(request, "client_password.html", {"msg":"data not valid"})



def client_delete(request, email):
    user = Client.objects.get(email=email)
    user.delete()
    return redirect("/client_reg")



def client_edit(request, email):
    client = Client.objects.get(email=email)
    return render(request, "client_edit.html", {"client": client})


def client_update(request):
    if request.method == "POST":
        print("error:")
        email = request.POST["email"]
        print("hello")
        client = Client.objects.get(email=email)
        client = ClientForm(request.POST, instance=client)
        print("error:", client.errors)
        if client.is_valid():
            print("error:", client.errors)
            client.save()
        return redirect("/client_details")
    return redirect("/client_details")


def book_slot(request):
    return render(request, "book_slot.html", {})


def staff(request):
    return render(request,"staff.html",{})


def staff_login(request):
    if request.method == "POST":
        staffid = request.POST["staffid"]
        password = request.POST["password"]
        print(staffid, "", password)
        staff = Staff.objects.filter(staffid=staffid, password=password)
        if staff.exists():
            request.session['staffid'] = staffid
            return render(request, "staff_profile.html", {"msg": staffid})
        else:
            return render(request, "staff.html", {"msg": "not exist"})
    return render(request, "staff.html", {"msg": "not exist"})


def staff_profile(request):
    return render(request,"staff_profile.html",{})


def staff_logout(request):
    request.session["staffid"] = ""
    del request.session["staffid"]
    return render(request,"staff.html",{})


def client_view_service(request):
    service=Service.objects.all()
    return render(request,"client_view_service.html",{"services":service})


def addcart(request,id):
    email=request.session['email']
    client=Client.objects.get(email=email)
    service=Service.objects.get(id=id)
    if request.method=='POST':
        print("hii")
        cart=CartForm(request.POST)
        print(cart.errors)
        print("hii")
        if cart.is_valid():
            print("hii")
            print(cart.errors)
            cart.save()
            return render(request,"cart.html",{"msg":"success","client":client.id,"service":service.id, "name": service.service_name})
    return render(request,"cart.html",{"msg":"fail","client":client.id,"service":service.id, "name": service.service_name})


def viewcart(request):
    email = request.session['email']
    client= Client.objects.get(email=email)
    cart = Cart.objects.filter(client_id=client.id)
    return render(request,"viewcart.html",{"carts":cart})


def staff_view_cart(request):
    cart=Cart.objects.all()
    return render(request,"staff_view_cart.html",{"carts":cart})


def approve_slot(request, service_id):
    approve=Cart.objects.get(id=service_id)
    approve.status = 1
    approve.save()
    return redirect("/staff_view_cart")


def reject_slot(request, service_id):
    reject=Cart.objects.get(id=service_id)
    reject.status = 2
    reject.save()
    return redirect("/staff_view_cart")



from django.shortcuts import render, redirect  
from product.forms import ProductForm  
from product.models import Product  
from django.http import JsonResponse
from product.models import Payment
 
def product(request):  
    if request.method == "POST":  
        form = ProductForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ProductForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    products = Product.objects.all()  
    return render(request,"show.html",{'products':products})  

def edit(request, id):  
    product = Product.objects.get(id=id)  
    return render(request,'edit.html', {'product':product}) 

def update(request, id):  
    product = Product.objects.get(id=id)  
    form = ProductForm(request.POST, instance = product)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'product': product})
  
def destroy(request, id):  
    product = Product.objects.get(id=id)  
    product.delete()  
    return redirect("/show")

def raw_sql(request):
	name = ''
	for p in Product.objects.raw('SELECT * FROM products'):
		name = nme + " " + p.pname
	return JsonResponse({'result':name})

def getjson(request):
	return JsonResponse({'name':'broadway'})

def pay(request):
	payment_serializer = PaymentSerializer(data = request.data)
	if payment_serializer.is_valid():
		payment_serializer.save()
		return JsonResponse({'success': True})
	return JsonResponse({'success': False})
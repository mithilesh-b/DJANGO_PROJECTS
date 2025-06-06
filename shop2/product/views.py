
import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from product.models import Product, ProductCategory
from . import forms  # . means the current folder
from django.contrib.auth.decorators import login_required

# For messages framework
from django.contrib import messages


def say_hello(request):
    return HttpResponse('Hello Django')


def startpage(request):
    cat_list = ProductCategory.objects.all()
    context = {"category_list":cat_list}
    return render(request, 'index.html', context)
    # return render(request, 'index.html')


def garmentpage(request):
    return render(request, 'garment.html')


def mobilepage(request):
    return render(request, 'mobile.html')


def testpage(request):
    context = {"name": "sanskar", "roll_no": 21670}
    return render(request, 'test.html', context)


def viewall(request):
    allproduct = Product.objects.all()
    context = {"my_products": allproduct}
    return render(request, 'showproduct.html', context)


def editproduct(request, pid):
    selected_product = Product.objects.get(product_id=pid)

    if request.method == "POST":
        pname = request.POST.get("p_name")
        pdesc = request.POST.get("p_desc")
        pprice = request.POST.get("price")

        selected_product.product_name = pname
        selected_product.product_description = pdesc
        selected_product.product_price = pprice

        selected_product.save()
        messages.success(request, "Data Updated")
        return redirect('/allibaba/showprod')

    context = {"edit_product": selected_product}
    return render(request, 'edit_product.html', context)


def add_product(request):
    if request.method == "POST":
        pname = request.POST.get("p_name")
        pdesc = request.POST.get("p_desc")
        pprice = request.POST.get("price")
        category_id = int(request.POST.get("category"))
        cat = ProductCategory.objects.get(pk=category_id)

        # Check if the category exists
        #category, created = ProductCategory.objects.get_or_create(p_cat_name=category_name)

        po = Product(
            product_name=pname,
            product_description=pdesc,
            product_price=pprice,
            product_category = cat
        )
        po.save()

        messages.success(request, "Product added successfully.")
        return redirect('/allibaba/showprod')

    # Fetch all categories for the dropdown
    categories = ProductCategory.objects.all()
    return render(request, 'add_product.html', {'categories': categories})

def deleteproduct(request, pid):
    selected_product = Product.objects.get(product_id=pid)
    selected_product.delete()
    messages.warning(request, "Data deleted")
    return redirect('/allibaba/showprod')

@login_required
def prod_cat(request):
    if request.method == "POST":
        form = forms.ProductCategoryForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your file has been uploaded")
            return redirect('product-catagory')

    myform = forms.ProductCategoryForm()
    return render(request, 'prod_cat.html', {'my_form': myform})


def showprodcat(request):
    prodcatlist = ProductCategory.objects.all()
    return render(request, 'showprodcat.html', {'prodcat_list': prodcatlist})


def edit_prodcat(request, pcatid):
    pcatobj = ProductCategory.objects.get(pk=pcatid)
    myform = forms.ProductCategoryForm(request.POST or None, request.FILES or None, instance=pcatobj)

    if request.method == "POST":
        if myform.is_valid():
            myform.save()
            messages.success(request, "Product category updated successfully")
            return redirect('show-product-catagory')
        else:
            messages.warning(request, "Form data was not valid")
            return redirect('show-product-catagory')

    return render(request, 'edit_prodcat.html', {'my_form': myform})


def delete_prodcat(request, pcatid):
    pcatobj = ProductCategory.objects.get(pk=pcatid)
    pcatobj.delete()

    if pcatobj.p_cat_image:
        os.remove(pcatobj.p_cat_image.path)

    messages.warning(request, "Category was deleted")
    return redirect('show-product-catagory')

def prod_list_bycat(request, cat_id):
    prod_list = Product.objects.filter(product_category=cat_id)            #get --> 1 row    filter--> more than 1 records
    return render(request, 'show_items_bycat.html', {'prod_list':prod_list})


def edit_prod_list_bycat(request, cat_id):
    # grab the object to be editted
    prod_list_obj = ProductCategory.objects.get(pk = cat_id)
    # build a form with the object instance
    myform = forms.ProductCategoryForm(request.POST or None, request.FILES or None, instance=prod_list_obj)

    if request.method == "POST":
        if myform.is_valid():
            myform.save()
            messages.success(request, "Product list by Category updated successfully")
            return redirect('home')
        else:
            messages.warning(request, "Form data was not valid")
            return redirect('showitemsbycat')

    return render(request, 'edit_prod_list_bycat.html', {'my_form': myform})


def delete_prod_list_bycat(request, cat_id):
    prod_list_obj = ProductCategory.objects.get(pk=cat_id)
    prod_list_obj.delete()
    messages.warning(request, "This Product list by Category is deleted")
    return redirect('home')


def search_product(request):
    if request.method == "POST":
        search_item =request.POST['search_area']
        
        something = Product.objects.filter(product_name__contains = search_item,product_description__contains = search_item )
        #get is used t get only one value & filter is used to more than value
        return render(request, 'searchresult.html', {'seach_result':something})
        

# import os
# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from product.models import Product, ProductCategory
# from . import forms  # . means the current folder

# # For messages framework
# from django.contrib import messages


# def say_hello(request):
#     return HttpResponse('Hello Django')


# def startpage(request):
#     return render(request, 'index.html')


# def garmentpage(request):
#     return render(request, 'garment.html')


# def mobilepage(request):
#     return render(request, 'mobile.html')


# def testpage(request):
#     context = {"name": "sanskar", "roll_no": 21670}
#     return render(request, 'test.html', context)


# def viewall(request):
#     allproduct = Product.objects.all()
#     context = {"my_products": allproduct}
#     return render(request, 'showproduct.html', context)


# def editproduct(request, pid):
#     selected_product = Product.objects.get(product_id=pid)

#     if request.method == "POST":
#         pname = request.POST.get("p_name")
#         pdesc = request.POST.get("p_desc")
#         pprice = request.POST.get("price")

#         selected_product.product_name = pname
#         selected_product.product_description = pdesc
#         selected_product.product_price = pprice

#         selected_product.save()
#         messages.success(request, "Data Updated")
#         return redirect('/allibaba/showprod')

#     context = {"edit_product": selected_product}
#     return render(request, 'edit_product.html', context)


# def add_product(request):
#     if request.method == "POST":
#         pname = request.POST.get("p_name")
#         pdesc = request.POST.get("p_desc")
#         pprice = request.POST.get("price")
#         pcategory = request.POST.get("category")

#         # Assuming you have a ForeignKey relationship between Product and ProductCategory
#         category = ProductCategory.objects.get(p_cat_name=pcategory)

#         po = Product(product_name=pname, product_description=pdesc, product_price=pprice, product_category=category)
#         po.save()

#         messages.success(request, "Data saved successfully, thank you")

#     categories = ProductCategory.objects.all()
#     return render(request, 'add_product.html', {'categories': categories})


# def deleteproduct(request, pid):
#     selected_product = Product.objects.get(product_id=pid)
#     selected_product.delete()
#     messages.warning(request, "Data deleted")
#     return redirect('/allibaba/showprod')


# def prod_cat(request):
#     if request.method == "POST":
#         form = forms.ProductCategoryForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your file has been uploaded")
#             return redirect('product-catagory')

#     myform = forms.ProductCategoryForm()
#     return render(request, 'prod_cat.html', {'my_form': myform})


# def showprodcat(request):
#     prodcatlist = ProductCategory.objects.all()
#     return render(request, 'showprodcat.html', {'prodcat_list': prodcatlist})


# def edit_prodcat(request, pcatid):
#     pcatobj = ProductCategory.objects.get(pk=pcatid)
#     myform = forms.ProductCategoryForm(request.POST or None, request.FILES or None, instance=pcatobj)

#     if request.method == "POST":
#         if myform.is_valid():
#             myform.save()
#             messages.success(request, "Product category updated successfully")
#             return redirect('show-product-catagory')
#         else:
#             messages.warning(request, "Form data was not valid")
#             return redirect('show-product-catagory')

#     return render(request, 'edit_prodcat.html', {'my_form': myform})


# def delete_prodcat(request, pcatid):
#     pcatobj = ProductCategory.objects.get(pk=pcatid)
#     pcatobj.delete()

#     if pcatobj.p_cat_image:
#         os.remove(pcatobj.p_cat_image.path)

#     messages.warning(request, "Category was deleted")
#     return redirect('show-product-catagory')


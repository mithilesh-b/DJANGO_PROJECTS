from django.http import HttpResponse
import requests
from django.shortcuts import redirect, render
from django.contrib import messages

#get request-----------------------------
def get_api_data(request):
    url = "http://127.0.0.1:9000/api/companies/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return render (request, "api_data.html", {'apidata': data})
    

def api_form(request):
    try:
        if request.method == "POST":
            names = request.POST.get("name")
            locations = request.POST.get("location")
            abouts = request.POST.get("about")
            types = request.POST.get("type")
            # status = request.post.get("active")


            status = False
            if 'active' in request.POST:
                status = True
            else:
                status = False

            url = "http://127.0.0.1:9000/api/companies/"

            payload = { 
                'name':names, 'location':locations, 'about':abouts, 'type':types, 'active': status
            }
            response = requests.post(url, json = payload)        #request package -> builtin method post, get etc
            if response.status_code == 201:                      #http response code 
                data = response.json()
                print (data)
                messages.success (request, "Data saved successfully")
            else: 
                print("data saving failed") 
                messages.success (request, "Data didn't save, Remote server didn't response properly")

    except Exception as ex:
        print(ex)
        messages.warning(request, "Some error occurs")
            
    return render (request, "api_form.html")



def updatedata(request, comp_id):
    url = f"http://127.0.0.1:9000/api/companies/{comp_id}/"
    
    if request.method == 'GET':
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return render(request, 'edit_data.html', {'data': data})
        else:
            return HttpResponse('Error retrieving data', status=500)

    elif request.method == 'POST':
        updated_data = {
            'name': request.POST.get('name'),
            'location': request.POST.get('location'),
            'about': request.POST.get('about'),
            'type': request.POST.get('type'),
            'active': request.POST.get('active') == 'on'
        }

        response = requests.put(url, json=updated_data)
        if response.status_code == 200:
            return redirect('success_page')  
        
        else:
            return HttpResponse('Error updating data', status=500)
        
def success_page(request):
    return redirect ("/getdata") 



def deletedata(request, comp_id):
    try:
        url = "http://127.0.0.1:9000/api/companies/" + str(comp_id) + "/"      #url string concatination
        response = requests.delete(url)
        if response.status_code == 204:                      #http response code 
            print("data deleted successfully")
            #messages.su
        else:
            print("someting went wrong in deleting")
    except Exception as ex:
        print(ex)
        messages.warning(request, "Some error occurs")
            
    return redirect ("/getdata")     


   
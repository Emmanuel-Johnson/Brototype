from django.http import HttpResponse

def register_view(request):
    if request.method == "POST":
        
        name = request.POST.get('name')
        age = request.POST.get('age')
        password = request.POST.get('password')
        
        has_lower = any(i.islower() for i in password)
        has_upper = any(i.isupper() for i in password)
        has_digit = any(i.isdigit() for i in password)
        
        if not name.isalpha():
            return HttpResponse("Name should only contain alphabets!")
            
        if not age.isdigit():
            return HttpResponse("Age should only be Integer!")
            
        if not (has_lower and has_upper and has_digit):
            return HttpResponse("Password should contain one atleast one small letter and atleast one capital letter and atleast one digit")
            
        return HttpResponse("Sucessfully registered!")
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'base/index.html')
def aboutUs(request):
    return render(request,'base/aboutUs.html')
def contactUs(request):
    return render(request,'base/contactUs.html')
def footer(request):
    return render(request,'base/footer.html')
#def life(request):
    #return render(request,'life/lifeInsurance.html')
def health(request):
    return render(request,'health/healthInsurance.html')
#def notary(request):
    #return render(request,'notary/notary.html')
#def rssa(request):
    #return render(request,'rssa/analyst.html')
def privacy(request):
    return render(request,'base/privacy.html')
from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request,'index.html')



def about_view(request):
    #return render(request,'about.html')
    pass

def contact_view(request):
    '''
    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            form.instance.name="Unknown"
            form.save()
            messages.add_message(request, messages.SUCCESS, "Form saved successfully.")
        else:
            messages.error(request, 'The form was not saved successfully.!')

    form = Contactform()
    return render(request,'contact.html',{"form": form})
    '''
    pass

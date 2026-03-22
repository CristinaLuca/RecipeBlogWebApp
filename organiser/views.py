from django.http.response import HttpResponse

from django.template import loader

from django.shortcuts import redirect, render

from organiser.models import Tag

from . forms import TagForm, TagFormManual

import re

from django.views.generic import View
from django.views.generic.edit import CreateView

#FORMS
#Generic view
class TagCreateView(CreateView):
    # specifies the form
    form_class = TagForm

    #specifies the template
    template_name = "organiser/input_tag.html"

    #redirect to
    success_url = "../homepage_v4"

def inputTag(request):
   
    if request.method == "POST":
        # user submit form (POST)
        # loads the submitted data in form
        form = TagForm(request.POST)

        # validation
        # required fields , max length, slug format
        if form.is_valid():
            # save to the DB
            form.save()
            
            # redirect after successful save
            return redirect("homepage_v4")

    else:
        # GET request
        # empty form displayed
        form = TagForm()
   
    return render(request, "organiser/input_tag.html", {"form": form})


# view with form
# handles both GET and POST requests
# manual saving
def inputTag_manual(request):
    template = loader.get_template("organiser/input_tag.html")

    if request.method == "POST":
        # user submit form (POST)
        # loads the submitted data in form
        form = TagFormManual(request.POST)

        # validation
        # required fields , max length, slug format
        if form.is_valid():
            # form.cleaned_data contains validated data
            # manually save to the DB
            Tag.objects.create(
                tagName=form.cleaned_data["tagName"],
                slug = form.cleaned_data["slug"]
            )
            
            # redirect after successful save
            return redirect("homepage_v4")

    else:
        # GET request
        # empty form displayed
        form = TagFormManual()

    context = {
                'form' : form
    }
    return HttpResponse(template.render(context, request))

# view with form. Only GET
def inputTag_v1(request):
    template = loader.get_template("organiser/input_tag.html")
    context = {
            'form' : TagForm()
    }
    return HttpResponse(template.render(context, request))



#********************


# homepage_Inheritance
# works with tag_details_v4.html
def homepage_Inheritance(request):
    template = loader.get_template("organiser/Tag_details_Inheritance.html")
    name = "<script> alert('Chris')</script>"
    match = re.search(r"alert\('(.+?)'\)", name)
    extracted = match.group(1) if match else ""


        # create a list of tag names and add them to a string
    tag_list = Tag.objects.all()
    output = ", ".join([tag.tagName for tag in tag_list])
    context = {
        'tagNames_String' : output,
        'tagNames' : tag_list,
        'name' : extracted
    }
    return HttpResponse(template.render(context, request))

# homepage_v4
class Homepage_v4(View):
    def get(self, request):
        template = loader.get_template("organiser/Tag_details_v4.html")

        # create a list of tag names and add them to a string
        tag_list = Tag.objects.all()
        output = ", ".join([tag.tagName for tag in tag_list])
        context = {
            'tagNames_String' : output,
            'tagNames' : tag_list,
        }
        return HttpResponse(template.render(context, request))


# homepage_v2
def homepage_v2(request):
    template = loader.get_template("organiser/Tag_details_v2.html")

    # create a list of tag names and add them to a string
    tag_list = Tag.objects.all()
    output = ", ".join([tag.tagName for tag in tag_list])
    context = {
        'tagNames_String' : output,
        'tagNames' : tag_list
    }
    return HttpResponse(template.render(context, request))


# homepage_v1 with STyle
def homepage_v1_withStyle(request):
    template = loader.get_template("organiser/Tag_details_v1_withStyle.html")

    # create a list of tag names and add them to a string
    tag_list = Tag.objects.all()
    output = ", ".join([tag.tagName for tag in tag_list])
    context = {
            'tagNames' : output,
            'tagName1' : tag_list[0],
            'tagName2' : tag_list[1],
    }
    return HttpResponse(template.render(context, request))

# homepage_v1 
def homepage_v1(request):
    template = loader.get_template("organiser/Tag_details_v1.html")

    # create a list of tag names and add them to a string
    tag_list = Tag.objects.all()
    output = ", ".join([tag.tagName for tag in tag_list])
    context = {
            'tagNames' : output,
            'tagName1' : tag_list[0],
            'tagName2' : tag_list[1],
    }
    return HttpResponse(template.render(context, request))
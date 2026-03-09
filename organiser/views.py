from django.http.response import HttpResponse

from django.template import loader

from organiser.models import Tag

import re

from django.views.generic import View

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
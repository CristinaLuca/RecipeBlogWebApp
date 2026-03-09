from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader

from django.views.generic import View, ListView, DetailView
from .models import BlogPost, Tag
from .mixin import BlogMixin

# to be uncommented when using the RecordTagView class
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.detail import SingleObjectMixin


# Create your views here.

# displays the list of blogs using class-based views
class BlogListView(ListView):
    #specify which model (table from the Database) to use
    model = BlogPost
    
    #specify the temlate
    template_name = 'blog/blog_template.html'
    
    #define the context
    context_object_name = 'blog_list'




class BlogDetailView(DetailView):
    #specify which model (table from the Database) to use. The template will extract from the model what it needs to display
    model = BlogPost
    
    #specify the temlate
    template_name = 'blog/blogDetails_template.html'
    
    #define the context
    context_object_name = 'blog'

    
    # allows adding extra context variables beyond what DetailView provides by default.
    # (customises the context data passed to the template)
    def get_context_data(self, **kwargs):
        # call the parent class
        context = super().get_context_data(**kwargs)
        

        #add the tags to the blog
        context["tags"] = self.object.tags.all()
        context["date"] = self.kwargs["date"]
        return context
      
    
#use mixin
class BlogDetailView_withMixin(BlogMixin, DetailView):
    model = BlogPost
    template_name = 'blog/blogDetails_template.html'
    context_object_name = 'blog'
    #slug_url_kwarg = 'slug'  # This should match the URL pattern parameter


# to be used with: path("<slug:slug>/tags/", views.RecordTagView.as_view(), name='blogPost-tag'),  
# This needs to be placed above other urls starting is <slug:slug> 
class RecordTagView(SingleObjectMixin, View): #SingleObjectMixin helps retrieve a single object (a BlogPost in this case) based on the URL pattern.
    # Records the tags for the current blogPost.
    model = BlogPost

    def get(self, request, *args, **kwargs):

            # Look up the blogpost we're interested in (object matching the pk or slug in the URL.)
        self.object = self.get_object()
        
        # Actually record the tags somehow here!
        
        # Get the tags from the POST request
        #tags_input = request.POST.get("tags")  # Example: "main, starter"
        tags_input = "starter, vegetarian"
        if tags_input:
            # Convert comma-separated tags into a list
            tag_names = [tag.strip() for tag in tags_input.split(",")]

            # Create or get Tag objects
            tag_objects = [Tag.objects.get_or_create(tagName=tag)[0] for tag in tag_names]

            # Add tags to the BlogPost
            self.object.tags.add(*tag_objects)
        
        # Redirect after processing
        #return HttpResponseRedirect(reverse('blogPost-tag', kwargs={'slug': self.object.slug}))    
        return HttpResponseRedirect(reverse('blog_detail', kwargs={'slug': self.object.slug}))

   
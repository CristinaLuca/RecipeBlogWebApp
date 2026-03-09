class BlogMixin:
    #A mixin to add extra context to the blog view
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = f"You're reading: {self.object.postTitle}"
        return context

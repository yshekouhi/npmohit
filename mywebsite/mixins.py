from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs) 

class MultiSlugMixin(object):
    model = None
    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        modelClass = self.model
        if slug is not None:
            try:
                obj = get_object_or_404(modelClass, slug=slug)
            except modelClass.MultiObjectsReterned:
                obj = modelClass.objects.filter(slug=slug)
        else:
            obj = super(MultiSlugMixin, self).get_object(*args, **kwargs)
        
        return obj
    



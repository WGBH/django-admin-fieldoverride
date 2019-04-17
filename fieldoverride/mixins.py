from django.views.generic.detail import SingleObjectMixin

"""
We'll need a mixin to:
    - get all the override fields for a model instance
    - set the context with either the override content (if it exists), OR
    - the context from the parental fields (in order of precedence)
"""

class FieldOverrideMixin(SingleObjectMixin):
    
    def get_context_data(self, **kwargs):
        context = super(FieldOverrideMixin, self).get_context_data(**kwargs)
        
        # This is where the magic will happen.
        
        return context
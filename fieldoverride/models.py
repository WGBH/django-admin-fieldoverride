from django.db import models


class FieldOverride(models.Model):
    """
    What do we need here?
        - What field am I?
        - What field(s) am I overriding?
        - what is my field type
        - what is the override data?
    
    So:
        1. Use the map_override_fields method to define the set of fields
        2. Save the above four fields
        
    We'll also want a Mixin that sets context of the override fields.  Since we know the path of override,
    we can use the map_override_fields method to do that AS WELL!
    
    """
    # I need to know what my model is...?
    # So this will have to be some sort of generic foreign key...
    
    # This is one of the 'field' values in override_fields
    field_name = models.CharField (
        _('Field Name'),
        max_length = 100,
        # choices = somehow get the list of map_override_fields field values
    )
    override_value = models.TextField (
        _('Override Value'),
        null = True, blank = True
    )
    
    
    def map_override_fields(self):
        """
        This is where you create the structure of:
            1. Fields that can be overridden.
            
        FOR NOW assume that the set of fields come from the 1:1 relationships to the FieldOverride model.
        
        So I'm expecting something like:
        
        override_fields = [
            {'field': 'description', 'field_type': 'TextField',
                'overrides': ['fmp__description', 'pbsmm__description_long']},
        ]
        
        where overrides is the list of fields in order of precedence, highest to lowest.
        
        I'm assuming the x__y syntax will work because e.g., in the Admin you can use that for all of the
        admin's parameters, and in the model _meta for things like setting default ordering.
        """
        override_fields = {}
        return None
        

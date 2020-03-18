from django import template

register = template.Library()

# we will write a function now which will act as a custom template filter

def cut1(value,arg):
    """
    This cuts out all values of arg from the string

    """
    return value.replace(arg,'') # we just used the .replace method of python string

# now we need to register this filter
register.filter('cut1',cut1) # first arguement is the name and secon arguement is the actual function    
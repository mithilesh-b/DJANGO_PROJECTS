from django import template
register = template.Library()

@register.filter()
def low(value):
    return value.lower()

@register.filter(name="cut")   #giving custom name 
def replaceval(value,arg):
    return value.replace(arg, "")    #eg -> value = "m-i-t-h-i-l-e-s-h", arg = "-"  o/p = "mithilesh"

@register.filter()
def getvalbykey(d, key):
    key = str(key)
    return d.get(key)

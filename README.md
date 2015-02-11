# materialize-css-form
Materializecss for Django Form

A simple Django template tag to work with Materializecss



## Install

```
pip install materializedjangoform
```

Add to INSTALLED_APPS:

```    
INSTALLED_APPS = (
     'materializecssform',
     ...
     )
```

## Usage

Use it like this, simple.

{% load materializecss %}
{{ form|materializecss }}


## Demo

Checkout this Demo site to see it in action.


## Help

### Widget

- TextInput
- Textarea
- Select 
- Filefield
- DateField

### TODO
- Multiple select


## Inspired by

https://github.com/tzangms/django-bootstrap-form

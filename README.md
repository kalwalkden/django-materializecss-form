# materialize-css-form
Materializecss for Django Form

A simple Django template tag to work with [Materializecss](http://materializecss.com/)





## Install

```
pip install django-materializecss-form
```

[on pypi](https://pypi.python.org/pypi/django-materializecss-form)

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

### All the form 

{{ form|materializecss }}

### Individual field

{{ form.<field name>|materializecss }}


### Custom size (default is 's12')

{{ form|materializecss:'m6' }}



## Demo

![Basic form](https://cloud.githubusercontent.com/assets/3958123/6165004/a1984f52-b2a4-11e4-8ae2-078505991b0d.png)

![DatePicker](https://cloud.githubusercontent.com/assets/3958123/6165005/a19bf044-b2a4-11e4-9989-6a64f9c97087.png)


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

[django-bootstrap-form](https://github.com/tzangms/django-bootstrap-form)


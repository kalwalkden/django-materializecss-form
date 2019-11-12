[![PyPI version](https://badge.fury.io/py/django-materializecss-form.svg)](https://pypi.org/project/django-materializecss-form/)

# materialize-css-form
Materializecss for Django Form

A simple Django template tag to work with [Materializecss](http://materializecss.com/)

## Install

From [PyPi](https://pypi.org/project/django-materializecss-form/):

```
pip install  django-materializecss-form
```

From [GitHub](https://github.com/kalwalkden/django-materializecss-form)

Add module to INSTALLED_APPS:

```
INSTALLED_APPS = (
     'materializecssform',
     ...
     )
```

Add Materialize CSS to your project ([Official Documentation](https://materializecss.com/getting-started.html)):

In your base.html:

```
<head>

{% block css %}
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.1/css/materialize.min.css" integrity="sha256-qj3p6P1fJIV+Ndv7RW1ovZI2UhOuboj9GcODzcNFIN8=" crossorigin="anonymous" />
{% endblock css %}

</head>
```

```

<body >

{% block javascript %}
<script
  src="https://code.jquery.com/jquery-3.3.1.min.js"
  integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
  crossorigin="anonymous"></script>

<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.1/js/materialize.min.js" integrity="sha256-SrBfGi+Zp2LhAvy9M1bWOCXztRU9Ztztxmu5BcYPcPE=" crossorigin="anonymous"></script>

<script>
$(document).ready(function(){

  // Initialize materialize data picker
  $('.datepicker').datepicker({'format': 'yyyy-mm-dd'});
  $('select').formSelect();

});
</script>
{% endblock javascript %}

...

</body>
```

## Usage

Import the module simply like this:

```html
{% load materializecss %}
```

### Full form

Format a whole form:

```html
{{ form|materializecss }}
```

### Individual field

Format only a specific field:

```html
{{ form.<field name>|materializecss }}
```

### Custom size (default is 's12')

Apply custom sizes in grid ([see Materialize CSS documentation](https://materializecss.com/grid.html)):
```html
{{ form|materializecss:'m6' }}
{{ form|materializecss:'custom_size=m6' }}
```


### Icons support

This is most useful for adding a descriptive icon when you are creating a custom layout by building the form one field at a time. Substitue FIELD_NAME below with one of the field names from your form.

```html
{{ form.FIELD_NAME|materializecss:'s12 m6, icon=person' }}
{{ form.FIELD_NAME|materializecss:'custom_size=s12 m6, icon=person' }}
```

#### Optional icon sets

If you're using optional icon sets you need to set `MATERIALIZECSS_ICON_SET` in your settings file:

```python
MATERIALIZECSS_ICON_SET = 'fontawesome'
```

Currently [Font Awesome](https://www.fontawesome.com/) and [GLYPHICONS](https://www.glyphicons.com) is supported, however you might need to modify your CSS for full support.

### Note about `DateTimeField`
Input field is rendered as a *datetime-local* type, this lets the user easily enter both a date and a time. As this field requires ISO-8601 format, your main project settings need to include the ISO format in order for the form to interpret this field valid:
```
from django.conf.global_settings import DATETIME_INPUT_FORMATS

# ISO 8601 datetime format to accept html5 datetime input values
DATETIME_INPUT_FORMATS += ["%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M"]
```

## Demo

![Basic form](https://cloud.githubusercontent.com/assets/3958123/6165004/a1984f52-b2a4-11e4-8ae2-078505991b0d.png)

![DatePicker](https://cloud.githubusercontent.com/assets/3958123/6165005/a19bf044-b2a4-11e4-9989-6a64f9c97087.png)

![DateTimePicker](https://user-images.githubusercontent.com/556361/49763533-8a44f580-fc92-11e8-8d24-f45373becd11.png)

## Help

### Widget

- TextInput
- Textarea
- CheckboxInput
- RadioSelect
- Select
- SelectMultiple
- CheckboxSelectMultiple
- Filefield
- DateField
- DateTimeField

## Inspired by

[django-bootstrap-form](https://github.com/tzangms/django-bootstrap-form)

## Originally Built By

Florent CLAPIÉ ([PyPI](https://pypi.org/user/florent1933/))

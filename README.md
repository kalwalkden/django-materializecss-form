# materialize-css-form
Materializecss for Django Form

A simple Django template tag to work with [Materializecss](http://materializecss.com/)





## Install


```
pip install  django-materializecss-form

```



[on pypi](https://pypi.python.org/pypi/django-materializecss-form)
[on GitHub](https://github.com/kalwalkden/django-materializecss-form)

Add to INSTALLED_APPS:

```
INSTALLED_APPS = (
     'materializecssform',
     ...
     )
```

Add Materializecss to your project:

In your base.html:

```
<head>

{% block css %}
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

Use it like this, simple.

{% load materializecss %}

### All the form

{{ form|materializecss }}

### Individual field

{{ form.<<field name>> | materializecss }}


### Custom size (default is 's12')

{{ form|materializecss:'m6' }}



## Demo

![Basic form](https://cloud.githubusercontent.com/assets/3958123/6165004/a1984f52-b2a4-11e4-8ae2-078505991b0d.png)

![DatePicker](https://cloud.githubusercontent.com/assets/3958123/6165005/a19bf044-b2a4-11e4-9989-6a64f9c97087.png)


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
- DateTimeField (doesn't show time yet)



## Inspired by

[django-bootstrap-form](https://github.com/tzangms/django-bootstrap-form)

## Originally Built By

Florent CLAPIÉ

[https://pypi.org/user/florent1933/] https://pypi.org/user/florent1933/


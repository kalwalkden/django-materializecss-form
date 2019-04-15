from django import forms
from django.template.loader import get_template
from django import template
from django.forms.fields import DateTimeField, DateField
from django.http import QueryDict

from materializecssform import config

register = template.Library()

@register.filter
def materializecss(element, options={}):
    # Set default values if none of them are set
    label_cols = 's12'
    icon = ''

    if options:
        # Split options string into a list of arguments
        arguments = [arg.strip() for arg in options.split(',')]

        # Check the first argument to see if it's of form argument=value
        if '=' not in arguments[0]:
            # If not, it's a custom size, so use that
            label_cols = arguments[0]
            # Remove this from the arguments list
            arguments.pop(0)

        # Join the remaining arguments into a querystring for easy parsing
        options = '&'.join(arguments)
        qs = QueryDict(options)
        # Check to see if a custom size was passed in this fashion and if so prefer it
        if qs.get('custom_size'):
            label_cols = qs.get('custom_size')
        # Get icon if it's been set
        icon = qs.get('icon', default='')

    markup_classes = {'label': label_cols, 'value': '', 'single_value': '', 'icon': icon}
    return render(element, markup_classes)



def add_input_classes(field):
    if not is_checkbox(field) and not is_multiple_checkbox(field) and not is_radio(field) \
        and not is_file(field):
        field_classes = field.field.widget.attrs.get('class', '')
        if config.MATERIALIZECSS_VALIDATION:
            field_classes += ' validate'
        if field.errors:
            field_classes+= ' invalid'
        field.field.widget.attrs['class'] = field_classes


def render(element, markup_classes):
    element_type = element.__class__.__name__.lower()

    # Get the icon set setting
    icon_set = config.MATERIALIZECSS_ICON_SET

    if element_type == 'boundfield':
        add_input_classes(element)
        template = get_template("materializecssform/field.html")
        context = {'field': element, 'classes': markup_classes, 'icon_set': icon_set}
    else:
        has_management = getattr(element, 'management_form', None)
        if has_management:
            for form in element.forms:
                for field in form.visible_fields():
                    add_input_classes(field)

            template = get_template("materializecssform/formset.html")
            context = {'formset': element, 'classes': markup_classes, 'icon_set': icon_set}
        else:
            for field in element.visible_fields():
                add_input_classes(field)

            template = get_template("materializecssform/form.html")
            context = {'form': element, 'classes': markup_classes, 'icon_set': icon_set}

    return template.render(context)


@register.filter
def is_checkbox(field):
    return isinstance(field.field.widget, forms.CheckboxInput)

@register.filter
def is_textarea(field):
    return isinstance(field.field.widget, forms.Textarea)


@register.filter
def is_multiple_checkbox(field):
    return isinstance(field.field.widget, forms.CheckboxSelectMultiple)


@register.filter
def is_radio(field):
    return isinstance(field.field.widget, forms.RadioSelect)

@register.filter
def is_date_input(field):
    return isinstance(field.field, DateField)

@register.filter
def is_datetime_input(field):
    return isinstance(field.field, DateTimeField)


@register.filter
def is_file(field):
    return isinstance(field.field.widget, forms.FileInput)


@register.filter
def is_select(field):
    return isinstance(field.field.widget, forms.Select)


@register.filter
def is_select_multiple(field):
    return isinstance(field.field.widget, forms.SelectMultiple)

from django import forms
from django.template.loader import get_template
from django import template
from django.forms.fields import DateTimeField, DateField

from materializecssform import config

register = template.Library()

@register.filter
def materializecss(element, label_cols={}):
    if not label_cols:
        label_cols = 's12'

    markup_classes = {'label': label_cols, 'value': '', 'single_value': ''}
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

    if element_type == 'boundfield':
        add_input_classes(element)
        template = get_template("materializecssform/field.html")
        context = {'field': element, 'classes': markup_classes}
    else:
        has_management = getattr(element, 'management_form', None)
        if has_management:
            for form in element.forms:
                for field in form.visible_fields():
                    add_input_classes(field)

            template = get_template("materializecssform/formset.html")
            context = {'formset': element, 'classes': markup_classes}
        else:
            for field in element.visible_fields():
                add_input_classes(field)

            template = get_template("materializecssform/form.html")
            context = {'form': element, 'classes': markup_classes}

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

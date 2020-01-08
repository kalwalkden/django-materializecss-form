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


def _add_input_classes_widget(widget, field_errors):
    if _is_multi_widget(widget):
        for subwidget in widget.widgets:
            _add_input_classes_widget(subwidget, field_errors)
    elif not _is_checkbox_widget(widget) and not _is_multiple_checkbox_widget(widget) \
            and not _is_radio_widget(widget) and not _is_file_widget(widget):
        classes = widget.attrs.get('class', '')
        if config.MATERIALIZECSS_VALIDATION:
            classes += ' validate'
        if field_errors:
            classes += ' invalid'
        widget.attrs['class'] = classes


def add_input_classes(field):
    _add_input_classes_widget(field.field.widget, field.errors)


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


def _is_checkbox_widget(widget):
    return isinstance(widget, forms.CheckboxInput)


def _is_multiple_checkbox_widget(widget):
    return isinstance(widget, forms.CheckboxSelectMultiple)


def _is_radio_widget(widget):
    return isinstance(widget, forms.RadioSelect)


def _is_file_widget(widget):
    return isinstance(widget, forms.FileInput)


def _is_multi_widget(widget):
    return isinstance(widget, forms.MultiWidget)


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

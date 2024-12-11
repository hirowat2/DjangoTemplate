from django.db import models

def create_dynamic_model(name, fields):
    class Meta:
        app_label = 'formula'

    attrs = {'__module__': __name__, 'Meta': Meta}
    for field_name, field_type in fields.items():
        attrs[field_name] = field_type

    return type(name, (models.Model,), attrs)

# Criando um modelo dinâmico
fields = {
    'name': models.CharField(max_length=100),
    'value': models.FloatField(),
}

DynamicVariable = create_dynamic_model('DynamicVariable', fields)

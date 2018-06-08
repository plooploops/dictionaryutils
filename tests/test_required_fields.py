from dictionaryutils import dictionary


# Windmill required fields
def test_required_data_fields():
    required_fields = [
        'data_type', 'data_format', 'data_category', 'object_id']
    for schema in dictionary.schema.values():
        if schema['category'].endswith('_file'):
            for field in required_fields:
                assert field in schema['properties'], \
                    '{} is required but not in {}'.format(field, schema['id'])


# Peregrine required fields
def test_required_project_fields():
    required_field = 'availability_type'
    schema = dictionary.schema['project']
    assert required_field in schema['properties'], \
        '{} is required for project'.format(required_field)

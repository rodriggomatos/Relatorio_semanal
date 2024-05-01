

class ProjectStatusManager:
    def __init__(self, columns, tasks):
        self.columns = columns
        self.tasks = tasks
        self.project_status = {}

    def get_project_status(self, task):
        project_status = {}
        fields_map = {field['name']: field for field in task.get('custom_fields', [])}
        for column_name in self.columns:
            custom_field = fields_map.get(column_name)
            if custom_field:
                value = None
                if custom_field.get('resource_subtype') == 'enum' and custom_field.get('enum_value'):
                    value = custom_field['enum_value']['name']
                elif custom_field.get('resource_subtype') == 'text':
                    value = custom_field.get('text_value', None)
                elif custom_field.get('type') == 'date':
                    date_value = custom_field.get('date_value')
                    value = date_value.get('date', None)
                if(value is not None):
                    project_status[column_name] = value
                    
        return project_status   
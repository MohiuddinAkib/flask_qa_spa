from flask_admin.contrib.sqla import ModelView


class UserVIew(ModelView):
    create_modal = True
    edit_modal = True
    can_view_details = True
    column_filters = ['name']
    column_searchable_list = ['name']
    column_exclude_list = ['password', ]
    column_editable_list = ['admin', 'expert']

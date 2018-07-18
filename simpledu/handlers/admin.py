from flask import Blueprint, render_template 

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/admin')
def admin_index():
    return 'admin'

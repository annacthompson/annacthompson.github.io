import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

# use option - shift - f to format html

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')

env = Environment( loader = FileSystemLoader(templates_dir))

for template_filename in env.list_templates('.html.jinja') :
    if template_filename[0] == '_' :
        continue

    template = env.get_template(template_filename)

    html_filename = template_filename.split('.')[0] + '.html'
    html_path = os.path.join(root, html_filename)
    dirname = os.path.dirname(html_path)
    if dirname != '' :
        os.makedirs(dirname, exist_ok=True)
    

    with open(html_path, 'w') as html_file:
        print('writing', html_path)
        html_file.write(template.render(
            global_template_variable='hi'
        ))

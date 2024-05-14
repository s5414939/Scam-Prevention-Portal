from jinja2 import Environment, FileSystemLoader
import os

# Set up the Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

# List of templates to render
templates = [
    'home.html',
    'scenarios.html',
    'overview.html',
    'contact.html',
    'ai.html',
    'videosection.html',
    'feedback.html',
]

# Render each template and save to the root directory
for template_name in templates:
    template = env.get_template(template_name)
    output_from_parsed_template = template.render()

    # Save the rendered template to a file
    with open(template_name, "w") as fh:
        fh.write(output_from_parsed_template)

from jinja2 import Environment, FileSystemLoader
import os

# Set up the environment
env = Environment(loader=FileSystemLoader('templates'))

# Render home.html
template = env.get_template('home.html')
output_from_parsed_template = template.render()

# Save the rendered template to a file
with open("home.html", "w") as fh:
    fh.write(output_from_parsed_template)

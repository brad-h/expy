"""Website Generator"""

import os

def _html_template(site_name, author, js_snippet, css_snippet):
    """Create a HTML Template given a site name,
    author, snippet to include JS files and CSS files
    """
    template_data = {
        'site_name': site_name,
        'author': author,
        'js': js_snippet,
        'css': css_snippet
    }
    with open('module43.template') as filehandle:
        template = filehandle.read()
    return template.format_map(template_data)

def ex43():
    """Prompt for site name, author and file types
    Create boilerplate project template
    """
    site = input('Site name: ')
    os.makedirs(site, exist_ok=True)
    author = input('Author: ')
    has_js = input('Do you want a folder for JavaScript? ').lower() == 'y'
    has_css = input('Do you want a folder for CSS? ').lower() == 'y'

    css_snippet = '<link rel="stylesheet" type="text/css" media="screen" href="main.css" />'
    js_snippet = '<script src="main.js"></script>'

    css_snippet = css_snippet if has_css else ''
    js_snippet = js_snippet if has_js else ''

    html = _html_template(site, author, js_snippet, css_snippet)
    with open(os.path.join(site, 'index.html'), 'w') as htmlhandle:
        htmlhandle.write(html)

    if has_js:
        os.makedirs(os.path.join(site, 'js'))
    if has_css:
        os.makedirs(os.path.join(site, 'css'))

if __name__ == '__main__':
    ex43()

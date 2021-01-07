import markdown2

TITLE_HTML = """
<div class="section">
    <div class="container container-single">
        <h1>{0} <a href="{1}" target="_blank"><img class="project-icon-link" src="{{{{ url_for('static', filename='{2}') }}}}" height="30" /></a></h1> 
    </div>
</div>
"""
TITLE_NO_LINK_HTML = """
<div class="section">
    <div class="container container-single">
        <h1>{0}</h1> 
    </div>
</div>
"""

DESC_HTML = """
<div class="section">
    <div class="container container-single">
        <p>{0}</p>
    </div>
</div>
"""

CONTENT_HTML = """

"""

def render_project_page(data):
    title, desc, content = list(map(lambda x: x.split("\n\n+++\n\n"), data.split("\n\n---\n\n")))
    html = ["{% extends \"base.html\" %}\n\n{% block content %}\n"]

    if len(title) == 1: # no github link
        html.append(TITLE_NO_LINK_HTML.format(title[0]))
    elif len(title) == 2:
        html.append(TITLE_HTML.format(title[0], *(title[1].split(" "))))

    html.append(DESC_HTML.format(desc[0]))

    pass
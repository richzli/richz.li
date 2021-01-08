import markdown2, re

TITLE_HTML = """
<div class="section">
    <div class="container container-single">
        <h1>{0} {1}</h1> 
    </div>
</div>
"""
ICON_LINK_HTML = """
<a href="{0}" target="_blank"><img class="project-icon-link" src="{{{{ url_for('static', filename='{1}') }}}}" height="30" /></a>
"""

CONTENT_HTML = """
<div class="section">
    <div class="container container-double">
        <div class="column">
            <div class="column-container">
                {0}
            </div>
        </div>
        <div class="column">
            <div class="column-container">
                {1}
            </div>
        </div>
    </div>
</div>
"""
IMAGE_HTML = """
<img class="project-img {1}" src="{{{{ url_for('static', filename='{0}') }}}}" />
"""
SINGLE_COLUMN_HTML = """
<div class="section">
    <div class="container container-single">
        <div class="column-container">
            {0}
        </div>
    </div>
</div>
"""

def format_text(s):
    return "<br>\n\n".join(markdown2.markdown(s, extras=["target-blank-links"]).split("\n\n"))

def render_project_page(data):
    title, *content = list(map(lambda x: re.split(r"\r?\n\r?\n\+\+\+\r?\n\r?\n", x), re.split(r"\r?\n\r?\n---\r?\n\r?\n", data)))
    html = ["{% extends \"base.html\" %}\n\n{% block content %}\n"]

    if len(title) == 1: # no github link
        html.append(TITLE_HTML.format(title[0], ""))
    elif len(title) == 2:
        html.append(TITLE_HTML.format(title[0], " ".join(map(lambda x: ICON_LINK_HTML.format(*x.split(" ")), title[1].splitlines()))))

    for i in range(len(content)):
        if len(content[i]) == 2:
            c_text, c_imgs = content[i]
            text = format_text(c_text)
            imgs = "".join(map(lambda x: IMAGE_HTML.format(*x.split(" ")), c_imgs.splitlines()))
            if i % 2:
                html.append(CONTENT_HTML.format(text, imgs))
            else:
                html.append(CONTENT_HTML.format(imgs, text))
        elif len(content[i]) == 1:
            if content[i][0].startswith("+ "):
                img = IMAGE_HTML.format(*content[i][0][2:].split(" "))
                html.append(SINGLE_COLUMN_HTML.format(img))
            else:
                html.append(SINGLE_COLUMN_HTML.format(format_text(content[i][0])))
    
    html.append("{% endblock %}")
    return "".join(html)
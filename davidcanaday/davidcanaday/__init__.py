from flask import Flask, render_template, send_file
import json

app = Flask(__name__)
pages = json.load(open('davidcanaday/davidcanaday/pages.json', 'r'))
widgetpages = pages['widget']
blogpages = pages['blog']


def renderPanelPage(name):
    return render_template('panel.html', image=pages[name]['image'], imagename=pages[name]['imagename'],
                           header1=pages[name]['header1'], text1=pages[name]['text1'], purl=pages[name]['purl'],
                           ptext=pages[name]['ptext'], wName=name)


def renderItem(ptype, name):
    pDict = {'widgets': widgetpages, 'blog': blogpages}[ptype]
    return render_template('embed.html', header1=pDict[name]['header1'], text1=pDict[name]['text1'],
                           itemUrl=f'/static/tiles/{ptype}/{name}/index.html')


@app.route('/')
def home():
    return renderPanelPage('/')


@app.route('/<string:page_name>/')
def blog(page_name):
    pn = f'/{page_name}'
    if pn in pages:
        return renderPanelPage(pn)


@app.route('/blog/<string:blog_id>/')
def blogPage(blog_id):
    return renderItem("blog", blog_id)


@app.route('/widgets/<string:widget_id>/')
def widgetPage(widget_id):
    return renderItem("widgets", widget_id)


if __name__ == '__main__':
    app.run()

def index():
    with open('pages/index.html') as template:
        return template.read()

def pink():
    with open('pages/pink.html') as template:
        return template.read()


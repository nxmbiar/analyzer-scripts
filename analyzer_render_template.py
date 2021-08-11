from jinja2 import Environment, FileSystemLoader
from os import path
from json import loads
import sys

file_loader = FileSystemLoader(path.join(path.dirname(__file__),'templates'))
env = Environment(loader=file_loader)

template = env.get_template('ANALYZER_ISSUE_TEMPLATE.md')

with open(path.join(sys.argv[1],'.github','test.json')) as f:
    issues = loads(f.read())
# issues = loads(sys.argv[1])

output = template.render(issues=issues)

with open(path.join(path.dirname(__file__),'ISSUE.md'),'w', encoding='utf-8') as f:
    f.write(output)

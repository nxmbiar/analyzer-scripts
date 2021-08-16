from jinja2 import Environment, FileSystemLoader
from os import path
from json import loads
import sys

file_loader = FileSystemLoader(path.join(path.dirname(__file__),'templates'))
env = Environment(loader=file_loader)

template = env.get_template('ANALYZER_ISSUE_TEMPLATE.md')

with open(path.join(sys.argv[1],'.github','failed_issues.json')) as f:
    issues = loads(f.read())
with open(path.join(sys.argv[1],'.github','successes.json')) as f:
    successes = loads(f.read())
with open(path.join(sys.argv[1],'.github','warnings.json')) as f:
    warnings = loads(f.read())
with open(path.join(sys.argv[1],'.github','wf.json')) as f:
    wfs = loads(f.read()[:-1])
# issues = loads(sys.argv[1])

print(issues)
print(wfs)
# wfs = []
# wfs.extend(issues.keys())
# wfs.extend(warnings.keys())
# wfs.extend(successes.keys())

no_issues = True
for wf in wfs:
    try:
        if len(issues[wf]) != 0 or len(warnings[wf]) != 0:
            no_issues = False
            break
    except KeyError:
        continue

print(f'::set-output name=no_issues::${no_issues}')
# print(wfs)
output = template.render(issues=issues, warnings=warnings, successes=successes, wfs=wfs, hash=sys.argv[2])

with open(path.join(path.dirname(__file__),'ISSUE.md'),'w', encoding="utf-8") as f:
    f.write(output)

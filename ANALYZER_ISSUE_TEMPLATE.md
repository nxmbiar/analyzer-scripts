---
title: Auto-Generated Issue By Analyzer Workflow
labels: bug
---

## The following errors were analyzed in the last commit

{% for key, value in failed_issues.items() %}
{% for issue in value %}
- [ ] In [{{ key.split('_')[0] }}]( /{{ key }} ) - {{ issue['title'] }} - {{ issue['description'] }} - {{ issue['moreInfo']}}
{% endfor %}
{% endfor %}


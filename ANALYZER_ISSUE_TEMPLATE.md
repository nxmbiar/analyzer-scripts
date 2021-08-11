## The following errors were analyzed in the last commit

{% for key, value in issues.items() %}
{% for issue in value %}
- [ ] In {{ key }} - {{ issue['title'] }} - {{ issue['description'] }} - {{ issue['moreInfo']}}
{% endfor %}
{% endfor %}

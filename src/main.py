from helper import JiraHelper
from auth import user_name, api_token, server
from fields import issue_fields

jira = JiraHelper(user_name, api_token, server)

# Creating Test in Jira
issue_key = jira.create_issue(issue_fields)

# Updating Issue Fields in Jira
jira.update_issue_fields(issue_key, issue_fields)

#To get an issue in Jira
issue = jira.get_issue(issue_key)
print(issue.fields.summary)

# Deleting Issue in Jira
jira.delete_issue(issue_key)

# jira.create_issues_from_file('jira/test-jira.xlsx')

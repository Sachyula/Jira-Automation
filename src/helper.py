from jira import JIRA
from jira.exceptions import JIRAError
import xlrd

class JiraHelper:

    def __init__(self, user_name, api_token,  server):
        try:
            self.jira = JIRA(basic_auth=(user_name, api_token), options={"server": server})
        except JIRAError as e:
            if e.status_code == 401:
                print ("Login to JIRA failed. Check your username and api token")

    def create_issue(self, issue_fields):
        issue_key = self.jira.create_issue(fields=issue_fields)
        return issue_key

    def update_issue_fields(self, issue_key, updated_issue_fields):
        issue = self.jira.issue(issue_key)
        issue.update(fields=updated_issue_fields)

    def delete_issue(self, issue_key):
        issue = self.jira.issue(issue_key)
        issue.delete()

    def get_issue(self, issue_key):
        issue = self.jira.issue(issue_key)
        return issue

    def create_issues_from_file(self, file_path):
        issues_list = []
        book = xlrd.open_workbook(file_path)
        sh1 = book.sheet_by_index(0)
        for rw in range(1, sh1.nrows):
            issue = {}
            for col in range(0, sh1.ncols):
                issue[sh1.cell(0,col).value] = sh1.cell(rw,col).value
            issues_list.append(issue)
        
        for issue_fields in issues_in_file:
            issue_key = self.create_issue(issue_fields)
            print("Issue {} has been successfully created!".format(issue_key))

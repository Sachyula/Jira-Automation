from jira import JIRA, JIRAError
import xlrd, json

class JiraHelper:

    def __init__(self, user_name, api_token,  server):
        try:
            self.jira = JIRA(basic_auth=(user_name, api_token), options={"server": server})
        except JIRAError as e:
            if e.status_code == 401:
                print ("Login to JIRA failed. Check your username and api token.")
            else:
                print ("Login to JIRA failed.", e.text)
        else:
            print("Successfully logged in!")

    def create_issue(self, issue_fields):
        try:
            issue_key = self.jira.create_issue(fields=issue_fields)
        except JIRAError as e:
            print("Oops! Unable to create ticket. ", e.text)
        else:
            print("Issue {} has been created successfully!".format(issue_key))
            return issue_key

    def update_issue_fields(self, issue_key, updated_issue_fields):
        try:
            issue = self.jira.issue(issue_key)
            issue.update(fields=updated_issue_fields)
        except JIRAError as e:
            print("Oops! Unable to update ticket. ", e.text)
        else:
            print("Issue {} has been updated successfully!".format(issue_key))

    def delete_issue(self, issue_key):
        try:
            issue = self.jira.issue(issue_key)
            issue.delete()
        except JIRAError as e:
            print("Oops! Unable to delete ticket. ", e.text)
        else:
            print("Successfully deleted issue, {}.".format(issue_key))

    def get_issue(self, issue_key):
        try:
            issue = self.jira.issue(issue_key)
        except JIRAError as e:
            print("Oops! could'nt find issue.", e.text)
        else:
            return issue

    def __get_dict_from_string(self, value):
        res = {}
        try:
            res = json.loads(value)
        except ValueError as e:
            print("Error in Excel Data")
        return res

    def create_issues_from_file(self, file_path):
        issues_list = []
        book = xlrd.open_workbook(file_path)
        sh1 = book.sheet_by_index(0)
        for rw in range(1, sh1.nrows):
            issue = {}
            for col in range(0, sh1.ncols):
                if(u'\xa0' in sh1.cell(rw,col).value):
                    issue[sh1.cell(0,col).value] = sh1.cell(rw,col).value.replace('\xa0', '')
                if('{' in sh1.cell(rw,col).value):
                    issue[sh1.cell(0,col).value] = self.__get_dict_from_string(sh1.cell(rw,col).value)
                else:
                    issue[sh1.cell(0,col).value] = sh1.cell(rw,col).value
            issues_list.append(issue)
        
        for i in range (0, len(issues_list)):
            print(i+1,"\b) ", end="")
            self.create_issue(issues_list[i])


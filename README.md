# Jira-Automation
A program to create issues, update issue fields and delete issues from Jira using jira-python library.

---

### Setting up project in local

- Prerequisites
    1) python 3.5 and above
    2) pip

- To install the jira library run,
    > pip install jira

- Setup api token
    - Need to create an api token to access the JIRA board.
    - Go to [token manager](https://id.atlassian.com/manage-profile/security/api-tokens), to create an api token.


### How to Use?

- Add user name, api token, server details in auth.py file
- add ticket details in fields.py file
- Run main.py to create/update/delete a ticket


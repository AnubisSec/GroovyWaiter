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


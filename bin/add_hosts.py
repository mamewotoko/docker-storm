#! /usr/bin/env python

import sys, subprocess

# add sudo config?
PROJECT_NAME = "storm"

def exec_process(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    stdout = stdout.rstrip()
    return stdout

n_supervisor = int(sys.argv[1])
hosts_str = "\n"

for i in range(1, n_supervisor+1):
    name = PROJECT_NAME+"_supervisor_" + str(i)
    id_command = ["docker", "ps", "-f", "name="+name, "--format", "{{.ID}}" ]
    address_command = ["docker", "inspect", "--format", "{{.NetworkSettings.IPAddress}}", name]
    idstr = exec_process(id_command)
    address = exec_process(address_command)

    hosts_str += " ".join([address, idstr, name])

for i in range(1, n_supervisor+1):
    name = PROJECT_NAME+"_supervisor_" + str(i)

    cmd = ["docker", "exec", name, "bash", "-c", "cat - >> /etc/hosts"]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    p.communicate(hosts_str)

    

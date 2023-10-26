## nmap-tool

nmap-tool is a wrapper around nmap. It takes original nmap commands as parameters and processes the output into csv and JSON format. The intended use of the tool is for easier and proper data analysis of nmap results.

## Commands to run for local-IoT project.

### (1) default (most common) protocol and port combinations

`sudo python3 nmap_scan.py -a "nmap -sS -sU -p T:1-1024,U:1-1024 -sV -T4 -sO 192.168.4.0/24"`

```
-sS: Performs a SYN scan (stealth scan) for TCP services.
-sU: Performs a UDP scan for UDP services.
-p T:1-1024,U:1-1024: Specifies the port range for both TCP (T) and UDP (U) protocols. Scans ports from 1 to 1024, which covers most of the well-known ports and services.
-sV: Probes open ports to determine the service version information.
-T4: Sets the timing template to "aggressive" for faster scanning (adjust this to a higher or lower number to control the scan speed).
-v: Increases verbosity, so you can see more information about the scan progress.
--open: Shows only open ports in the results.
-sO: Performs an IP protocol scan, which detects which IP protocols (e.g., ICMP, IGMP, etc.) are supported by the target hosts.
192.168.4.0/24: Specifies the target IP range (replace this with the appropriate IP range for the network you're scanning).
```

### (2) brute-force all possible protocols on an open port

We use Nmap scripting engine (NSE) with a script called banner-plus. This script allows you to identify services running on non-standard ports by attempting to match the response from the server to known protocol banners.

e.g., `nmap -p [port_number] --script banner-plus [target_ip]`

### (3) scan for all available services in a network, considering both TCP,  UDP and IP protocols

`sudo python3 nmap_scan.py -a "nmap -p 1-65535 -sS -sU -sO -sV -T4 --reason 192.168.4.0/24"`

Breakdown:

```
-p 1-65535: Scans all ports from 1 to 65535.
-sS: Performs a SYN scan (stealth scan) for TCP services.
-sU: Performs a UDP scan for UDP services.
-sV: Probes open ports to determine the service version information.
-T4: Sets the timing template to "aggressive" for faster scanning (adjust this to a higher or lower number to control the scan speed).
-v: Increases verbosity, so you can see more information about the scan progress.
--reason: Displays the reason why a port is set to a specific state.
--open: Shows only open ports in the results.
192.168.4.0/24: Specifies the target IP range (replace this with the appropriate IP range for the network you're scanning).
```

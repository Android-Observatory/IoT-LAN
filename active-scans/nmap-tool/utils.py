from nmap_tool import Tool
import xmltodict
import csv
import io
import json
import re

def sanitize_filename(filename):
    # Replace invalid characters with an underscore
    return re.sub(r'[\\/:"*?<>|]+', '_', filename)

def dicttocsv(out_dict, csv_writer):
    scanner = out_dict['nmaprun']['@scanner']
    args = out_dict['nmaprun']['@args']
    start_time = out_dict['nmaprun']['@start']
    start_time_str = out_dict['nmaprun']['@startstr']
    version = out_dict['nmaprun']['@version']
    xmloutputversion = out_dict['nmaprun']['@xmloutputversion']
    verbose = out_dict['nmaprun']['verbose']['@level']
    hosts_up = out_dict['nmaprun']['runstats']['hosts']['@up'],
    hosts_down = out_dict['nmaprun']['runstats']['hosts']['@down'],
    hosts_total = out_dict['nmaprun']['runstats']['hosts']['@total']

    hosts = out_dict['nmaprun']['host']
    if not isinstance(hosts, list):
        hosts = [hosts]
    for host in hosts:
        address = host['address']
        ip_addr = ''
        mac_addr = ''
        vendor = ''
        if isinstance(address, list):
            for addr_item in address:
                if addr_item['@addrtype'] == 'ipv4':
                    ip_addr = addr_item['@addr']
                elif addr_item['@addrtype'] == 'mac':
                    mac_addr = addr_item['@addr']
                    vendor = addr_item.get('@vendor', '')
        else:
            ip_addr = address['@addr']


        ports_data = host.get('ports', {})
        if 'port' in ports_data:
            ports = ports_data['port']
            if not isinstance(ports, list):
                ports = [ports]

            for port in ports:
                protocol = port['@protocol']
                port_id = port['@portid']
                state = port['state']['@state']
                reason = port['state']['@reason']
                service = 'unknown'
                service_version = 'unknown'
                if 'service' in port:
                    service = port['service']['@name']
                    if '@product' in port['service']:
                        service_version = port['service']['@product'] + ' ' + port['service'].get('@version', 'unknown')

                row = {
                    'scanner': scanner,
                    'args': args,
                    'start_time': start_time,
                    'start_time_str': start_time_str,
                    'version': version,
                    'xmloutputversion': xmloutputversion,
                    'verbose': verbose,
                    'hosts_up': hosts_up,
                    'hosts_down': hosts_down,
                    'hosts_total': hosts_total,
                    'ip_addr': ip_addr,
                    'mac_addr': mac_addr,
                    'vendor': vendor,
                    'protocol': protocol,
                    'port_id': port_id,
                    'state': state,
                    'reason': reason,
                    'service': service,
                    'service_version': service_version,
                }
                csv_writer.writerow(row)


class Nmap(Tool):
    """
    Nmap tool execution class.
    """

    def __init__(self, path="nmap", default_args="-oX -"):
        """
        Initialize the Nmap Tool object

        Args:
            path(str): The full path (or the name) of nmap. Default
                is "nmap"
            default_args(str): Any default args that should always be
                part of the nmap arguments. Default is xml output argument
                "-oX -".
        """
        super().__init__(path, default_args=default_args)

    def run_xmltodict_output(self, args, timeout=None, csv_file=None):
        """
        Run the command as a child with the specified arguments
        and return the output as a dict along with the error if any.
        The xml to dict format is generated by xmltodict package which
        is based on the format specified here -
        https://www.xml.com/pub/a/2006/05/31/converting-between-xml-and-json.html

        Args:
            args(str): The arguments to be supplied to nmap.
            timeout(int): The timeout in seconds while waiting
                for the output. Default is None. For details check
                subprocess.Popen() timeout argument.
        Returns:
            tuple of dict,str: Tuple of xml output converted to dict
                and error converted from bytes to str.
                (stdout,stderr)
        """
        out, err = self.run(args, timeout=timeout)
        err = err.decode() if err else None
        if not out:
            if not err:
                err = "No output received from nmap"
        else:
            out_dict = xmltodict.parse(out, dict_constructor=dict)

            if csv_file:
                dump_filename = 'dict_dump_' + sanitize_filename(csv_file.split('.csv')[0]) + '.json'
                with open(dump_filename, 'w') as fp:
                    fp.write(json.dumps(out_dict))

                with open(sanitize_filename(csv_file), mode='w') as f:
                    writer = csv.DictWriter(f, fieldnames=['scanner', 'args', 'start_time', 'start_time_str', 'version', 'xmloutputversion', 'verbose', 'hosts_up', 'hosts_down', 'hosts_total', 'ip_addr', 'mac_addr', 'vendor', 'protocol', 'port_id', 'state', 'reason', 'service', 'version'])
                    writer.writeheader()
                    dicttocsv(out_dict, writer)

            return (out_dict, err)
        return (None, err)

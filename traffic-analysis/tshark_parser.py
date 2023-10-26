import csv
import sys
import os
from subprocess import Popen, PIPE

pcap_file = sys.argv[1]
print(pcap_file)
out_file = sys.argv[2]
feature_header = ['trans_protocol', 'stream_id', 'src ip', 'dst ip', 'src port', 'dst port', 'Protocol']
# TCP: 
p1 = Popen(["tshark", "-r", pcap_file, "-T", "fields", "-e", "tcp.stream"], stdout=PIPE)
p2 = Popen(["sort", "-n"], stdin=p1.stdout, stdout=PIPE)
p3 = Popen(["uniq"], stdin=p2.stdout, stdout=PIPE)
# Get the output
output = p3.communicate()[0].decode('utf-8').strip()
for stream_id in filter(None, output.split('\n')):
    # print(stream_id)
    
    command = ["tshark", "-r", pcap_file, 
                "-Y", 'tcp.stream==%s' % stream_id,
                "-Tfields",
                "-e", "_ws.col.Protocol",
                "-e", "ip.src",
                "-e", "ip.dst",
                "-e", "tcp.srcport",
                # "-e", "udp.srcport",
                "-e", "tcp.dstport",
                # "-e", "udp.dstport"
                ] 
    result = []
    process = Popen(command, stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()
    if err:
        print("Error reading file: '{}'".format(err.decode('utf-8')))
    count = 0 
    ip_src = 0
    cur_protocol = set()
    for packet in filter(None, out.decode('utf-8').split('\n')):
        packet = packet.split()
        if len(packet) < 5:  # Check if all fields are present
            continue  # Skip the packet if fields are incomplete
        cur_protocol.add(packet[0])
        if count == 0:
            count += 1
            ip_src = packet[1]
            ip_dst = packet[2]
            srcport = packet[3]
            dstport = packet[4]
    if ip_src ==0:
        print('Empty stream: ',stream_id)
        continue
    with open(out_file, 'a+', newline='') as f:
        writer = csv.writer(f)
        if f.tell() == 0:  # Check if the file is empty and write the header
            writer.writerow(feature_header)
        writer.writerow(['TCP', stream_id, ip_src, ip_dst, srcport, dstport, ';'.join(cur_protocol)])


# UDP: 
p1 = Popen(["tshark", "-r", pcap_file, "-T", "fields", "-e", "udp.stream"], stdout=PIPE)
p2 = Popen(["sort", "-n"], stdin=p1.stdout, stdout=PIPE)
p3 = Popen(["uniq"], stdin=p2.stdout, stdout=PIPE)
# Get the output
output = p3.communicate()[0].decode('utf-8').strip()
for stream_id in filter(None, output.split('\n')):
    # print(stream_id)
    
    command = ["tshark", "-r", pcap_file, 
                "-Y", 'udp.stream==%s' % stream_id,
                "-Tfields",
                "-e", "_ws.col.Protocol",
                "-e", "ip.src",
                "-e", "ip.dst",
                "-e", "udp.srcport",
                # "-e", "udp.srcport",
                "-e", "udp.dstport",
                # "-e", "udp.dstport"
                ] 
    result = []
    process = Popen(command, stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()
    if err:
        print("Error reading file: '{}'".format(err.decode('utf-8')))
    
    count = 0 
    ip_src = 0
    cur_protocol = set()
    for packet in filter(None, out.decode('utf-8').split('\n')):
        packet = packet.split()
        if len(packet) < 5:  # Check if all fields are present
            continue  # Skip the packet if fields are incomplete
        cur_protocol.add(packet[0])
        if count == 0:
            count += 1
            ip_src = packet[1]
            ip_dst = packet[2]
            srcport = packet[3]
            dstport = packet[4]

    if ip_src ==0:
        print('Empty stream: ',stream_id)
        continue
    with open(out_file, 'a+', newline='') as f:
        writer = csv.writer(f)
        if f.tell() == 0:  # Check if the file is empty and write the header
            writer.writerow(feature_header)
        writer.writerow(['UDP', stream_id, ip_src, ip_dst, srcport, dstport, ';'.join(cur_protocol)])

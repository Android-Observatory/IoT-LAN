## Traffic classifier

**Step 1:** Process pcap to produce intermediary nDPI results: `sh  parse_via_ndpi.sh`

The script **parse_via_ndpi.sh** is the reference point for this. It takes an input directory with pcaps. This script specifically expects the following structure:

```
|<Input directory>
|-- xiaomi-induction
|   |-- 2022-12-23_15.18.39_192.168.10.222.pcap
|   |-- 2022-12-24_15.18.40_192.168.10.222.pcap
|   |-- 2022-12-25_15.18.40_192.168.10.222.pcap
|   |-- 2022-12-26_15.18.40_192.168.10.222.pcap
|   |-- 2022-12-27_15.18.41_192.168.10.222.pcap
|   `-- 2022-12-28_15.18.41_192.168.10.222.pcap
|-- xiaomi-ricecooker
|   |-- 2022-12-23_18.12.12_192.168.10.197.pcap
|   |-- 2022-12-24_18.12.12_192.168.10.197.pcap
|   |-- 2022-12-25_18.12.18_192.168.10.197.pcap
|   |-- 2022-12-26_18.12.19_192.168.10.197.pcap
|   |-- 2022-12-27_18.12.33_192.168.10.197.pcap
|   `-- 2022-12-28_18.12.56_192.168.10.197.pcap
```

Then, produces a final directory with the CSV and JSON files with traffic flows classified by nDPI. You will need to set the `source_dir="" and final_dir=""` in the bash script. 


Similar script exists for tshark and bro/zeek

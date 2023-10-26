#!/bin/bash

# Set the source directory
source_dir="/home/aniketh/devel/src/IoT-local/dataset/nmap-dataset-local"

# Set the final directory
final_dir="/home/aniketh/devel/src/IoT-local/parsed_nmap_traffic"

# Loop through each subdirectory in the source directory
for dir in "$source_dir"/*; do
  # Check if the current item is a directory
  if [ -d "$dir" ] && [ -n "$(find "$dir" -maxdepth 1 -name '*.pcap' -print -quit)" ]; then
    # Get the directory name
    dir_name="$(basename "$dir")"

    # Loop through each pcap file in the directory
    for pcap_file in "$dir"/*.pcap; do
      # Get the filename without extension
      pcap_name="$(basename "$pcap_file" .pcap)"

      # Run the ndpiReader C binary on the pcap file and save the output to a CSV file
      csv_file="$final_dir/$dir_name-$pcap_name.csv"
      json_file="$final_dir/$dir_name-$pcap_name.json"
      log_file="$final_dir/$dir_name-$pcap_name-ndpiReader_stdout.log"
      ./ndpiReader -i "$pcap_file" -D -P 4:8:10:128:25 -C "$csv_file" -k "$json_file" >> "$log_file"
    done
  fi
done


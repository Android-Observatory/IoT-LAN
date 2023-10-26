#!/bin/bash

# Define the path to the Bro binary
bro_binary="/opt/zeek/bin/zeek"

# Define the source directory containing the target directories
source_dir="/home/aniketh/devel/src/IoT-local/dataset/idle-dataset-nov"

# Define the final directory where you want to store the results
final_dir="/home/aniketh/devel/src/IoT-local/results/bro_results/nov_parsed"

# Create the final directory if it doesn't exist
mkdir -p "$final_dir"

# Loop through each item in the source directory
for dir in "$source_dir"/*; do
    # Check if the current item is a directory and contains pcap files
    if [ -d "$dir"  ] && [ -n "$(find "$dir" -maxdepth 1 -name '*.pcap' -print -quit)"  ]; then
        # Get the directory name
        dir_name="$(basename "$dir")"
        
        # Create a new subdirectory for the current directory's logs
        new_subdir="${final_dir}/${dir_name}"
        mkdir -p "${new_subdir}"
        
        # Loop through each pcap file in the directory
	for pcap_file in "$dir"/*.pcap; do
	    pcap_name="$(basename "$pcap_file" .pcap)"
	    pcap_name_subdir="${new_subdir}/${pcap_name}"
	    mkdir -p "${pcap_name_subdir}" 
	    (cd "${pcap_name_subdir}" && "${bro_binary}" -Cr "${pcap_file}" -e 'redef LogAscii::use_json=T;')
	    echo "Successfully processed: ${pcap_name_subdir}"
    	done
    fi
done



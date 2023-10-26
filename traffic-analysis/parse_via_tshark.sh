# Define the source directory containing the target directories
source_dir="/home/aniketh/devel/src/IoT-local/dataset/idle-dataset-dec"

# Define the final directory where you want to store the results
final_dir="/home/aniketh/devel/src/IoT-local/results/tshark_results"

# Create the final directory if it doesn't exist
mkdir -p "$final_dir"

# Loop through each item in the source directory
for dir in "$source_dir"/*; do
    # Check if the current item is a directory and contains pcap files
    if [ -d "$dir"  ] && [ -n "$(find "$dir" -maxdepth 1 -name '*.pcap' -print -quit)"  ]; then
        # Get the directory name
        dir_name="$(basename "$dir")"

        for pcap_file in "$dir"/*.pcap; do
            pcap_name="$(basename "$pcap_file" .pcap)"
	    result_name="$final_dir/$dir_name-$pcap_name.csv" 
            python3 tshark_parser.py ${pcap_file} ${result_name}  
        done
    fi
done

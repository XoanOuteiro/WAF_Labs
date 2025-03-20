#!/bin/bash

# Clear the existing block_patterns.conf
echo "" > /etc/nginx/block_patterns.conf

# Read block patterns from the block_patterns.txt and convert them into NGINX map rules
while IFS= read -r line
do
    if [[ ! -z "$line" ]]; then
        # Format each line as a map entry
        echo "    if (\$request_uri ~* \"$line\") { set \$blocked 1; }" >> /etc/nginx/block_patterns.conf
    fi
done < /etc/nginx/block_patterns.txt


FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY block_patterns.txt /etc/nginx/block_patterns.txt
COPY generate_patterns.sh /usr/local/bin/generate_patterns.sh

RUN chmod +x /usr/local/bin/generate_patterns.sh
RUN /usr/local/bin/generate_patterns.sh

EXPOSE 80


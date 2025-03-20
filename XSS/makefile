# The image names
VULNERABLE_IMAGE = web_app_image
FIREWALL_IMAGE = nginx_firewall_image

# Define the Docker networks
NETWORK_NAME = vulnerable_network

# Build the containers
build:
	@echo "Building the vulnerable web app..."
	docker build -t $(VULNERABLE_IMAGE) ./web_app
	@echo "Building the NGINX firewall..."
	docker build -t $(FIREWALL_IMAGE) ./nginx_proxy

# Create a custom network for the containers to communicate
create-network:
	@echo "Creating Docker network..."
	docker network create $(NETWORK_NAME)

# Remove the custom network if exists
remove-network:
	@echo "Removing Docker network..."
	docker network rm $(NETWORK_NAME)

# Run the containers
run: create-network
	@echo "Starting the containers..."
	docker run -d --network $(NETWORK_NAME) --name web_app -p 5000:5000 $(VULNERABLE_IMAGE)
	docker run -d --network $(NETWORK_NAME) --name nginx_firewall -p 80:80 $(FIREWALL_IMAGE)

# Stop and remove the containers
stop:
	@echo "Stopping and removing containers..."
	docker stop web_app nginx_firewall
	docker rm web_app nginx_firewall

# Clean everything (stop containers, remove images, and network)
clean: stop remove-network
	@echo "Cleaning up images..."
	docker rmi $(VULNERABLE_IMAGE) $(FIREWALL_IMAGE)
	@echo "Removing Docker network..."
	docker network rm $(NETWORK_NAME)

# Rebuild the containers (clean + build)
rebuild: clean build run


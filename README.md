# litestar-login
Create a simple login page using the Litestar framework

# Build the Docker image
docker build -t litestar-login .

# Run the Docker container
docker run --name login-page -p 8000:8000 litestar-login
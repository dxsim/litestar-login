# litestar-login
Create a simple login page using the Litestar framework

Requires `Python-3.11^`

# Build the Docker image
```docker build -t litestar-login .```

# Run the Docker container
```docker run -d --name login-page -p 8000:8000 litestar-login```
# Setup Guide

## Prerequisites

### Local Machine
- Docker and Docker Compose installed
- Git configured
- AWS credentials (for S3 model access)

### AWS Account
- S3 bucket with fine-tuned TinyBERT model
- ECR repository created (`sentiment-analysis-api`)
- EC2 instance running (Ubuntu 20.04 or later)
- IAM user with ECR and S3 permissions

### GitHub Repository
- Code pushed to main branch
- Repository secrets configured

---

## 1. Configure GitHub Secrets

Go to **Settings → Secrets and variables → Actions** and add:

```
AWS_ACCESS_KEY_ID          Your AWS access key
AWS_SECRET_ACCESS_KEY      Your AWS secret key
BUCKET_NAME                S3 bucket name with model
```

---

## 2. EC2 Setup (One-time)

SSH into your EC2 instance:

```bash
ssh ec2-user@YOUR_EC2_PUBLIC_IP
```

Install Docker and Docker Compose:

```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Verify installation
docker --version
docker-compose --version
```

Setup GitHub Actions self-hosted runner:

1. Go to **Repository → Settings → Actions → Runners → New self-hosted runner**
2. Follow GitHub's instructions for Linux
3. Start the runner: `./run.sh`

---

## 3. Local Development

Clone and setup:

```bash
git clone https://github.com/YOUR_USERNAME/sentiment-api-deployment.git
cd sentiment-api-deployment

# Create environment file
cp .env.example .env

# Edit .env with your credentials
nano .env
```

Start services:

```bash
# Build and start
docker-compose up -d

# Wait for model download (~1-2 minutes)
sleep 60

# Verify health
curl http://localhost/health

# View logs
docker-compose logs -f
```

Test the application:

```bash
# Open browser
http://localhost/

# Or test via curl
curl -X POST http://localhost/predict \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "text=This movie was amazing!"
```

---

## 4. Deploy to EC2

Push your code to trigger CI/CD:

```bash
git add .
git commit -m "Deploy sentiment analysis API"
git push origin main
```

The pipeline will:
1. Build Docker image
2. Push to AWS ECR
3. Deploy on EC2 with docker-compose

Monitor deployment:

```bash
# Watch GitHub Actions
https://github.com/YOUR_USERNAME/sentiment-api-deployment/actions

# SSH to EC2 and check logs
ssh ec2-user@YOUR_EC2_PUBLIC_IP
docker-compose logs -f
```

---

## 5. Verify Deployment

Once deployment completes:

```bash
# Check containers
docker-compose ps

# Test health endpoint
curl http://YOUR_EC2_PUBLIC_IP/health

# Test sentiment analysis
http://YOUR_EC2_PUBLIC_IP/

# Show which container is serving requests (load balancing demo)
curl http://YOUR_EC2_PUBLIC_IP/container-info
```

---

## 6. Scale to Multiple Instances

Test horizontal scaling locally:

```bash
# Scale to 3 app instances
docker-compose up --scale app=3 -d

# Request multiple times to see different container IDs
for i in {1..10}; do curl http://localhost/container-info; done

# Stop
docker-compose down
```

---

## Common Commands

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f app
docker-compose logs -f nginx

# Restart services
docker-compose restart

# Stop services
docker-compose down

# Rebuild
docker-compose up -d --build
```

---

You're ready to deploy! 🚀

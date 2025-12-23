<div align="center">

# 🎯 Sentiment Analysis API - Production Deployment

*Fine-tuned TinyBERT with Nginx load balancing, Docker orchestration, and automated CI/CD on AWS*

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.5-009688.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED.svg)](https://www.docker.com/)
[![Nginx](https://img.shields.io/badge/Nginx-Reverse%20Proxy-009639.svg)](https://nginx.org/)
[![AWS](https://img.shields.io/badge/AWS-ECR%20%7C%20EC2%20%7C%20S3-FF9900.svg)](https://aws.amazon.com/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF.svg)](https://github.com/features/actions)

</div>

---

## 🎯 Overview

Production-grade sentiment analysis API featuring **fine-tuned TinyBERT model**, **Nginx load balancing**, **multi-container orchestration**, and **automated deployment** on AWS with zero-downtime scaling capabilities.

---

## 🌈 Application Demo

*[Image: Screenshot of sentiment analysis web interface]*

---

## 🌈 Video Demo

<p align="center">
  <a href="https://youtube.com/" target="_blank">
    <img 
      src="https://img.youtube.com/vi/YOUR_VIDEO_ID/maxresdefault.jpg"
      alt="Watch Demo"
      width="700"
    />
  </a>
</p>

<p align="center"><b>▶️ Click to watch architecture & deployment demo</b></p>

---

## 🌈 Architecture Diagrams

<div align="center">

*[Image: System architecture showing Nginx → FastAPI → S3 flow]*

*[Image: CI/CD pipeline diagram: Git → GitHub Actions → ECR → EC2]*

*[Image: Docker Compose multi-container orchestration diagram]*

</div>

---

## ✨ Key Features

### 🧠 **FINE-TUNED ML MODEL**
- TinyBERT optimized for sentiment classification
- Binary classification: Positive/Negative
- Model stored and versioned in AWS S3

### ⚡ **NGINX LOAD BALANCING**
- Reverse proxy architecture for production-grade setup
- Automatic request distribution across scaled instances
- Professional separation of concerns

### 🚀 **AUTOMATED CI/CD PIPELINE**
- GitHub Actions for build and deployment
- Automatic image push to AWS ECR
- Zero-downtime deployments on EC2

### 📦 **HORIZONTAL SCALING**
- Scale API instances with single command: `--scale app=5`
- Nginx automatically load balances across all instances
- Ready for production workloads


---

## 🛠️ Tech Stack

- **Machine Learning:** PyTorch, Transformers, TinyBERT
- **Backend:** FastAPI, Uvicorn
- **Infrastructure:** Docker, Docker Compose, Nginx
- **DevOps & CI/CD:** GitHub Actions, AWS (ECR, EC2, S3)

---

## 📁 Project Structure

```
FineTuningBERT/
├── fastapi_app/
│   ├── app.py                 # FastAPI application with container-info endpoint
│   ├── get_model.py          # S3 model downloader
│   ├── requirements.txt       # Python dependencies
│   └── templates/
│       └── index.html        # Web interface
├── tinybert-sentiment-analysis/
│   └── [Fine-tuned model files]
├── .github/workflows/
│   └── deploy.yml            # CI/CD pipeline (build → push → deploy)
├── nginx.conf                # Reverse proxy configuration
├── docker-compose.yml        # Multi-container orchestration
├── Dockerfile                # FastAPI container
├── Dockerfile.nginx          # Nginx container
└── .env.example              # Environment variables template
```

---

## 🏗️ Architecture Highlights

**Request Flow:**
```
User Request (Port 80)
    ↓
Nginx Container (Reverse Proxy)
    ↓
FastAPI Container(s) (Port 8000)
    ↓
TinyBERT Model (S3)
    ↓
Sentiment Prediction
```

**CI/CD Pipeline:**
```
Push to Main → Build Image → Push to ECR → Deploy on EC2 → docker-compose up
```

---

## 🚀 Quick Start

**Local Development:**
```bash
cp .env.example .env
docker-compose up -d
curl http://localhost/health
```

**Deployment to EC2:**
```bash
git push origin main  # Triggers automated CI/CD
```

👉 **[Complete Setup & Deployment Guide](SETUP.md)**

---

## 🎓 What I Learned

- Fine-tuning and deploying transformer models
- Nginx reverse proxy and load balancing architecture
- Docker Compose for multi-container orchestration
- Horizontal scaling with Docker containers
- GitHub Actions CI/CD pipeline automation
- AWS cloud services (ECR, EC2, S3)
- Production-ready application design
- Health checks and monitoring best practices
- Infrastructure as Code principles

---

## 🔮 Future Enhancements

- **Kubernetes Migration:** Scale beyond Docker Compose
- **Rate Limiting:** Implement rate limiting in Nginx
- **Monitoring:** Prometheus + Grafana dashboards
- **Caching:** Redis for prediction caching
- **Authentication:** OAuth2/JWT for API security

---

## 👤 Author

**Harsh Patel**  
📧 code.by.hp@gmail.com  
🔗 [GitHub](https://github.com/CodeBy-HP) • [LinkedIn](https://www.linkedin.com/in/harsh-patel-389593292/)


---

<div align="center">

**⭐ If you find this project helpful, please star it!**

</div>

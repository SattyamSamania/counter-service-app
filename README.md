# Counter Service

A Python-based microservice demonstrating **full CI/CD automation** with Docker, AWS, and GitHub Actions.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)

---

## Project Overview
`counter-service` is a Python microservice built to demonstrate:

- Automated CI/CD pipelines using GitHub Actions
- Docker containerization and deployment
- Versioning and GitHub releases
- Deployment on AWS EC2 using ECR as container registry
- Code quality and vulnerability scans

---

## Tech Stack
- **Python 3.12** – Backend microservice
- **FastAPI / Gunicorn** – Web server
- **Docker & Docker Compose** – Containerization
- **AWS ECR & EC2** – Cloud registry and deployment
- **GitHub Actions** – CI/CD automation
- **SonarCloud** – Code quality analysis
- **Snyk** – Vulnerability scanning

---

## Architecture
```text
GitHub (development branch)
        |
        v
GitHub Actions Pipeline
        |-- SonarCloud Scan
        |-- Versioning & Release
        |-- Build Docker Image
        |-- Snyk Scan
        |-- Push to AWS ECR
        |-- Deploy to EC2
        |
        v
AWS EC2 (Docker container running counter-service)
```
--- 


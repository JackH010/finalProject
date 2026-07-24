# Local CI/CD Pipeline: GitHub → Jenkins → Docker → Terraform

This project implements a fully automated local deployment pipeline. A push to the `main` branch on GitHub is automatically detected by Jenkins, which rebuilds a Docker image of the application and uses Terraform to redeploy it as a running container — with no manual intervention required.

## Overview

**Flow:** `git push` → Jenkins polls GitHub → checks out code → builds Docker image → runs Terraform → Terraform deploys updated container

## Tech Stack

- **Git/GitHub** — version control and source of truth for all pipeline code
- **Jenkins** — CI/CD orchestration, running as a Docker container
- **Docker** — packaging for the application, and the runtime for both Jenkins and the deployed app
- **Terraform** (`kreuzwerker/docker` provider) — declarative deployment of the app container


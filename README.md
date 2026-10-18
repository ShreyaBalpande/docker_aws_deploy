# 🚀 You Made IT Girl! — Docker, AWS EC2 & CI/CD Deployment

A hands-on DevOps project focused on containerizing a Streamlit application, deploying it to AWS EC2, and automating the build and deployment process using GitHub Actions.

This project helped me understand how an application moves from source code to a running application on a cloud server.

## 📌 Project Overview

The goal of this project was to deploy my Streamlit application using Docker and AWS EC2, then automate the deployment workflow using GitHub Actions.

I worked with containerization, cloud infrastructure, CI/CD automation, and troubleshooting real deployment issues.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web application framework |
| Docker | Containerization |
| Docker Hub | Docker image registry |
| AWS EC2 | Cloud hosting |
| Ubuntu | Server operating system |
| GitHub Actions | CI/CD automation |
| Git & GitHub | Version control and source code management |

## 🏗️ Architecture

The project follows this deployment workflow:

```text
Developer
   |
   | Push code to GitHub
   v
GitHub Repository
   |
   v
GitHub Actions
   |
   +--> Install Python dependencies
   |
   +--> Check Python syntax
   |
   +--> Build Docker image
   |
   +--> Push image to Docker Hub
   |
   v
Deploy to AWS EC2 through SSH
   |
   +--> Pull the latest Docker image
   |
   +--> Restart the application container
   |
   v
Streamlit Application
   |
   v
Browser Access on Port 8501
```

## ⚙️ Key Features

- **Containerization:** Packaged the Streamlit application into a Docker image.
- **Image management:** Published the Docker image to Docker Hub.
- **Cloud deployment:** Ran the container on an Ubuntu-based AWS EC2 instance.
- **Continuous Integration:** Used GitHub Actions to install dependencies and check Python syntax.
- **Continuous Deployment:** Automated Docker image publishing and application deployment on pushes to the `main` branch.
- **Troubleshooting:** Investigated networking, security groups, SSH authentication, and remote deployment connectivity.

## 🐳 Docker Setup

### Build the Docker image locally

Clone the repository:

```bash
git clone https://github.com/ShreyaBalpande/docker_aws_deploy.git
cd docker_aws_deploy
```

Build the Docker image:

```bash
docker build -t you-made-it-girl .
```

### Run the container

```bash
docker run -d \
  --name you-made-it-girl \
  -p 8501:8501 \
  you-made-it-girl
```

Open the application in your browser:

```text
http://localhost:8501
```

To check the running container:

```bash
docker ps
```

To view container logs:

```bash
docker logs you-made-it-girl
```

To stop the container:

```bash
docker stop you-made-it-girl
```

## 📦 Docker Hub

The Docker image used for deployment is available at:

**[View Docker Hub Repository](https://hub.docker.com/r/shreyab0108/you-made-it-girl)**

Pull the published image:

```bash
docker pull shreyab0108/you-made-it-girl:latest
```

Run it locally:

```bash
docker run -d \
  --name you-made-it-girl \
  -p 8501:8501 \
  shreyab0108/you-made-it-girl:latest
```

## ☁️ AWS EC2 Deployment

I deployed the Docker container on an Ubuntu EC2 instance.

### Deployment steps

1. Launched an Ubuntu EC2 instance.
2. Connected to the server using SSH.
3. Updated Ubuntu packages.
4. Installed and started Docker.
5. Pulled the Docker image from Docker Hub.
6. Started the container and mapped port `8501`.
7. Configured the EC2 security group for application access.
8. Verified that the application was accessible through the instance's public IP address.

### Install Docker on Ubuntu

```bash
sudo apt update
sudo apt install -y docker.io
sudo systemctl enable --now docker
```

Verify the installation:

```bash
sudo docker --version
```

### Run the application on EC2

```bash
sudo docker pull shreyab0108/you-made-it-girl:latest

sudo docker run -d \
  --name you-made-it-girl \
  --restart unless-stopped \
  -p 8501:8501 \
  shreyab0108/you-made-it-girl:latest
```

The application can be accessed at:

```text
http://<EC2-PUBLIC-IP>:8501
```

Replace `<EC2-PUBLIC-IP>` with the instance's public IPv4 address.

**Note:** The EC2 instance used for this learning project has been terminated. The commands above describe how to recreate the deployment; the application will not be accessible through the old instance IP.

## 🔄 CI/CD with GitHub Actions

I configured a GitHub Actions workflow to automate the application delivery process.

### Continuous Integration (CI)

When code is pushed to `main` or a pull request targets `main`, the workflow:

- Checks out the repository.
- Sets up Python.
- Installs the dependencies listed in `requirements.txt`.
- Checks Python syntax using `compileall`.

### Docker Image Publishing

After the CI job succeeds on a push to `main`, the workflow:

- Sets up Docker Buildx.
- Authenticates with Docker Hub using GitHub repository secrets.
- Builds the Docker image.
- Pushes the image to Docker Hub with `latest` and commit-specific tags.

### Continuous Deployment (CD)

After the image publishing job succeeds on a push to `main`, the deployment job:

- Connects to the EC2 instance using SSH.
- Pulls the latest Docker image.
- Removes the previous application container.
- Starts a new container with the updated image.

This workflow reduces manual deployment steps and helps keep the deployed application in sync with the repository.

## 🔐 Secrets and Security

Sensitive credentials are stored as GitHub Actions repository secrets rather than being hardcoded into the workflow.

The workflow uses the following secrets:

| Secret | Purpose |
|---|---|
| `DOCKERHUB_USERNAME` | Docker Hub username |
| `DOCKERHUB_TOKEN` | Docker Hub access token |
| `EC2_HOST` | Public IP address of the EC2 instance |
| `EC2_USER` | SSH username for the instance |
| `EC2_SSH_KEY` | Private SSH key used by GitHub Actions |

Never commit private keys, access tokens, passwords, or other credentials to the repository.

For production deployments, SSH access should be restricted, secrets should be rotated when necessary, and deployment permissions should follow the principle of least privilege.

## 🧩 Challenges and Troubleshooting

This project was not just about getting the application running. I also worked through issues that helped me understand deployment more deeply.

### 1. Application accessibility

The container was running, and a local HTTP request on EC2 returned HTTP 200, but the application was initially inaccessible externally.

**What I learned:** A running container does not guarantee external accessibility. Docker port mapping, security-group rules, network routing, and the application's listening address all need to be checked.

### 2. SSH authentication

The GitHub Actions deployment job initially reported a private-key parsing error.

**What I learned:** SSH private keys must be stored correctly in GitHub secrets, and the matching public key must be authorized on the EC2 instance.

### 3. SSH connection timeout

GitHub Actions initially could not connect to EC2 over SSH.

**What I learned:** Successful SSH access from a personal computer does not guarantee access from a GitHub-hosted runner. Security-group rules and the runner's network access also matter.

### 4. Rebuilding after terminating EC2

After terminating the original instance, I launched a new instance, reinstalled Docker, redeployed the existing image, and updated the deployment configuration.

**What I learned:** EC2 instance details, such as the public IP address, can change when infrastructure is recreated. Deployment secrets and configuration must be updated accordingly.

## 📚 What I Learned

Through this project, I gained hands-on experience with:

- Building and running Docker containers.
- Publishing container images to Docker Hub.
- Deploying a Python application on AWS EC2.
- Writing and troubleshooting GitHub Actions workflows.
- Automating Docker builds and deployments.
- Configuring SSH authentication and cloud security groups.
- Debugging connectivity issues between local machines, cloud servers, and CI/CD runners.
- Understanding how CI, container registries, cloud infrastructure, and CD work together.

## 🚀 Future Improvements

Some improvements I would like to explore next:

- Add automated application tests.
- Add a Docker image vulnerability scanning step.
- Use AWS Systems Manager or another approach to reduce public SSH exposure.
- Add deployment health checks and rollback capabilities.
- Configure HTTPS using a reverse proxy and a domain name.
- Introduce infrastructure as code using Terraform.
- Improve monitoring and logging.

## 👩‍💻 About This Project

This is a hands-on learning project built to strengthen my understanding of Docker, AWS, and DevOps practices.

The most valuable part was learning to troubleshoot the problems that appear when moving from local development to cloud deployment.

**Build. Deploy. Debug. Learn. Repeat.**

---

⭐ If you find this project useful, feel free to explore the repository and share your feedback.


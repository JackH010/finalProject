terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "myapp" {
  name         = "myapp:latest"
  keep_locally = true
}

resource "docker_container" "myapp" {
  name  = "myapp-container"
  image = docker_image.myapp.image_id

  ports {
    internal = 5000
    external = 8081
  }
}
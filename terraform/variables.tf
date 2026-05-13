variable "app_name" {
  description = "Name of the application"
  type        = string
  default     = "my-devops-app"
}

variable "app_port" {
  description = "Host port to expose the app on"
  type        = number
  default     = 5000
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "local"
}

variable "docker_image" {
  description = "Docker image name and tag"
  type        = string
  default     = "my-devops-app:latest"
}
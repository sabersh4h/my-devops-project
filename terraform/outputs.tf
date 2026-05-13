output "app_config_path" {
  description = "Path to the generated app config file"
  value       = local_file.app_config.filename
}

output "deploy_script_path" {
  description = "Path to the generated deploy script"
  value       = local_file.deploy_script.filename
}

output "summary" {
  description = "Deployment summary"
  value       = "App '${var.app_name}' configured for '${var.environment}' on port ${var.app_port}"
}
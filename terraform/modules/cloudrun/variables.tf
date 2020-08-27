variable "project" {
  description = "Project ID"
}

variable "region" {
  description = "Region"
}

variable "network" {
  description = "The name of the network being created"
}

variable database_instance {
  description = "Name of the mysql instance"
  type        = string
}

variable "database_version" {
  description = "The database version"
}

variable "user_name" {
  default = "test"
}

variable "user_password" {
  default = "test"
}

variable "instance_name" {
  description = "Name of the postgres instance (PROJECT_ID:REGION:INSTANCE_NAME))"
  type        = string
}

variable "name" {
  description = "Instance Name"
}

variable "location" {
  description = "Zone"
}

variable "display_name" {
  description = "Instance Name"
}

variable "redis_version" {
  description = "Redis Version"
}

variable "size" {
  description = "Memory Size in GB"
}

variable "tier" {
  description = "Service Tier"
}
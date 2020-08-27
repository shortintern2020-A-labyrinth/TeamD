variable "auto_create_subnetworks" {
  type        = bool
  description = "When set to true, the network is created in 'auto subnet mode' and it will create a subnet for each region automatically across the 10.128.0.0/9 address range. When set to false, the network is created in 'custom subnet mode' so the user can explicitly connect subnetwork resources."
  default     = false
}

variable "description" {
  type        = string
  description = "An optional description of this resource. The resource must be recreated to modify this field."
  default     = "Toptal VPC network"
}

variable "network" {
  description = "The name of the network being created"
}

variable "project" {
  description = "Toptal Project"
}

variable "region" {
  description = "Region of resources"
}

variable "routing_mode" {
  type        = string
  default     = "GLOBAL"
  description = "The network routing mode (default 'GLOBAL')"
}

variable "subnet_description" {
  type        = string
  description = "An optional description of this resource. The resource must be recreated to modify this field."
  default     = "Toptal VPC subnetwork"
}

variable "shared_vpc_host" {
  type        = bool
  description = "Makes this project a Shared VPC host if 'true' (default 'false')"
  default     = false
}

variable "subnetwork" {
  description = "The name of the subnetwork being created"
}
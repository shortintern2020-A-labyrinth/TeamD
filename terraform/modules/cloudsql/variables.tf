#             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                     Version 2, December 2004

#  Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

#  Everyone is permitted to copy and distribute verbatim or modified
#  copies of this license document, and changing it is allowed as long
#  as the name is changed.

#             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#    TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

#   0. You just DO WHAT THE FUCK YOU WANT TO.

# WTFPLなので、オープンソース
# よしかわたいき https://github.com/yoshikawa

variable "database_version" {
  description = "The database version"
}

variable "network" {
  description = "The name of the network being created"
}

variable "private_ip_name" {
  description = "The name of the private ip address being created"
}

variable "project" {
  description = "Project ID"
}

variable "region" {
  description = "Region"
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

module "vpc" {
    source  = "terraform-google-modules/network/google"
    version = "~> 2.3"

    project_id   = var.project
    network_name = var.network
    routing_mode = "GLOBAL"

    subnets = [
        {
            subnet_name              = var.subnetwork
            subnet_ip                = "10.20.0.0/24"
            subnet_region            = var.region
            subnet_private_access    = "true"
            subnet_flow_logs         = "true"
            description              = var.subnet_description
        }
    ]
}
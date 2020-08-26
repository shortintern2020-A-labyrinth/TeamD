locals {
  database_version = "MYSQL_5_7"       # "MYSQL_5_7"
  network          = "sittyo"          # Network name
  region           = "asia-northeast1" # asia-northeast1
  project_id       = "a4shittyo-app"   # GCP Project ID
  subnetwork       = "vpc-subnet"      # Subnetwork name
}

// Configure the Google Cloud provider
provider "google" {
  credentials = file("CREDENTIALS_FILE.json")
  project     = local.project_id
  region      = local.region
}

provider "google-beta" {
  credentials = file("CREDENTIALS_FILE.json")
  project     = local.project_id
  region      = local.region
}

module "cloudsql" {
  source           = "./modules/cloudsql"
  network          = local.network
  database_version = local.database_version
  private_ip_name  = "10.20.0.100/24" # Private IP Name
  project          = local.project_id
  region           = local.region
}

module "cloudrun" {
  source = "./modules/cloudrun"

  project = local.project_id
  region  = local.region
}

module "memorystore" {
  source        = "./modules/memorystore"
  display_name  = "redis"        # Display Name
  ip_range      = ""             #
  location      = ""             # Zone
  name          = "redis-sittyo" # Instance name
  network       = local.network
  project       = local.project_id
  redis_version = "REDIS_5_0" # 5.0
  region        = local.region
  size          = "1"           # 1
  tier          = "STANDARD_HA" # STANDARD_HA
}

module "vpc" {
  source     = "./modules/vpc"
  project    = local.project_id
  network    = local.network
  region     = local.region
  subnetwork = local.subnetwork
}

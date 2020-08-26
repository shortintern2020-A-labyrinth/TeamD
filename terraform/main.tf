locals {
  database_version = "MYSQL_5_7"       # "MYSQL_5_7"
  network          = "sittyo"          # Network name
  region           = "asia-northeast1" # asia-northeast1
  project_id       = "a4shittyo-app"   # GCP Project ID
  subnetwork       = "vpc-subnet"      # Subnetwork name
  db_instance_name = "db"
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
  instance_name    = local.db_instance_name
  network          = local.network
  database_version = local.database_version
  private_ip_name  = "10.20.0.100/24" # Private IP Name
  project          = local.project_id
  region           = local.region
}

module "cloudrun" {
  source            = "./modules/cloudrun"
  project           = local.project_id
  region            = local.region
  database_instance = local.db_instance_name
}

module "memorystore" {
  source        = "./modules/memorystore"
  display_name  = "redis"        # Display Name
  ip_range      = "10.30.0.0/24" #
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

locals {
  database_version = "MYSQL_5_7"       # "MYSQL_5_7"
  network          = "default"         # Network name
  region           = "asia-northeast1" # asia-northeast1
  project_id       = "a4shittyo-app"   # GCP Project ID
  db_instance_name = "murikamo"
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

# module "cloudsql" {
#   source           = "./modules/cloudsql"
#   instance_name    = local.db_instance_name
#   network          = local.network
#   database_version = local.database_version
#   project          = local.project_id
#   region           = local.region
# }

module "cloudrun" {
  source            = "./modules/cloudrun"
  network           = local.network
  project           = local.project_id
  region            = local.region
  database_version  = local.database_version
  database_instance = local.db_instance_name
  instance_name     = local.db_instance_name
  display_name      = "lastredis" # Display Name
  name              = "lastredis" # Instance name
  location          = ""
  redis_version     = "REDIS_5_0"   # 5.0
  size              = "1"           # 1
  tier              = "STANDARD_HA" # STANDARD_HA
}

# module "memorystore" {
#   source        = "./modules/memorystore"
#   display_name  = "redis"        # Display Name
#   location      = ""             # Zone
#   name          = "redis-sittyo" # Instance name
#   network       = local.network
#   project       = local.project_id
#   redis_version = "REDIS_5_0" # 5.0
#   region        = local.region
#   size          = "1"           # 1
#   tier          = "STANDARD_HA" # STANDARD_HA
# }

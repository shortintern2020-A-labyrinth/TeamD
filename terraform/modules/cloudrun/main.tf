locals {
  db_network = join("/", ["projects", var.project, "global", "networks", var.network])
}

resource "google_compute_global_address" "private_ip_address" {
  provider = google-beta

  # name          = var.private_ip_name
  name          = "private-ip-address"
  purpose       = "VPC_PEERING"
  address_type  = "INTERNAL"
  prefix_length = 16
  network       = "projects/${var.project}/global/networks/default"
  depends_on    = [var.network]
}

resource "google_service_networking_connection" "private_vpc_connection" {
  provider = google-beta

  network       = "projects/${var.project}/global/networks/default"
  service                 = "servicenetworking.googleapis.com"
  reserved_peering_ranges = [google_compute_global_address.private_ip_address.name]
}

resource "google_cloud_run_service" "mywebapp" {
  name     = "a4shittyo-app"
  project  = var.project
  location = var.region

    depends_on = [
    google_vpc_access_connector.connector,
    google_redis_instance.cache
  ]

  template {
    spec {
      containers {
        image = "gcr.io/a4shittyo-app/django"
        ports {
          container_port = 8000
        }
        env {
          name = "redis_host"
          value = google_redis_instance.cache.host
        }
        env {
          name = "redis_port"
          value = google_redis_instance.cache.port
        }
        env {
          name = "db_private_ip"
          value = google_sql_database_instance.instance.private_ip_address
        }
      }
    }
    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale"      = 1000
        "run.googleapis.com/cloudsql-instances" = var.database_instance
        "run.googleapis.com/vpc-access-connector" : google_vpc_access_connector.connector.id
      }
    }
  }
  traffic {
    percent         = 100
    latest_revision = true
  }
}

resource "google_sql_database_instance" "instance" {
  provider = google-beta

  database_version = var.database_version
  project = var.project
  name             = var.instance_name
  region           = var.region

  depends_on = [
    google_vpc_access_connector.connector
  ]

  settings {
    tier = "db-f1-micro"
    ip_configuration {
      ipv4_enabled    = true
      private_network = local.db_network
    }
  }
}

resource "google_sql_user" "users" {
  name     = var.user_name
  instance = google_sql_database_instance.instance.name
  password = var.user_password
}

resource "google_redis_instance" "cache" {
  display_name       = var.display_name
  name               = var.name
  memory_size_gb     = var.size
  location_id        = var.location
  project            = var.project
  redis_version      = var.redis_version
  region             = var.region
  tier               = var.tier
}


# Add a private VPC connector to for private access from Cloud Run to CloudSQL(MySQL) and Memorystore(redis).
resource "google_vpc_access_connector" "connector" {
  provider = google-beta
  
  name          = "connector"
  ip_cidr_range = "10.0.0.0/28"
  region  = var.region
  network = "default"
  project = var.project

  depends_on = [
    google_vpc_access_connector.connector
  ]
}
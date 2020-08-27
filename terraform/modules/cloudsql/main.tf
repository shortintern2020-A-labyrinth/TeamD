resource "google_sql_database_instance" "instance" {
  provider = google-beta

  name             = var.instance_name
  database_version = var.database_version
  region           = var.region

  depends_on = [
    google_vpc_access_connector.connector
  ]

  settings {
    tier = "db-f1-micro"
    ip_configuration {
      ipv4_enabled    = false
      private_network = google_vpc_access_connector.connector.id
    }
  }
}

resource "google_sql_user" "users" {
  name     = var.user_name
  instance = google_sql_database_instance.instance.name
  password = var.user_password
}

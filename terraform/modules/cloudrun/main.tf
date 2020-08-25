resource "google_cloud_run_service" "mywebapp" {
  name     = "a4shittyo-app"
  project  = var.project
  location = var.region
  template {
    spec {
      containers {
        image = "gcr.io/a4shittyo/django"
      }
    }
  }
  traffic {
    percent         = 100
    latest_revision = true
  }
}
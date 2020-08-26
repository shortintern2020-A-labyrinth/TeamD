resource "google_cloud_run_service" "mywebapp" {
  name     = "a4shittyo-app"
  project  = var.project
  location = var.region
  template {
    spec {
      containers {
        image = "gcr.io/a4shittyo-app/django"
        ports {
          container_port = 8000
        }
      }
    }
    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale"      = 1000
        "run.googleapis.com/cloudsql-instances" = var.database_instance
        "run.googleapis.com/client-name"        = "terraform"
        # "run.googleapis.com/vpc-access-connector" = "my-connector"
      }
    }
  }
  traffic {
    percent         = 100
    latest_revision = true
  }
}

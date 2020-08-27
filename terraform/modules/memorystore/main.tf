resource "google_redis_instance" "cache" {
  authorized_network = var.network
  display_name       = var.display_name
  name               = var.name
  memory_size_gb     = var.size
  location_id        = var.location
  project            = var.project
  redis_version      = var.redis_version
  region             = var.region
  tier               = var.tier
}

terraform {

  required_version = ">= 1.5.0"

  required_providers {
    digitalocean = {
      source = "digitalocean/digitalocean"
      version = "2.57.0"
    }
  }

  backend "local" {
    path = "/etc/backups/digitaloceanstate.tfstate"
  }
}

provider "digitalocean" {

    token = var.do_token
}

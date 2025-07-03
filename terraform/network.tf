resource "digitalocean_vpc" "vpc" {
  name = "vpc"
  region = "nyc1"
  ip_range = "10.250.0.0/16"
}

resource "digitalocean_firewall" "meufirewall" {
  name = "meufirewall"

  droplet_ids = [digitalocean_droplet.minhavm.id]

  inbound_rule {
    protocol         = "tcp"
    port_range       = "22"
    source_addresses = ["SEU_IP"]
  }

  inbound_rule {
    protocol         = "tcp"
    port_range       = "80"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  inbound_rule {
    protocol         = "tcp"
    port_range       = "443"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

 
  outbound_rule {
    protocol              = "tcp"
    port_range            = "all" 
    destination_addresses = ["0.0.0.0/0", "::/0"]
  }

  outbound_rule {
    protocol              = "udp"
    port_range            = "all" 
    destination_addresses = ["0.0.0.0/0", "::/0"]
  }

  outbound_rule {
    protocol              = "icmp" 
    destination_addresses = ["0.0.0.0/0", "::/0"]
  }
}




resource "digitalocean_monitor_alert" "cpu_alert" {
  alerts {
    email = ["SEU_EMAIL"]
    slack {
      channel = "Production Alerts"
      url     = "SLACK_WEBHOOK"
    }
  }
  window      = "5m"
  type        = "v1/insights/droplet/cpu"
  compare     = "GreaterThan"
  value       = 20
  enabled     = true
  entities    = [digitalocean_droplet.minhavm.id]
  description = "Ta usando muita Cpu! Para ai mano..."
}

resource "digitalocean_droplet" "minhavm" {
  image   = "ubuntu-24-10-x64"
  name    = "minhavm"
  region  = "nyc1"
  size    = "s-2vcpu-4gb"
  vpc_uuid = digitalocean_vpc.vpc.id
  backups = true
  monitoring = true
  ssh_keys = [ "SEU_TOKEN" ] #Inserir chave .pub na digital ocean e inserir o fingerprint aqui

  backup_policy {
    plan    = "weekly"
    weekday = "FRI"
    hour    = 8
  }
}

resource "digitalocean_volume" "meuvolume" {
  name                    = "volume-dados-minhavm"
  region                  = digitalocean_droplet.minhavm.region 
  size                    = 100
  initial_filesystem_type = "ext4"
  description             = "Volume de 100GB"
}


resource "digitalocean_volume_attachment" "volume_anexado" {
  droplet_id = digitalocean_droplet.minhavm.id
  volume_id  = digitalocean_volume.meuvolume.id
}
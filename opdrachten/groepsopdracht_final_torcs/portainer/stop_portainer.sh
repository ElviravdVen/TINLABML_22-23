 #!/usr/bin/env bash
 
portainer_container=$(docker ps -a -q --filter ancestor=portainer/portainer-ce)
docker stop ${portainer_container}
docker container rm ${portainer_container}
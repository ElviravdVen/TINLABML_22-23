  #!/usr/bin/env bash
  
docker container prune
docker ps -a -q | xargs docker rm
docker images -a -q | xargs docker rmi -f
docker image prune
docker image prune -a
# e.g. ./docker-build-push http://moll.somenergia.lan:2375/ https://github.com/Som-Energia/somenergia-kpis.git#main registry.somenergia.coop:5000/somenergia-something:latest
# or   ./docker-build-push http://moll.somenergia.lan:2375/ /opt/airflow/repos/somenergia-kpis/ registry.somenergia.coop:5000/somenergia-something:latesto

echo "no va encara"
exit

docker login $1

docker context create moll_docker_daemon --description "moll docker daemon" --docker "host=http://moll.somenergia.lan:2375/"

docker context use moll_docker_daemon

docker build -t $3 $2

docker push $3


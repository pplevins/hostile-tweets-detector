@REM Building docker image of the api server code and pushing it to DockerHub
docker build -t pplevins/hostile-tweets-detector:v1.0 .
docker push pplevins/hostile-tweets-detector:v1.0
docker image tag pplevins/hostile-tweets-detector:v1.0 pplevins/hostile-tweets-detector:latest
docker push pplevins/hostile-tweets-detector:latest

@REM Login to OpenShift
oc login --token=<my-api-token> --server=https://api.rm3.7wse.p1.openshiftapps.com:6443
oc apply -f tweets-secret.yaml

oc apply -f tweets-server-deployment.yaml
oc apply -f tweets-server-service.yaml
oc expose svc/tweets-server
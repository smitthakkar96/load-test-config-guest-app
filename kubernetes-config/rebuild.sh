kubectl delete -f locust-master-controller.yaml
kubectl delete -f locust-master-service.yaml
kubectl delete -f locust-worker-controller.yaml

kubectl create -f locust-master-controller.yaml
kubectl create -f locust-master-service.yaml
kubectl create -f locust-worker-controller.yaml

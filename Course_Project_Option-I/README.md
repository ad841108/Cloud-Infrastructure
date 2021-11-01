# cloud_final_project

## Steps to run your Docker images on Kubernetes Engine
1. docker pull ad841108/clouddriver2
2. Juypter notebook: docker pull jupyter/minimal-notebook
3. Apache Spark: docker pull bitnami/spark
4. Apache Hadoop: docker pull sequenceiq/hadoop-docker
5. Sonarqube: docker pull sonarqube
6. Tag them respectively and push it to the container registry on GCP platform
7. Create cluster:  gcloud container clusters create --machine-type n1-standard-2 --num-nodes 2 --zone us-central1-a --cluster-version latest dli3kubernetescluster
8. Deploy all of them

## URLs for all docker images on Docker Hub
1. Main Termiinal Application: https://hub.docker.com/r/ad841108/clouddriver2?fbclid=IwAR0PUZU6lWCW-3lzKEUJ1KIRi6x42Ebisleptmqil6Vip2c5-lv2C48Vp4o
2. Juypter notebook: https://hub.docker.com/r/jupyter/minimal-notebook
3. Apache Spark: https://hub.docker.com/r/bitnami/spark/
4. Apache Hadoop: https://hub.docker.com/r/sequenceiq/hadoop-docker/
5. Sonarqube: https://hub.docker.com/_/sonarqube

## Screenshot for the Kubernetes Engine with the containers running on it.
<img width="1280" src="https://github.com/ad841108/Cloud-Infrastructure/blob/master/Course_Project_Option-I/Main%20Terminal%20Application%20Running%20on%20Kubernetes.png">
<img width="1280" src="https://github.com/ad841108/Cloud-Infrastructure/blob/master/Course_Project_Option-I/Docker%20Image%20Running%20on%20Kubernetes.png">


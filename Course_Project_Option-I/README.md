# cloud_final_project_checkpoint

## URLs for all docker images on Docker Hub
1. Main Termiinal Application: https://hub.docker.com/r/ad841108/gui_app
2. Juypter notebook: https://hub.docker.com/r/jupyter/minimal-notebook
3. Apache Spark: https://hub.docker.com/r/bitnami/spark/
4. Apache Hadoop Datanode: https://hub.docker.com/r/bde2020/hadoop-datanode
5. Apache Hadoop Namenode: https://hub.docker.com/r/bde2020/hadoop-namenode
6. Sonarqube: https://hub.docker.com/_/sonarqube

## Steps to run your Docker images on Kubernetes Engine
#### Pull docker image, tag them and push them to GCP
1. Web application: docker pull ad841108/gui_app
2. Juypter notebook: docker pull jupyter/minimal-notebook
3. Apache Spark: docker pull bitnami/spark
4. Apache Hadoop Datanode: docker pull bde2020/hadoop-datanode
5. Apache Hadoop Namenode: docker pull bde2020/hadoop-namenode
6. Sonarqube: docker pull sonarqube
7. Tag them respectively and push it to the container registry on GCP platform
8. Create cluster:  gcloud container clusters create --machine-type n1-standard-2 --num-nodes 2 --zone us-central1-a --cluster-version latest dli3kubernetescluster
9. Deploy all of them


## Screenshot for the Kubernetes Engine with the containers running on it.
<img width="1280" src="https://github.com/ad841108/Cloud-Infrastructure/blob/master/Course_Project_Option-I/Main%20Terminal%20Application%20Running%20on%20Kubernetes.png">
<img width="1280" src="https://github.com/ad841108/Cloud-Infrastructure/blob/master/Course_Project_Option-I/Docker%20Image%20Running%20on%20Kubernetes.png">


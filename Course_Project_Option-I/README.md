# cloud_final_project_checkpoint

## URLs for all docker images on Docker Hub
1. Main Termiinal Application: https://hub.docker.com/r/ad841108/gui_app
2. Juypter notebook: https://hub.docker.com/r/jupyter/minimal-notebook
3. Apache Spark: https://hub.docker.com/r/bitnami/spark/
4. Apache Hadoop Datanode: https://hub.docker.com/r/bde2020/hadoop-datanode
5. Apache Hadoop Namenode: https://hub.docker.com/r/bde2020/hadoop-namenode
6. Sonarqube: https://hub.docker.com/_/sonarqube

## Steps to run your Docker images on Kubernetes Engine

#### build the docker image of your web application
1. cd App 
2. docker build -f Dockerfile -t ad841108/gui_app .
3. docker push ad841108/gui_app
You have to build and push the image to your own docker account

#### Pull docker images, tag them and push them to GCP
1. Web application: docker pull ad841108/gui_app
2. Juypter notebook: docker pull jupyter/minimal-notebook
3. Apache Spark: docker pull bitnami/spark
4. Apache Hadoop Datanode: docker pull bde2020/hadoop-datanode
5. Apache Hadoop Namenode: docker pull bde2020/hadoop-namenode
6. Sonarqube: docker pull sonarqube
7. Tag them respectively and push it to the container registry on GCP platform
8. You have to edit "temporal-genius-326917" of the following commands to your own project name
9. docker tag ad841108/gui_app gcr.io/temporal-genius-326917/ad841108/gui_app:1
10. docker push gcr.io/temporal-genius-326917/ad841108/gui_app:1
11. docker tag jupyter/minimal-notebook gcr.io/temporal-genius-326917/jupyter/minimal-notebook:1
12. docker push jupyter/minimal-notebook gcr.io/temporal-genius-326917/jupyter/minimal-notebook:1
13. docker tag bitnami/spark gcr.io/temporal-genius-326917/bitnami/spark:1
14. docker push gcr.io/temporal-genius-326917/bitnami/spark:1
15. docker tag ad841108/gui_app gcr.io/temporal-genius-326917/ad841108/gui_app:1
16. docker push gcr.io/temporal-genius-326917/ad841108/gui_app:1
17. docker tag bde2020/hadoop-datanode gcr.io/temporal-genius-326917/bde2020/hadoop-datanode:1
18. docker push gcr.io/temporal-genius-326917/bde2020/hadoop-datanode:1
19. docker tag bde2020/hadoop-namenode gcr.io/temporal-genius-326917/bde2020/hadoop-namenode:1
20. docker push bde2020/hadoop-namenode gcr.io/temporal-genius-326917/bde2020/hadoop-namenode:1
21. docker tag ad841108/sonarqube gcr.io/temporal-genius-326917/sonarqube:1
22. docker push gcr.io/temporal-genius-326917/sonarqube:1

#### Deploy all of the images to Kubernetes Engine
1. Create cluster:  gcloud container clusters create --machine-type n1-standard-2 --num-nodes 2 --zone us-central1-a --cluster-version latest dli3kubernetescluster
2. Reserve a static IP address for each service including the web application
<img width="1280" src="https://github.com/ad841108/Cloud-Infrastructure/blob/master/Course_Project_Option-I/image/StaticIP.png">
3. upload yaml_files folder to gcp cloud storage
<img width="1280" src="https://github.com/ad841108/Cloud-Infrastructure/blob/master/Course_Project_Option-I/image/upload_yaml_files2.png">
4. Copy it to your gcp shell. You should replace gs://artifacts.temporal-genius-326917.appspot.com/containers/yaml_files to your own cloud storage path 
<img width="1280" src="https://github.com/ad841108/Cloud-Infrastructure/blob/master/Course_Project_Option-I/image/upload_yaml_files.png">

``gsutil cp -r gs://artifacts.temporal-genius-326917.appspot.com/containers/yaml_files .``
5. ``cd yaml_files`` and run ``kubectl apply -f .``

## Screenshot for the Kubernetes Engine with the containers running on it.
<img width="1280" src="https://github.com/ad841108/Cloud-Infrastructure/blob/master/Course_Project_Option-I/Main%20Terminal%20Application%20Running%20on%20Kubernetes.png">
<img width="1280" src="https://github.com/ad841108/Cloud-Infrastructure/blob/master/Course_Project_Option-I/Docker%20Image%20Running%20on%20Kubernetes.png">


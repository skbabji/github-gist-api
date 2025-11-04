pipeline{
    agent{
        kubernetes {
          yaml '''
            apiVersion: v1
            kind: Pod
            metadata:
              labels:
                app: jenkins
            serviceAccount: jenkins-cluster-admin
            spec:
              containers:
              - name: python
                image: python-3.13.9-slim
                command:
                - cat
                tty: true
              - name: docker
                image: dind
                command:
                - cat
                tty: true
              - name: kubectl
                image: kubectl-docker:1
                command:
                - cat
                tty: true
            '''
        }
    }
    stages{
        stage("Checkout"){
            steps{
              checkout scm
            }
        }
        stage("Build & Test"){
          steps{
            container('python'){
              sh '''
              python3.13 -m venv venv
              . venv/bin/activate
              pip install --upgrade pip
              pip install -r requirements.txt -r requirements-dev.txt
              pytest --cov=app
              bandit -r app
              '''
            }
          }
        }
        stage("Build Image"){
          steps{
            container('docker'){
              sh '''
              docker build github-gist-api -t .
              '''
            }

          }
        }
        stage("Publish Image"){
          steps{
            withCredentials([usernamePassword(credentialsId: 'docker-hub-cred', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USER')]) {
              container('docker'){
                sh '''
                docker login -u $DOCKER_USER -p $DOCKER_PASSWORD
                docker push $DOCKER_USER/github-gist-api-$BUILD_NUMBER
                '''
              }
            }
          }
        }
        stage("Deploy to Kubernetes"){
          steps{
            container('kubectl'){
              withCredentials([file(credentialsId: 'kube-config', variable: 'KUBE_CONFIG')]) {
                sh'''
                export KUBE_CONFIG=$KUBE_CONFIG
                kubectl run github-gist-api --image=$DOCKER_USER/github-gist-api-$BUILD_NUMBER --port=8080
                '''
              }
            }
          }
            
        }
    }
}
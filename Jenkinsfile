pipeline {
    agent {
        docker {
            image 'python:3.9-alpine'
            args '-u root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    environment {
        DOCKER_IMAGE = "kalivara17/python-k8s-app"
    }
    stages {
        stage('App Check') {
            steps {
                sh 'python --version'
                sh 'ls -lrth'
            }
        }
        stage('Docker Build & Push') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE}:latest ."
                    sh "docker push ${DOCKER_IMAGE}:latest"
                }
            }
        }
        stage('K8s Deploy') {
            steps {
                sh "kubectl apply -f k8s-deployment.yaml"
            }
        }
    }
}

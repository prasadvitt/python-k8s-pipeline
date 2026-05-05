pipeline {
    agent {
        docker {
            image 'docker:latest'
            args '-u root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    environment {
        DOCKER_IMAGE = "kalivara17/python-k8s-app"
    }
    stages {
        stage('App Check') {
            steps {
                sh 'docker --version'
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
                echo "Deploying to Kubernetes..."
            }
        }
    }
}

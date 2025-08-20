pipeline {
    agent any
    stages {
        stage('Install env') {
            steps {
                sh 'pip install -r .\\requirements.txt'
            }
        }
        stage('Healthcheck Nodes') {
            steps {
                sh 'dir'
                sh 'python3 .\\healthcheck.py'
            }
        }
    }
}

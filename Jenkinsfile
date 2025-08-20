pipeline {
    agent any
    stages {
        stage('Install env') {
            steps {
                bat 'pip install -r .\\requirements.txt'
            }
        }
        stage('Healthcheck Nodes') {
            steps {
                bat 'dir'
                bat 'python3 .\\healthcheck.py'
            }
        }
    }
}

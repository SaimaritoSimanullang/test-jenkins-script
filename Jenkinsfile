pipeline {
    agent any
    stages {
        stage('Healthcheck Nodes') {
            steps {
                sh 'dir'
                sh 'python3 .\healthcheck.py'
            }
        }
    }
}

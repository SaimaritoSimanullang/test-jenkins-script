pipeline {
    agent any
    stages {
        stage('Healthcheck Nodes') {
            steps {
                sh 'python3 healthcheck.py'
            }
        }
    }
}

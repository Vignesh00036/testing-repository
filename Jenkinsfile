pipeline {
    agent any
    triggers {
        pollSCM */5 * * * *
    }
    stages {
        stage ('Running python') {
            steps {
                echo 'Running'
                sh '''
                    python3 test.py
                '''
            }
        }
    }
}

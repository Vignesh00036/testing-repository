pipeline {
    agent any
    triggers {
        pollSCM '* * * * *'
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

        stage ('Interacting with python') {
            steps {
                echo 'Interacting'
                sh '''
                    4
                '''
            }
        }
    }
}

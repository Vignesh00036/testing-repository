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
    }
}

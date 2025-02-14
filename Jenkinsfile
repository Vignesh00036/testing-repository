pipeline {
    agent any
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage ('Installing Python') {
            steps {
                echo 'Installing'
                sh '''
                    sudo apt install python3 python3-pip -y
                '''
            }
        }
        
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
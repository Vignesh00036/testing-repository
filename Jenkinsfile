def gv

pipeline {
    agent any
    parameters {
        choice(name: 'version', choices:['1.2.0', '1.2.1', '1.2.2'], description:'Choose the version for your convenience use')
        booleanParam(name: 'protection', defaultValue: true)
    }
    stages {
        stage ('init') {
            steps {
                script {
                    gv = load "script.groovy"
                }
            }
        }

        stage ('test') {
            steps {
                script {
                    gv.testing()   
                }
            }
        }

        stage ('run') {
            steps {
                script {
                    gv.running()
                }
            }
        }
    }
}

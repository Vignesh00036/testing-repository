def testing() {
    echo "Testing application version ${params.version}"
}

def running() {
    echo "Running python ${params.version}"
    sh '''
        python3 test.py
    '''
}

return this

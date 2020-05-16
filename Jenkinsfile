pipeline {
  agent {
    docker { image 'nikobraz/mycmdb:latest' }
  }
  stages {
    stage('Test') {
      steps {
        sh 'python3 -V'
        sh 'python3 -m django --version'
      }
    }
  }
}

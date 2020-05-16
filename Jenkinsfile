pipeline {
  agent {
    dockerfile {
      filename './Dockerfile'
    }

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
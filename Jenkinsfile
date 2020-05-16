pipeline {
  agent {
    dockerfile {
      filename './Dockerfile'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh 'python3 -V'
        sh 'python3 -m django --version'
      }
    }
   stage('Test') {
      steps {
        sh 'python3 -V'
        sh 'python3 -m django --version'
      }
    }
   stage('Run') {
      steps {
        sh 'python3 -V'
        sh 'python3 -m django --version'
      }
    }
  }
}

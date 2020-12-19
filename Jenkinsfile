node('master') {
    cleanWs()
    def dockerTool = tool name: 'docker', type: 'dockerTool'
    withEnv(["DOCKER=${dockerTool}/bin", "PATH=$PATH:${dockerTool}/bin"]) {
        stage('git checkout') {
            checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/Nikobraz/mycmdb.git']]])
        }
        stage('build') {
        
            customImage = docker.build("nikobraz/mycmdb:${env.BUILD_ID}", ".")
            docker.image("nikobraz/mycmdb:${env.BUILD_ID}").withRun() { c ->
                sh 'ls -lah'
            }
        }
        stage('push') {
            withDockerRegistry(credentialsId: 'be53aead-ae88-43c5-b4d9-14fa3bc9c125', toolName: 'docker') {
                customImage.push()
                customImage.push('latest')
            }
        }
    }
}

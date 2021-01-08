import org.jenkinsci.plugins.pipeline.modeldefinition.Utils

node('master') {
    cleanWs()
    if(!BUILD) {
        BUILD = 'true'
    }
    def dockerTool = tool name: 'docker', type: 'dockerTool'
    withEnv(["DOCKER=${dockerTool}/bin", "PATH=$PATH:${dockerTool}/bin"]) {
        stage('git checkout') {
            if(BUILD == 'true') {
                checkout([$class: 'GitSCM',
                      branches: [[name: '*/master']],
                      doGenerateSubmoduleConfigurations: false,
                      extensions: [],
                      submoduleCfg: [],
                      userRemoteConfigs: [[url: 'https://github.com/Nikobraz/mycmdb.git']]])
            } else {
                Utils.markStageSkippedForConditional('git checkout')
            }
        }
        stage('build') {
            if(BUILD == 'true') {
                customImage = docker.build("nikobraz/mycmdb:${env.BUILD_ID}", ".")
                /*
                docker.image("nikobraz/mycmdb:${env.BUILD_ID}").withRun() { c ->
                    sh 'ls -lah'
                }
                */
            } else {
                Utils.markStageSkippedForConditional('build')
            }
        }
        stage('push') {
            if(BUILD == 'true') {
                withDockerRegistry(credentialsId: 'be53aead-ae88-43c5-b4d9-14fa3bc9c125', toolName: 'docker') {
                    customImage.push()
                    customImage.push('latest')
                }
            } else {
                Utils.markStageSkippedForConditional('push')
            }
        }
        stage('deploy') {
            if(BUILD == 'true') {
                tag = env.BUILD_ID
            } else {
                tag = 'latest'
            }
            try {
                docker.image("nikobraz/mycmdb:${tag}").run('--name mycmdb -p 8000:8000')
            } catch (Exception ex) {
                docker.script."${docker.shell()}" "docker stop mycmdb && docker rm -f mycmdb"
                docker.image("nikobraz/mycmdb:${tag}").run('--name mycmdb -p 8000:8000')
            }
        }
    }
}

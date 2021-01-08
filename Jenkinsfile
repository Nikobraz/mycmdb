import org.jenkinsci.plugins.pipeline.modeldefinition.Utils

node('master') {
    cleanWs()
    if (!BUILD) {
        BUILD = 'true'
    }
    def dockerTool = tool name: 'docker', type: 'dockerTool'
    withEnv(["DOCKER=${dockerTool}/bin", "PATH=$PATH:${dockerTool}/bin"]) {
        stageWhen('build', params.BUILD) {
            customImage = docker.build("nikobraz/mycmdb:${env.BUILD_ID}", ".")
            /*
            docker.image("nikobraz/mycmdb:${env.BUILD_ID}").withRun() { c ->
                sh 'ls -lah'
            }
            */
        }
        stageWhen('push', params.BUILD) {
            withDockerRegistry(credentialsId: 'be53aead-ae88-43c5-b4d9-14fa3bc9c125', toolName: 'docker') {
                customImage.push()
                customImage.push('latest')
            }
        }
        stage('deploy') {
            if (BUILD == 'true') {
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

def stageWhen(String name, Boolean expr, Closure body) {
    stage(name) {
        if (expr) {
            body.call()
        } else {
            Utils.markStageSkippedForConditional(name)
        }
    }
}

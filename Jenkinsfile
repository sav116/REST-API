@Library('jenkins-library') _

node('cloud-agent') {

  stage('Clone'){
    container('kaniko') {
      checkout scm
        stash includes: '**', name: 'repo'
    }
  }

  stage('Tests') {
    node('centos'){
      unstash 'repo'
      sh 'docker system prune -f'
      sh 'docker-compose up --build --exit-code-from app'
    }
  }

  stage('Kaniko Build & Push Image') {
    container('kaniko') {
      scmInfo = checkout scm
      runKanikoBuildPush(GIT_COMMIT: "${scmInfo.GIT_COMMIT}")
    }
  }

  stage('Helm chart update and commit') {
    container('jenkins-yq') {
      withCredentials([gitUsernamePassword(credentialsId: 'gitlab_cred',gitToolName: 'git-tool')]) {
          runHelmUpdateCommit(GIT_COMMIT: "${scmInfo.GIT_COMMIT}", INIT_CONTAINER: "false")
        }
      }
    }
  }
}

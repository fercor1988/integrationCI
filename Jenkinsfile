//Create verify CI
pipeline {
  agent any
  stages {
         stage('Connect-Repository-GitHub'){
                steps{
                  git poll: true, url: 'https://github.com/fercor1988/integrationCI.git'
                }
         }
         stage('Create-Workspace-Virtual'){
                steps{
                      sh 'bash -c "virtualenv entorno_virtual && source entorno_virtual/bin/activate"'
                }
         }
         stage('Create-Workspace-Virtual-Requeriments'){
                steps{
                      sh 'bash -c "virtualenv entorno_virtual && source entorno_virtual/bin/activate && pip install -r code/requirements.txt"'
                }
         }
         stage('Start-Application'){
                steps{
                      sh 'bash -c "virtualenv entorno_virtual && source entorno_virtual/bin/activate && pip install -r code/requirements.txt && python code/main.py &"'
                }
         }
         stage('Start-Application-TestUnit'){
                steps{
                      sh 'bash -c "virtualenv entorno_virtual && source entorno_virtual/bin/activate && pip install -r code/requirements.txt && python code/main.py & && cd code && pytest && cd .."'
                }
         }
         stage('Delete-Image-Docker'){
                steps{
                      sh 'docker rmi fercor3188/testpython:latest'
                }
         }
         stage('Create-Image-Docker'){
                steps{
                      sh 'docker build . --rm -t fercor3188/testpython:latest'
                }
         }
         stage('Push-Image-Docker'){
                steps{
                      sh 'docker push fercor3188/testpython:latest'
                }
         }
  }
}

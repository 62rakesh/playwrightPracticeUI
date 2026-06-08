// pipeline {
//     agent any
//
//     stages {
//
//         stage('Checkout') {
//             steps {
//                 checkout scm
//             }
//         }
//
//         stage('Build Docker Image') {
//             steps {
//                 sh 'docker build -t playwright-ui-framework .'
//             }
//         }
//
//         stage('Run Tests') {
//             steps {
//                 sh '''
//                 docker run --rm \
//                 -v $(pwd)/reports:/app/reports \
//                 playwright-ui-framework
//                 '''
//             }
//         }
//     }
// }


pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Docker Validation') {
            steps {
                sh 'docker --version'
            }
        }
    }
}
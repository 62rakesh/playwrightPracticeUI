pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                bat 'playwright install chromium'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytes -m "login or logout"'
            }
        }
    }

    post {
        always {
            archiveArtifacts(
            artifacts: 'reports/screenshots/*.png',
            allowEmptyArchive: true
            )
            publishHTML([
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports/html',
                reportFiles: '*.html',
                reportName: 'Playwright Test Report'
            ])
        }
    }
}
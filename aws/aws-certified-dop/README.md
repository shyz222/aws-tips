# 目次
- [目次](#目次)
- [目的](#目的)
- [背景](#背景)
- [参考](#参考)
- [内容](#内容)
  - [Codeシリーズ全般](#codeシリーズ全般)
  - [CodeCommit](#codecommit)
  - [CodeBuild](#codebuild)
# 目的
- 資格取得を通じて理解をより深めるため
- awsを用いたシステムのアーキテクトをする際に、devopsに関する知識を初めから持っておくことで、拡張性や運用性に考慮したシステムを設計できるようにするため
# 背景
- 機械学習/分析関連のPJに参画してから１年経ち、実際の運用作業を通じてDevOps(MLOps)の重要性を痛感したから
# 参考
- [AWS Certified DevOps Engineer Professional 2022 - Hands On!](https://www.udemy.com/course/aws-certified-devops-engineer-professional-hands-on/)
# 内容
- 知らなかったことや大事なことを記載していく
## Codeシリーズ全般
- [取得できるイベント一覧](https://dev.classmethod.jp/articles/new-code-series-notification/)
## CodeCommit
- 特になし
## CodeBuild
- CodeCommitのPRをCodeBuildで検証するアーキテクチャ
  - [Validating AWS CodeCommit Pull Requests with AWS CodeBuild and AWS Lambda](https://aws.amazon.com/jp/blogs/devops/validating-aws-codecommit-pull-requests-with-aws-codebuild-and-aws-lambda/)
    - 2019年の記事でちょっと古い
    - <p align='center'><img src='./img/README_2023-01-07-15-50-23.png' width='70%'></p>
    - ↓の方が今のAWSサービスに則していてシンプル
  - [CodeCommitのプルリクをCodeBuildで検証しAWS ChatbotでSlack通知する](https://qiita.com/joe-king-sh/items/d896ec66a93212e92147)
    - AWS chatbotを用いてslack通知している
    - <p align='center'><img src='./img/README_2023-01-07-15-49-15.png' width='70%'></p>
    - 自分のPJではTeamsを用いているが、AWS chatbotがTeams対応していないため、AWS Chatbotの代わりにLambdaで実装している
      - [ウェブフックを使用して Amazon SNS メッセージを Amazon Chime、Slack、または Microsoft Teams に発行する方法を教えてください。](https://aws.amazon.com/jp/premiumsupport/knowledge-center/sns-lambda-webhooks-chime-slack-teams/)
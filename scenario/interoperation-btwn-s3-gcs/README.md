# 目次
- [目次](#目次)
- [目的](#目的)
- [背景](#背景)
# 目的
- boto3を用いてs3-gcs間でオブジェクトを転送するlambdaを作成する
# 背景
- パブリッククラウド間のデータ転送を実現するサービスは下記がある
    - [AWS DataSync](https://aws.amazon.com/jp/blogs/news/migrating-google-cloud-storage-to-amazon-s3-using-aws-datasync/)
    - [GCP Storage Tranfer Service(STS)](https://cloud.google.com/storage-transfer-service?hl=ja)
- 一方要件として下記が求められていた
    1. AWS側で機能を構築すること
    2. サーバレスで構築すること
- STSはGCP側で機能を構築することになってしまい、AWS DataSyncはEC2を構築する必要があったため、上記サービスはともに要件を満たせず
- 代替案として、boto3の[リクエストエンドポイントおよびアクセスキー/シークレットをGCSのHMACキーに変更する方法](https://cloud.google.com/storage/docs/aws-simple-migration?hl=ja)でlambdaを実装することとなった。
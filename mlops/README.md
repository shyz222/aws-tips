# 目次
- [目次](#目次)
- [目的](#目的)
- [背景](#背景)
- [学習教材](#学習教材)
- [学習内容](#学習内容)
# 目的
- MLOpsの理解度向上
- AI/MLシステムにかかわる各ロールの違いや実施していることを俯瞰的に理解すること
# 背景
- 分析関係のプロジェクトにアサインされたため
- 今後AL/MLシステムの専門性に富んだエンジニアになりたいため
# 学習教材
- 書籍
  - [仕事ではじめる機械学習](https://www.amazon.co.jp/%E4%BB%95%E4%BA%8B%E3%81%A7%E3%81%AF%E3%81%98%E3%82%81%E3%82%8B%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92-%E7%AC%AC2%E7%89%88-%E6%9C%89%E8%B3%80-%E5%BA%B7%E9%A1%95/dp/4873119472)
  - [機械学習デザインパターン](https://www.amazon.co.jp/%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3-%E2%80%95%E3%83%87%E3%83%BC%E3%82%BF%E6%BA%96%E5%82%99%E3%80%81%E3%83%A2%E3%83%87%E3%83%AB%E6%A7%8B%E7%AF%89%E3%80%81MLOps%E3%81%AE%E5%AE%9F%E8%B7%B5%E4%B8%8A%E3%81%AE%E5%95%8F%E9%A1%8C%E3%81%A8%E8%A7%A3%E6%B1%BA-Valliappa-Lakshmanan/dp/4873119561)
  - [実践AWSデータサイエンス](https://www.amazon.co.jp/%E5%AE%9F%E8%B7%B5-AWS%E3%83%87%E3%83%BC%E3%82%BF%E3%82%B5%E3%82%A4%E3%82%A8%E3%83%B3%E3%82%B9-%E2%80%95%E3%82%A8%E3%83%B3%E3%83%89%E3%83%84%E3%83%BC%E3%82%A8%E3%83%B3%E3%83%89%E3%81%AEMLOps%E3%83%91%E3%82%A4%E3%83%97%E3%83%A9%E3%82%A4%E3%83%B3%E5%AE%9F%E8%A3%85-Chris-Fregly/dp/4873119685)

# 学習内容
- AI/MLシステムの基本的なワークフロー
  - <p align='center'><img src='./img/README_2022-12-03-16-11-12.png' width='70%'></p>
  - ref
    - [GoogleCloudで機械学習を実装するためのベストプラクティス](https://cloud.google.com/architecture/ml-on-gcp-best-practices?hl=ja#machine-learning-workflow-orchestration)
    - [機械学習のワークフローってどうなっているの ? AWS の機械学習サービスをグラレコで解説](https://aws.amazon.com/jp/builders-flash/202003/awsgeek-sagemaker/?awsf.filter-name=*all)
- AI/MLシステムにかかわる人員と役割（呼び方は色々あると思う。。。）
  1. 探索的データ分析を実施する人達(Data Scientists/ML Engineers)
     1. 特徴量エンジニアリング
     2. モデル開発（加工/探索/訓練/評価）
  2. データエンジニアリングする人達(Data Engineer)
     1. データ収集
     2. ETL
  3. 上記をクラウドサービス等を用いてシステムとして構築・管理する人達(Cloud/Platform/Software/MLOps/SysOps Engineer)
     1. システム化
     2. パイプライン化
     3. セキュリティ
     4. ガバナンス
     5. その他諸々
   - <p align='center'><img src='./img/README_2022-12-03-16-06-04.png' width='70%'></p>
   - ref
     - [AWSで構築するMLOps基盤](https://pages.awscloud.com/rs/112-TZM-766/images/20201015_AWS%E3%81%A6%E3%82%99%E6%A7%8B%E7%AF%89%E3%81%99%E3%82%8BMLOps%E5%9F%BA%E7%9B%A4_%E9%85%8D%E5%B8%83%E7%89%88__AIMLTokyo7.pdf)

- MLOpsとは
  - AI/MLシステムにおけるDevOpsこと
  - 一般的なDevOpsとの違いはCI/CDにCT(Continuos Training)があること
  - MLOpsレベル
    - MLOpsレベル0:手動
    - MLOpsレベル1:MLパイプラインの自動化
    - MLOpsレベル2:CI/CDパイプラインの自動化
  - ref
    - [MLOps:機械学習における継続的デリバリーと自動化のパイプライン](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
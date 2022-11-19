# AWS-Certified-SOA
## 目的
* AWSのOperation/Security/Governance関連の知識習得
## 背景
* 業務では付加価値に直結するサービス開発にばかり従事しているため習得機会がない
* 一方で、長期的なサービス稼働・運用を考慮するとOperation/Security/Governanceは運用コストに大きく関わってくるためベスプラを学んでおきたい
## 学習教材
* [AWS認定資格試験テキスト AWS認定SysOpsアドミニストレーター - アソシエイト AWS認定資格試験テキスト](https://www.amazon.co.jp/AWS%E8%AA%8D%E5%AE%9A%E8%B3%87%E6%A0%BC%E8%A9%A6%E9%A8%93%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88-AWS%E8%AA%8D%E5%AE%9ASysOps%E3%82%A2%E3%83%89%E3%83%9F%E3%83%8B%E3%82%B9%E3%83%88%E3%83%AC%E3%83%BC%E3%82%BF%E3%83%BC-%E3%82%A2%E3%82%BD%E3%82%B7%E3%82%A8%E3%82%A4%E3%83%88-NRI%E3%83%8D%E3%83%83%E3%83%88%E3%82%B3%E3%83%A0%E6%A0%AA%E5%BC%8F%E4%BC%9A%E7%A4%BE/dp/481560908X)
## 学習内容（知らなかったことを箇条書きしておく）
* [VPCフローログの見方](https://qiita.com/miyuki_samitani/items/f83bc082156a36770828)
* ELBとRoute53のヘルスチェック機能の違い
    * ELB
        * http/httpsを指定している場合パスを指定してヘルスチェック可能
        * ステータスコードの確認のみ
    * Route53
        * ELBのヘルスチェック機能をドメイン名にも適用させてようなかんじ
        * ステータスコード+サイト文字列の確認
        * ターゲットにIPまたはドメイン名指定可能
    * ref
        * [ELBとRoute 53のヘルスチェック仕様の違い](https://dev.classmethod.jp/articles/health-check-spec-elb-route53/)
* Lambdaのスケーリング
    * 垂直スケーリング：メモリ増やす
    * 水平スケーリング：[同時実行数の予約](https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/configuration-concurrency.html)
* S3バケット・オブジェクトの削除
    * バケット削除
        ```
        aws s3 rb <S3URI>
        ```
    * オブジェクト削除
        ```
        aws s3 rm <S3URI>
    * バケット削除を実行してもバケットが残るパターン
        * バージョニングを有効にしていたとき
            * オブジェクトは削除マーカーのついたオブジェクトとして残る。ただし、存在しないように見える。
            * バケットは↑のバージョニングされたオブジェクトが残っているので、削除されない。
            * 空のバケットが残ってるかんじ
* AWS <Service/Personal> Health Dasheboard
    * AWS Service Health Dasheboard
        * AWSサービス全体の状態をまとめているサービス（どのリージョンでどんな障害が起きているとか）
    * AWS Service Personal Dasheboard
        * AWSアカウント内で利用しているサービス・リージョン・リソースなどの状態がわかるサービス
* AWS Organizationの機能セット
    * 一括請求機能（Consolidated Billing）
        * メンバーアカウントの請求管理のみを管理アカウントに統合することができる
    * すべての機能
        * メンバーアカウントの請求管理のAWSリソース権限管理なども管理アカウントに統合することができる
    * 請求管理は統合したいがAWSリソース管理は独立させたい場合一括請求機能が適切
    * 「一括請求機能」から「すべての機能」へは後からも変更できる
    * 
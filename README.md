# aws
## 目的
* awsに関して業務またはプライベートで学んだ内容のアウトプット・備忘録
## ルール
### ディレクトリ
* サービス単体に関する内容はサービス名
* 複数のサービスを組み合わせた内容やシナリオ/ユースケースに沿う内容はシナリオ名
```
{serviceName}
scenario/{scenarioDetail}
```
* ex
```
EC2
Lambda
scenario/how-to-manage-multi-account
```
### git開発戦略
* 基本はgit-flow
* 開発単位ごとにfeatureブランチを作成し作業（個人用なのでmaster直でも良いがgitの使い方・コマンド忘れないように）
* 個人用なのでdevelop/hotfix/releaseは採用しない

<script src="https://blz-soft.github.io/md_style/release/v1.2/md_style.js" ></script>
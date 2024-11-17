# 目次
- [目次](#目次)
- [目的](#目的)
- [背景](#背景)
- [参考](#参考)
- [内容](#内容)
  - [AWS](#aws)
    - [Amazon Bedrock Overview 【Amazon Bedrock Series #01】](#amazon-bedrock-overview-amazon-bedrock-series-01)
    - [Amazon Bedrock モデル推論 a.準備編 【Amazon Bedrock Series #02a】](#amazon-bedrock-モデル推論-a準備編-amazon-bedrock-series-02a)
    - [Amazon Bedrock モデル推論 b.実践編 【Amazon Bedrock Series #02b】](#amazon-bedrock-モデル推論-b実践編-amazon-bedrock-series-02b)
    - [Amazon Bedrock Agents 自律型 AI の実現に向けて: 検討編 【Amazon Bedrock Series #04a】](#amazon-bedrock-agents-自律型-ai-の実現に向けて-検討編-amazon-bedrock-series-04a)
    - [Amazon Bedrock Knowledge Bases](#amazon-bedrock-knowledge-bases)
  - [GCP](#gcp)
    - [GenOps: 生成 AI 向けに MLOps が進化](#genops-生成-ai-向けに-mlops-が進化)
    - [GenOps: マイクロサービスと従来の DevOps の世界から学ぶ](#genops-マイクロサービスと従来の-devops-の世界から学ぶ)
  - [Azure](#azure)
    - [LLMOps:ΔMLOps by MS ito shunta](#llmopsδmlops-by-ms-ito-shunta)
    - [Azure ベースライン OpenAI エンドツーエンド チャット リファレンス アーキテクチャ](#azure-ベースライン-openai-エンドツーエンド-チャット-リファレンス-アーキテクチャ)
    - [Azure OpenAI モデルのログと監視を実装する](#azure-openai-モデルのログと監視を実装する)
    - [Azure Databricks を使用して MLOps を調整する](#azure-databricks-を使用して-mlops-を調整する)
    - [マルチモーダル/AI Agent/LLMOps 3つの技術トレンドで理解するLLMの今後の展望](#マルチモーダルai-agentllmops-3つの技術トレンドで理解するllmの今後の展望)
    - [ChatGPT - LLMシステム開発大全](#chatgpt---llmシステム開発大全)
    - [AOAI Dev Day LLMシステム開発 Tips集](#aoai-dev-day-llmシステム開発-tips集)
    - [](#)
# 目的
- LLMOpsの勉強
# 背景
# 参考
- [プロンプトエンジニアリングによる、Amazon Bedrock でのセキュアな RAG アプリケーション](https://aws.amazon.com/jp/blogs/news/secure-rag-applications-using-prompt-engineering-on-amazon-bedrock/)
- [【AWS】BedrockのAgentを使ったら1時間弱でRAGを構築できた](https://zenn.dev/ncdc/articles/41bf6e7735ec9f)
# 内容
## AWS
### [Amazon Bedrock Overview 【Amazon Bedrock Series #01】](https://pages.awscloud.com/rs/112-TZM-766/images/AWS-Black-Belt_2024_Amazon-Bedrock-Overview_v1.pdf)
  - <p align='center'><img src='./img/README-template_2024-10-27-14-16-29.png' width='70%'></p>
  - <p align='center'><img src='./img/README-template_2024-10-27-14-32-03.png' width='70%'></p>
  - <p align='center'><img src='./img/README-template_2024-10-27-15-24-11.png' width='70%'></p>
  - <p align='center'><img src='./img/README-template_2024-10-27-15-18-23.png' width='70%'></p>
  - <p align='center'><img src='./img/README-template_2024-10-27-15-18-49.png' width='70%'></p>
  - <p align='center'><img src='./img/README-template_2024-10-27-15-19-12.png' width='70%'></p>
  - <p align='center'><img src='./img/README-template_2024-10-27-15-20-58.png' width='70%'></p>
  - <p align='center'><img src='./img/README-template_2024-10-27-15-21-47.png' width='70%'></p>
  - <p align='center'><img src='./img/README-template_2024-10-27-15-40-18.png' width='70%'></p>
  - <p align='center'><img src='./img/README-template_2024-10-27-15-40-45.png' width='70%'></p>
  - <p align='center'><img src='./img/README-template_2024-10-27-15-41-32.png' width='70%'></p>
  - <p align='center'><img src='./img/README-template_2024-10-27-16-00-42.png' width='70%'></p>
  - <p align='center'><img src='./img/README-template_2024-10-27-16-01-41.png' width='70%'></p>
  - <p align='center'><img src='./img/README-template_2024-10-27-16-02-41.png' width='70%'></p>
  - <p align='center'><img src='./img/README-template_2024-10-27-16-13-18.png' width='70%'></p>
  - <p align='center'><img src='./img/README-template_2024-10-27-16-13-44.png' width='70%'></p>
  - <p align='center'><img src='./img/README-template_2024-10-27-16-14-00.png' width='70%'></p>
  - <p align='center'><img src='./img/README-template_2024-10-27-16-14-20.png' width='70%'></p>
  - cross-regionについて(別資料)
    - <p align='center'><img src='./img/README-template_2024-10-27-16-17-43.png' width='70%'></p>
    - <p align='center'><img src='./img/README-template_2024-10-27-16-18-08.png' width='70%'></p>
    - <p align='center'><img src='./img/README-template_2024-10-27-16-18-37.png' width='70%'></p>
    - <p align='center'><img src='./img/README-template_2024-10-27-16-18-54.png' width='70%'></p>
  - <p align='center'><img src='./img/README-template_2024-10-27-16-39-25.png' width='70%'></p>
  - <p align='center'><img src='./img/README-template_2024-10-27-16-39-43.png' width='70%'></p>
### [Amazon Bedrock モデル推論 a.準備編 【Amazon Bedrock Series #02a】](https://pages.awscloud.com/rs/112-TZM-766/images/AWS-Black-Belt_2024_Amazon-Bedrock-Model-Inference-a_0909_v1.pdf)
  - <p align='center'><img src='./img/README_2024-11-02-17-57-24.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-57-52.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-58-12.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-58-50.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-59-25.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-00-09.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-00-26.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-01-10.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-01-25.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-01-41.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-03-08.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-03-39.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-04-17.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-04-31.png' width='70%'></p>
### [Amazon Bedrock モデル推論 b.実践編 【Amazon Bedrock Series #02b】](https://pages.awscloud.com/rs/112-TZM-766/images/AWS-Black-Belt_2024_Amazon-Bedrock-Model-Inference-b_0909_v1.pdfs)
  - <p align='center'><img src='./img/README_2024-11-02-18-05-25.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-09-52.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-10-18.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-10-54.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-11-29.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-11-52.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-14-15.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-14-29.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-15-12.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-15-43.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-16-11.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-16-59.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-17-13.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-18-17-57.png' width='70%'></p>
### [Amazon Bedrock Agents 自律型 AI の実現に向けて: 検討編 【Amazon Bedrock Series #04a】](https://pages.awscloud.com/rs/112-TZM-766/images/AWS-Black-Belt_2024_Amazon-Bedrock-Agents_0930_v1.pdf)
  - <p align='center'><img src='./img/README_2024-11-03-14-51-47.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-14-52-11.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-14-52-29.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-14-52-44.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-14-54-21.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-00-23.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-01-34.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-01-51.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-02-12.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-04-41.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-04-53.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-05-08.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-07-14.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-07-27.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-07-45.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-07-59.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-08-16.png' width='70%'></p>
### [Amazon Bedrock Knowledge Bases](https://pages.awscloud.com/rs/112-TZM-766/images/AWS-Black-Belt_2024_Amazon-Bedrock-Knowledge-Bases_0920_v1.pdf)
  - <p align='center'><img src='./img/README_2024-11-03-15-34-33.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-36-33.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-35-46.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-35-58.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-37-01.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-41-57.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-42-11.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-42-26.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-43-03.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-43-16.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-43-51.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-44-05.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-44-19.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-52-02.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-15-52-16.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-07-41.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-08-21.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-09-45.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-10-05.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-15-45.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-16-00.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-22-35.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-29-43.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-30-19.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-30-31.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-30-45.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-31-00.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-31-12.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-33-31.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-34-30.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-34-41.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-35-03.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-35-16.png' width='70%'></p> 
  - <p align='center'><img src='./img/README_2024-11-03-16-39-57.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-40-10.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-40-40.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-40-54.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-03-16-41-15.png' width='70%'></p>
## GCP
### [GenOps: 生成 AI 向けに MLOps が進化](https://cloud.google.com/blog/ja/products/ai-machine-learning/learn-how-to-build-and-scale-generative-ai-solutions-with-genops)
  - <p align='center'><img src='./img/README_2024-11-09-14-14-47.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-09-14-17-09.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-09-14-24-31.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-09-14-25-57.png' width='70%'></p>
### [GenOps: マイクロサービスと従来の DevOps の世界から学ぶ](https://cloud.google.com/blog/ja/products/devops-sre/genops-learnings-from-microservices-and-traditional-devops)
  - <p align='center'><img src='./img/README_2024-11-09-14-56-04.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-09-14-56-32.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-09-15-02-22.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-09-15-05-08.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-09-15-05-23.png' width='70%'></p>
## Azure
### [LLMOps:ΔMLOps by MS ito shunta](https://speakerdeck.com/shuntaito/llmops-dmlops)
  - <p align='center'><img src='./img/README_2024-10-27-17-04-10.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-10-27-17-11-48.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-10-27-17-12-43.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-16-48-05.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-16-48-36.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-16-49-31.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-16-52-35.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-16-52-59.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-16-55-02.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-16-56-42.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-16-59-45.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-01-14.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-02-21.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-02-56.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-04-05.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-05-53.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-13-23.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-14-06.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-15-04.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-22-29.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-22-47.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-23-10.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-24-54.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-29-51.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-30-34.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-31-56.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-32-24.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-33-28.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-34-14.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-36-43.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-38-02.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-02-17-47-02.png' width='70%'></p>
### [Azure ベースライン OpenAI エンドツーエンド チャット リファレンス アーキテクチャ](https://learn.microsoft.com/ja-jp/azure/architecture/ai-ml/architecture/baseline-openai-e2e-chat)
  - <p align='center'><img src='./img/README_2024-11-09-15-21-22.png' width='70%'></p>
### [Azure OpenAI モデルのログと監視を実装する](https://learn.microsoft.com/ja-jp/azure/architecture/ai-ml/openai/architecture/log-monitor-azure-openai)
  - <p align='center'><img src='./img/README_2024-11-09-15-23-20.png' width='70%'></p>
### [Azure Databricks を使用して MLOps を調整する](https://learn.microsoft.com/ja-jp/azure/architecture/ai-ml/idea/orchestrate-machine-learning-azure-databricks)
  - <p align='center'><img src='./img/README_2024-11-09-15-23-54.png' width='70%'></p>
### [マルチモーダル/AI Agent/LLMOps 3つの技術トレンドで理解するLLMの今後の展望](https://speakerdeck.com/hirosatogamo/llmops-3tunoji-shu-torendodeli-jie-surullmnojin-hou-nozhan-wang)
  - <p align='center'><img src='./img/README_2024-11-17-14-59-19.png' width='70%'></p>
  - <p align='center'><img src='./img/README_2024-11-17-15-02-52.png' width='70%'></p>
  - 
### [ChatGPT - LLMシステム開発大全](https://speakerdeck.com/hirosatogamo/chatgpt-azure-openai-da-quan)
### [AOAI Dev Day LLMシステム開発 Tips集](https://speakerdeck.com/hirosatogamo/aoai-dev-day-llmsisutemukai-fa-tipsji)
### []()

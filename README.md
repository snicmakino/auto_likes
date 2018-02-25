# auto_likes
This application likes Twitter posts with certain keywords automatically using AWS lambda  
AWS lambdaを利用したTwitter自動いいねツール  

## Apex
This application using [apex](http://apex.run/)

## Getting Start
### install Apex and create Apex project
Apexのインストールを行い、本ツール用のプロジェクトを作成する  
http://apex.run/

### clone project
apexプロジェクト直下のfunctionsディレクトリに移動し、本プロジェクトをクローンする  
```bash
cd [apex_project_root]/functions
clone https://github.com/snicmakino/auto_likes.git  
cd auto_likes
```

### create function.json
function.json.exampleを元に、function.jsonを作成する  
`cp function.json.example function.json`  

functions.jsonの中身を編集する
- [TwitterApps](https://apps.twitter.com/) で取得した情報を入力  
    "TWITTER_CONSUMER_KEY"  
    "TWITTER_CONSUMER_SECRET"  
    "TWITTER_ACCESS_KEY"  
    "TWITTER_ACCESS_SECRET"  

- いいねしたい検索条件をカンマ区切りで設定  
    "SEARCH_KEYWORDS"  

- いいねしたくないユーザをカンマ区切りで設定  
    "NG_USERS"  
    
### build Apex project
```bash
cd [apex_project_root]/functions  
apex build auto_likes
```

### deploy Apex project
```bash
apex deploy auto_likes
```

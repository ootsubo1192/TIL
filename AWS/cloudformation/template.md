# template

```yaml
AWSTemplateFormatVersion: "version date"
Description:
    String
metadate:
    template metadata
Parameters:
    set of parameters
Mappings:
    set of mappings
Conditions:
    Set of conditions
Transform
    set of transforms
Resources:
    set of resources
Outputs:
    set of outputs
```

`AWSTepmlateFormatVersion`->テンプレートのバージョン(重要)

`Description`(記述)->テンプレートの説明文(重要)

`Metadata`(メタデータ)->テンプレートに関する追加情報の記述

`Parameters`(設定値)->スタック作成時にユーザーに入力を求めるもの(重要)

`Mappings`(地図作成)->キーと値のマッピング

`Conditions`(状態)->条件名と条件判断内容

`Transform`(変換)->サーバレスアプリケーションや定形コンテンツ挿入のためのマクロを指定

`Resources`(供給源)->AWSサービスのスタックを構成するリソースとプロパティ(必須のパラメータ)

'Outputs`(生産)->スタック構成後にCloudFormationから出力する値(重要)

Resourcesのみがゆいつの必須のパラメータになります。EC2やRDSの詳しい設定を記述する


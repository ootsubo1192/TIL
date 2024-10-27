# OSINT 実践ガイド

## 目的
いろんな便利サイトまとめ

## セキュリティ
- [OWASP](https://owasp.org/)
Webアプリケーションのセキュリティに関しの活動をしている非営利機関
    - [OWASP Top Ten](https://owasp.org/www-project-top-ten/)
        調査した中で、危険度が最も高いと判断された10個の脆弱性についてまとめられている。(各年度の情報がまとまってないので検索が必要…)
    - [Zed Attack Proxy(zap)](https://www.zaproxy.org/)
    Webアプリケーション開発者が簡易的に脆弱性診断を実施することを目的に作成されたもの
    - [Application Security Varification Standard(ASVS)](https://owasp.org/www-project-application-security-verification-standard/)
    設計･開発･脆弱性診断時に必要となるセキュリティ要件についてまとめられている

- [IPA 安全なウェブサイトの作り方](https://www.ipa.go.jp/security/vuln/websecurity/about.html)

### OSINTとは
**Open Source Inteligence**
オープンになっている情報源から情報を収集する
`インテリジェンス`は、将来の状況や状況の予測、予測を可能にし行動方針(COA)の違いを明らかにすることで決定のための材料を提供する。

#### デジタルOSINT
##### [OSINT Framework](https://osintframework.com/)
##### [Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html)
##### [Mapping Tools for Open Source Inteligence with Cyber Kill Chain for Adversarial Aware Security](https://www.mdpi.com/2227-7390/10/12/2054)
##### [MITRE ATT&CK](https://attack.mitre.org/matrices/enterprise/)
ハッカーグループが、そのライフサイクルの間にどのような行動をするのかを、敵対者側の視点に立って分類したフレームワーク
##### [Common Vulnerability Scoring System](https://www.first.org/cvss/specification-document)

### OSINTO ツール
#### 資産の外部公開状況を把握する
攻撃者は、インターネット上に攻撃目標となる｢資産 ｣が公開されていないか調べる。防御する側も同様にツールを使って状況を把握する必要がある。
##### [Shodan](https://www.shodan.io/)
無償でいいがアカウント登録しないと機能が限られる。画像の検索もできる`country:"JP" org:""`
##### [BinaryEdge](https://binaryedge.io/)
無償のアカウント登録が必要。メールアドレスの漏洩もチェックできる
##### [Censys](https://censys.com/)
無償のアカウント登録が必要。

#### パスワードが漏洩していないか調査する
ログインパスワードが漏洩すると、正規のユーザになりすましてシステムにログインされる。検索サイトで漏洩していないかを定期的にチェックする
##### [Have I Been Pwned](https://haveibeenpwned.com/)
ドメイン単位で検索するには検証をクリアする必要がある
##### [DeHashed](https://dehashed.com/)
無償のアカウント登録が必要。ドメイン単位で検索できるが、無償アカントだとヒットしていた場合に詳細を確認できない
##### [BugMeNot](https://bugmenot.com/)

#### マルウェア情報を調査する
重要ファイルを人質に取るランサムウェアなど、企業にとってマルウェア対策は最も重要なセキュリティ対策の一つになっている
##### [VirusTotal](https://www.virustotal.com/)
不審なファイルをアップロードすることでマルウェアが含まれていないかどうかチェックすることができる。が、**アップロードしたファイルは第三者にダウンロードされるので注意する。**
**Webブラウザの拡張機能もあるが、ダウンロードファイルを自動でアップロードする機能もあるので注意する**
##### [ANY.RUN](https://app.any.run/)
マルウェアを仮想環境で安全に実行する仕組みを提供
無償のユーザー登録が必要
##### [Joe Sandbox](https://www.joesandbox.com/)
無償のユーザー登録が必要
ビヘイビアグラフでマルウェアの挙動をビジュアル表現

#### Webサイトのレピュテーションを調査する
不審なWebサイトを見つけたら、｢Webサイトのレピュテーション調査｣を実施して悪意を持って作られたサイトかどうかをチェックする癖をつける。
##### [aguse](https://www.aguse.jp/)
Webブラウザーで直接アクセスするのが不安な場合に代理アクセスしてくれる
自社のWebサイトが正しく運用されているかどうかのチェックもできる
##### [urlscan.io](https://urlscan.io/)

#### ゼロデイやエクスプロイトの有無を調査する
企業のセキュリティ確保には、｢ゼロデイ｣に関する調査も欠かせない。いち早く情報を入手して準備をすることで被害に遭うリスクを減らすことができる。
##### [Zero-day Vulnerability Database](https://www.zero-day.cz/database/)
自社で使用しているソフトウェアのゼロデイ脆弱性の有無を確認
##### [Published/Upcoming Advisories](https://www.zerodayinitiative.com/advisories/upcoming/)
##### [SecurityHome.eu](https://securityhome.eu/)

#### Microsoft月例セキュリティパッチについて情報収集する
セキュリティの維持には、発見された脆弱性を修正するセキュリティパッチに関する情報収集が欠かせない。
毎月第2火曜日(米国時間)
##### [Zero Day Initiative - Blog](https://www.zerodayinitiative.com/blog)
SECURITY UPDATE REVIEW でパッチ情報が一覧表形式で見れる
##### [Bleeping Computer](https://www.bleepingcomputer.com/)
Newsから確認
##### [SANS Internet Storm Center](https://isc.sans.edu/)
Diariesから確認

#### 自社に関連する脆弱性情報を収集する
攻撃者はターゲットとなる組織のシステムにある脆弱性を優先的に狙って攻撃をしかけてくる。自社システムに関係する脆弱性情報がないかを定期的に調査する必要がある。
##### [NVD](https://nvd.nist.gov/vuln/search)
NISTが管理している脆弱性情報データベース
##### [JVN iPedia](https://jvndb.jvn.jp/)
日本国内で使用されているソフトウェアなどの脆弱性情報
##### [Vulmon](https://vulmon.com/)
CVE番号、会社名、製品名で検索可能
##### [Vumetric Cybersecurity Portal](https://cyber.vumetric.com/)
ダッシュボード形式で脆弱性情報を掲載している

#### SSL/TLSのセキュリティ強度を確認する
WebサイトやWebベースのサービスを運営している企業にとって、SSL/TLSのセキュリティ強度を維持することは非常に重要なタスクになる。
##### [SSL Server Test](https://www.ssllabs.com/ssltest/)
スキャン結果をダッシュボードに表示させないようにするには`Do not show the results on the boards`にチェックを付けて実行する
##### [Test TLS](https://testtls.com/)

#### 執行したサーバ証明書の有無を確認する
インターネットからアクセスできるサーバのSSL/TLSサーバ証明書の失効は致命的な問題となる
##### [Entrust Certificate Search](https://ui.ctsearch.entrust.com/ui/ctsearchui)
サーバ証明書の有効期限をサブドメインも含めて確認できる
##### [Certificate Checker](https://ssltools.godaddy.com/views/certChecker)

#### 自己著名証明書の有無を調べる
自己著名証明書を明確な理由なしに自社で使用していると面倒に巻き込まれる
##### [SSL/TLS Certificate Test Tool](https://network-tools.webwiz.net/ssl-certificate-checker.htm)
Self Signed パラメータをチェック
##### [Self Signed Certificate Checker](https://s4e.io/tools/self-signed-certificate-checker)

#### 投稿写真から住所などが特定されていないか調べる
SNSに投稿した写真から、標的型攻撃の手がかりにされる危険がある。写真からどういう情報が漏れるか確認する
##### [Google画像検索](https://images.google.com/)
##### [TinEye](https://tineye.com/)
Google画像検索で検索できなかった際に使用する

#### メールアドレスの漏洩の有無を調べる
業務で利用しているメールアドレスがインターネット上で広く知られている状態になっていると、標的型攻撃のターゲットとなってしまう。
##### [Hunter](https://hunter.io)
事前にユーザー登録が必要。

#### IPアドレスの使用場所を特定する
##### [MaxMind](https://www.maxmind.com/en/geoip-web-services-demo)
##### [eXTReMe-IP-Lookup.com](https://extreme-ip-lookup.com/)
URLにIPアドレスを指定できるのでこのサイトはKinabaで使用できそう

#### Wi-FiのSSIDが知れ渡っていないか調べる
SSIDは攻撃者にとって有用な情報となりえる
##### [WiGLE.net](https://www.wigle.net/)
SSIDから場所を特定できる。無償のユーザー登録が必要

#### Exifデータの埋め込みをチェックする
写真に埋め込まれたExifデータから知られたくない情報が外部に漏れる
##### [EXIF Data Viewer Online](https://linangdata.com/exif-reader/)

#### アーカイブやキャッシュを活用する
過去のWeb画面を調査する
##### Googleキャッシュ
https:// を cache:// に変更
##### [Internet Archive](https://archive.org/)
画面まで確認できる

#### 自社のIPアドレスレンジを把握する
##### [ipinfo.io](https://ipinfo.io/)

#### 使用しているWebテクノロジーを把握する
自社のWebサイトで使用しているソフトウェアを把握する
##### [BuiltWith](https://builtwith.com/ja/)

#### IPアドレスやドメイン名の利用履歴を調べる
自社サイトで使用しているIPアドレスやドメインが過去に悪用されたものの場合｢悪質なサイト｣とみなされる危険がある
##### [SrcurityTrails](https://securitytrails.com/)
無償の会員登録が必要。履歴を確認して[AbuselIPDB](https://www.abuseipdb.com/)で調査する

#### 送信ドメイン認証の対応状況をチェックする
自社の対応状況を調べる
##### [EasyDMARC](https://easydmarc.com/tools)

#### IoC情報を入手してインシデントに備える
攻撃やマルウエアの特徴を示したIndicators of Compromise 情報の入手が不可欠
##### [AlienVault Open Threat Exchange](https://otx.alienvault.com/)
##### [ThreatMiner](https://www.threatminer.org/)
ファイルハッシュも検索できる

#### フィッシング関連情報を入手する
##### [PhishTank](https://phishtank.com/)
フィッシングサイトと思われるURLを入力
##### [OpnePhish]()

### OSINT情報を可視化
セキュリティ情報の全体像を見渡す。

##### [MIPS](https://github.com/MISP/MISP)
OSSとして提供されている脅威情報プラットフォーム
インストール直後は自己著名証明書が使用されているためエラーが出る
##### [OpenCTI](https://github.com/OpenCTI-Platform/opencti)
サイバー脅威インテリジェンスシステム
ElasticSearchを使用して稼働することもできそう

#### OSINT情報の活用
- CISOを通じて経営戦略に関わるような判断材料を提示する
- 中･長期的なインフラ投資の優先順位を決定するような材料を提示する



## 便利ツール
- [Documatic](https://www.documatic.com/)
ドキュメントの開発プロセスを削減するツール。APIリファレンスからユーザーガイドなど

- [Transform](https://transform.tools/)
あらゆるデータ形式から別の形式に変換するツール。JSON <-> YAMLなど

- [Roadmap.sh](https://roadmap.sh/)
あらゆる言語や技術のロードマップを見れる

- [opensourcealternative.to](https://www.opensourcealternative.to/)
OSSを探す時。代替ツールを探す時。

- [Zapier](https://zapier.com/)
日常的なタスクの自動化をするためのフレームワークを作成するツール

- [ExplainShell](https://explainshell.com/)
難しいシェルコマンドを分解して解説してくれるツール

- [DevHints](https://devhints.io/)
プログラミング言語やツールのチートシートみれる

- [Carbon](https://carbon.now.sh/)
スライドにコードを貼り付ける際に便利なツール

- [CyberChef](https://gchq.github.io/CyberChef/)
あらゆる便利ツールを使える
>2・8・10・16進数変換
Base64、URL、古典暗号（シーザー暗号やヴィジュネル暗号など）、現代暗号（AES/DES/RSAなど）のエンコード・デコード
IPv4・IPv6アドレスのパースやフォーマット変換
テキストエンコーディングの変換
MD5・SHA-1・SHA-2などのハッシュ値計算
EXIF情報の抽出・削除
QRコードの作成・読み取り


## 資料
[知っておくと仕事が捗る便利ツール17選](https://qiita.com/twrcd1227/items/70ecf7717067764c3c7d#opensourcealternativeto)
[サイバー攻撃から企業システムを守る！　OSINT実践ガイド](https://amzn.asia/d/eQgsqFA)

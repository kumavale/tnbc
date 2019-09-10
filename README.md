# tnbc
\`Tosho card Next' Balance Check  
<u>図書カードNEXT > [残額確認](https://www.toshocardnext.ne.jp/tosho/pc/CardUserLoginPage/login.do)</u> with CLI  

## Requirement
* Python 3.6 or above  
* bs4  
* [requests](https://github.com/psf/requests)  

## Usage
> `python tnbc.py [ID1] [ID2] [ID3] [ID4] [PIN]`  

```
$ python tnbc.py 0123 4567 8901 2345 0123
ＩＤ番号 : 0123456789012345
有効期限 : 20XX 年 12 月 31 日
ご利用可能残額 : 0円
```


# 星空键道6个人版

**WARNING: 本人已不再使用该方案，不会再有任何更新，可能某日便悄得刪库了。** 

仓库里包含了修改后的方案文件, 词库文件和 opencc 文件, 先正常安装原版键道6, 再覆盖即可.

主要的修改有:

- 对 630 词库进行修改, 将一部分低频的词或本人不用的词换成了更常用的词.
- 新增 ssb 词库, 规则为特殊的 ss 码加首字的 b 码, 可将特殊词的编码空间进一步扩大.
- ssb 词库中增加了 ss 码的次选, 因 ss 码本就需要使用空格上屏, 加入次选不会增加码长.
- 调整了默认词库, 优化了多种读法的词, 加入了一些常用的词.
- 降低了 630 的全码的优先级, 让其它的码先出.
- 加入了个人版本的数学词库.
- 将 emoji 改为官方的 rime-emoji 仓库的版本, 手动转换到简体字版本, 将其添加为 `emoji_cn.json` 作为默认方案.
- 为 emoji 增加菜单上的开关, 方便在手机上使用.
- 调整默认的 `s2twp.json`, 将词汇转换补全, 需要伪装台湾人时可修改简繁转换方案到 `s2twp.json`, 大陆词会被直接转为台湾词. (如 `人工智能 -> 人工智慧`)
- 添加了 `u` `v` 以及 `op` 引导的反查功能.

`*` 标记说明该词有飞键且两种输入方式都是允许的.

## 630

- gau 姑娘 -> 刚好
- mau 美女 -> 美好

## ssb 词库 (***重要的补充词库, 后需会加入开关方便自行选择是否使用***)

- bt
  - btu 白天

- bx
  - bxo 必需
  - bxv 不像

- ey
  - eyo 试用

- fc
  - fco 这次

- sx
  - sxu 私信

- yr
  - yri 依然
  - yro 炎热
  - yrv 一人

- yx
  - yxa 也许
  - yxo 影响
  - yxu 印象
  - yxv 一些

## 反查

### U键全拼 (xkjd6fw)

`u` 键按下后进入全拼反查模式, 直接输入单字的全拼即可查询.

如查询 `噩` 的编码, 则输入 `ue` 就可以找到编码是 `xevi`.

### V键两分 (xkjd6fw)

`v` 键按下后进入两分模式, 直接输入单字的两部件拆分的全拼即可查询.

如查询 `掴` 的编码, 则输入 `vshouguo` 就可找到编码是 `gliu`.

### OP键写字

`op` 两键按下后进入写字模式, 直接输入单字的双拼与前两笔即可查询.

如查询 `仞` 的编码, 则输入 `oprnui` 就可以找到编码是 `rnia`.

注意, 这里的前两笔**不含字根**, 只是单纯的**前两笔**.

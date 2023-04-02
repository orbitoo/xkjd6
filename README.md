# 星空键道6个人版

仓库里包含了修改后的方案文件, 词库文件和 opencc 文件, 先正常安装原版键道6, 再覆盖即可.

主要的修改有:

- 对 630 词库进行修改, 将一部分低频的词或本人不用的词换成了更常用的词.
- 新增 ssb 词库, 规则为特殊的 ss 码加首字的 b 码, 可将特殊词的编码空间进一步扩大.
- 调整了默认词库, 优化了多种读法的词, 加入了一些常用的词.
- 加入了个人版本的数学词库.
- 将 emoji 改为官方的 rime-emoji 仓库的版本, 手动转换到简体字版本, 将其添加为 `emoji_cn.json` 作为默认方案.
- 为 emoji 增加菜单上的开关, 方便在手机上使用.
- 调整默认的 `s2twp.json`, 将词汇转换补全, 需要伪装台湾人时可修改简繁转换方案到 `s2twp.json`, 大陆词会被直接转为台湾词. (如 `人工智能 -> 人工智慧`)

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

## 默认词库

### 词库调整

- bkfru (null) -> 笔锋
- gefei (null) -> 搁这
- gens (null) -> 搁那
- gzskoi (null) -> 高四
- lkhqvi (null) -> 李华
- lxrno (null) -> 良人
- mxbj (null) -> 蜜雪冰城
- tcqi (null) -> 提词器
- tkcki (null) -> 提词
- tsmn 她们 -> 它们
- tsmna (null) -> 她们
- tsmno 它们 -> (deleted)
- qpgl 张果 -> 掌掴
- qpgli 掌掴 -> 张果
- wkjno (null) -> 痴嗔
- xsdsv (null) -> 厦大
- yhto 益和堂 -> 益禾堂
- ykbf 一般 -> 一半
- ykbfv 一半 -> 一般
- ylnk 淤泥 -> 与你
- ylnkv 与你 -> 淤泥

### 多音补充

- pjgm* 曝光 (bzgm)
- qpgg 掌掴 (qpgl)

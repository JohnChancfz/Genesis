# item
name | type | default | remark 
---|---|---|---
id | int | auto | ID
cid | int | | 分类id
name | varchar(20) | '' | 名称
description | varchar(255) | null | 描述
coverImg | varchar(255) | null | 封面图
content | text | | 内容
raisingMoney | double(10,2) | 0.00 | 标的估值
investmentCycle | int | 0 | 投资期限(年)
region | varchar(255) | | 项目地域
createTime | datetime | | 创建时间annotation
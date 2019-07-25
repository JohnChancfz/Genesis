# router
name | type | default | remark 
---|---|---|---
id | int | auto | ID
type | int | | 分类id
name | varchar(20) | '' | 名称
version | varchar(255) | | 版本
description | text | null | 描述
ip | varchar(16) | 0.0.0.0 | 路由IP
mac | varchar(50) |  | MAC地址
region | varchar(255) | | 地域
upTime | varchar(50) | | 运行时间
status | int | 0 | 状态
createTime | datetime | | 创建时间
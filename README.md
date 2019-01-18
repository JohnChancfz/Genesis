# What is Genesis ?
Java Code Generation



### 20190119

* md文件生成 基于spring boot jpa实体类 (Date,@Column  未实现)


## future

    1. 生成spring boot项目 (暂定gradle) 
    2. 添加权限管理 (暂定shiro) 
    3. 生成后台管理页面 (暂定ant-design-pro)
    
> 1.maven 2.spring security 3.vue.js 欢迎添加 

>  先做成导出现有的后台系统 bootstrap


## config

```
# package name
package_name = 'com.cfz.admin'

# entity
entity = {'fileName': 'entity',
          'isExtends': False,
          'basePath': 'com.cfz.admin.entity.support',
          'baseName': 'BaseEntity'}

# dao dao/impl
dao = {'fileName': 'dao',
       'isExtends': False,
       'basePath': 'com.cfz.admin.dao.support',
       'baseName': 'BaseDao',
       }

# service service/impl
service = {'fileName': 'service',
           'isExtends': False,
           'basePath': 'com.cfz.admin.service.support',
           'baseName': 'BaseService',
           }

# controller
service = {'fileName': 'controller',
           'isExtends': False,
           'basePath': 'com.cfz.admin.controller.support',
           'baseName': 'BaseController',
           }

```

> 暂时写在config.py里面 没时间 实现config 读取config配置文件

## log
> 未实现

## out
   
    - out
    -- entity
    -- dao
        -- impl
    -- service
        -- impl
    -- controller


# contact

    johnchancfz@yahoo.com
    
    

![打赏](https://thumbnail0.baidupcs.com/thumbnail/ad1d59c5d845eb14e2c9c8b472e90cfa?fid=3827379193-250528-1094346648416821&time=1547845200&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-%2Bx2e6J5FcwC%2BhV5ORHcSvIu8jnI%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=422529015482700127&dp-callid=0&size=c710_u400&quality=100&vuk=-&ft=video)




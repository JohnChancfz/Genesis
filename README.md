# Genesis
Java Code Generation


```
graph LR
A-->B
```

### 20190119

* md文件生成 基于spring boot jpa实体类


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



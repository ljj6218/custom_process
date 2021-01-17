# custom_process

## 项目介绍
“自定义流程管理”项目，使用技术栈：  
1、Flask + Vue  
2、mysql+mongo    
## 目的  
通过“人机物环管”五个要素，把管理、生产、新闻记事等，进行自定义。  
结构化数据，存储进mysql，非结构化数据，存储进mongo。  
利用“人机物环管”五个要素之间的关系，描述业务逻辑的框架，  
进行查询时，可以快速定位位置，了解过去已经发生的事，和未来需要做的事。  
从而**降低复杂业务逻辑的学习成本，让新人快速上手业务处理，让老手更快找到需要的东西。**
## 原理介绍
 抽象化

    理论 ——> 现实

    人：角色 ——> 具体人员

    机：类型 ——> 机器编号

    物：类型 ——> 物料编号

    环：类型 ——> 环境代号

    管，通过上面四种实体进行组合，实现一定的目的

    模板 ——> 计划 ——> 实际步骤 ——> 具体内容 ——> 日志

    CustomProcessBase不断实例化出子级

    



身份证号

    八级

    人机物环管的归属、分类

    模型 id 层级 id

步骤

日志：

    时间、地点、人物、起因、经过、结果


逻辑核心-管理：CustomProcessBase
    
    不设置、不保存前后关系，只要能填满字段就可以创建
    所以，可以同时进行多项互不影响的管理

    条件：需要的别的模型对象提供的字段
    自己独有的字段

    例如：
        炒菜，热锅的同时，可以洗菜、切菜
        可以根据该管理的条件找到上一步
        本步完成，可以查找条件，获得下一步能进行哪些管理
    增：满足条件，可以编辑本管理
    删：没有下一步依赖该管理，可以删除
    改：没有下一步依赖该管理，可以修改
    查：
    起因：满足条件,就可以随时发起/分解父级管理任务
    经过：描述、介绍 text
        ~~人：~~
        机：Machine
        物：Good
        ~~环：~~
        ~~管：~~
    结果：记录在该管理里面 
    时间：记录在该管理里面
    地点：Environment
    人物：SysUser
    导出：json
    导入：json

CustomProcessBase结构

    id：唯一标识
    parent_id：父级的唯一标识
        1、他自身的抽象、模板
        2、父级
    condition，条件
        other_obj.fields：
        fields：
    desc：描述
    result，结果
        key：value

    时间：创建时间，更新时间

    人：SysUser   rel表
    机：Machine   rel表
    物：Good   rel表
    环：Environment   rel表

新规则定义
    
    比如，选符合某个条件的人，做为某个管理的“SysUser   rel表”的来源：
    1、添加，查询这个条件的人的代码，随时查询，
    2、由设计者指定id列表，存储备用，
    3、利用身份证体系，进行范围划定

# 项目安装运行
下载项目

    git clone git@github.com:ljj6218/custom_process.git

安装后端环境

    pipenv install

运行后端
可以使用 flask 命令或者 python 的 -m 开关来运行这个应用。  
在 运行应用之前，需要在终端里导出 FLASK_APP 环境变量:  

    export FLASK_APP=hello.py  
    flask run  
如果是在 Windows 下，那么导出环境变量的语法取决于使用的是哪种命令行解释器。 在 Command Prompt 下:  

    set FLASK_APP=hello.py
    flask run
在 PowerShell 下:

    $env:FLASK_APP = "hello.py"
    flask run
还可以使用 python -m flask:

    export FLASK_APP=hello.py
    python -m flask run


安装前端环境

    cd web/
    npm install -g cnpm --registry=https://registry.npm.taobao.org && npm install
运行前端

    npm run serve
    
访问：  
http://localhost:5000/  
里面有前端跳转链接（http://localhost:8081/  ）和admin后台跳转链接（http://localhost:5000/admin/  ）
    
    


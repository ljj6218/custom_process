# custom_process
“自定义流程管理”项目

抽象化

    理论 ——> 现实

    人：角色 ——> 具体人员

    机：类型 ——> 机器编号

    物：类型 ——> 物料编号

    环：类型 ——> 环境代号

    管，通过上面四种实体进行组合，实现一定的目的

    模板 ——> 计划 ——> 实际步骤 ——> 具体内容 ——> 日志
    项目     设计图纸  施工图纸    实物         记账   
    CustomProcessBase 0级
            CustomProcessBase n级（记录人机物环管n级）
                    人机物环管 关联表
                                人机物环
                                            日志
    {name} 
            {name, next}
                    {name, plan_id}
                               {step_id, type, id}
                                          {type, id, log}
    {name} 
            {name, IdCard}
                    {rel_ids, base_id}
                               {case_id, rel_id}
                                          {case_id, log}

身份证号

    八级

    人机物环管的归属、分类

    模型 id 层级 id

步骤

日志：

    时间、地点、人物、起因、经过、结果

描述：text


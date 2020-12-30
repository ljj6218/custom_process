# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



t_authority_menu = db.Table(
    'authority_menu',
    db.Column('id', db.BigInteger, server_default=db.FetchedValue()),
    db.Column('created_at', db.DateTime),
    db.Column('updated_at', db.DateTime),
    db.Column('deleted_at', db.DateTime),
    db.Column('menu_level', db.BigInteger),
    db.Column('parent_id', db.String(191)),
    db.Column('path', db.String(191)),
    db.Column('name', db.String(191)),
    db.Column('hidden', db.Integer),
    db.Column('component', db.String(191)),
    db.Column('title', db.String(191)),
    db.Column('icon', db.String(191)),
    db.Column('sort', db.BigInteger),
    db.Column('authority_id', db.String(90)),
    db.Column('menu_id', db.BigInteger),
    db.Column('keep_alive', db.Integer),
    db.Column('default_menu', db.Integer)
)



t_casbin_rule = db.Table(
    'casbin_rule',
    db.Column('p_type', db.String(100)),
    db.Column('v0', db.String(100)),
    db.Column('v1', db.String(100)),
    db.Column('v2', db.String(100)),
    db.Column('v3', db.String(100)),
    db.Column('v4', db.String(100)),
    db.Column('v5', db.String(100))
)



class CustomProcessBase(db.Model):
    __tablename__ = 'custom_process_base'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    name = db.Column(db.String(64), info='名称')
    from_url = db.Column(db.String(512), info='来源')
    to_url = db.Column(db.String(512), info='去向')



class CustomProcessBaseEnvironmentRel(db.Model):
    __tablename__ = 'custom_process_base_environment_rel'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    environment_id = db.Column(db.BigInteger)
    base_id = db.Column(db.BigInteger)



class CustomProcessBaseGoodsRel(db.Model):
    __tablename__ = 'custom_process_base_goods_rel'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    base_id = db.Column(db.BigInteger)
    goods_id = db.Column(db.BigInteger)



class CustomProcessBaseMachineRel(db.Model):
    __tablename__ = 'custom_process_base_machine_rel'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    base_id = db.Column(db.BigInteger)
    machine_id = db.Column(db.BigInteger)



class CustomProcessBaseUserRel(db.Model):
    __tablename__ = 'custom_process_base_user_rel'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    base_id = db.Column(db.BigInteger)
    user_id = db.Column(db.BigInteger)



class Environment(db.Model):
    __tablename__ = 'environment'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    name = db.Column(db.String(64), info='名称')



class ExaCustomer(db.Model):
    __tablename__ = 'exa_customers'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    customer_name = db.Column(db.String(191), info='客户名')
    customer_phone_data = db.Column(db.String(191), info='客户手机号')
    sys_user_id = db.Column(db.BigInteger, info='管理ID')
    sys_user_authority_id = db.Column(db.String(191), info='管理角色ID')



class ExaFileChunk(db.Model):
    __tablename__ = 'exa_file_chunks'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    exa_file_id = db.Column(db.BigInteger)
    file_chunk_number = db.Column(db.BigInteger)
    file_chunk_path = db.Column(db.String(191))



class ExaFileUploadAndDownload(db.Model):
    __tablename__ = 'exa_file_upload_and_downloads'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    name = db.Column(db.String(191), info='文件名')
    url = db.Column(db.String(191), info='文件地址')
    tag = db.Column(db.String(191), info='文件标签')
    key = db.Column(db.String(191), info='编号')



class ExaFile(db.Model):
    __tablename__ = 'exa_files'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    file_name = db.Column(db.String(191))
    file_md5 = db.Column(db.String(191))
    file_path = db.Column(db.String(191))
    chunk_total = db.Column(db.BigInteger)
    is_finish = db.Column(db.Integer)



t_exa_simple_uploaders = db.Table(
    'exa_simple_uploaders',
    db.Column('chunk_number', db.String(191), info='当前切片标记'),
    db.Column('current_chunk_size', db.String(191), info='当前切片容量'),
    db.Column('current_chunk_path', db.String(191), info='切片本地路径'),
    db.Column('total_size', db.String(191), info='总容量'),
    db.Column('identifier', db.String(191), info='文件标识（md5）'),
    db.Column('filename', db.String(191), info='文件名'),
    db.Column('total_chunks', db.String(191), info='切片总数'),
    db.Column('is_done', db.Integer, info='是否上传完成'),
    db.Column('file_path', db.String(191), info='文件本地路径')
)



class ExaWfLeaf(db.Model):
    __tablename__ = 'exa_wf_leaves'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    cause = db.Column(db.String(191))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)



class Good(db.Model):
    __tablename__ = 'goods'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    name = db.Column(db.String(64), info='名称')



class IdCard(db.Model):
    __tablename__ = 'id_card'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    type = db.Column(db.Integer, info='类型')
    id1 = db.Column(db.String(8))
    id2 = db.Column(db.String(8))
    id3 = db.Column(db.String(8))
    id4 = db.Column(db.String(8))
    id5 = db.Column(db.String(8))
    id6 = db.Column(db.String(8))
    id7 = db.Column(db.String(8))
    id8 = db.Column(db.String(8))



class IdCardDecode(db.Model):
    __tablename__ = 'id_card_decode'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    name = db.Column(db.String(64))



class JwtBlacklist(db.Model):
    __tablename__ = 'jwt_blacklists'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    jwt = db.Column(db.Text, info='jwt')



class Machine(db.Model):
    __tablename__ = 'machine'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    name = db.Column(db.String(64), info='名称')



class SysApi(db.Model):
    __tablename__ = 'sys_apis'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    path = db.Column(db.String(191), info='api路径')
    description = db.Column(db.String(191), info='api中文描述')
    api_group = db.Column(db.String(191), info='api组')
    method = db.Column(db.String(191), server_default=db.FetchedValue())



class SysAuthority(db.Model):
    __tablename__ = 'sys_authorities'

    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)
    authority_id = db.Column(db.String(90), primary_key=True, unique=True, info='角色ID')
    authority_name = db.Column(db.String(191), info='角色名')
    parent_id = db.Column(db.String(191), info='父角色ID')



class SysAuthorityMenu(db.Model):
    __tablename__ = 'sys_authority_menus'

    sys_base_menu_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    sys_authority_authority_id = db.Column(db.String(90), primary_key=True, nullable=False, info='角色ID')



class SysBaseMenuParameter(db.Model):
    __tablename__ = 'sys_base_menu_parameters'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    sys_base_menu_id = db.Column(db.BigInteger)
    type = db.Column(db.String(191), info='地址栏携带参数为params还是query')
    key = db.Column(db.String(191), info='地址栏携带参数的key')
    value = db.Column(db.String(191), info='地址栏携带参数的值')



class SysBaseMenu(db.Model):
    __tablename__ = 'sys_base_menus'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    menu_level = db.Column(db.BigInteger)
    parent_id = db.Column(db.String(191), info='父菜单ID')
    path = db.Column(db.String(191), info='路由path')
    name = db.Column(db.String(191), info='路由name')
    hidden = db.Column(db.Integer, info='是否在列表隐藏')
    component = db.Column(db.String(191), info='对应前端文件路径')
    sort = db.Column(db.BigInteger, info='排序标记')
    keep_alive = db.Column(db.Integer, info='附加属性')
    default_menu = db.Column(db.Integer, info='附加属性')
    title = db.Column(db.String(191), info='附加属性')
    icon = db.Column(db.String(191), info='附加属性')



class SysDataAuthorityId(db.Model):
    __tablename__ = 'sys_data_authority_id'

    sys_authority_authority_id = db.Column(db.String(90), primary_key=True, nullable=False, info='角色ID')
    data_authority_id_authority_id = db.Column(db.String(90), primary_key=True, nullable=False, info='角色ID')



class SysDictionary(db.Model):
    __tablename__ = 'sys_dictionaries'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    name = db.Column(db.String(191), info='字典名（中）')
    type = db.Column(db.String(191), info='字典名（英）')
    status = db.Column(db.Integer, info='状态')
    desc = db.Column(db.String(191), info='描述')



class SysDictionaryDetail(db.Model):
    __tablename__ = 'sys_dictionary_details'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    label = db.Column(db.String(191), info='展示值')
    value = db.Column(db.BigInteger, info='字典值')
    status = db.Column(db.Integer, info='启用状态')
    sort = db.Column(db.BigInteger, info='排序标记')
    sys_dictionary_id = db.Column(db.BigInteger, info='关联标记')



class SysOperationRecord(db.Model):
    __tablename__ = 'sys_operation_records'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    ip = db.Column(db.String(191), info='请求ip')
    method = db.Column(db.String(191), info='请求方法')
    path = db.Column(db.String(191), info='请求路径')
    status = db.Column(db.BigInteger, info='请求状态')
    latency = db.Column(db.BigInteger, info='延迟')
    agent = db.Column(db.String(191), info='代理')
    error_message = db.Column(db.String(191), info='错误信息')
    body = db.Column(db.String, info='请求Body')
    resp = db.Column(db.String, info='响应Body')
    user_id = db.Column(db.BigInteger, info='用户id')



class SysUser(db.Model):
    __tablename__ = 'sys_users'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    uuid = db.Column(db.String(191), info='用户UUID')
    username = db.Column(db.String(191), info='用户登录名')
    password = db.Column(db.String(191), info='用户登录密码')
    nick_name = db.Column(db.String(191), server_default=db.FetchedValue(), info='用户昵称')
    header_img = db.Column(db.String(191), server_default=db.FetchedValue(), info='用户头像')
    authority_id = db.Column(db.String(90), server_default=db.FetchedValue(), info='用户角色ID')



class Template(db.Model):
    __tablename__ = 'template'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    name = db.Column(db.String(64))



class WorkflowEdge(db.Model):
    __tablename__ = 'workflow_edges'

    id = db.Column(db.String(191), primary_key=True, unique=True, info='唯一标识')
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    workflow_process_id = db.Column(db.String(191), info='流程标识')
    clazz = db.Column(db.String(191), info='类型（线）')
    source = db.Column(db.String(191), info='起点节点')
    target = db.Column(db.String(191), info='目标节点')
    source_anchor = db.Column(db.BigInteger, info='起点')
    target_anchor = db.Column(db.BigInteger, info='目标点')
    description = db.Column(db.String(191), info='详细介绍')
    shape = db.Column(db.String(191), info='形状')
    label = db.Column(db.String(191), info='标题')
    hide_icon = db.Column(db.Integer, info='隐藏图标')
    condition_expression = db.Column(db.String(191), info='条件标识')
    seq = db.Column(db.String(191), info='序号')
    reverse = db.Column(db.Integer, info='是否反向')



class WorkflowEndPoint(db.Model):
    __tablename__ = 'workflow_end_points'

    workflow_edge_id = db.Column(db.String(191))
    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    x = db.Column(db.Float(asdecimal=True))
    y = db.Column(db.Float(asdecimal=True))
    index = db.Column(db.BigInteger)



class WorkflowMove(db.Model):
    __tablename__ = 'workflow_moves'

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    workflow_process_id = db.Column(db.String(191), info='工作流模板ID')
    workflow_node_id = db.Column(db.String(191), info='工作流节点ID')
    business_type = db.Column(db.String(191), info='业务标记')
    business_id = db.Column(db.BigInteger, info='业务ID')
    promoter_id = db.Column(db.BigInteger, info='当前流转发起人')
    operator_id = db.Column(db.BigInteger, info='当前流转操作人')
    action = db.Column(db.String(191), info='工作流驱动事件')
    param = db.Column(db.String(191), info='工作流驱动参数')
    is_active = db.Column(db.Integer, info='是否是活跃节点 ')



class WorkflowNode(db.Model):
    __tablename__ = 'workflow_nodes'

    id = db.Column(db.String(191), primary_key=True, unique=True, info='节点id')
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    workflow_process_id = db.Column(db.String(191), info='流程标识')
    clazz = db.Column(db.String(191), info='节点类型')
    label = db.Column(db.String(191), info='节点名称')
    type = db.Column(db.String(191), info='图标类型')
    shape = db.Column(db.String(191), info='形状')
    description = db.Column(db.String(191), info='详细介绍')
    view = db.Column(db.String(191), info='前端视图文件')
    x = db.Column(db.Float(asdecimal=True), info='x位置')
    y = db.Column(db.Float(asdecimal=True), info='y位置')
    wait_state = db.Column(db.String(191), info='等待属性')
    state_value = db.Column(db.String(191), info='等待值')
    to = db.Column(db.String(191), info='收件人')
    subject = db.Column(db.String(191), info='标题')
    content = db.Column(db.String(191), info='内容')
    cycle = db.Column(db.String(191), info='循环时间')
    duration = db.Column(db.String(191), info='持续时间')
    hide_icon = db.Column(db.Integer, info='是否隐藏图标')
    due_date = db.Column(db.DateTime, info='到期时间')
    assign_type = db.Column(db.String(191), info='审批类型')
    assign_value = db.Column(db.String(191), info='审批类型值')
    success = db.Column(db.Integer, info='是否成功')



class WorkflowProcess(db.Model):
    __tablename__ = 'workflow_processes'

    id = db.Column(db.String(191), primary_key=True, unique=True, info='流程标识')
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    name = db.Column(db.String(191), info='流程名称')
    category = db.Column(db.String(191), info='分类')
    clazz = db.Column(db.String(191), info='类型')
    label = db.Column(db.String(191), info='流程标题')
    hide_icon = db.Column(db.Integer, info='是否隐藏图标')
    description = db.Column(db.String(191), info='详细介绍')
    view = db.Column(db.String(191), info='前端视图文件')



class WorkflowStartPoint(db.Model):
    __tablename__ = 'workflow_start_points'

    workflow_edge_id = db.Column(db.String(191))
    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime, index=True)
    x = db.Column(db.Float(asdecimal=True))
    y = db.Column(db.Float(asdecimal=True))
    index = db.Column(db.BigInteger)

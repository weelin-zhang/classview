# classview
基类视图简单用法
api
swagger
permissions




app -->图书管理,测试form,modelform,updteview, createview,listview,detailview


api-->集成swagger

blog --->测试permissions

deployment---->实现权限分级，admin--leader--staff



# django-guardian 重要方法:

from guardian.shortcuts import *

def assign_perm(perm, user_or_group, obj=None):

    '''
        针对(object permission, gloal permission)
        新增user, group的object或者global permission
        添加object permission 或者 global permission
        当obj=None时， 添加的 global permission, 该permission并不会作用到某一个obj上, 该user,group必须重新获取才能检查得到新添加权限
        当obj!=None时，添加的 object permission

        当obj==None时, 参数perm必须是 app_label.codenam
    '''
    pass



def remove_perm(perm, user_or_group=None, obj=None):
    '''
        针对(object permission, gloal permission)
        当obj == None 删除user或者group的global  permission, 该permission的移除不会作用到某一个obj上, 该user,group必须重新获取才能检查得到权限移除
        当obj != None 删除user或者group的object  permission
        当obj==None时, 参数perm必须是 app_label.codenam

        当删除global permisson时, 没有返回 None
        当删除object permisson时,返回; (1, {'guardian.UserObjectPermission': 1}) or (0, {'guardian.UserObjectPermission': 0})

    '''


def get_perms(user_or_group, obj):
    '''
        针对(object permission)
        获取user或者group针对obj拥有的object permission
        返回此user or group所拥有的所有的object permission的列表:
        eg: ['change_post']
    '''
    pass

def get_user_perms(user, obj):
    '''
        针对(object permission)
        获取user针对obj拥有的object permission
        返回此user or group所拥有的所有的object permission的列表:
        eg: <QuerySet ['change_post', 'delete_post']>
    '''
    pass

def get_group_perms(group, obj):
    '''
        针对(object permission)
        获取user针对obj拥有的object permission
        返回此group所拥有的所有的object permission的列表:
        eg: <QuerySet ['change_post', 'delete_post']>
    '''
    pass

def get_perms_for_model(cls):
    '''
        cls: Model模型
        返回: 这个模型拥有的所有的Permission集合:
        <QuerySet [<Permission: blog | post | Can add post>, <Permission: blog | post | Can change post>, <Permission: blog | post | Can delete post>, <Permission: blog | post | give favor post>, <Permission: blog | post | remove favor post>]>
    '''


def get_users_with_perms(obj, attach_perms=False, with_superusers=False, with_group_users=True):
    """
        针对(object permission)
        获得拥有给定对象obj的任一object permission的所有user的集合(返回拥有对象obj的object permission的user)
        eg: <QuerySet [<User: zhangweijian>, <User: zwj>]>

        参数:
            attach_perms:默认 False
                if attach_perms==True  返回格式: {<User: zhangweijian>: ['add_post'], <User: zwj>: ['change_post', 'delete_post']}
                if attach_perms==False 返回格式: <QuerySet [<User: zhangweijian>, <User: zwj>]>
            with_superusers: 默认 False
                if with_superusers==True, 结果中包含超级用户,比如admin

            with_group_users: 默认 True
                if with_group_users==True, 考虑从gruop继承来的该obj对象的object permission的user
                if with_group_usres==False, 那么不考虑从gruop继承来的该obj对象的object permission的user
    """


def get_groups_with_perms(obj, attach_perms=False):
    """
        针对(object permission)
        获得拥有给定对象obj的任一object permission的所有group的集合(返回拥有对象obj的object permission的group)
        eg: <QuerySet [<Group: delpost>]>

    """





def get_objects_for_user(user, perms, klass=None, use_groups=True, any_perm=False,
                         with_superuser=True, accept_global_perms=True):
    """
        默认针对(object permission), 当accept_global_perms=True时, global permission可以计算在内
        该方法通过传入 user, perms(app_label.codename string or list of app_label.codename string)来确定满足条件的objects
        返回用户对其拥有perms的objects, perms为列表时取用交集.
        eg: <QuerySet [<Post: patch post1 title>]>

        user: 用户
        perms: 用户需要拥有的object permissions(perms中的 perm必须属于同一个Model, 即相同的app_label)
        klass: Model or queryset or manager
        use_groups: 默认为True, user表示匹配的object permission可以继承自group
        any_perm: 默认Fasle, 否则perms中有一个就算
        with_superuser: 默认True, 当为False时，哪怕user=admin也返回一个空的集合
        accept_global_perms: 默认True, accept_global_perms可以被当做object permission计算在内, 生效前提是with_superuser=True

    """


def get_objects_for_group(group, perms, klass=None, any_perm=False, accept_global_perms=True):
    """
        默认针对(object permission), 当accept_global_perms=True时, global permission可以计算在内
        group: 用户组
        perms: 用户需要拥有的object permissions(perms中的 perm必须属于同一个Model, 即相同的app_label)
        klass: Model or queryset or manager
        accept_global_perms: 默认True, accept_global_perms可以被当做object permission计算在内

    """





# classview
基类视图简单用法
api
swagger
permissions




app -->图书管理,测试form,modelform,updteview, createview,listview,detailview


api-->集成swagger

blog --->测试permissions

deployment---->实现权限分级，admin--leader--staff,基于project,使用object permission实现
superuser可以给任何人员分配权限,
顶级用户可以给其下一级所有小组leader分配权限(前提自己有某一对象的权限)
小组leader可以为任何一个一线研发任务分配权限




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

        补充:
          django.contrib.auth.models.User的实例的定义的has_perm方法:
          1. user.has_perm(perm, obj)表示object permission
          2. user.has_perm(perm)表示global permission
          3. 表示global permission时, 要用app_label.codename
    '''
    pass



def get_user_perms(user, obj):
    '''
        针对(object permission)
        获取user针对obj拥有的object permission
        返回此user or group所拥有的所有的object permission的列表:
        eg: <QuerySet ['change_post', 'delete_post']>

        补充: superuser无法使用get_user_perms(admin, obj)获得object perms
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
        klass: 当没有个klas时, perm是必须是完整的(app_label.codename),Model or queryset or manager(manager时,输出为管理器对象)
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
        klass: Model or queryset or manager(使用manager)时，结果也是个Manager
        accept_global_perms: 默认True, accept_global_perms可以被当做object permission计算在内

    """



class ObjectPermissionChecker(object):
        """
        def __init__(self, user_or_group=None):
        """
        Constructor for ObjectPermissionChecker.
        :param user_or_group: should be an ``User``, ``AnonymousUser`` or
          ``Group`` instance
        """
        self.user, self.group = get_identity(user_or_group)
        self._obj_perms_cache = {}

    def has_perm(self, perm, obj):
        """
        检查用户后者组是否有给定的perm权限
        """
        # 用户没激活没有权限
        if self.user and not self.user.is_active:
            return False
        # 超级用户肯定有权限
        elif self.user and self.user.is_superuser:
            return True
        # 确定能从app_label.codename拿到codename
        perm = perm.split('.')[-1]

        # 普通激活用户需要具体判定
        return perm in self.get_perms(obj)

    def get_group_filters(self, obj):
        pass

    def get_user_filters(self, obj):
        pass

    def get_user_perms(self, obj):
        ctype = get_content_type(obj)

        perms_qs = Permission.objects.filter(content_type=ctype)
        user_filters = self.get_user_filters(obj)
        user_perms_qs = perms_qs.filter(**user_filters)
        user_perms = user_perms_qs.values_list("codename", flat=True)

        return user_perms

    def get_group_perms(self, obj):
        ctype = get_content_type(obj)

        perms_qs = Permission.objects.filter(content_type=ctype)
        group_filters = self.get_group_filters(obj)
        group_perms_qs = perms_qs.filter(**group_filters)
        group_perms = group_perms_qs.values_list("codename", flat=True)

        return group_perms

    def get_perms(self, obj):
        """
        Returns list of ``codename``'s of all permissions for given ``obj``.
        """

    def get_local_cache_key(self, obj):
        """
        Returns cache key for ``_obj_perms_cache`` dict.
        """
        ctype = get_content_type(obj)
        return (ctype.id, force_text(obj.pk))

    def prefetch_perms(self, objects):
        """
        执行此方法后将会,提前把self.user对应的所有潜在的object perm计算出来供get_perms/get_user_perms/../has_perm使用,
        其结果被存储到了self._obj_perms_cache[key]中,起到了缓存作用.

        返回格式为字典:
        key: objects对应的model的content_type的id和object.id组成的元组
        value: self.user针对object.id拥有的所有权限

        {(13, '1'): ['deploy_project'], (13, '2'): ['add_project'], (13, '3'): [], (13, '4'): []}

        Prefetches the permissions for objects in ``objects`` and puts them in the cache.

        """
        if self.user and not self.user.is_active:
            return []

        User = get_user_model()
        pks, model, ctype = _get_pks_model_and_ctype(objects)

        if self.user and self.user.is_superuser:
            perms = list(chain(
                *Permission.objects
                .filter(content_type=ctype)
                .values_list("codename")))

            for pk in pks:
                key = (ctype.id, force_text(pk))
                self._obj_perms_cache[key] = perms

            return True

        group_model = get_group_obj_perms_model(model)

        if self.user:
            fieldname = 'group__%s' % (
                User.groups.field.related_query_name(),
            )
            group_filters = {fieldname: self.user}
        else:
            group_filters = {'group': self.group}

        if group_model.objects.is_generic():
            group_filters.update({
                'content_type': ctype,
                'object_pk__in': pks,
            })
        else:
            group_filters.update({
                'content_object_id__in': pks
            })

        if self.user:
            model = get_user_obj_perms_model(model)
            user_filters = {
                'user': self.user,
            }

            if model.objects.is_generic():
                user_filters.update({
                    'content_type': ctype,
                    'object_pk__in': pks
                })
            else:
                user_filters.update({
                    'content_object_id__in': pks
                })

            # Query user and group permissions separately and then combine
            # the results to avoid a slow query
            user_perms_qs = model.objects.filter(**user_filters).select_related('permission')
            group_perms_qs = group_model.objects.filter(**group_filters).select_related('permission')
            perms = chain(user_perms_qs, group_perms_qs)
        else:
            perms = chain(
                *(group_model.objects.filter(**group_filters).select_related('permission'),)
            )

        # initialize entry in '_obj_perms_cache' for all prefetched objects
        for obj in objects:
            key = self.get_local_cache_key(obj)
            if key not in self._obj_perms_cache:
                self._obj_perms_cache[key] = []

        for perm in perms:
            if type(perm).objects.is_generic():
                key = (ctype.id, perm.object_pk)
            else:
                key = (ctype.id, force_text(perm.content_object_id))

            self._obj_perms_cache[key].append(perm.permission.codename)

        return True
        """


def permission_required:
    pass
    """
        @permission_required('auth.change_user', return_403=True)
        def my_view(request):
            return HttpResponse('Hello')

        @permission_required('auth.change_user', (User, 'username', 'username'))
        def my_view(request, username):
            '''
            auth.change_user permission would be checked based on given
            'username'. If view's parameter would be named ``name``, we would
            rather use following decorator::

                @permission_required('auth.change_user', (User, 'username', 'name'))
            '''
            user = get_object_or_404(User, username=username)
            return user.get_absolute_url()

        @permission_required('auth.change_user',
            (User, 'username', 'username', 'groups__name', 'group_name'))
        def my_view(request, username, group_name):
            '''
            Similar to the above example, here however we also make sure that
            one of user's group is named same as request's ``group_name`` param.
            '''
            user = get_object_or_404(User, username=username,
            group__name=group_name)
            return user.get_absolute_url()



        # 测试object permission 装饰器
        from guardian.decorators import permission_required_or_403

        from django.http import HttpResponse
        @permission_required_or_403("blog.delete_post", (Post, 'pk', 'pk'))
        def post_detail(request, pk):
            p = Post.objects.get(pk=pk)
            return HttpResponse(p.title)

    """


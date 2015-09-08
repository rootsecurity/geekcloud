# coding:utf-8
from django.conf.urls import patterns, include, url
from jasset.views import *

urlpatterns = patterns('',
    url(r'^asset_add/$', asset_add),
    # url(r"^host_add_multi/$", host_add_batch),
    url(r'^group_add/$', group_add),
    url(r'^group_list/$', group_list),
    url(r'^asset_list/$', asset_list),
    url(r'^asset_del/$', asset_del),
    url(r"^asset_detail/$", asset_detail),
    url(r'^asset_edit/$', asset_edit),
    # url(r'^search/$', host_search),
    # url(r"^host_detail/$", host_detail),
    # url(r"^dept_host_ajax/$", dept_host_ajax),
    # url(r"^show_all_ajax/$", show_all_ajax),
    # url(r'^group_edit/$', group_edit),
    # url(r'^group_list/$', group_list),
    # url(r'^group_detail/$', group_detail),
    # url(r'^group_del_host/$', group_del_host),
    # url(r'^group_del/$', group_del),
    # url(r'^host_edit/batch/$', host_edit_batch),
    # url(r'^host_edit_common/batch/$', host_edit_common_batch),
)
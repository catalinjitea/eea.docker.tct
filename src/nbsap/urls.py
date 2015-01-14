from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView, TemplateView
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # homepage URLs
    url(r'^$', 'nbsap.views.goals', {'code': 'a'}, name='goals'),
    url(r'^goals/(?P<code>[\w\-]+)$', 'nbsap.views.goals', name='goals'),
    url(r'^crashme$', 'nbsap.views.crashme', name='crashme'),

    url(r'^implementation$', 'nbsap.views.implementation', name='implementation'),
    url(r'^implementation/intro$', 'nbsap.views.implementation_page', name='implementation_page'),
    url(r'^implementation/(?P<code>((\d+\.)*\d+$))$', 'nbsap.views.implementation', name='implementation'),

    url(r'^eu_targets$', 'nbsap.views.eu_targets', {'code': '1'}, name='eu_targets'),
    url(r'^eu_targets/(?P<code>[\w\-]+)$', 'nbsap.views.eu_targets', name='eu_targets'),
    url(r'^eu_targets/(?P<target_id>[\w\-]+)/objectives/export/preview/$', 'nbsap.views.eu_target_nat_strategy_export_preview', name='nat_strategy_export_preview'),
    url(r'^eu_targets/(?P<target_id>[\w\-]+)/objectives/export/$', 'nbsap.views.eu_target_nat_strategy_export', name='nat_strategy_export'),

    url(r'^indicator/(?P<pk>(\d+))$', 'nbsap.views.indicator', name='indicator'),

    url(r'^objectives$', 'nbsap.views.nat_strategy', name='nat_strategy'),
    url(r'^objectives\.xlsx$', 'nbsap.views.nat_strategy_download', name='nat_strategy_download'),
    url(r'^objectives/(?P<code>[\w\.\-]+)$', 'nbsap.views.nat_strategy', name='nat_strategy'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^i18n/', include('django.conf.urls.i18n')),

    # Django generic view classes
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),

    # Disallow search engines to index data
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

    # URLs for mapping form
    url(r'^goals/title$',
            'nbsap.views.get_goal_title',
            name='goal_title'),
    url(r'^goals/title/(?P<pk>[\w\-]+)$',
            'nbsap.views.get_goal_title',
            name='goal_title'),

     url(r'^actions/title$',
            'nbsap.views.get_action_title',
            name='action_title'),
    url(r'^actions/title/(?P<pk>[\w\-]+)$',
            'nbsap.views.get_action_title',
            name='action_title'),

    url(r'^eu_targets/title$',
            'nbsap.views.get_eu_target_title',
            name='eu_target_title'),
    url(r'^eu_targets/title/(?P<pk>[\w\-]+)$',
            'nbsap.views.get_eu_target_title',
            name='eu_target_title'),
    url(r'^eu_targets/actions/(?P<pk>[\w\-]+)$',
            'nbsap.views.get_actions_for_target',
            name='target_action'),



    url(r'^aichi_targets/title$',
            'nbsap.views.get_aichi_target_title',
            name='aichi_target_title'),
    url(r'^aichi_targets/title/(?P<pk>[\w\-]+)$',
            'nbsap.views.get_aichi_target_title',
            name='aichi_target_title'),

    url(r'^objectives/title$',
            'nbsap.views.get_national_objective_title',
            name='objective_title'),
    url(r'^objectives/title/(?P<pk>[\w\-]+)$',
            'nbsap.views.get_national_objective_title',
            name='objective_title'),

    # othe URLs
    url(r'^tinymce/', include('tinymce.urls')),


    # authentication URLs
    url(r'^accounts/login/$', 'nbsap.views.login_view', name='login'),
    url(r'^accounts/logout/$', 'nbsap.views.logout_view', name='logout'),

    # administration URLs
    url(r'^administration/$',
            'nbsap.views.admin_home',
            name='admin_home'),

    url(r'^administration/targets/$',
            'nbsap.views.list_eu_targets',
            name='list_eu_targets'),

    url(r'^administration/targets/add/',
        'nbsap.views.edit_eu_strategy_target',
        name='edit_eu_target'),

    url(r'^administration/targets/(?P<pk>[\w\-]+)/$',
        'nbsap.views.view_eu_strategy_target',
        name='view_eu_strategy_target'),

    url(r'^administration/targets/(?P<pk>[\w\-]+)/edit/$',
        'nbsap.views.edit_eu_strategy_target',
        name='edit_eu_strategy_target'),

    url(r'^administration/targets/(?P<pk>[\w\-]+)/delete/$',
        'nbsap.views.delete_eu_strategy_target',
        name='delete_eu_strategy_target'),

    url(r'^administration/objectives/$',
            'nbsap.views.list_national_objectives',
            name='list_national_objectives'),

    url(r'^administration/objectives/(?P<pk>[\w\-]+)$',
            'nbsap.views.view_national_objective',
            name='view_national_objective'),

    url(r'^administration/objectives/(?P<pk>[\w\-]+)/edit$',
            'nbsap.views.edit_national_objective',
            name='edit_national_objective'),

    url(r'^administration/objectives/(?P<parent>[\w\-]+)/add$',
            'nbsap.views.edit_national_objective',
            name='edit_national_objective'),

    url(r'^administration/objectives/add/$',
            'nbsap.views.edit_national_objective',
             name='edit_national_objective'),

    url(r'^administration/objectives/(?P<pk>[\w\-]+)/delete',
            'nbsap.views.delete_national_objective',
             name='delete_national_objective'),

    url(r'^administration/objectives/(?P<objective>[\w\-]+)/actions/add',
            'nbsap.views.edit_national_action',
             name='edit_national_action'),

    url(r'^administration/objectives/(?P<objective>[\w\-]+)/actions/(?P<pk>[\w\-]+)/edit',
            'nbsap.views.edit_national_action',
            name='edit_national_action'),

    url(r'^administration/objectives/(?P<objective>[\w\-]+)/actions/(?P<pk>[\w\-]+)/$',
            'nbsap.views.view_national_action',
            name='view_national_action'),

    url(r'^administration/objectives/(?P<objective>[\w\-]+)/actions/(?P<pk>[\w\-]+)/delete',
            'nbsap.views.delete_national_action',
            name='delete_national_action'),

    url(r'^administration/mapping/$',
            'nbsap.views.list_national_strategy',
            name='list_national_strategy'),

    url(r'^administration/mapping/add$',
            'nbsap.views.edit_national_strategy',
            name='edit_national_strategy'),

    url(r'^administration/mapping/(?P<pk>[\w\-]+)/add$',
            'nbsap.views.edit_national_strategy',
            name='edit_national_strategy'),

    url(r'^administration/mapping/(?P<strategy>[\w\-]+)/delete$',
            'nbsap.views.delete_national_strategy',
            name='delete_national_strategy'),

    url(r'^administration/pages$', 'nbsap.views.admin_pages', name='admin_pages'),
    url(r'^administration/page/(?P<handle>[\w\-]+)/edit$', 'nbsap.views.admin_page', name='admin_page'),

)

# Django Rosetta support for translation
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('', url(r'^translate/', include('rosetta.urls')),)


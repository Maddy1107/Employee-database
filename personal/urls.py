from django.conf.urls import url
from . import views


app_name = 'personal'

urlpatterns = [

    url(r'^employees/generators/(?P<emp_id>[0-9]+)$', views.generator, name='generate'),

    url(r'^joining_letter/(?P<emp_id>[0-9]+)$', views.generate_JL,name='pdf'),

    url(r'^NOC/(?P<emp_id>[0-9]+)$', views.generate_NOC,name='pdf1'),

    url(r'^confirmation_letter/(?P<emp_id>[0-9]+)$', views.generate_CL,name='pdf2'),

    url(r'^COD/(?P<emp_id>[0-9]+)$', views.generate_COD,name='pdf3'),

    url(r'^offer_letter/(?P<emp_id>[0-9]+)$', views.generate_OL,name='pdf4'),

    url(r'^exit/(?P<emp_id>[0-9]+)$', views.generate_EI,name='pdf5'),

    url(r'^IL/(?P<emp_id>[0-9]+)$', views.generate_IL,name='pdf6'),

    url(r'^transfer/(?P<emp_id>[0-9]+)$', views.generate_transfer,name='pdf7'),

    url(r'^promotion/(?P<emp_id>[0-9]+)$', views.generate_PL,name='pdf8'),

    url(r'^$', views.index, name='index'),

    url(r'^admin_home$', views.index2, name='index1'),

    url(r'^export/xls/$', views.export_users_xls, name='export_users_xls'),

    url(r'^employees/$', views.emps, name='employees'),

    url(r'^admin_employees/$', views.emps2, name='employees1'),

    url(r'^employees/(?P<emp_id>[0-9]+)$', views.details, name='detail'),

    url(r'^admin_employees/(?P<emp_id>[0-9]+)$', views.details1, name='detail1'),

    url(r'^add/$',views.EmpCreate.as_view(), name='emp-add'),

    url(r'^add/fam/$',views.EmpCreate1.as_view(), name='fam-add'),

    url(r'^add/med/$',views.EmpCreate2.as_view(), name='med-add'),

    url(r'^add/emer/$',views.EmpCreate3.as_view(), name='emer-add'),

    url(r'^add/edu/$',views.EmpCreate4.as_view(), name='edu-add'),

    url(r'^add/empl/$',views.EmpCreate5.as_view(), name='empl-add'),

    url(r'^add/ref/$',views.EmpCreate6.as_view(), name='ref-add'),

    url(r'^addxlist/(?P<emp_id>[0-9]+)$',views.addxlist, name='addx'),

    url(r'^addx/(?P<emp_id>[0-9]+)$',views.EmpCreatex.as_view(), name='emp-add1'),

    url(r'^addx/fam/(?P<emp_id>[0-9]+)$',views.EmpCreatex1.as_view(), name='fam-add1'),

    url(r'^addx/med/(?P<emp_id>[0-9]+)$',views.EmpCreatex2.as_view(), name='med-add1'),

    url(r'^addx/emer/(?P<emp_id>[0-9]+)$',views.EmpCreatex3.as_view(), name='emer-add1'),

    url(r'^addx/edu/(?P<emp_id>[0-9]+)$',views.EmpCreatex4.as_view(), name='edu-add1'),

    url(r'^addx/empl/(?P<emp_id>[0-9]+)$',views.EmpCreatex5.as_view(), name='empl-add1'),

    url(r'^addx/ref/(?P<emp_id>[0-9]+)$',views.EmpCreatex6.as_view(), name='ref-add1'),

    url(r'^add/success/$', views.success, name='success'),

    url(r'^employees/updatelist/(?P<emp_id>[0-9]+)$', views.UpdateList, name='update'),

    url(r'^employees/update/(?P<emp_id>[0-9]+)$',views.EmpUpdate.as_view(), name='emp-update'),

    url(r'^employees/update/(?P<emp_id>[0-9]+)/fam/$',views.EmpUpdate1.as_view(), name='fam-update'),

    url(r'^employees/update/(?P<emp_id>[0-9]+)/med/$',views.EmpUpdate2.as_view(), name='med-update'),

    url(r'^employees/update/(?P<emp_id>[0-9]+)/emer/$',views.EmpUpdate3.as_view(), name='emer-update'),

    url(r'^employees/update/(?P<emp_id>[0-9]+)/qual/$',views.EmpUpdate4.as_view(), name='qual-update'),

    url(r'^employees/update/(?P<emp_id>[0-9]+)/empl/$',views.EmpUpdate5.as_view(), name='empl-update'),

    url(r'^employees/update/(?P<emp_id>[0-9]+)/ref/$',views.EmpUpdate6.as_view(), name='ref-update'),

    url(r'^employees/(?P<emp_id>[0-9]+)/delete$',views.EmpDelete.as_view(), name='emp-delete'),
]

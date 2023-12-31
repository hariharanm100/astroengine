from django.urls import path
from . import views

urlpatterns = [
    path('', views.multiple4_home, name="multiple4Home"),
    path('multi4Data/', views.multi4_data, name="multi4Data"),
    path('addCombinationGroupNames/', views.add_combination_group_names, name="addCombinationGroupNames"),
    path('add_combination_group_names_req/', views.add_combination_group_names_req, name="addCombinationGroupNamesReq"),
    path('viewCombGroupName/', views.view_comb_group_name, name="viewCombGroupName"),
    path('updateCombGroupName/', views.update_comb_group_name, name="updateCombGroupName"),
    path('updateCombGroupNameReq/', views.update_comb_group_name_req, name="updateCombGroupNameReq"),
    path('deleteCombinationGroupName/', views.delete_combination_group_name, name="deleteCombinationGroupName"),
    path('addCombinationChanger/', views.add_combination_changer, name="addCombChanger"),
    path('addCombinationChangerReq/', views.add_combination_changer_req, name="addCombinationChangerReq"),
    path('viewCombChanger/', views.view_comb_changer, name="viewCombChanger"),
    path('updateCombChanger/', views.update_combination_changer, name="updateCombChanger"),
    path('updateCombChangerReq/', views.update_comb_changer_req, name="updateCombChangerReq"),
    path('deleteCombinationChanger/', views.delete_combination_changer, name="deleteCombChanger"),
    path('multiple1ChartSave/', views.multiple1_chart_save, name="multiple1ChartSave"),
    path('m1ChartsView/', views.m1charts_view, name="m1ChartsView"),
    path('m1ChartsDelete/', views.m1charts_delete, name="m1ChartsDelete"),
    path('m1ChartsView/m1ChartsGenerate/<id>/', views.m1charts_generate, name="m1ChartsGenerate"),
    path('multiple2ChartSave/', views.multiple2_chart_save, name="multiple2ChartSave"),
    path('m2ChartsView/', views.m2charts_view, name="m2ChartsView"),
    path('m2ChartsDelete/', views.m2charts_delete, name="m2ChartsDelete"),
    path('m2ChartsView/m2ChartsGenerate/<id>/', views.m2charts_generate, name="m2ChartsGenerate"),
    path('multiple3ChartSave/', views.multiple3_chart_save, name="multiple3ChartSave"),
    path('m3ChartsView/', views.m3charts_view, name="m3ChartsView"),
    path('m3ChartsDelete/', views.m3charts_delete, name="m3ChartsDelete"),
    path('m3ChartsView/m3ChartsGenerate/<id>/', views.m3charts_generate, name="m3ChartsGenerate"),
    path('downloadableFiles/', views.downloadable_files, name="downloadableFiles"),
    path('downloadableCombChanger/', views.downloadable_comb_changer, name="downloadableCombChanger"),
    path('downloadablePltChanger/', views.downloadable_plt_changer, name="downloadablePltChanger"),
    path('downloadableCategory/', views.downloadable_category, name="downloadableCategory"),
    path('downloadablePoints/', views.downloadable_combination_points, name="downloadablePoints"),
    path('combinationPltReq/', views.combination_plt_req, name="combinationPltReq"),
    path('multiple4ChartSave/', views.multiple4_chart_save, name="multiple4ChartSave"),
    path('m4ChartsView/', views.m4charts_view, name="m4ChartsView"),
    path('m4ChartsView/m4ChartsGenerate/<id>/', views.m4charts_generate, name="m4ChartsGenerate"),
    path('m4ChartsDelete/', views.m4charts_delete, name="m4ChartsDelete"),
    path('applyingcombchg/', views.applying_combination_changers, name="applyingCombChg"),
    path('savingCombiantionPoints/', views.saving_combiantion_points, name="savingCombiantionPoints"),
    path('deleteCombiantionPoints/', views.delete_combiantion_points, name="deleteCombiantionPoints"),
    path('multiple5Home/', views.multiple5_home, name="multiple5Home"),
    path('multi5Data/', views.multi5_data, name="multi5Data"),

]
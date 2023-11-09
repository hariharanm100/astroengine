from datetime import date, datetime, timedelta
from django.http import HttpResponse, JsonResponse
from numpy import savez_compressed
import pandas as pd
from persontoperson.p1conp2 import *
from persontoperson.models import distance_multiplier
from django_pandas.io import read_frame
from persontoperson.personone import single_concatenation_table, single_points_table, point_planets_planet_aspects
from persontoperson.singledegree import onematch
from .models import DateLisDB


def dm_data():
    data = distance_multiplier.objects.all()
    data = read_frame(data)
    return data


def distance_between_planets(distance_df, dm_data_df):
    df1 = distance_df.copy()
    df2 = dm_data_df.copy()
    Su_dp_lst = []
    Mo_dp_lst = []
    Me_dp_lst = []
    Ma_dp_lst = []
    Ju_dp_lst = []
    Ve_dp_lst = []
    Sa_dp_lst = []
    Ra_dp_lst = []
    Ke_dp_lst = []
    As_dp_lst = []
    dp_total_lst = []
    for index, row in df1.iterrows():
        if len(str(row.Su_Conc)) > 1:
            try:
                temp = (df2.loc[df2['distance'] == round(row.Su_Dis_lst,1)]["multiplier"].values[0])
                Su_dp_lst.append(row.Su_Point * float(temp))
            except Exception as e:
                Su_dp_lst.append(0)
        else:
            Su_dp_lst.append(0)

        if len(str(row.Mo_Conc)) > 1:
            temp = (df2.loc[df2['distance'] == round(row.Mo_Dis_lst, 1)]["multiplier"].values[0])
            Mo_dp_lst.append(row.Mo_Point * float(temp))
        else:
            Mo_dp_lst.append(0)

        if len(str(row.Me_Conc)) > 1:
            temp = (df2.loc[df2['distance'] == round(row.Me_Dis_lst, 1)]["multiplier"].values[0])
            Me_dp_lst.append(row.Me_Point * float(temp))
        else:
            Me_dp_lst.append(0)

        if len(str(row.Ma_Conc)) > 1:
            temp = (df2.loc[df2['distance'] == round(row.Ma_Dis_lst, 1)]["multiplier"].values[0])
            Ma_dp_lst.append(row.Ma_Point * float(temp))
        else:
            Ma_dp_lst.append(0)

        if len(str(row.Ju_Conc)) > 1:
            temp = (df2.loc[df2['distance'] == round(row.Ju_Dis_lst, 1)]["multiplier"].values[0])
            Ju_dp_lst.append(row.Ju_Point * float(temp))
        else:
            Ju_dp_lst.append(0)

        if len(str(row.Ve_Conc)) > 1:
            temp = (df2.loc[df2['distance'] == round(row.Ve_Dis_lst, 1)]["multiplier"].values[0])
            Ve_dp_lst.append(row.Ve_Point * float(temp))
        else:
            Ve_dp_lst.append(0)

        if len(str(row.Sa_Conc)) > 1:
            temp = (df2.loc[df2['distance'] == round(row.Sa_Dis_lst, 1)]["multiplier"].values[0])
            Sa_dp_lst.append(row.Sa_Point * float(temp))
        else:
            Sa_dp_lst.append(0)

        if len(str(row.Ra_Conc)) > 1:
            temp = (df2.loc[df2['distance'] == round(row.Ra_Dis_lst, 1)]["multiplier"].values[0])
            Ra_dp_lst.append(row.Ra_Point * float(temp))
        else:
            Ra_dp_lst.append(0)

        if len(str(row.Ke_Conc)) > 1:
            temp = (df2.loc[df2['distance'] == round(row.Ke_Dis_lst, 1)]["multiplier"].values[0])
            Ke_dp_lst.append(row.Ke_Point * float(temp))
        else:
            Ke_dp_lst.append(0)

        if len(str(row.As_Conc)) > 1:
            temp = (df2.loc[df2['distance'] == round(row.As_Dis_lst, 1)]["multiplier"].values[0])
            As_dp_lst.append(row.As_Point * float(temp))
        else:
            As_dp_lst.append(0)
    df = pd.DataFrame(columns=['type'])
    type_list = ["Conj", "180", "120<", ">120", "90<", ">90", "60<", ">60"]
    for i in type_list:
        lst = list_to_list_of_lists([i for j in range(10)])
        for k in lst:
            df.loc[len(df)] = k
    df.loc[len(df)] = [">150"]
    df['planet'] = (["Su", "Mo", "Me", "Ma", "Ju", "Ve", "Sa", "Ra", "Ke", "As"] * (len(df) // 2 + 1))[:len(df)]
    df.loc[df.type == ">150", "planet"] = "Ma"
    if Su_dp_lst[-1] != 0:
        Su_dp_lst[-1] = (Su_dp_lst[-1] * 1.5)
    if Mo_dp_lst[-1] != 0:
        Mo_dp_lst[-1] = (Mo_dp_lst[-1] * 1.5)
    if Me_dp_lst[-1] != 0:
        Me_dp_lst[-1] = (Me_dp_lst[-1] * 1.5)
    if Ma_dp_lst[-1] != 0:
        Ma_dp_lst[-1] = (Ma_dp_lst[-1] * 1.5)
    if Ju_dp_lst[-1] != 0:
        Ju_dp_lst[-1] = (Ju_dp_lst[-1] * 1.5)
    if Ve_dp_lst[-1] != 0:
        Ve_dp_lst[-1] = (Ve_dp_lst[-1] * 1.5)
    if Sa_dp_lst[-1] != 0:
        Sa_dp_lst[-1] = (Sa_dp_lst[-1] * 1.5)
    if Ra_dp_lst[-1] != 0:
        Ra_dp_lst[-1] = (Ra_dp_lst[-1] * 1.5)
    if Ke_dp_lst[-1] != 0:
        Ke_dp_lst[-1] = (Ke_dp_lst[-1] * 1.5)
    if As_dp_lst[-1] != 0:
        As_dp_lst = (As_dp_lst[-1] * 1.5)
    df["Su_dp_lst"] = Su_dp_lst
    df["Mo_dp_lst"] = Mo_dp_lst
    df["Me_dp_lst"] = Me_dp_lst
    df["Ma_dp_lst"] = Ma_dp_lst
    df["Ju_dp_lst"] = Ju_dp_lst
    df["Ve_dp_lst"] = Ve_dp_lst
    df["Sa_dp_lst"] = Sa_dp_lst
    df["Ra_dp_lst"] = Ra_dp_lst
    df["Ke_dp_lst"] = Ke_dp_lst
    df["As_dp_lst"] = As_dp_lst
    for index, row in df.iterrows():
        if row.type == "Conj":
            dp_total_lst.append((row.Su_dp_lst + row.Mo_dp_lst + row.Me_dp_lst + row.Ma_dp_lst  + row.Ju_dp_lst
                 + row.Ve_dp_lst + row.Sa_dp_lst + row.Ra_dp_lst + row.Ke_dp_lst + row.As_dp_lst)*2)
        if row.type == "180":
            dp_total_lst.append((row.Su_dp_lst + row.Mo_dp_lst + row.Me_dp_lst + row.Ma_dp_lst + row.Ju_dp_lst
                                 + row.Ve_dp_lst + row.Sa_dp_lst + row.Ra_dp_lst + row.Ke_dp_lst + row.As_dp_lst) * 1.5)
        if row.type == "120<":
            dp_total_lst.append((row.Su_dp_lst + row.Mo_dp_lst + row.Me_dp_lst + row.Ma_dp_lst + row.Ju_dp_lst
                                 + row.Ve_dp_lst + row.Sa_dp_lst + row.Ra_dp_lst + row.Ke_dp_lst + row.As_dp_lst))
        if row.type == ">120":
            dp_total_lst.append((row.Su_dp_lst + row.Mo_dp_lst + row.Me_dp_lst + row.Ma_dp_lst + row.Ju_dp_lst
                                 + row.Ve_dp_lst + row.Sa_dp_lst + row.Ra_dp_lst + row.Ke_dp_lst + row.As_dp_lst))
        if row.type == "90<":
            dp_total_lst.append((row.Su_dp_lst + row.Mo_dp_lst + row.Me_dp_lst + row.Ma_dp_lst + row.Ju_dp_lst
                                 + row.Ve_dp_lst + row.Sa_dp_lst + row.Ra_dp_lst + row.Ke_dp_lst + row.As_dp_lst) * 0.7)
        if row.type == ">90":
            dp_total_lst.append((row.Su_dp_lst + row.Mo_dp_lst + row.Me_dp_lst + row.Ma_dp_lst + row.Ju_dp_lst
                                 + row.Ve_dp_lst + row.Sa_dp_lst + row.Ra_dp_lst + row.Ke_dp_lst + row.As_dp_lst)* 0.7)
        if row.type == "60<":
            dp_total_lst.append((row.Su_dp_lst + row.Mo_dp_lst + row.Me_dp_lst + row.Ma_dp_lst + row.Ju_dp_lst
                                 + row.Ve_dp_lst + row.Sa_dp_lst + row.Ra_dp_lst + row.Ke_dp_lst + row.As_dp_lst)* 0.4)
        if row.type == ">60":
            dp_total_lst.append((row.Su_dp_lst + row.Mo_dp_lst + row.Me_dp_lst + row.Ma_dp_lst + row.Ju_dp_lst
                                 + row.Ve_dp_lst + row.Sa_dp_lst + row.Ra_dp_lst + row.Ke_dp_lst + row.As_dp_lst)* 0.4)
        if row.type == ">150":
            dp_total_lst.append((row.Su_dp_lst + row.Mo_dp_lst + row.Me_dp_lst + row.Ma_dp_lst + row.Ju_dp_lst
                                 + row.Ve_dp_lst + row.Sa_dp_lst + row.Ra_dp_lst + row.Ke_dp_lst + row.As_dp_lst)* 1.5)
    df["dp_total_lst"] = dp_total_lst
    return df


def interaccion(distance_planets_df):
    df1 = distance_planets_df.copy()
    df = pd.DataFrame()
    temp_lst = []
    planets = ["Su", "Mo", "Me", "Ma", "Ju", "Ve", "Sa", "Ra", "Ke", "As"]
    for i in planets:
        for j in planets:
            temp_lst.append(i+("(p1)") +"<" + j+("(p2)"))
    df["INTERACCION"] = temp_lst
    df2 = df1.set_index("planet")
    inter_list = []
    main_lis = []
    temp = df2.Su_dp_lst
    for i in planets:
        inter_list.append(temp[i].to_list())
    temp = df2.Mo_dp_lst
    for i in planets:
        inter_list.append(temp[i].to_list())
    temp = df2.Me_dp_lst
    for i in planets:
        inter_list.append(temp[i].to_list())
    temp = df2.Ma_dp_lst
    for i in planets:
        inter_list.append(temp[i].to_list())
    temp = df2.Ju_dp_lst
    for i in planets:
        inter_list.append(temp[i].to_list())
    temp = df2.Ve_dp_lst
    for i in planets:
        inter_list.append(temp[i].to_list())
    temp = df2.Sa_dp_lst
    for i in planets:
        inter_list.append(temp[i].to_list())
    temp = df2.Ra_dp_lst
    for i in planets:
        inter_list.append(temp[i].to_list())
    temp = df2.Ke_dp_lst
    for i in planets:
        inter_list.append(temp[i].to_list())
    temp = df2.As_dp_lst
    for i in planets:
        inter_list.append(temp[i].to_list())
    for i in inter_list:
        main_lis.append(i[0]*2 + i[1]*1.5+i[2]+i[3]+(i[4]+i[5])*0.7+ (i[6]+i[7])*0.4)
    main_lis[30] = main_lis[30] + df1.iloc[80, df1.columns.get_loc("Su_dp_lst")]
    main_lis[31] = main_lis[31] + df1.iloc[80, df1.columns.get_loc("Mo_dp_lst")]
    main_lis[32] = main_lis[32] + df1.iloc[80, df1.columns.get_loc("Me_dp_lst")]
    main_lis[33] = main_lis[33] + df1.iloc[80, df1.columns.get_loc("Ma_dp_lst")]
    main_lis[34] = main_lis[34] + df1.iloc[80, df1.columns.get_loc("Ju_dp_lst")]
    main_lis[35] = main_lis[35] + df1.iloc[80, df1.columns.get_loc("Ve_dp_lst")]
    main_lis[36] = main_lis[36] + df1.iloc[80, df1.columns.get_loc("Sa_dp_lst")]
    main_lis[37] = main_lis[37] + df1.iloc[80, df1.columns.get_loc("Ra_dp_lst")]
    main_lis[38] = main_lis[38] + df1.iloc[80, df1.columns.get_loc("Ke_dp_lst")]
    main_lis[39] = main_lis[39] + df1.iloc[80, df1.columns.get_loc("As_dp_lst")]
    df["puntaje"] = main_lis
    return df


def recreate_interaccion(interaccion_df):
    df1 = interaccion_df.copy()
    interaccion_temp_lis = []
    puntaje_temp_lis = []
    planets = ["Su", "Mo", "Me", "Ma", "Ju", "Ve", "Sa", "Ra", "Ke", "As"]
    for i in planets:
        for j in planets:
            interaccion_temp_lis.append(str(j) + str(" < ") + str(i))
    count =1
    range_count = 0
    while count <= 10:
        for i in range(range_count, 100, 10): 
            puntaje_temp_lis.append(df1.loc[i]["puntaje"])
        count += 1
        range_count += 1
    df = pd.DataFrame()
    df['INTERACCION'] = interaccion_temp_lis
    df['puntaje'] = puntaje_temp_lis
    return df


def breakdown_interaccion(recreate_interaccion_df, exdegree):
    df1 = recreate_interaccion_df.copy()
    if exdegree == "SU":
        temp_main_df = df1[0:10]
        sum_puntaje = sum(df1[0:10]['puntaje'].to_list())
        temp_main_df = temp_main_df.append({'INTERACCION': "TOTAL", 'puntaje': sum_puntaje}, ignore_index=True) 
        return temp_main_df, df1[0:10]['INTERACCION'].to_list(), df1[0:10]['puntaje'].to_list()
    if exdegree == "MO":
        temp_main_df = df1[10:20]
        sum_puntaje = sum(df1[10:20]['puntaje'].to_list())
        temp_main_df = temp_main_df.append({'INTERACCION': "TOTAL", 'puntaje': sum_puntaje}, ignore_index=True) 
        return temp_main_df, df1[10:20]['INTERACCION'].to_list(), df1[10:20]['puntaje'].to_list()
    if exdegree == "ME":
        temp_main_df = df1[20:30]
        sum_puntaje = sum(df1[20:30]['puntaje'].to_list())
        temp_main_df = temp_main_df.append({'INTERACCION': "TOTAL", 'puntaje': sum_puntaje}, ignore_index=True) 
        return temp_main_df, df1[20:30]['INTERACCION'].to_list(), df1[20:30]['puntaje'].to_list()
    if exdegree == "MA":
        temp_main_df = df1[30:40]
        sum_puntaje = sum(df1[30:40]['puntaje'].to_list())
        temp_main_df = temp_main_df.append({'INTERACCION': "TOTAL", 'puntaje': sum_puntaje}, ignore_index=True) 
        return temp_main_df, df1[30:40]['INTERACCION'].to_list(), df1[30:40]['puntaje'].to_list()
    if exdegree == "JU":
        temp_main_df = df1[40:50]
        sum_puntaje = sum(df1[40:50]['puntaje'].to_list())
        temp_main_df = temp_main_df.append({'INTERACCION': "TOTAL", 'puntaje': sum_puntaje}, ignore_index=True) 
        return temp_main_df, df1[40:50]['INTERACCION'].to_list(), df1[40:50]['puntaje'].to_list()
    if exdegree == "VE":
        temp_main_df = df1[50:60]
        sum_puntaje = sum(df1[50:60]['puntaje'].to_list())
        temp_main_df = temp_main_df.append({'INTERACCION': "TOTAL", 'puntaje': sum_puntaje}, ignore_index=True) 
        return temp_main_df, df1[50:60]['INTERACCION'].to_list(), df1[50:60]['puntaje'].to_list()
    if exdegree == "SA":
        temp_main_df = df1[60:70]
        sum_puntaje = sum(df1[60:70]['puntaje'].to_list())
        temp_main_df = temp_main_df.append({'INTERACCION': "TOTAL", 'puntaje': sum_puntaje}, ignore_index=True) 
        return temp_main_df, df1[60:70]['INTERACCION'].to_list(), df1[60:70]['puntaje'].to_list()
    if exdegree == "RA":
        temp_main_df = df1[70:80]
        sum_puntaje = sum(df1[70:80]['puntaje'].to_list())
        temp_main_df = temp_main_df.append({'INTERACCION': "TOTAL", 'puntaje': sum_puntaje}, ignore_index=True) 
        return temp_main_df, df1[70:80]['INTERACCION'].to_list(), df1[70:80]['puntaje'].to_list()
    if exdegree == "KE":
        temp_main_df = df1[80:90]
        sum_puntaje = sum(df1[80:90]['puntaje'].to_list())
        temp_main_df = temp_main_df.append({'INTERACCION': "TOTAL", 'puntaje': sum_puntaje}, ignore_index=True) 
        return temp_main_df, df1[80:90]['INTERACCION'].to_list(), df1[80:90]['puntaje'].to_list()
    if exdegree == "AS":
        temp_main_df = df1[90:100]
        sum_puntaje = sum(df1[90:100]['puntaje'].to_list())
        temp_main_df = temp_main_df.append({'INTERACCION': "TOTAL", 'puntaje': sum_puntaje}, ignore_index=True) 
        return temp_main_df, df1[90:100]['INTERACCION'].to_list(), df1[90:100]['puntaje'].to_list()
    if exdegree == "ALL":
        return df1[0:100], df1[0:100]['INTERACCION'].to_list(), df1[0:100]['puntaje'].to_list()
            



def peek_main(su_d, mo_d, me_d, ma_d, ju_d, ve_d, sa_d, ra_d, ke_d, as_d, su_d2, mo_d2, me_d2, ma_d2, ju_d2, ve_d2, sa_d2, ra_d2, ke_d2, as_d2):
    constants_start_and_end_limit = constants_limit_for_sign()
    eve_person_one = event_person(constants_start_and_end_limit, su_d, mo_d, me_d, ma_d, ju_d, ve_d, sa_d, ra_d, ke_d, as_d)
    eve_person_two = event_person(constants_start_and_end_limit, su_d2, mo_d2, me_d2, ma_d2, ju_d2, ve_d2, sa_d2, ra_d2, ke_d2, as_d2)
    house_df = house_table(eve_person_one)
    house_sign_df = house_and_sign(house_df)
    sign_house_df = sign_and_house(house_sign_df)
    sign_planet_house_df = sign_planet_and_house(eve_person_one, sign_house_df)
    pasp_table_df = pasp_table_degs()
    sign_table_df = sign_table_degs()
    sep_degree_df = sep_degree_p1p2(eve_person_one, eve_person_two)
    con_sign_planet_df = concatenation_sign_house(sign_planet_house_df, pasp_table_df, sign_table_df, eve_person_two)
    single_concatenation_df = single_concatenation_table(sign_planet_house_df)
    single_point_df = single_points_table(single_concatenation_df)
    point_planet_aspects_df = point_planets_planet_aspects(single_point_df)
    point_df = points_table(con_sign_planet_df, point_planet_aspects_df)
    distance_df = distance_table(point_df, sep_degree_df)
    dm_data_df = dm_data()
    distance_planets_df = distance_between_planets(distance_df, dm_data_df)
    interaccion_df = interaccion(distance_planets_df)
    recreate_interaccion_df = recreate_interaccion(interaccion_df)
    return recreate_interaccion_df

def all_calculation_multiple_two(su_d, mo_d, me_d, ma_d, ju_d, ve_d, sa_d, ra_d, ke_d, as_d, su_d2, mo_d2, me_d2, ma_d2, ju_d2, ve_d2, sa_d2, ra_d2, ke_d2, as_d2):
    constants_start_and_end_limit = constants_limit_for_sign()
    eve_person_one = event_person(constants_start_and_end_limit, su_d, mo_d, me_d, ma_d, ju_d, ve_d, sa_d, ra_d, ke_d, as_d)
    eve_person_two = event_person(constants_start_and_end_limit, su_d2, mo_d2, me_d2, ma_d2, ju_d2, ve_d2, sa_d2, ra_d2, ke_d2, as_d2)
    house_df = house_table(eve_person_one)
    house_sign_df = house_and_sign(house_df)
    sign_house_df = sign_and_house(house_sign_df)
    sign_planet_house_df = sign_planet_and_house(eve_person_one, sign_house_df)
    pasp_table_df = pasp_table_degs()
    sign_table_df = sign_table_degs()
    sep_degree_df = sep_degree_p1p2(eve_person_one, eve_person_two)
    con_sign_planet_df = concatenation_sign_house(sign_planet_house_df, pasp_table_df, sign_table_df, eve_person_two)
    single_concatenation_df = single_concatenation_table(sign_planet_house_df)
    single_point_df = single_points_table(single_concatenation_df)
    point_planet_aspects_df = point_planets_planet_aspects(single_point_df)
    point_df = points_table(con_sign_planet_df, point_planet_aspects_df)
    distance_df = distance_table(point_df, sep_degree_df)
    dm_data_df = dm_data()
    distance_planets_df = distance_between_planets(distance_df, dm_data_df)
    interaccion_df = interaccion(distance_planets_df)
    return interaccion_df

def remove_extra_quotes(sinter):
    a = sinter.replace("(p1)<", "")
    a = a.replace("(p2)", "")
    return a


def natalOperation(date_lst, ttime, p1place, p2place):
    interaccionDf = pd.DataFrame()
    for dst in date_lst:
        p1datelist = []
        p1date = dst.split('-')
        p1datelist.append(p1date[2])
        p1datelist.append(p1date[1])
        p1datelist.append(p1date[0])
        p1date = '.'.join(p1datelist)
        one_degree_result = onematch(p1date, ttime, p1place)
        two_degree_result = onematch(p1date, ttime, p2place)
        interaccionResult = all_calculation_multiple_two(one_degree_result[0], one_degree_result[1], one_degree_result[2], one_degree_result[3], one_degree_result[4], one_degree_result[5], one_degree_result[6], one_degree_result[7], one_degree_result[8], one_degree_result[9], two_degree_result[0], two_degree_result[1], two_degree_result[2], two_degree_result[3], two_degree_result[4], two_degree_result[5], two_degree_result[6], two_degree_result[7], two_degree_result[8], two_degree_result[9])
        interaccionResult = interaccionResult.rename(columns={"puntaje": dst})
        interaccionResult.set_index("INTERACCION", inplace=True)
        interaccionDf = pd.concat([interaccionDf, interaccionResult], axis=1)
    interaccionDf = interaccionDf.reset_index()
    interaccionDf['INTERACCION'] = interaccionDf['INTERACCION'].apply(remove_extra_quotes)
    interaccionDf.set_index("INTERACCION", inplace=True)
    return (interaccionDf.columns.tolist()), (interaccionDf.T.to_dict('list'))
    
def peekmultiple_main(request):
    date_list = []
    if request.method == "GET":
        user_id = 1
        if (request.GET.get('fdate')):
            fdate = (request.GET.get('fdate'))
            tdate = (request.GET.get('tdate'))
            fdate = (datetime.strptime(fdate, '%Y-%m-%d')).date()
            tdate = (datetime.strptime(tdate, '%Y-%m-%d')).date()
            sdate = fdate  
            edate = tdate
            delta = edate - sdate   
            firstfetch = DateLisDB.objects.filter(id__in=[user_id])  
            firstFetchResult = []  
            if firstfetch:
                for i in firstfetch:
                    firstFetchResult.append(i.datelis)
                for i in range(delta.days + 1):
                    day = sdate + timedelta(days=i)
                    firstFetchResult.append(str(day))
                save_date_lis = ','.join(firstFetchResult)
                s = DateLisDB(id=user_id, datelis = save_date_lis)
                s.save()                
            else:
                for i in range(delta.days + 1):
                    day = sdate + timedelta(days=i)
                    firstFetchResult.append(str(day))
                save_date_lis = ','.join(firstFetchResult)
                s = DateLisDB(id=user_id, datelis = save_date_lis)
                s.save()                


     

def pk_main(request):
    user_id =1
    date_list = []
    str1 = DateLisDB.objects.filter(id__in=[user_id])
    for i in str1:
        str1 = i.datelis   
    date_list = str1.split(",")
    if (request.GET.get('p1place')):
        p1place = (request.GET.get('p1place'))
        p2place = (request.GET.get('p2place'))
        ttime = request.GET.get('ttime')
        date_re = natalOperation(date_list, ttime, p1place, p2place)
        return date_re

def pclear():
    user_id = 1
    dfetch = DateLisDB.objects.filter(id__in=[user_id]) 
    dfetch.delete()         

def peeksingle(request):
    user_id =1
    str1 = DateLisDB.objects.filter(id__in=[user_id])
    if str1:
        for i in str1:
            str1 = i.datelis   
        date_list = str1.split(",")
        date_list.append(request.GET.get('addsdate'))
        save_date_lis = ','.join(date_list)
        s = DateLisDB(id=user_id, datelis = save_date_lis)
        s.save() 
    else:
        sdt = str(request.GET.get('addsdate'))
        s = DateLisDB(id=user_id, datelis = sdt)
        s.save() 


def allsundays(year, wname):
    d = date(year, 1, 1)                    
    d += timedelta(days = wname - d.weekday())  
    while d.year == year:
        yield d
        d += timedelta(days = 7)
    

def checkmakers(request):
    processYear = request.GET.get('fyear')
    if request.GET.get('monvalue') == "True":
        d_lis = []
        a =  allsundays(int(processYear), 7)
        for i in a:
            d_lis.append(str(i))
        user_id =1
        str1 = DateLisDB.objects.filter(id__in=[user_id])
        if str1:
            for i in str1:
                str1 = i.datelis   
            date_list = str1.split(",")
            save_date_lis = ','.join(date_list)
            d_lis = ','.join(d_lis)
            save_date_lis = save_date_lis + ","+ d_lis
            s = DateLisDB(id=user_id, datelis = save_date_lis)
            s.save() 
        else:
            d_lis = ','.join(d_lis)
            s = DateLisDB(id=user_id, datelis = d_lis)
            s.save() 
    if request.GET.get('tuevalue') == "True":
        d_lis = []
        a =  allsundays(int(processYear), 8)
        for i in a:
            d_lis.append(str(i))
        user_id =1  
        str1 = DateLisDB.objects.filter(id__in=[user_id])
        if str1:
            for i in str1:
                str1 = i.datelis   
            date_list = str1.split(",")
            save_date_lis = ','.join(date_list)
            d_lis = ','.join(d_lis)
            save_date_lis = save_date_lis + ","+ d_lis
            s = DateLisDB(id=user_id, datelis = save_date_lis)
            s.save() 
        else:
            d_lis = ','.join(d_lis)
            s = DateLisDB(id=user_id, datelis = d_lis)
            s.save() 
    if request.GET.get('wedvalue') == "True":
        d_lis = []
        a =  allsundays(int(processYear), 9)
        for i in a: 
            d_lis.append(str(i))
        user_id =1  
        str1 = DateLisDB.objects.filter(id__in=[user_id])
        if str1:
            for i in str1:
                str1 = i.datelis   
            date_list = str1.split(",")
            save_date_lis = ','.join(date_list)
            d_lis = ','.join(d_lis)
            save_date_lis = save_date_lis + ","+ d_lis
            s = DateLisDB(id=user_id, datelis = save_date_lis)
            s.save() 
        else:
            d_lis = ','.join(d_lis)
            s = DateLisDB(id=user_id, datelis = d_lis)
            s.save() 
    if request.GET.get('thuvalue') == "True":
        d_lis = []
        a =  allsundays(int(processYear), 10)
        for i in a: 
            d_lis.append(str(i))
        user_id =1  
        str1 = DateLisDB.objects.filter(id__in=[user_id])
        if str1:
            for i in str1:
                str1 = i.datelis   
            date_list = str1.split(",")
            save_date_lis = ','.join(date_list)
            d_lis = ','.join(d_lis)
            save_date_lis = save_date_lis + ","+ d_lis
            s = DateLisDB(id=user_id, datelis = save_date_lis)
            s.save() 
        else:
            d_lis = ','.join(d_lis)
            s = DateLisDB(id=user_id, datelis = d_lis)
            s.save() 

    if request.GET.get('frivalue') == "True":
        d_lis = []
        a =  allsundays(int(processYear), 4)
        for i in a: 
            d_lis.append(str(i))
        user_id =1  
        str1 = DateLisDB.objects.filter(id__in=[user_id])
        if str1:
            for i in str1:
                str1 = i.datelis   
            date_list = str1.split(",")
            save_date_lis = ','.join(date_list)
            d_lis = ','.join(d_lis)
            save_date_lis = save_date_lis + ","+ d_lis
            s = DateLisDB(id=user_id, datelis = save_date_lis)
            s.save() 
        else:
            d_lis = ','.join(d_lis)
            s = DateLisDB(id=user_id, datelis = d_lis)
            s.save() 
    if request.GET.get('satvalue') == "True":
        d_lis = []
        a =  allsundays(int(processYear), 5)
        for i in a: 
            d_lis.append(str(i))
        user_id =1  
        str1 = DateLisDB.objects.filter(id__in=[user_id])
        if str1:
            for i in str1:
                str1 = i.datelis   
            date_list = str1.split(",")
            save_date_lis = ','.join(date_list)
            d_lis = ','.join(d_lis)
            save_date_lis = save_date_lis + ","+ d_lis
            s = DateLisDB(id=user_id, datelis = save_date_lis)
            s.save() 
        else:
            d_lis = ','.join(d_lis)
            s = DateLisDB(id=user_id, datelis = d_lis)
            s.save() 
    if request.GET.get('sunvalue') == "True":
        d_lis = []
        a =  allsundays(int(processYear), 6)
        for i in a: 
            d_lis.append(str(i))
        user_id =1  
        str1 = DateLisDB.objects.filter(id__in=[user_id])
        if str1:
            for i in str1:
                str1 = i.datelis   
            date_list = str1.split(",")
            save_date_lis = ','.join(date_list)
            d_lis = ','.join(d_lis)
            save_date_lis = save_date_lis + ","+ d_lis
            s = DateLisDB(id=user_id, datelis = save_date_lis)
            s.save() 
        else:
            d_lis = ','.join(d_lis)
            s = DateLisDB(id=user_id, datelis = d_lis)
            s.save() 
    if request.GET.get('s15') == "True":
        user_id = 1
        dls = []
        for i in range(1,13):
            dls.append("15-"+str(i)+"-"+str(processYear))
        str1 = DateLisDB.objects.filter(id__in=[user_id])
        if str1:
            for i in str1:
                str1 = i.datelis   
                dls = ','.join(dls)
                result_dlis = str1 + ","+ dls 
                s = DateLisDB(id=user_id, datelis = result_dlis)
                s.save() 
        else:
            dls = ','.join(dls)
            s = DateLisDB(id=user_id, datelis = dls)
            s.save() 
    if request.GET.get('s115') == "True":
        user_id = 1
        dls = []
        for i in range(1,13):
            dls.append("1-"+str(i)+"-"+str(processYear))
            dls.append("15-"+str(i)+"-"+str(processYear))
        str1 = DateLisDB.objects.filter(id__in=[user_id])
        if str1:
            for i in str1:
                str1 = i.datelis   
                dls = ','.join(dls)
                result_dlis = str1 + ","+ dls 
                s = DateLisDB(id=user_id, datelis = result_dlis)
                s.save() 
        else:
            dls = ','.join(dls)
            s = DateLisDB(id=user_id, datelis = dls)
            s.save() 
                
    if request.GET.get('s110') == "True":
        user_id = 1
        dls = []
        for i in range(1,13):
            dls.append("1-"+str(i)+"-"+str(processYear))
            dls.append("10-"+str(i)+"-"+str(processYear))
            dls.append("20-"+str(i)+"-"+str(processYear))
            dls.append("30-"+str(i)+"-"+str(processYear))
        str1 = DateLisDB.objects.filter(id__in=[user_id])
        if str1:
            for i in str1:
                str1 = i.datelis   
                dls = ','.join(dls)
                result_dlis = str1 + ","+ dls 
                s = DateLisDB(id=user_id, datelis = result_dlis)
                s.save() 
        else:
            dls = ','.join(dls)
            s = DateLisDB(id=user_id, datelis = dls)
            s.save() 
                
                  
        
        
        
def processSpecificDay(request):
    user_id = 1
    dl = []
    day = request.GET.get('sday')
    month = request.GET.get('smonth')
    fyear = request.GET.get('sfyear')
    tyear = request.GET.get('styear')
    for i in range(int(fyear), (int(tyear)+1)):
        dl.append(str(day)+"-"+str(month)+"-"+str(i))
    str1 = DateLisDB.objects.filter(id__in=[user_id])
    if str1:
        for i in str1:
            str1 = i.datelis   
        dls = ','.join(dl)
        result_dlis = str1 + ","+ dls
        s = DateLisDB(id=user_id, datelis = result_dlis)
        s.save() 
    else:
        dls = ','.join(dl)
        s = DateLisDB(id=user_id, datelis = dls)
        s.save() 
    

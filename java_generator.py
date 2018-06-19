# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 上午8:46
# @Author  : Azrael.Bai
# @File    : java_generator.py

origin_string = '''
GongShang_HZ_BianGengXinXi_GuanLiDAO tmpDao%d=(GongShang_HZ_BianGengXinXi_GuanLiDAO)SystemContext.ApplicationContext.getBean("GongShang_HZ_BianGengXinXi_GuanLiDAO");
List<GongShang_HZ_BianGengXinXi_GuanLi> tmpList%d=tmpDao%d.getGongShang_HZ_BianGengXinXi_GuanLiList("GongShang_HZ_BianGengXinXi.ofcompany="+tmpObj.getBold_id());
if(!(tmpList%d.isEmpty())) {
	dataExistsNum += 1;
}
'''

replace_list = [
    'GongShang_HZ_BianGengXinXi',
    'GongShang_HZ_FenZhiJiGou',
    'GongShang_HZ_ZhuYaoRenYuan',
    'GongShang_HZ_GuDongXinXi',
    'GongShang_HZ_GuQuanBianGengXinXi',
    'GongShang_HZ_DongChanDiYanDengJiXinXi',
    'GongShang_HZ_GuQuanChuZhiDengJiXinXi',
    'GongShang_HZ_JingYingYiChangXinXi',
    'CaiPanWenShu_HZ',
    'ZhiXingXinXi_HZ',
    'KaiTingGongGao_HZ',
    'FaYuanGongGao_HZ',
]

be_replace_string = "GongShang_HZ_BianGengXinXi"

i = 1
for str in replace_list:
    out = origin_string.replace(be_replace_string, str)
    print out % (i,i,i,i)
    i+=1


table_name_dict = {
    "GongShang_GSGW_JiBenXinXi": "iac_gsgw_baseinfo",
    "GongShang_GSGW_ChuZiXinXi": "iac_gsgw_cntrbinfo",
    "GongShang_GSGW_BianGengXinXi": "iac_gsgw_changerecordsinfo",
    "GongShang_GSGW_FenZhiJiGou": "iac_gsgw_branch",
    "GongShang_GSGW_ZhuYaoRenYuan": "iac_gsgw_keyperson",
    "GongShang_GSGW_GuDongXinXi": "iac_gsgw_shareholderinfo",
    "GongShang_GSGW_GuQuanBianGengXinXi": "iac_gsgw_changeshareholdinginfo",
    "GongShang_GSGW_DongChanDiYanDengJiXinXi": "iac_gsgw_chattelmortgageinfo",
    "GongShang_GSGW_GuQuanChuZhiDengJiXinXi": "iac_gsgw_equitypledgedinfo",
    "GongShang_GSGW_JingYingYiChangXinXi": "iac_gsgw_abnormaloperationinfo",
    "CaiPanWenShu_ZGFY": "judgement_zgfy",
    "ZhiXingXinXi_ZGFY": "executeinfo_zgfy",
    "KaiTingGongGao_DFFY": "courtannouncement_dffy",
    "GongGaoRenGongGao_DFFY": "bulletinannouncement_dffy",
    "GongShang_HZ_JiBenXinXi": "iac_hz_baseinfo",
    "GongShang_HZ_BianGengXinXi": "iac_hz_changerecordsinfo",
    "GongShang_HZ_FenZhiJiGou": "iac_hz_branch",
    "GongShang_HZ_ZhuYaoRenYuan": "iac_hz_keyperson",
    "GongShang_HZ_GuDongXinXi": "iac_hz_shareholderinfo",
    "GongShang_HZ_GuQuanBianGengXinXi": "iac_hz_changeshareholdinginfo",
    "GongShang_HZ_DongChanDiYanDengJiXinXi": "iac_hz_chattelmortgageinfo",
    "GongShang_HZ_GuQuanChuZhiDengJiXinXi": "iac_hz_equitypledgedinfo",
    "GongShang_HZ_JingYingYiChangXinXi": "iac_hz_abnormaloperationinfo",
    "CaiPanWenShu_HZ": "judgement_hz",
    "ZhiXingXinXi_HZ": "executeinfo_hz",
    "KaiTingGongGao_HZ": "courtannouncement_hz",
    "FaYuanGongGao_HZ": "bulletinannouncement_hz",
    "GongShang_QCC_JiBenXinXi": "iac_qcc_baseinfo",
    "GongShang_QCC_BianGengXinXi": "iac_qcc_changerecordsinfo",
    "GongShang_QCC_FenZhiJiGou": "iac_qcc_branch",
    "GongShang_QCC_ZhuYaoRenYuan": "iac_qcc_keyperson",
    "GongShang_QCC_GuDongXinXi": "iac_qcc_shareholderinfo",
    "GongShang_QCC_DongChanDiYanDengJiXinXi": "iac_qcc_chattelmortgageinfo",
    "GongShang_QCC_GuQuanChuZhiDengJiXinXi": "iac_qcc_equitypledgedinfo",
    "GongShang_QCC_JingYingYiChangXinXi": "iac_qcc_abnormaloperationinfo",
    "CaiPanWenShu_QCC": "judgement_qcc",
    "ZhiXingXinXi_QCC": "executeinfo_qcc",
    "KaiTingGongGao_QCC": "courtannouncement_qcc",
    "FaYuanGongGao_QCC": "bulletinannouncement_qcc",
    "GongShang_QXB_JiBenXinXi": "iac_qxb_baseinfo",
    "GongShang_QXB_BianGengXinXi": "iac_qxb_changerecordsinfo",
    "GongShang_QXB_FenZhiJiGou": "iac_qxb_branch",
    "GongShang_QXB_ZhuYaoRenYuan": "iac_qxb_keyperson",
    "GongShang_QXB_GuDongXinXi": "iac_qxb_shareholderinfo",
    "GongShang_QXB_DongChanDiYanDengJiXinXi": "iac_qxb_chattelmortgageinfo",
    "GongShang_QXB_GuQuanChuZhiDengJiXinXi": "iac_qxb_equitypledgedinfo",
    "GongShang_QXB_JingYingYiChangXinXi": "iac_qxb_abnormaloperationinfo",
    "CaiPanWenShu_QXB": "judgement_qxb",
    "ZhiXingXinXi_QXB": "executeinfo_qxb",
    "KaiTingGongGao_QXB": "courtannouncement_qxb",
    "FaYuanGongGao_QXB": "bulletinannouncement_qxb",
}

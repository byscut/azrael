# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 上午8:46
# @Author  : Azrael.Bai
# @File    : java_generator.py

origin_string = '''
			bean_str = "%s";
			GongShang_GSGW_ChuZiXinXi_GuanLiDAO tmpDao%d=(GongShang_GSGW_ChuZiXinXi_GuanLiDAO)SystemContext.ApplicationContext.getBean("GongShang_GSGW_ChuZiXinXi_GuanLiDAO");
			List<GongShang_GSGW_ChuZiXinXi_GuanLi> tmpList%d=tmpDao%d.getGongShang_GSGW_ChuZiXinXi_GuanLiList(bean_str+".ofcompany="+tmpObj.getBold_id());
			for(int i = 0;i < tmpList%d.size();i++) {
				if(tmpList%d.get(i).getShuJuYouXiaoXing()==1171) {
					//处理比对
					HashMap<String,String> chuzixinxi_gw = new HashMap<String,String>();

					if(table_fields.containsKey(bean_str.toLowerCase())) {
						ArrayList<String> fields = table_fields.get(bean_str.toLowerCase());
						for(String field_name: fields) {
							String re_str = (String)this.reflectFunciton(field_name, tmpList%d.get(i));
							chuzixinxi_gw.put(field_name, re_str);
						}
					}
					gwInfo.chuzixinxi_gw_list.add(chuzixinxi_gw);
				}
			}
'''
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

replace_list = [
    'GongShang_GSGW_BianGengXinXi',
    'GongShang_GSGW_FenZhiJiGou',
    'GongShang_GSGW_ZhuYaoRenYuan',
    'GongShang_GSGW_GuDongXinXi',
    'GongShang_GSGW_GuQuanBianGengXinXi',
    'GongShang_GSGW_DongChanDiYanDengJiXinXi',
    'GongShang_GSGW_GuQuanChuZhiDengJiXinXi',
    'GongShang_GSGW_JingYingYiChangXinXi',
    'CaiPanWenShu_ZGFY',
    'ZhiXingXinXi_ZGFY',
    'KaiTingGongGao_DFFY',
    'GongGaoRenGongGao_DFFY',
]

be_replace_string = "GongShang_GSGW_ChuZiXinXi"

replace_list2 = [
    'biangengxinxi',
    'fenzhijigou',
    'zhiyaorenyuan',
    'gudongxinxi',
    'guquanbiangeng',
    'dongchandiya',
    'guquanchuzhi',
    'jingyingyichang',
    'caipanwenshu',
    'zhixingxinxi',
    'kaitingonggao',
    'fayuangonggao',
]

be_replace_string2 = "chuzixinxi"


# i = 1
# for str in replace_list:
#     out = origin_string.replace(be_replace_string, str)
#     out = out.replace(be_replace_string2, replace_list2[i-1])
#
#     print out % (table_name_dict[str],i,i,i,i,i,i)
#     i+=1


os = '''
			if(hzInfo.chuzixinxi_gw_list != null && gwInfo.chuzixinxi_gw_list != null) {
				compareList(company_id, "变更信息",hzInfo.chuzixinxi_gw_list,gwInfo.chuzixinxi_gw_list,
						source_name,base_name,Config.hz_chuzixinxi_primary_key,Config.hz_chuzixinxi_value,
						Config.gw_chuzixinxi_primary_key,Config.gw_chuzixinxi_value);
			}else if(hzInfo.chuzixinxi_gw_list == null || gwInfo.chuzixinxi_gw_list != null) {
				System.out.println("待对比数据源" + source_name + "没有模块" + "变更信息" + "基准数据源"+base_name+"有。");
			}else if(hzInfo.chuzixinxi_gw_list != null || gwInfo.chuzixinxi_gw_list == null) {
				System.out.println( "基准数据源"+base_name+"缺失模块" + "变更信息");
			}
'''


for str in replace_list2:
    out = os.replace(be_replace_string2, str)
    print out

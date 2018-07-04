# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 下午5:01
# @Author  : Azrael.Bai
# @File    : Model_def.py
#!/usr/bin/python
# -*- coding: utf-8 -*-
from model.Level1Config import *
from model.CustomConfig import *
from model.CustomConfig import __COMPANY_NAME__
from model.CustomConfig import __USER_ID__
from model.ModelDef_Attachment import *

GongShang_HZ_JiBenXinXi_bold_id={'DBColName':'bold_id','isIDCol':True, 'refPOJOColName':'IAC_HZ_BaseInfo.bold_id', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'ID', 'PGFieldType':'Integer', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_JiBenXinXi_GeiDingGongSiMingCheng={'DBColName':'GeiDingGongSiMingCheng', 'refPOJOColName':'IAC_HZ_BaseInfo.ofcompany', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'给定企业名称', 'PGFieldType':'Combo', 'PGComboProvider':SelectableCompany_Dict,'PGFieldWidthFactor':2,'PGFieldHeightFactor':1,'PGFieldHidden':False , 'PGFieldRequiredValue':True ,}
GongShang_HZ_JiBenXinXi_ShuJuYouXiaoXing={'DBColName':'ShuJuYouXiaoXing', 'refPOJOColName':'IAC_HZ_BaseInfo.datavalidity', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'本记录有效', 'PGFieldType':'combo', 'PGComboProvider':YesNoDict,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False , 'PGFieldDefaultValue':1171,}
GongShang_HZ_JiBenXinXi_GongSiShiFouCunZai={'DBColName':'GongSiShiFouCunZai', 'refPOJOColName':'IAC_HZ_BaseInfo.existence', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'公司是否存在', 'PGFieldType':'combo', 'PGComboProvider':YesNoDict,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False , 'PGFieldDefaultValue':1171,}
GongShang_HZ_JiBenXinXi_ShiJiGongSiMingCheng={'DBColName':'ShiJiGongSiMingCheng', 'refPOJOColName':'IAC_HZ_BaseInfo.realcompanyname', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'实际企业名称', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':2,'PGFieldHeightFactor':1,'PGFieldHidden':False , 'PGFieldRequiredValue':True ,}
GongShang_HZ_JiBenXinXi_TongYiSheHuiXinYongHao={'DBColName':'TongYiSheHuiXinYongHao', 'refPOJOColName':'IAC_HZ_BaseInfo.creditcode', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'统一信用代码', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_JiBenXinXi_ZhuCeHao={'DBColName':'ZhuCeHao', 'refPOJOColName':'IAC_HZ_BaseInfo.registeredcode', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'注册号', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_JiBenXinXi_ShengFen={'DBColName':'ShengFen', 'refPOJOColName':'IAC_HZ_BaseInfo.province', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'省份', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_JiBenXinXi_JingYingZhuangTai={'DBColName':'JingYingZhuangTai', 'refPOJOColName':'IAC_HZ_BaseInfo.businessstatus', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'经营状态', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_JiBenXinXi_GongSiLeiXing={'DBColName':'GongSiLeiXing', 'refPOJOColName':'IAC_HZ_BaseInfo.companytype', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'公司类型', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_JiBenXinXi_ChengLiRiQi={'DBColName':'ChengLiRiQi', 'refPOJOColName':'IAC_HZ_BaseInfo.registereddate', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'成立日期', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_JiBenXinXi_FaDingDaiBiaoRen={'DBColName':'FaDingDaiBiaoRen', 'refPOJOColName':'IAC_HZ_BaseInfo.legalman', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'法定代表人', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_JiBenXinXi_YingYeQiXian={'DBColName':'YingYeQiXian', 'refPOJOColName':'IAC_HZ_BaseInfo.period', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'营业期限', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_JiBenXinXi_ZhuCeZiBen={'DBColName':'ZhuCeZiBen', 'refPOJOColName':'IAC_HZ_BaseInfo.registeredcapital', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'注册资本', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_JiBenXinXi_HeZhunRiQi={'DBColName':'HeZhunRiQi', 'refPOJOColName':'IAC_HZ_BaseInfo.approvaldate', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'核准日期', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_JiBenXinXi_ZhuYingHangYe={'DBColName':'ZhuYingHangYe', 'refPOJOColName':'IAC_HZ_BaseInfo.mainbusiness', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'主营行业', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_JiBenXinXi_DengJiJiGuan={'DBColName':'DengJiJiGuan', 'refPOJOColName':'IAC_HZ_BaseInfo.registeredoffice', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'登记机关', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_JiBenXinXi_QiYeDiZhi={'DBColName':'QiYeDiZhi', 'refPOJOColName':'IAC_HZ_BaseInfo.address', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'企业地址', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':2,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_JiBenXinXi_JingYingFanWei={'DBColName':'JingYingFanWei', 'refPOJOColName':'IAC_HZ_BaseInfo.businessscope', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'经营范围', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':3,'PGFieldHeightFactor':3,'PGFieldHidden':False ,}
GongShang_HZ_JiBenXinXi_DengJiRen={'DBColName':'DengJiRen', 'refPOJOColName':'IAC_HZ_BaseInfo.regperson', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'登记人', 'PGFieldType':'Combo', 'PGComboProvider':PersonDict_Employee_or_SystemUser,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':True,'PGFieldDefaultValue':__USER_ID__,}
GongShang_HZ_JiBenXinXi_DengJiShiJian={'DBColName':'DengJiShiJian', 'refPOJOColName':'IAC_HZ_BaseInfo.regtime', 'DBColType':'Timestamp','PGFieldName':'', 'PGFieldLabel':'登记时间', 'PGFieldType':'datetime', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':True,'PGFieldDefaultValue':True}
GongShang_HZ_JiBenXinXi_BeiZhu={'DBColName':'BeiZhu', 'refPOJOColName':'IAC_HZ_BaseInfo.remark', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'备注', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':3,'PGFieldHeightFactor':2,'PGFieldHidden':False ,}
GongShang_HZ_JiBenXinXi = {
    'Name':'工商基本信息（海致）','ActionName':'工商基本信息（海致）','Image':'icons/JiBenXinXi.png',
    'POJOName':'IAC_HZ_BaseInfo',
    'POJOQuerySQL':'select obj from IAC_HZ_BaseInfo obj where obj.'+WaiBaoZhiXin_Query1_Part,
    'COListQueryCondition':'IAC_HZ_BaseInfo.'+WaiBaoZhiXin_Query1_Part+' order by IAC_HZ_BaseInfo.ofcompany desc',
    'COListAdditionalQueryCondition':'" and o.DengJiRen="+'+__USER_ID__,
    'ClassName':'GongShang_HZ_JiBenXinXi',
    'DialogContentTitle':'工商基本信息（海致）',
    'QueryConditionList' : [
                  GongShang_HZ_JiBenXinXi_GeiDingGongSiMingCheng,GongShang_HZ_JiBenXinXi_ShiJiGongSiMingCheng,GongShang_HZ_JiBenXinXi_TongYiSheHuiXinYongHao,GongShang_HZ_JiBenXinXi_ZhuCeHao,GongShang_HZ_JiBenXinXi_ShengFen
         ],
    'TableColumnsList' : [
        GongShang_HZ_JiBenXinXi_GeiDingGongSiMingCheng, GongShang_HZ_JiBenXinXi_GongSiShiFouCunZai,GongShang_HZ_JiBenXinXi_ShiJiGongSiMingCheng,GongShang_HZ_JiBenXinXi_TongYiSheHuiXinYongHao,
        GongShang_HZ_JiBenXinXi_ShengFen,
        GongShang_HZ_JiBenXinXi_ChengLiRiQi,
        GongShang_HZ_JiBenXinXi_FaDingDaiBiaoRen,
        GongShang_HZ_JiBenXinXi_ZhuCeZiBen,
        GongShang_HZ_JiBenXinXi_DengJiRen, GongShang_HZ_JiBenXinXi_DengJiShiJian,
         ],
    'ViewColumnsList' : [
        GongShang_HZ_JiBenXinXi_GeiDingGongSiMingCheng,GongShang_HZ_JiBenXinXi_ShuJuYouXiaoXing,GongShang_HZ_JiBenXinXi_GongSiShiFouCunZai,GongShang_HZ_JiBenXinXi_ShiJiGongSiMingCheng, GongShang_HZ_JiBenXinXi_TongYiSheHuiXinYongHao,
        GongShang_HZ_JiBenXinXi_ZhuCeHao, GongShang_HZ_JiBenXinXi_ShengFen, GongShang_HZ_JiBenXinXi_JingYingZhuangTai,
        GongShang_HZ_JiBenXinXi_GongSiLeiXing, GongShang_HZ_JiBenXinXi_ChengLiRiQi,
        GongShang_HZ_JiBenXinXi_FaDingDaiBiaoRen,
        GongShang_HZ_JiBenXinXi_DengJiJiGuan, GongShang_HZ_JiBenXinXi_QiYeDiZhi,GongShang_HZ_JiBenXinXi_JingYingFanWei,
        GongShang_HZ_JiBenXinXi_DengJiRen, GongShang_HZ_JiBenXinXi_DengJiShiJian,
         ],
    'EditColumnsList':  [
        GongShang_HZ_JiBenXinXi_GeiDingGongSiMingCheng,GongShang_HZ_JiBenXinXi_ShuJuYouXiaoXing,GongShang_HZ_JiBenXinXi_GongSiShiFouCunZai,GongShang_HZ_JiBenXinXi_ShiJiGongSiMingCheng, GongShang_HZ_JiBenXinXi_TongYiSheHuiXinYongHao,
        GongShang_HZ_JiBenXinXi_ZhuCeHao, GongShang_HZ_JiBenXinXi_ShengFen, GongShang_HZ_JiBenXinXi_JingYingZhuangTai,
        GongShang_HZ_JiBenXinXi_GongSiLeiXing, GongShang_HZ_JiBenXinXi_ChengLiRiQi,
        GongShang_HZ_JiBenXinXi_FaDingDaiBiaoRen,
        GongShang_HZ_JiBenXinXi_YingYeQiXian, GongShang_HZ_JiBenXinXi_ZhuCeZiBen, GongShang_HZ_JiBenXinXi_HeZhunRiQi,
        GongShang_HZ_JiBenXinXi_ZhuYingHangYe, GongShang_HZ_JiBenXinXi_DengJiJiGuan, GongShang_HZ_JiBenXinXi_QiYeDiZhi,GongShang_HZ_JiBenXinXi_JingYingFanWei,
        GongShang_HZ_JiBenXinXi_DengJiRen, GongShang_HZ_JiBenXinXi_DengJiShiJian,
         ],
    'AllColumns':[
                  GongShang_HZ_JiBenXinXi_bold_id,GongShang_HZ_JiBenXinXi_GeiDingGongSiMingCheng,GongShang_HZ_JiBenXinXi_ShuJuYouXiaoXing,GongShang_HZ_JiBenXinXi_GongSiShiFouCunZai,GongShang_HZ_JiBenXinXi_ShiJiGongSiMingCheng,GongShang_HZ_JiBenXinXi_TongYiSheHuiXinYongHao,GongShang_HZ_JiBenXinXi_ZhuCeHao,GongShang_HZ_JiBenXinXi_ShengFen,GongShang_HZ_JiBenXinXi_JingYingZhuangTai,GongShang_HZ_JiBenXinXi_GongSiLeiXing,GongShang_HZ_JiBenXinXi_ChengLiRiQi,GongShang_HZ_JiBenXinXi_FaDingDaiBiaoRen,
                  GongShang_HZ_JiBenXinXi_YingYeQiXian,GongShang_HZ_JiBenXinXi_ZhuCeZiBen,GongShang_HZ_JiBenXinXi_HeZhunRiQi,GongShang_HZ_JiBenXinXi_ZhuYingHangYe,GongShang_HZ_JiBenXinXi_DengJiJiGuan,GongShang_HZ_JiBenXinXi_QiYeDiZhi,GongShang_HZ_JiBenXinXi_JingYingFanWei,GongShang_HZ_JiBenXinXi_DengJiRen,GongShang_HZ_JiBenXinXi_DengJiShiJian,GongShang_HZ_JiBenXinXi_BeiZhu,
                  ],
    'DetailCO':[],
    'MasterCORefColumn':GongShang_HZ_JiBenXinXi_bold_id,
    'MasterCOAttachments':[AssignedSelectableCompany_Attachment],'MasterCOAttachments_Reflect':[{'From':AssignedSelectableCompany_Attachment_MingCheng,'To':GongShang_HZ_JiBenXinXi_GeiDingGongSiMingCheng,'DealWay':'Replace'}],
    'BusiActions':[AddAction_Default,EditAction_Default],
    'Normal_methods':'''\
        public void computeOnAttachmentClickFinished(){
        }
        private Double recompute(){
            label_help.setText("");
            label_help.setToolTipText(label_help.getText());
            return 0d;
        }'''
    }

GongShang_HZ_JiBenXinXi_GuanLi = {
    'Name':'工商基本信息管理（海致）','ActionName':'工商基本信息管理（海致）','Image':'icons/JiBenXinXi.png',
    'POJOName':'IAC_HZ_BaseInfo',
    'POJOQuerySQL':'',
    'COListQueryCondition':' order by IAC_HZ_BaseInfo.ofcompany desc',
    'ClassName':'GongShang_HZ_JiBenXinXi_GuanLi',
    'DialogContentTitle':'工商基本信息管理（海致）',
    'QueryConditionList' : [
                  GongShang_HZ_JiBenXinXi_GeiDingGongSiMingCheng,GongShang_HZ_JiBenXinXi_ShuJuYouXiaoXing,GongShang_HZ_JiBenXinXi_ShiJiGongSiMingCheng,GongShang_HZ_JiBenXinXi_TongYiSheHuiXinYongHao,GongShang_HZ_JiBenXinXi_ZhuCeHao,GongShang_HZ_JiBenXinXi_ShengFen,GongShang_HZ_JiBenXinXi_DengJiRen
         ],
    'TableColumnsList' : [
        GongShang_HZ_JiBenXinXi_GeiDingGongSiMingCheng, GongShang_HZ_JiBenXinXi_GongSiShiFouCunZai,GongShang_HZ_JiBenXinXi_ShiJiGongSiMingCheng,GongShang_HZ_JiBenXinXi_TongYiSheHuiXinYongHao,
        GongShang_HZ_JiBenXinXi_ShengFen,
        GongShang_HZ_JiBenXinXi_ChengLiRiQi,
        GongShang_HZ_JiBenXinXi_FaDingDaiBiaoRen,
        GongShang_HZ_JiBenXinXi_ZhuCeZiBen,
        GongShang_HZ_JiBenXinXi_DengJiRen, GongShang_HZ_JiBenXinXi_DengJiShiJian,
         ],
    'ViewColumnsList' : [
        GongShang_HZ_JiBenXinXi_GeiDingGongSiMingCheng, GongShang_HZ_JiBenXinXi_ShuJuYouXiaoXing,GongShang_HZ_JiBenXinXi_GongSiShiFouCunZai,GongShang_HZ_JiBenXinXi_ShiJiGongSiMingCheng,GongShang_HZ_JiBenXinXi_TongYiSheHuiXinYongHao,
        GongShang_HZ_JiBenXinXi_ZhuCeHao, GongShang_HZ_JiBenXinXi_ShengFen, GongShang_HZ_JiBenXinXi_JingYingZhuangTai,
        GongShang_HZ_JiBenXinXi_GongSiLeiXing, GongShang_HZ_JiBenXinXi_ChengLiRiQi,
        GongShang_HZ_JiBenXinXi_FaDingDaiBiaoRen,
        GongShang_HZ_JiBenXinXi_DengJiJiGuan, GongShang_HZ_JiBenXinXi_QiYeDiZhi,
        GongShang_HZ_JiBenXinXi_DengJiRen, GongShang_HZ_JiBenXinXi_DengJiShiJian,
         ],
    'EditColumnsList':  [
        GongShang_HZ_JiBenXinXi_GeiDingGongSiMingCheng, GongShang_HZ_JiBenXinXi_ShuJuYouXiaoXing,GongShang_HZ_JiBenXinXi_GongSiShiFouCunZai,GongShang_HZ_JiBenXinXi_ShiJiGongSiMingCheng,GongShang_HZ_JiBenXinXi_TongYiSheHuiXinYongHao,
        GongShang_HZ_JiBenXinXi_ZhuCeHao, GongShang_HZ_JiBenXinXi_ShengFen, GongShang_HZ_JiBenXinXi_JingYingZhuangTai,
        GongShang_HZ_JiBenXinXi_GongSiLeiXing, GongShang_HZ_JiBenXinXi_ChengLiRiQi,
        GongShang_HZ_JiBenXinXi_FaDingDaiBiaoRen,
        GongShang_HZ_JiBenXinXi_YingYeQiXian, GongShang_HZ_JiBenXinXi_ZhuCeZiBen, GongShang_HZ_JiBenXinXi_HeZhunRiQi,
        GongShang_HZ_JiBenXinXi_ZhuYingHangYe, GongShang_HZ_JiBenXinXi_DengJiJiGuan, GongShang_HZ_JiBenXinXi_QiYeDiZhi,
        GongShang_HZ_JiBenXinXi_JingYingFanWei,
         ],
    'AllColumns':[
                  GongShang_HZ_JiBenXinXi_bold_id,GongShang_HZ_JiBenXinXi_GeiDingGongSiMingCheng,GongShang_HZ_JiBenXinXi_ShuJuYouXiaoXing,GongShang_HZ_JiBenXinXi_GongSiShiFouCunZai,GongShang_HZ_JiBenXinXi_ShiJiGongSiMingCheng,GongShang_HZ_JiBenXinXi_TongYiSheHuiXinYongHao,GongShang_HZ_JiBenXinXi_ZhuCeHao,GongShang_HZ_JiBenXinXi_ShengFen,GongShang_HZ_JiBenXinXi_JingYingZhuangTai,GongShang_HZ_JiBenXinXi_GongSiLeiXing,GongShang_HZ_JiBenXinXi_ChengLiRiQi,GongShang_HZ_JiBenXinXi_FaDingDaiBiaoRen,
                  GongShang_HZ_JiBenXinXi_YingYeQiXian,GongShang_HZ_JiBenXinXi_ZhuCeZiBen,GongShang_HZ_JiBenXinXi_HeZhunRiQi,GongShang_HZ_JiBenXinXi_ZhuYingHangYe,GongShang_HZ_JiBenXinXi_DengJiJiGuan,GongShang_HZ_JiBenXinXi_QiYeDiZhi,GongShang_HZ_JiBenXinXi_JingYingFanWei,GongShang_HZ_JiBenXinXi_DengJiRen,GongShang_HZ_JiBenXinXi_DengJiShiJian,GongShang_HZ_JiBenXinXi_BeiZhu,
                  ],
    'DetailCO':[],
    'MasterCORefColumn':GongShang_HZ_JiBenXinXi_bold_id,
    'MasterCOAttachments':[AssignedSelectableCompany_Attachment],'MasterCOAttachments_Reflect':[{'From':AssignedSelectableCompany_Attachment_MingCheng,'To':GongShang_HZ_JiBenXinXi_GeiDingGongSiMingCheng,'DealWay':'Replace'}],
    'BusiActions':[AddAction_Default,EditAction_Default],
    'Normal_methods':'''\
        public void computeOnAttachmentClickFinished(){
        }
        private Double recompute(){
            label_help.setText("");
            label_help.setToolTipText(label_help.getText());
            return 0d;
        }'''
    }

#========================================================================================================================================
GongShang_HZ_BianGengXinXi_bold_id={'DBColName':'bold_id','isIDCol':True, 'refPOJOColName':'IAC_HZ_ChangeRecordsInfo.bold_id', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'ID', 'PGFieldType':'Integer', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_BianGengXinXi_OfCompany={'DBColName':'OfCompany', 'refPOJOColName':'IAC_HZ_ChangeRecordsInfo.ofcompany', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'实际企业名称', 'PGFieldType':'Combo', 'PGComboProvider':SelectableCompany_HZ_Dict,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':False,'PGFieldRequiredValue':True}
GongShang_HZ_BianGengXinXi_ShuJuYouXiaoXing={'DBColName':'ShuJuYouXiaoXing', 'refPOJOColName':'IAC_HZ_ChangeRecordsInfo.datavalidity', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'本记录有效', 'PGFieldType':'combo', 'PGComboProvider':YesNoDict,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False , 'PGFieldDefaultValue':1171,}
GongShang_HZ_BianGengXinXi_BianGengRiQi={'DBColName':'BianGengRiQi', 'refPOJOColName':'IAC_HZ_ChangeRecordsInfo.changedate', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'变更日期', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_BianGengXinXi_BianGengQianNeiRong={'DBColName':'BianGengQianNeiRong', 'refPOJOColName':'IAC_HZ_ChangeRecordsInfo.beforecontent', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'变更前内容', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':3,'PGFieldHidden':False ,}
GongShang_HZ_BianGengXinXi_BianGengHouNeiRong={'DBColName':'BianGengHouNeiRong', 'refPOJOColName':'IAC_HZ_ChangeRecordsInfo.aftercontent', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'变更后内容', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':3,'PGFieldHidden':False ,}
GongShang_HZ_BianGengXinXi_BianGengShiXiang={'DBColName':'BianGengShiXiang', 'refPOJOColName':'IAC_HZ_ChangeRecordsInfo.changeitem', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'变更事项', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_BianGengXinXi_DengJiRen={'DBColName':'DengJiRen', 'refPOJOColName':'IAC_HZ_ChangeRecordsInfo.regperson', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'登记人', 'PGFieldType':'Combo', 'PGComboProvider':PersonDict_Employee_or_SystemUser,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':True,'PGFieldDefaultValue':__USER_ID__,}
GongShang_HZ_BianGengXinXi_DengJiShiJian={'DBColName':'DengJiShiJian', 'refPOJOColName':'IAC_HZ_ChangeRecordsInfo.regtime', 'DBColType':'Timestamp','PGFieldName':'', 'PGFieldLabel':'登记时间', 'PGFieldType':'datetime', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':True,'PGFieldDefaultValue':True}
GongShang_HZ_BianGengXinXi = {
    'Name':'工商变更信息（海致）','ActionName':'工商变更信息（海致）','Image':'icons/GongShangBianGeng.png',
    'POJOName':'IAC_HZ_ChangeRecordsInfo',
    'POJOQuerySQL':'select obj from IAC_HZ_ChangeRecordsInfo obj where obj.'+WaiBaoZhiXin_Query2_Part,
    'COListQueryCondition':'IAC_HZ_ChangeRecordsInfo.'+WaiBaoZhiXin_Query2_Part+' order by IAC_HZ_ChangeRecordsInfo.changedate desc',
    'COListAdditionalQueryCondition':'" and o.DengJiRen="+'+__USER_ID__,
    'ClassName':'GongShang_HZ_BianGengXinXi',
    'DialogContentTitle':'工商变更信息（海致）',
    'QueryConditionList' : [
                  GongShang_HZ_BianGengXinXi_OfCompany,GongShang_HZ_BianGengXinXi_BianGengRiQi,GongShang_HZ_BianGengXinXi_BianGengShiXiang,
         ],
    'TableColumnsList' : [
                  GongShang_HZ_BianGengXinXi_OfCompany,GongShang_HZ_BianGengXinXi_BianGengRiQi,GongShang_HZ_BianGengXinXi_BianGengShiXiang,GongShang_HZ_BianGengXinXi_BianGengQianNeiRong,GongShang_HZ_BianGengXinXi_BianGengHouNeiRong,
                  GongShang_HZ_BianGengXinXi_DengJiRen,GongShang_HZ_BianGengXinXi_DengJiShiJian,
         ],
    'ViewColumnsList' : [
                  GongShang_HZ_BianGengXinXi_OfCompany,GongShang_HZ_BianGengXinXi_ShuJuYouXiaoXing,GongShang_HZ_BianGengXinXi_BianGengRiQi,GongShang_HZ_BianGengXinXi_BianGengShiXiang,GongShang_HZ_BianGengXinXi_BianGengQianNeiRong,GongShang_HZ_BianGengXinXi_BianGengHouNeiRong,
                  GongShang_HZ_BianGengXinXi_DengJiRen,GongShang_HZ_BianGengXinXi_DengJiShiJian,
         ],
    'EditColumnsList':  [
                  GongShang_HZ_BianGengXinXi_OfCompany,GongShang_HZ_BianGengXinXi_ShuJuYouXiaoXing,GongShang_HZ_BianGengXinXi_BianGengRiQi,GongShang_HZ_BianGengXinXi_BianGengShiXiang,GongShang_HZ_BianGengXinXi_BianGengQianNeiRong,GongShang_HZ_BianGengXinXi_BianGengHouNeiRong,
         ],
    'AllColumns':[
                  GongShang_HZ_BianGengXinXi_bold_id,GongShang_HZ_BianGengXinXi_OfCompany,GongShang_HZ_BianGengXinXi_ShuJuYouXiaoXing,GongShang_HZ_BianGengXinXi_BianGengRiQi,GongShang_HZ_BianGengXinXi_BianGengShiXiang,GongShang_HZ_BianGengXinXi_BianGengQianNeiRong,GongShang_HZ_BianGengXinXi_BianGengHouNeiRong,
                  GongShang_HZ_BianGengXinXi_DengJiRen,GongShang_HZ_BianGengXinXi_DengJiShiJian,
                  ],
    'DetailCO':[],
    'MasterCORefColumn':GongShang_HZ_BianGengXinXi_bold_id,
    'MasterCOAttachments':[SelectableCompany_HZ_Attachment],'MasterCOAttachments_Reflect':[{'From':SelectableCompany_HZ_Attachment_MingCheng,'To':GongShang_HZ_BianGengXinXi_OfCompany,'DealWay':'Replace'}],
    'BusiActions':[AddAction_Default,EditAction_Default],
    'Normal_methods':'''\
        public void computeOnAttachmentClickFinished(){
        }
        private Double recompute(){
            label_help.setText("");
            label_help.setToolTipText(label_help.getText());
            return 0d;
        }'''
    }

#========================================================================================================================================
GongShang_HZ_BianGengXinXi_GuanLi = {
    'Name':'工商变更信息管理（海致）','ActionName':'工商变更信息管理（海致）','Image':'icons/GongShangBianGeng.png',
    'POJOName':'IAC_HZ_ChangeRecordsInfo',
    'POJOQuerySQL':'',
    'COListQueryCondition':' order by IAC_HZ_ChangeRecordsInfo.changedate desc',
    'ClassName':'GongShang_HZ_BianGengXinXi_GuanLi',
    'DialogContentTitle':'工商变更信息管理（海致）',
    'QueryConditionList': [
        GongShang_HZ_BianGengXinXi_OfCompany, GongShang_HZ_BianGengXinXi_BianGengRiQi,
        GongShang_HZ_BianGengXinXi_BianGengShiXiang, GongShang_HZ_BianGengXinXi_DengJiRen,
    ],
    'TableColumnsList': [
        GongShang_HZ_BianGengXinXi_OfCompany, GongShang_HZ_BianGengXinXi_BianGengRiQi,
        GongShang_HZ_BianGengXinXi_BianGengShiXiang, GongShang_HZ_BianGengXinXi_BianGengQianNeiRong,
        GongShang_HZ_BianGengXinXi_BianGengHouNeiRong,
        GongShang_HZ_BianGengXinXi_DengJiRen, GongShang_HZ_BianGengXinXi_DengJiShiJian,
    ],
    'ViewColumnsList': [
        GongShang_HZ_BianGengXinXi_OfCompany, GongShang_HZ_BianGengXinXi_ShuJuYouXiaoXing,GongShang_HZ_BianGengXinXi_BianGengRiQi,
        GongShang_HZ_BianGengXinXi_BianGengShiXiang, GongShang_HZ_BianGengXinXi_BianGengQianNeiRong,
        GongShang_HZ_BianGengXinXi_BianGengHouNeiRong,
        GongShang_HZ_BianGengXinXi_DengJiRen, GongShang_HZ_BianGengXinXi_DengJiShiJian,
    ],
    'EditColumnsList': [
        GongShang_HZ_BianGengXinXi_OfCompany, GongShang_HZ_BianGengXinXi_ShuJuYouXiaoXing,GongShang_HZ_BianGengXinXi_BianGengRiQi,
        GongShang_HZ_BianGengXinXi_BianGengShiXiang, GongShang_HZ_BianGengXinXi_BianGengQianNeiRong,
        GongShang_HZ_BianGengXinXi_BianGengHouNeiRong,
        GongShang_HZ_BianGengXinXi_DengJiRen, GongShang_HZ_BianGengXinXi_DengJiShiJian,
    ],
    'AllColumns': [
        GongShang_HZ_BianGengXinXi_bold_id, GongShang_HZ_BianGengXinXi_OfCompany,GongShang_HZ_BianGengXinXi_ShuJuYouXiaoXing,
        GongShang_HZ_BianGengXinXi_BianGengRiQi, GongShang_HZ_BianGengXinXi_BianGengShiXiang,
        GongShang_HZ_BianGengXinXi_BianGengQianNeiRong, GongShang_HZ_BianGengXinXi_BianGengHouNeiRong,
        GongShang_HZ_BianGengXinXi_DengJiRen, GongShang_HZ_BianGengXinXi_DengJiShiJian,
    ],
    'DetailCO': [],
    'MasterCORefColumn': GongShang_HZ_BianGengXinXi_bold_id,
    'MasterCOAttachments': [SelectableCompany_HZ_Attachment], 'MasterCOAttachments_Reflect': [
        {'From': SelectableCompany_HZ_Attachment_MingCheng, 'To': GongShang_HZ_BianGengXinXi_OfCompany,
         'DealWay': 'Replace'}],
    'BusiActions': [AddAction_Default, EditAction_Default],
    'Normal_methods': '''\
        public void computeOnAttachmentClickFinished(){
        }
        private Double recompute(){
            label_help.setText("");
            label_help.setToolTipText(label_help.getText());
            return 0d;
        }'''
}

#========================================================================================================================================
GongShang_HZ_FenZhiJiGou_bold_id={'DBColName':'bold_id','isIDCol':True, 'refPOJOColName':'IAC_HZ_Branch.bold_id', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'ID', 'PGFieldType':'Integer', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_FenZhiJiGou_OfCompany={'DBColName':'OfCompany', 'refPOJOColName':'IAC_HZ_Branch.ofcompany', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'实际企业名称', 'PGFieldType':'Combo', 'PGComboProvider':SelectableCompany_HZ_Dict,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':False,'PGFieldRequiredValue':True}
GongShang_HZ_FenZhiJiGou_ShuJuYouXiaoXing={'DBColName':'ShuJuYouXiaoXing', 'refPOJOColName':'IAC_HZ_Branch.datavalidity', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'本记录有效', 'PGFieldType':'combo', 'PGComboProvider':YesNoDict,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False , 'PGFieldDefaultValue':1171,}
GongShang_HZ_FenZhiJiGou_GongSiMingCheng={'DBColName':'GongSiMingCheng', 'refPOJOColName':'IAC_HZ_Branch.companyname', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'分支公司名称', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_FenZhiJiGou_FaDingDaiBiaoRen={'DBColName':'FaDingDaiBiaoRen', 'refPOJOColName':'IAC_HZ_Branch.legalman', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'法定代表人', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_FenZhiJiGou_ChengLiRiQi={'DBColName':'ChengLiRiQi', 'refPOJOColName':'IAC_HZ_Branch.registereddate', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'成立日期', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_FenZhiJiGou_ZhuCeZiJin={'DBColName':'ZhuCeZiJin', 'refPOJOColName':'IAC_HZ_Branch.registeredcapital', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'注册资金', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_FenZhiJiGou_DiZhi={'DBColName':'DiZhi', 'refPOJOColName':'IAC_HZ_Branch.address', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'地址', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':2,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_FenZhiJiGou_DengJiRen={'DBColName':'DengJiRen', 'refPOJOColName':'IAC_HZ_Branch.regperson', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'登记人', 'PGFieldType':'Combo', 'PGComboProvider':PersonDict_Employee_or_SystemUser,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':True,'PGFieldDefaultValue':__USER_ID__,}
GongShang_HZ_FenZhiJiGou_DengJiShiJian={'DBColName':'DengJiShiJian', 'refPOJOColName':'IAC_HZ_Branch.regtime', 'DBColType':'Timestamp','PGFieldName':'', 'PGFieldLabel':'登记时间', 'PGFieldType':'datetime', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':True,'PGFieldDefaultValue':True}
GongShang_HZ_FenZhiJiGou = {
    'Name':'工商分支机构（海致）','ActionName':'工商分支机构（海致）','Image':'icons/FenZhiJiGou.png',
    'POJOName':'IAC_HZ_Branch',
    'POJOQuerySQL':'select obj from IAC_HZ_Branch obj where obj.'+WaiBaoZhiXin_Query2_Part,
    'COListQueryCondition':'IAC_HZ_Branch.'+WaiBaoZhiXin_Query2_Part+' order by IAC_HZ_Branch.companyname desc',
    'COListAdditionalQueryCondition':'" and o.DengJiRen="+'+__USER_ID__,
    'ClassName':'GongShang_HZ_FenZhiJiGou',
    'DialogContentTitle': '工商分支机构（海致）',
    'QueryConditionList': [
        GongShang_HZ_FenZhiJiGou_OfCompany, GongShang_HZ_FenZhiJiGou_GongSiMingCheng,
        GongShang_HZ_FenZhiJiGou_ChengLiRiQi, GongShang_HZ_FenZhiJiGou_FaDingDaiBiaoRen, GongShang_HZ_FenZhiJiGou_DiZhi,
    ],
    'TableColumnsList': [
        GongShang_HZ_FenZhiJiGou_OfCompany, GongShang_HZ_FenZhiJiGou_GongSiMingCheng,
        GongShang_HZ_FenZhiJiGou_FaDingDaiBiaoRen, GongShang_HZ_FenZhiJiGou_ChengLiRiQi,
        GongShang_HZ_FenZhiJiGou_ZhuCeZiJin, GongShang_HZ_FenZhiJiGou_DiZhi,
        GongShang_HZ_FenZhiJiGou_DengJiRen, GongShang_HZ_FenZhiJiGou_DengJiShiJian,
    ],
    'ViewColumnsList': [
        GongShang_HZ_FenZhiJiGou_OfCompany, GongShang_HZ_FenZhiJiGou_ShuJuYouXiaoXing,GongShang_HZ_FenZhiJiGou_GongSiMingCheng,
        GongShang_HZ_FenZhiJiGou_FaDingDaiBiaoRen, GongShang_HZ_FenZhiJiGou_ChengLiRiQi,
        GongShang_HZ_FenZhiJiGou_ZhuCeZiJin, GongShang_HZ_FenZhiJiGou_DiZhi,
        GongShang_HZ_FenZhiJiGou_DengJiRen, GongShang_HZ_FenZhiJiGou_DengJiShiJian,
    ],
    'EditColumnsList': [
        GongShang_HZ_FenZhiJiGou_OfCompany, GongShang_HZ_FenZhiJiGou_ShuJuYouXiaoXing,GongShang_HZ_FenZhiJiGou_GongSiMingCheng,
        GongShang_HZ_FenZhiJiGou_FaDingDaiBiaoRen, GongShang_HZ_FenZhiJiGou_ChengLiRiQi,
        GongShang_HZ_FenZhiJiGou_ZhuCeZiJin, GongShang_HZ_FenZhiJiGou_DiZhi,
        GongShang_HZ_FenZhiJiGou_DengJiRen, GongShang_HZ_FenZhiJiGou_DengJiShiJian,
    ],
    'AllColumns': [
        GongShang_HZ_FenZhiJiGou_OfCompany, GongShang_HZ_FenZhiJiGou_bold_id, GongShang_HZ_FenZhiJiGou_ShuJuYouXiaoXing,GongShang_HZ_FenZhiJiGou_GongSiMingCheng,
        GongShang_HZ_FenZhiJiGou_FaDingDaiBiaoRen, GongShang_HZ_FenZhiJiGou_ChengLiRiQi,
        GongShang_HZ_FenZhiJiGou_ZhuCeZiJin, GongShang_HZ_FenZhiJiGou_DiZhi,
        GongShang_HZ_FenZhiJiGou_DengJiRen, GongShang_HZ_FenZhiJiGou_DengJiShiJian,
    ],
    'DetailCO':[],
    'MasterCORefColumn':GongShang_HZ_FenZhiJiGou_bold_id,
    'MasterCOAttachments':[SelectableCompany_HZ_Attachment],'MasterCOAttachments_Reflect':[{'From':SelectableCompany_HZ_Attachment_MingCheng,'To':GongShang_HZ_FenZhiJiGou_OfCompany,'DealWay':'Replace'}],
    'BusiActions':[AddAction_Default,EditAction_Default],
    'Normal_methods':'''\
        public void computeOnAttachmentClickFinished(){
        }
        private Double recompute(){
            label_help.setText("");
            label_help.setToolTipText(label_help.getText());
            return 0d;
        }'''
    }

#========================================================================================================================================
GongShang_HZ_FenZhiJiGou_GuanLi = {
    'Name':'工商分支机构管理（海致）','ActionName':'工商分支机构管理（海致）','Image':'icons/FenZhiJiGou.png',
    'POJOName':'IAC_HZ_Branch',
    'POJOQuerySQL':'',
    'COListQueryCondition':' order by IAC_HZ_Branch.companyname desc',
    'ClassName':'GongShang_HZ_FenZhiJiGou_GuanLi',
    'DialogContentTitle':'工商分支机构管理（海致）',
    'QueryConditionList': [
        GongShang_HZ_FenZhiJiGou_OfCompany, GongShang_HZ_FenZhiJiGou_GongSiMingCheng,
        GongShang_HZ_FenZhiJiGou_ChengLiRiQi, GongShang_HZ_FenZhiJiGou_FaDingDaiBiaoRen, GongShang_HZ_FenZhiJiGou_DiZhi,
        GongShang_HZ_FenZhiJiGou_DengJiRen,
    ],
    'TableColumnsList': [
        GongShang_HZ_FenZhiJiGou_OfCompany, GongShang_HZ_FenZhiJiGou_GongSiMingCheng,
        GongShang_HZ_FenZhiJiGou_FaDingDaiBiaoRen, GongShang_HZ_FenZhiJiGou_ChengLiRiQi,
        GongShang_HZ_FenZhiJiGou_ZhuCeZiJin, GongShang_HZ_FenZhiJiGou_DiZhi,
        GongShang_HZ_FenZhiJiGou_DengJiRen, GongShang_HZ_FenZhiJiGou_DengJiShiJian,
    ],
    'ViewColumnsList': [
        GongShang_HZ_FenZhiJiGou_OfCompany, GongShang_HZ_FenZhiJiGou_ShuJuYouXiaoXing,GongShang_HZ_FenZhiJiGou_GongSiMingCheng,
        GongShang_HZ_FenZhiJiGou_FaDingDaiBiaoRen, GongShang_HZ_FenZhiJiGou_ChengLiRiQi,
        GongShang_HZ_FenZhiJiGou_ZhuCeZiJin, GongShang_HZ_FenZhiJiGou_DiZhi,
        GongShang_HZ_FenZhiJiGou_DengJiRen, GongShang_HZ_FenZhiJiGou_DengJiShiJian,
    ],
    'EditColumnsList': [
        GongShang_HZ_FenZhiJiGou_OfCompany, GongShang_HZ_FenZhiJiGou_ShuJuYouXiaoXing,GongShang_HZ_FenZhiJiGou_GongSiMingCheng,
        GongShang_HZ_FenZhiJiGou_FaDingDaiBiaoRen, GongShang_HZ_FenZhiJiGou_ChengLiRiQi,
        GongShang_HZ_FenZhiJiGou_ZhuCeZiJin, GongShang_HZ_FenZhiJiGou_DiZhi,
        GongShang_HZ_FenZhiJiGou_DengJiRen, GongShang_HZ_FenZhiJiGou_DengJiShiJian,
    ],
    'AllColumns': [
        GongShang_HZ_FenZhiJiGou_OfCompany, GongShang_HZ_FenZhiJiGou_bold_id,GongShang_HZ_FenZhiJiGou_ShuJuYouXiaoXing, GongShang_HZ_FenZhiJiGou_GongSiMingCheng,
        GongShang_HZ_FenZhiJiGou_FaDingDaiBiaoRen, GongShang_HZ_FenZhiJiGou_ChengLiRiQi,
        GongShang_HZ_FenZhiJiGou_ZhuCeZiJin, GongShang_HZ_FenZhiJiGou_DiZhi,
        GongShang_HZ_FenZhiJiGou_DengJiRen, GongShang_HZ_FenZhiJiGou_DengJiShiJian,
    ],
    'DetailCO': [],
    'MasterCORefColumn':GongShang_HZ_FenZhiJiGou_bold_id,
    'MasterCOAttachments':[SelectableCompany_HZ_Attachment],'MasterCOAttachments_Reflect':[{'From':SelectableCompany_HZ_Attachment_MingCheng,'To':GongShang_HZ_FenZhiJiGou_OfCompany,'DealWay':'Replace'}],
    'BusiActions':[AddAction_Default,EditAction_Default],
    'Normal_methods':'''\
        public void computeOnAttachmentClickFinished(){
        }
        private Double recompute(){
            label_help.setText("");
            label_help.setToolTipText(label_help.getText());
            return 0d;
        }'''
    }

#========================================================================================================================================
GongShang_HZ_ZhuYaoRenYuan_bold_id={'DBColName':'bold_id','isIDCol':True, 'refPOJOColName':'IAC_HZ_KeyPerson.bold_id', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'ID', 'PGFieldType':'Integer', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_ZhuYaoRenYuan_OfCompany={'DBColName':'OfCompany', 'refPOJOColName':'IAC_HZ_KeyPerson.ofcompany', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'实际企业名称', 'PGFieldType':'Combo', 'PGComboProvider':SelectableCompany_HZ_Dict,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':False,'PGFieldRequiredValue':True}
GongShang_HZ_ZhuYaoRenYuan_ShuJuYouXiaoXing={'DBColName':'ShuJuYouXiaoXing', 'refPOJOColName':'IAC_HZ_KeyPerson.datavalidity', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'本记录有效', 'PGFieldType':'combo', 'PGComboProvider':YesNoDict,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False , 'PGFieldDefaultValue':1171,}
GongShang_HZ_ZhuYaoRenYuan_MingZi={'DBColName':'MingZi', 'refPOJOColName':'IAC_HZ_KeyPerson.name', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'名字', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_ZhuYaoRenYuan_ZhiWei={'DBColName':'ZhiWei', 'refPOJOColName':'IAC_HZ_KeyPerson.position', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'职位', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_ZhuYaoRenYuan_DengJiRen={'DBColName':'DengJiRen', 'refPOJOColName':'IAC_HZ_KeyPerson.regperson', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'登记人', 'PGFieldType':'Combo', 'PGComboProvider':PersonDict_Employee_or_SystemUser,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':True,'PGFieldDefaultValue':__USER_ID__,}
GongShang_HZ_ZhuYaoRenYuan_DengJiShiJian={'DBColName':'DengJiShiJian', 'refPOJOColName':'IAC_HZ_KeyPerson.regtime', 'DBColType':'Timestamp','PGFieldName':'', 'PGFieldLabel':'登记时间', 'PGFieldType':'datetime', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':True,'PGFieldDefaultValue':True}
GongShang_HZ_ZhuYaoRenYuan = {
    'Name':'工商主要人员（海致）','ActionName':'工商主要人员（海致）','Image':'icons/GaoGuan.png',
    'POJOName':'IAC_HZ_KeyPerson',
    'POJOQuerySQL':'select obj from IAC_HZ_KeyPerson obj where obj.'+WaiBaoZhiXin_Query2_Part,
    'COListQueryCondition':'IAC_HZ_KeyPerson.'+WaiBaoZhiXin_Query2_Part+' order by IAC_HZ_KeyPerson.name desc',
    'COListAdditionalQueryCondition':'" and o.DengJiRen="+'+__USER_ID__,
    'ClassName': 'GongShang_HZ_ZhuYaoRenYuan',
    'DialogContentTitle': '工商主要人员（海致）',
    'QueryConditionList': [
        GongShang_HZ_ZhuYaoRenYuan_OfCompany, GongShang_HZ_ZhuYaoRenYuan_MingZi, GongShang_HZ_ZhuYaoRenYuan_ZhiWei,
    ],
    'TableColumnsList': [
        GongShang_HZ_ZhuYaoRenYuan_OfCompany, GongShang_HZ_ZhuYaoRenYuan_MingZi, GongShang_HZ_ZhuYaoRenYuan_ZhiWei,
        GongShang_HZ_ZhuYaoRenYuan_DengJiRen, GongShang_HZ_ZhuYaoRenYuan_DengJiShiJian,
    ],
    'ViewColumnsList': [
        GongShang_HZ_ZhuYaoRenYuan_OfCompany, GongShang_HZ_ZhuYaoRenYuan_ShuJuYouXiaoXing,GongShang_HZ_ZhuYaoRenYuan_MingZi, GongShang_HZ_ZhuYaoRenYuan_ZhiWei,
        GongShang_HZ_ZhuYaoRenYuan_DengJiRen, GongShang_HZ_ZhuYaoRenYuan_DengJiShiJian,
    ],
    'EditColumnsList': [
        GongShang_HZ_ZhuYaoRenYuan_OfCompany, GongShang_HZ_ZhuYaoRenYuan_ShuJuYouXiaoXing,GongShang_HZ_ZhuYaoRenYuan_MingZi, GongShang_HZ_ZhuYaoRenYuan_ZhiWei,
        GongShang_HZ_ZhuYaoRenYuan_DengJiRen, GongShang_HZ_ZhuYaoRenYuan_DengJiShiJian,
    ],
    'AllColumns': [
        GongShang_HZ_ZhuYaoRenYuan_bold_id, GongShang_HZ_ZhuYaoRenYuan_OfCompany, GongShang_HZ_ZhuYaoRenYuan_ShuJuYouXiaoXing,GongShang_HZ_ZhuYaoRenYuan_MingZi,
        GongShang_HZ_ZhuYaoRenYuan_ZhiWei, GongShang_HZ_ZhuYaoRenYuan_DengJiRen,
        GongShang_HZ_ZhuYaoRenYuan_DengJiShiJian,
    ],
    'DetailCO': [],
    'MasterCORefColumn':GongShang_HZ_ZhuYaoRenYuan_bold_id,
    'MasterCOAttachments':[SelectableCompany_HZ_Attachment],'MasterCOAttachments_Reflect':[{'From':SelectableCompany_HZ_Attachment_MingCheng,'To':GongShang_HZ_ZhuYaoRenYuan_OfCompany,'DealWay':'Replace'}],
    'BusiActions':[AddAction_Default,EditAction_Default],
    'Normal_methods':'''\
        public void computeOnAttachmentClickFinished(){
        }
        private Double recompute(){
            label_help.setText("");
            label_help.setToolTipText(label_help.getText());
            return 0d;
        }'''
    }

#========================================================================================================================================
GongShang_HZ_ZhuYaoRenYuan_GuanLi = {
    'Name':'工商主要人员管理（海致）','ActionName':'工商主要人员管理（海致）','Image':'icons/GaoGuan.png',
    'POJOName':'IAC_HZ_KeyPerson',
    'POJOQuerySQL':'',
    'COListQueryCondition':' order by IAC_HZ_KeyPerson.name desc',
    'ClassName':'GongShang_HZ_ZhuYaoRenYuan_GuanLi',
    'DialogContentTitle':'工商主要人员管理（海致）',
    'QueryConditionList': [
        GongShang_HZ_ZhuYaoRenYuan_OfCompany, GongShang_HZ_ZhuYaoRenYuan_MingZi, GongShang_HZ_ZhuYaoRenYuan_ZhiWei,
        GongShang_HZ_ZhuYaoRenYuan_DengJiRen,
    ],
    'TableColumnsList': [
        GongShang_HZ_ZhuYaoRenYuan_OfCompany, GongShang_HZ_ZhuYaoRenYuan_MingZi, GongShang_HZ_ZhuYaoRenYuan_ZhiWei,
        GongShang_HZ_ZhuYaoRenYuan_DengJiRen, GongShang_HZ_ZhuYaoRenYuan_DengJiShiJian,
    ],
    'ViewColumnsList': [
        GongShang_HZ_ZhuYaoRenYuan_OfCompany, GongShang_HZ_ZhuYaoRenYuan_ShuJuYouXiaoXing,GongShang_HZ_ZhuYaoRenYuan_MingZi, GongShang_HZ_ZhuYaoRenYuan_ZhiWei,
        GongShang_HZ_ZhuYaoRenYuan_DengJiRen, GongShang_HZ_ZhuYaoRenYuan_DengJiShiJian,
    ],
    'EditColumnsList': [
        GongShang_HZ_ZhuYaoRenYuan_OfCompany, GongShang_HZ_ZhuYaoRenYuan_ShuJuYouXiaoXing,GongShang_HZ_ZhuYaoRenYuan_MingZi, GongShang_HZ_ZhuYaoRenYuan_ZhiWei,
        GongShang_HZ_ZhuYaoRenYuan_DengJiRen, GongShang_HZ_ZhuYaoRenYuan_DengJiShiJian,
    ],
    'AllColumns': [
        GongShang_HZ_ZhuYaoRenYuan_bold_id, GongShang_HZ_ZhuYaoRenYuan_OfCompany, GongShang_HZ_ZhuYaoRenYuan_ShuJuYouXiaoXing,GongShang_HZ_ZhuYaoRenYuan_MingZi,
        GongShang_HZ_ZhuYaoRenYuan_ZhiWei, GongShang_HZ_ZhuYaoRenYuan_DengJiRen,
        GongShang_HZ_ZhuYaoRenYuan_DengJiShiJian,
    ],
    'DetailCO': [],
    'MasterCORefColumn':GongShang_HZ_ZhuYaoRenYuan_bold_id,
    'MasterCOAttachments':[SelectableCompany_HZ_Attachment],'MasterCOAttachments_Reflect':[{'From':SelectableCompany_HZ_Attachment_MingCheng,'To':GongShang_HZ_ZhuYaoRenYuan_OfCompany,'DealWay':'Replace'}],
    'BusiActions':[AddAction_Default,EditAction_Default],
    'Normal_methods':'''\
        public void computeOnAttachmentClickFinished(){
        }
        private Double recompute(){
            label_help.setText("");
            label_help.setToolTipText(label_help.getText());
            return 0d;
        }'''
    }

#========================================================================================================================================
GongShang_HZ_GuDongXinXi_bold_id={'DBColName':'bold_id','isIDCol':True, 'refPOJOColName':'IAC_HZ_ShareholderInfo.bold_id', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'ID', 'PGFieldType':'Integer', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuDongXinXi_OfCompany={'DBColName':'OfCompany', 'refPOJOColName':'IAC_HZ_ShareholderInfo.ofcompany', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'实际企业名称', 'PGFieldType':'Combo', 'PGComboProvider':SelectableCompany_HZ_Dict,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':False,'PGFieldRequiredValue':True}
GongShang_HZ_GuDongXinXi_ShuJuYouXiaoXing={'DBColName':'ShuJuYouXiaoXing', 'refPOJOColName':'IAC_HZ_ShareholderInfo.datavalidity', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'本记录有效', 'PGFieldType':'combo', 'PGComboProvider':YesNoDict,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False , 'PGFieldDefaultValue':1171,}
GongShang_HZ_GuDongXinXi_GuDongMingCheng={'DBColName':'GuDongMingCheng', 'refPOJOColName':'IAC_HZ_ShareholderInfo.shareholdername', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'股东名称', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuDongXinXi_GuDongLeiXing={'DBColName':'GuDongLeiXing', 'refPOJOColName':'IAC_HZ_ShareholderInfo.shareholdertype', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'股东类型', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuDongXinXi_RenJiaoE={'DBColName':'RenJiaoE', 'refPOJOColName':'IAC_HZ_ShareholderInfo.subscriptionamount', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'认缴额', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuDongXinXi_ShiJiaoE={'DBColName':'ShiJiaoE', 'refPOJOColName':'IAC_HZ_ShareholderInfo.paiedamount', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'实缴额', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuDongXinXi_ChiGuBiLi={'DBColName':'ChiGuBiLi', 'refPOJOColName':'IAC_HZ_ShareholderInfo.ratio', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'持股比例', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuDongXinXi_DengJiRen={'DBColName':'DengJiRen', 'refPOJOColName':'IAC_HZ_ShareholderInfo.regperson', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'登记人', 'PGFieldType':'Combo', 'PGComboProvider':PersonDict_Employee_or_SystemUser,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':True,'PGFieldDefaultValue':__USER_ID__,}
GongShang_HZ_GuDongXinXi_DengJiShiJian={'DBColName':'DengJiShiJian', 'refPOJOColName':'IAC_HZ_ShareholderInfo.regtime', 'DBColType':'Timestamp','PGFieldName':'', 'PGFieldLabel':'登记时间', 'PGFieldType':'datetime', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':True,'PGFieldDefaultValue':True}
GongShang_HZ_GuDongXinXi = {
    'Name':'工商股东信息（海致）','ActionName':'工商股东信息（海致）','Image':'icons/GuDongXinXi.png',
    'POJOName':'IAC_HZ_ShareholderInfo',
    'POJOQuerySQL':'select obj from IAC_HZ_ShareholderInfo obj where obj.'+WaiBaoZhiXin_Query2_Part,
    'COListQueryCondition':'IAC_HZ_ShareholderInfo.'+WaiBaoZhiXin_Query2_Part+' order by IAC_HZ_ShareholderInfo.shareholdername desc',
    'COListAdditionalQueryCondition':'" and o.DengJiRen="+'+__USER_ID__,
    'ClassName':'GongShang_HZ_GuDongXinXi',
    'DialogContentTitle':'工商股东信息（海致）',
    'QueryConditionList' : [
        GongShang_HZ_GuDongXinXi_OfCompany, GongShang_HZ_GuDongXinXi_GuDongMingCheng,
        GongShang_HZ_GuDongXinXi_GuDongLeiXing,
    ],
    'TableColumnsList': [
        GongShang_HZ_GuDongXinXi_OfCompany, GongShang_HZ_GuDongXinXi_GuDongMingCheng,
        GongShang_HZ_GuDongXinXi_GuDongLeiXing, GongShang_HZ_GuDongXinXi_RenJiaoE, GongShang_HZ_GuDongXinXi_ShiJiaoE,
        GongShang_HZ_GuDongXinXi_ChiGuBiLi,
        GongShang_HZ_GuDongXinXi_DengJiRen, GongShang_HZ_GuDongXinXi_DengJiShiJian,
    ],
    'ViewColumnsList': [
        GongShang_HZ_GuDongXinXi_OfCompany, GongShang_HZ_GuDongXinXi_ShuJuYouXiaoXing,GongShang_HZ_GuDongXinXi_GuDongMingCheng,
        GongShang_HZ_GuDongXinXi_GuDongLeiXing, GongShang_HZ_GuDongXinXi_RenJiaoE, GongShang_HZ_GuDongXinXi_ShiJiaoE,
        GongShang_HZ_GuDongXinXi_ChiGuBiLi,
        GongShang_HZ_GuDongXinXi_DengJiRen, GongShang_HZ_GuDongXinXi_DengJiShiJian,
    ],
    'EditColumnsList': [
        GongShang_HZ_GuDongXinXi_OfCompany, GongShang_HZ_GuDongXinXi_ShuJuYouXiaoXing,GongShang_HZ_GuDongXinXi_GuDongMingCheng,
        GongShang_HZ_GuDongXinXi_GuDongLeiXing, GongShang_HZ_GuDongXinXi_RenJiaoE, GongShang_HZ_GuDongXinXi_ShiJiaoE,
        GongShang_HZ_GuDongXinXi_ChiGuBiLi,
        GongShang_HZ_GuDongXinXi_DengJiRen, GongShang_HZ_GuDongXinXi_DengJiShiJian,
    ],
    'AllColumns': [
        GongShang_HZ_GuDongXinXi_bold_id, GongShang_HZ_GuDongXinXi_OfCompany, GongShang_HZ_GuDongXinXi_ShuJuYouXiaoXing,GongShang_HZ_GuDongXinXi_GuDongMingCheng,
        GongShang_HZ_GuDongXinXi_GuDongLeiXing, GongShang_HZ_GuDongXinXi_RenJiaoE, GongShang_HZ_GuDongXinXi_ShiJiaoE,
        GongShang_HZ_GuDongXinXi_ChiGuBiLi,
        GongShang_HZ_GuDongXinXi_DengJiRen, GongShang_HZ_GuDongXinXi_DengJiShiJian,
    ],
    'DetailCO': [],
    'MasterCORefColumn':GongShang_HZ_GuDongXinXi_bold_id,
    'MasterCOAttachments':[SelectableCompany_HZ_Attachment],'MasterCOAttachments_Reflect':[{'From':SelectableCompany_HZ_Attachment_MingCheng,'To':GongShang_HZ_GuDongXinXi_OfCompany,'DealWay':'Replace'}],
    'BusiActions':[AddAction_Default,EditAction_Default],
    'Normal_methods':'''\
        public void computeOnAttachmentClickFinished(){
        }
        private Double recompute(){
            label_help.setText("");
            label_help.setToolTipText(label_help.getText());
            return 0d;
        }'''
    }


#========================================================================================================================================
GongShang_HZ_GuDongXinXi_GuanLi = {
    'Name':'工商股东信息管理（海致）','ActionName':'工商股东信息管理（海致）','Image':'icons/GuDongXinXi.png',
    'POJOName':'IAC_HZ_ShareholderInfo',
    'POJOQuerySQL':'',
    'COListQueryCondition':' order by IAC_HZ_ShareholderInfo.shareholdername desc',
    'ClassName':'GongShang_HZ_GuDongXinXi_GuanLi',
    'DialogContentTitle':'工商股东信息管理（海致）',
    'QueryConditionList': [
        GongShang_HZ_GuDongXinXi_OfCompany, GongShang_HZ_GuDongXinXi_GuDongMingCheng,
        GongShang_HZ_GuDongXinXi_GuDongLeiXing, GongShang_HZ_GuDongXinXi_DengJiRen,
    ],
    'TableColumnsList': [
        GongShang_HZ_GuDongXinXi_OfCompany, GongShang_HZ_GuDongXinXi_GuDongMingCheng,
        GongShang_HZ_GuDongXinXi_GuDongLeiXing, GongShang_HZ_GuDongXinXi_RenJiaoE, GongShang_HZ_GuDongXinXi_ShiJiaoE,
        GongShang_HZ_GuDongXinXi_ChiGuBiLi,
        GongShang_HZ_GuDongXinXi_DengJiRen, GongShang_HZ_GuDongXinXi_DengJiShiJian,
    ],
    'ViewColumnsList': [
        GongShang_HZ_GuDongXinXi_OfCompany, GongShang_HZ_GuDongXinXi_ShuJuYouXiaoXing,GongShang_HZ_GuDongXinXi_GuDongMingCheng,
        GongShang_HZ_GuDongXinXi_GuDongLeiXing, GongShang_HZ_GuDongXinXi_RenJiaoE, GongShang_HZ_GuDongXinXi_ShiJiaoE,
        GongShang_HZ_GuDongXinXi_ChiGuBiLi,
        GongShang_HZ_GuDongXinXi_DengJiRen, GongShang_HZ_GuDongXinXi_DengJiShiJian,
    ],
    'EditColumnsList': [
        GongShang_HZ_GuDongXinXi_OfCompany,GongShang_HZ_GuDongXinXi_ShuJuYouXiaoXing, GongShang_HZ_GuDongXinXi_GuDongMingCheng,
        GongShang_HZ_GuDongXinXi_GuDongLeiXing, GongShang_HZ_GuDongXinXi_RenJiaoE, GongShang_HZ_GuDongXinXi_ShiJiaoE,
        GongShang_HZ_GuDongXinXi_ChiGuBiLi,
        GongShang_HZ_GuDongXinXi_DengJiRen, GongShang_HZ_GuDongXinXi_DengJiShiJian,
    ],
    'AllColumns': [
        GongShang_HZ_GuDongXinXi_bold_id, GongShang_HZ_GuDongXinXi_OfCompany, GongShang_HZ_GuDongXinXi_ShuJuYouXiaoXing,GongShang_HZ_GuDongXinXi_GuDongMingCheng,
        GongShang_HZ_GuDongXinXi_GuDongLeiXing, GongShang_HZ_GuDongXinXi_RenJiaoE, GongShang_HZ_GuDongXinXi_ShiJiaoE,
        GongShang_HZ_GuDongXinXi_ChiGuBiLi,
        GongShang_HZ_GuDongXinXi_DengJiRen, GongShang_HZ_GuDongXinXi_DengJiShiJian,
    ],
    'DetailCO': [],
    'MasterCORefColumn':GongShang_HZ_GuDongXinXi_bold_id,
    'MasterCOAttachments':[SelectableCompany_HZ_Attachment],'MasterCOAttachments_Reflect':[{'From':SelectableCompany_HZ_Attachment_MingCheng,'To':GongShang_HZ_GuDongXinXi_OfCompany,'DealWay':'Replace'}],
    'BusiActions':[AddAction_Default,EditAction_Default],
    'Normal_methods':'''\
        public void computeOnAttachmentClickFinished(){
        }
        private Double recompute(){
            label_help.setText("");
            label_help.setToolTipText(label_help.getText());
            return 0d;
        }'''
    }

#========================================================================================================================================
GongShang_HZ_GuQuanBianGengXinXi_bold_id={'DBColName':'bold_id','isIDCol':True, 'refPOJOColName':'IAC_HZ_ChangeShareholdingInfo.bold_id', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'ID', 'PGFieldType':'Integer', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuQuanBianGengXinXi_OfCompany={'DBColName':'OfCompany', 'refPOJOColName':'IAC_HZ_ChangeShareholdingInfo.ofcompany', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'实际企业名称', 'PGFieldType':'Combo', 'PGComboProvider':SelectableCompany_HZ_Dict,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':False,'PGFieldRequiredValue':True}
GongShang_HZ_GuQuanBianGengXinXi_ShuJuYouXiaoXing={'DBColName':'ShuJuYouXiaoXing', 'refPOJOColName':'IAC_HZ_ChangeShareholdingInfo.datavalidity', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'本记录有效', 'PGFieldType':'combo', 'PGComboProvider':YesNoDict,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False , 'PGFieldDefaultValue':1171,}
GongShang_HZ_GuQuanBianGengXinXi_GuDongMingCheng={'DBColName':'GuDongMingCheng', 'refPOJOColName':'IAC_HZ_ChangeShareholdingInfo.shareholdername', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'股东名称', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuQuanBianGengXinXi_BianGengQianBiLi={'DBColName':'BianGengQianBiLi', 'refPOJOColName':'IAC_HZ_ChangeShareholdingInfo.changebefore', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'变更前比例', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuQuanBianGengXinXi_BianGengHouBiLi={'DBColName':'BianGengHouBiLi', 'refPOJOColName':'IAC_HZ_ChangeShareholdingInfo.changeafter', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'变更后比例', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuQuanBianGengXinXi_BianGengRiQi={'DBColName':'BianGengRiQi', 'refPOJOColName':'IAC_HZ_ChangeShareholdingInfo.changedate', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'变更日期', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuQuanBianGengXinXi_GongShiRiQi={'DBColName':'GongShiRiQi', 'refPOJOColName':'IAC_HZ_ChangeShareholdingInfo.publishdate', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'公示日期', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuQuanBianGengXinXi_DengJiRen={'DBColName':'DengJiRen', 'refPOJOColName':'IAC_HZ_ChangeShareholdingInfo.regperson', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'登记人', 'PGFieldType':'Combo', 'PGComboProvider':PersonDict_Employee_or_SystemUser,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':True,'PGFieldDefaultValue':__USER_ID__,}
GongShang_HZ_GuQuanBianGengXinXi_DengJiShiJian={'DBColName':'DengJiShiJian', 'refPOJOColName':'IAC_HZ_ChangeShareholdingInfo.regtime', 'DBColType':'Timestamp','PGFieldName':'', 'PGFieldLabel':'登记时间', 'PGFieldType':'datetime', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':True,'PGFieldDefaultValue':True}
GongShang_HZ_GuQuanBianGengXinXi = {
    'Name':'工商股权变更信息（海致）','ActionName':'工商股权变更信息（海致）',
    'POJOName':'IAC_HZ_ChangeShareholdingInfo',
    'POJOQuerySQL':'select obj from IAC_HZ_ChangeShareholdingInfo obj where obj.'+WaiBaoZhiXin_Query2_Part,
    'COListQueryCondition':'IAC_HZ_ChangeShareholdingInfo.'+WaiBaoZhiXin_Query2_Part+' order by IAC_HZ_ChangeShareholdingInfo.shareholdername desc',
    'COListAdditionalQueryCondition':'" and o.DengJiRen="+'+__USER_ID__,
    'ClassName':'GongShang_HZ_GuQuanBianGengXinXi',
    'DialogContentTitle': '工商股权变更信息（海致）',
    'QueryConditionList': [
        GongShang_HZ_GuQuanBianGengXinXi_OfCompany, GongShang_HZ_GuQuanBianGengXinXi_GuDongMingCheng,
        GongShang_HZ_GuQuanBianGengXinXi_BianGengRiQi,
    ],
    'TableColumnsList': [
        GongShang_HZ_GuQuanBianGengXinXi_OfCompany, GongShang_HZ_GuQuanBianGengXinXi_GuDongMingCheng,
        GongShang_HZ_GuQuanBianGengXinXi_BianGengQianBiLi, GongShang_HZ_GuQuanBianGengXinXi_BianGengHouBiLi,
        GongShang_HZ_GuQuanBianGengXinXi_BianGengRiQi, GongShang_HZ_GuQuanBianGengXinXi_GongShiRiQi,
        GongShang_HZ_GuQuanBianGengXinXi_DengJiRen, GongShang_HZ_GuQuanBianGengXinXi_DengJiShiJian,
    ],
    'ViewColumnsList': [
        GongShang_HZ_GuQuanBianGengXinXi_OfCompany, GongShang_HZ_GuQuanBianGengXinXi_ShuJuYouXiaoXing,GongShang_HZ_GuQuanBianGengXinXi_GuDongMingCheng,
        GongShang_HZ_GuQuanBianGengXinXi_BianGengQianBiLi, GongShang_HZ_GuQuanBianGengXinXi_BianGengHouBiLi,
        GongShang_HZ_GuQuanBianGengXinXi_BianGengRiQi, GongShang_HZ_GuQuanBianGengXinXi_GongShiRiQi,
        GongShang_HZ_GuQuanBianGengXinXi_DengJiRen, GongShang_HZ_GuQuanBianGengXinXi_DengJiShiJian,
    ],
    'EditColumnsList': [
        GongShang_HZ_GuQuanBianGengXinXi_OfCompany, GongShang_HZ_GuQuanBianGengXinXi_ShuJuYouXiaoXing,GongShang_HZ_GuQuanBianGengXinXi_GuDongMingCheng,
        GongShang_HZ_GuQuanBianGengXinXi_BianGengQianBiLi, GongShang_HZ_GuQuanBianGengXinXi_BianGengHouBiLi,
        GongShang_HZ_GuQuanBianGengXinXi_BianGengRiQi, GongShang_HZ_GuQuanBianGengXinXi_GongShiRiQi,
        GongShang_HZ_GuQuanBianGengXinXi_DengJiRen, GongShang_HZ_GuQuanBianGengXinXi_DengJiShiJian,
    ],
    'AllColumns': [
        GongShang_HZ_GuQuanBianGengXinXi_bold_id, GongShang_HZ_GuQuanBianGengXinXi_OfCompany,GongShang_HZ_GuQuanBianGengXinXi_ShuJuYouXiaoXing,
        GongShang_HZ_GuQuanBianGengXinXi_GuDongMingCheng, GongShang_HZ_GuQuanBianGengXinXi_BianGengQianBiLi,
        GongShang_HZ_GuQuanBianGengXinXi_BianGengHouBiLi, GongShang_HZ_GuQuanBianGengXinXi_BianGengRiQi,
        GongShang_HZ_GuQuanBianGengXinXi_GongShiRiQi, GongShang_HZ_GuQuanBianGengXinXi_DengJiRen,
        GongShang_HZ_GuQuanBianGengXinXi_DengJiShiJian,
    ],
    'DetailCO': [],
    'MasterCORefColumn':GongShang_HZ_GuQuanBianGengXinXi_bold_id,
    'MasterCOAttachments':[SelectableCompany_HZ_Attachment],'MasterCOAttachments_Reflect':[{'From':SelectableCompany_HZ_Attachment_MingCheng,'To':GongShang_HZ_GuQuanBianGengXinXi_OfCompany,'DealWay':'Replace'}],
    'BusiActions':[AddAction_Default,EditAction_Default],
    'Normal_methods':'''\
        public void computeOnAttachmentClickFinished(){
        }
        private Double recompute(){
            label_help.setText("");
            label_help.setToolTipText(label_help.getText());
            return 0d;
        }'''
    }


#========================================================================================================================================
GongShang_HZ_GuQuanBianGengXinXi_GuanLi = {
    'Name':'工商股权变更信息管理（海致）','ActionName':'工商股权变更信息管理（海致）',
    'POJOName':'IAC_HZ_ChangeShareholdingInfo',
    'POJOQuerySQL':'',
    'COListQueryCondition':' order by IAC_HZ_ChangeShareholdingInfo.shareholdername desc',
    'ClassName':'GongShang_HZ_GuQuanBianGengXinXi_GuanLi',
    'DialogContentTitle':'工商股权变更信息管理（海致）',
    'QueryConditionList' : [
        GongShang_HZ_GuQuanBianGengXinXi_OfCompany, GongShang_HZ_GuQuanBianGengXinXi_GuDongMingCheng,
        GongShang_HZ_GuQuanBianGengXinXi_BianGengRiQi, GongShang_HZ_GuQuanBianGengXinXi_DengJiRen,
    ],
    'TableColumnsList': [
        GongShang_HZ_GuQuanBianGengXinXi_OfCompany, GongShang_HZ_GuQuanBianGengXinXi_GuDongMingCheng,
        GongShang_HZ_GuQuanBianGengXinXi_BianGengQianBiLi, GongShang_HZ_GuQuanBianGengXinXi_BianGengHouBiLi,
        GongShang_HZ_GuQuanBianGengXinXi_BianGengRiQi, GongShang_HZ_GuQuanBianGengXinXi_GongShiRiQi,
        GongShang_HZ_GuQuanBianGengXinXi_DengJiRen, GongShang_HZ_GuQuanBianGengXinXi_DengJiShiJian,
    ],
    'ViewColumnsList': [
        GongShang_HZ_GuQuanBianGengXinXi_OfCompany, GongShang_HZ_GuQuanBianGengXinXi_ShuJuYouXiaoXing,GongShang_HZ_GuQuanBianGengXinXi_GuDongMingCheng,
        GongShang_HZ_GuQuanBianGengXinXi_BianGengQianBiLi, GongShang_HZ_GuQuanBianGengXinXi_BianGengHouBiLi,
        GongShang_HZ_GuQuanBianGengXinXi_BianGengRiQi, GongShang_HZ_GuQuanBianGengXinXi_GongShiRiQi,
        GongShang_HZ_GuQuanBianGengXinXi_DengJiRen, GongShang_HZ_GuQuanBianGengXinXi_DengJiShiJian,
    ],
    'EditColumnsList': [
        GongShang_HZ_GuQuanBianGengXinXi_OfCompany,GongShang_HZ_GuQuanBianGengXinXi_ShuJuYouXiaoXing, GongShang_HZ_GuQuanBianGengXinXi_GuDongMingCheng,
        GongShang_HZ_GuQuanBianGengXinXi_BianGengQianBiLi, GongShang_HZ_GuQuanBianGengXinXi_BianGengHouBiLi,
        GongShang_HZ_GuQuanBianGengXinXi_BianGengRiQi, GongShang_HZ_GuQuanBianGengXinXi_GongShiRiQi,
        GongShang_HZ_GuQuanBianGengXinXi_DengJiRen, GongShang_HZ_GuQuanBianGengXinXi_DengJiShiJian,
    ],
    'AllColumns': [
        GongShang_HZ_GuQuanBianGengXinXi_bold_id, GongShang_HZ_GuQuanBianGengXinXi_OfCompany,GongShang_HZ_GuQuanBianGengXinXi_ShuJuYouXiaoXing,
        GongShang_HZ_GuQuanBianGengXinXi_GuDongMingCheng, GongShang_HZ_GuQuanBianGengXinXi_BianGengQianBiLi,
        GongShang_HZ_GuQuanBianGengXinXi_BianGengHouBiLi, GongShang_HZ_GuQuanBianGengXinXi_BianGengRiQi,
        GongShang_HZ_GuQuanBianGengXinXi_GongShiRiQi, GongShang_HZ_GuQuanBianGengXinXi_DengJiRen,
        GongShang_HZ_GuQuanBianGengXinXi_DengJiShiJian,
    ],
    'DetailCO':[],
    'MasterCORefColumn':GongShang_HZ_GuQuanBianGengXinXi_bold_id,
    'MasterCOAttachments':[SelectableCompany_HZ_Attachment],'MasterCOAttachments_Reflect':[{'From':SelectableCompany_HZ_Attachment_MingCheng,'To':GongShang_HZ_GuQuanBianGengXinXi_OfCompany,'DealWay':'Replace'}],
    'BusiActions':[AddAction_Default,EditAction_Default],
    'Normal_methods':'''\
        public void computeOnAttachmentClickFinished(){
        }
        private Double recompute(){
            label_help.setText("");
            label_help.setToolTipText(label_help.getText());
            return 0d;
        }'''
    }

#========================================================================================================================================
GongShang_HZ_DongChanDiYanDengJiXinXi_bold_id={'DBColName':'bold_id','isIDCol':True, 'refPOJOColName':'IAC_HZ_ChattelMortgageInfo.bold_id', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'ID', 'PGFieldType':'Integer', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_DongChanDiYanDengJiXinXi_OfCompany={'DBColName':'OfCompany', 'refPOJOColName':'IAC_HZ_ChattelMortgageInfo.ofcompany', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'实际企业名称', 'PGFieldType':'Combo', 'PGComboProvider':SelectableCompany_HZ_Dict,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':False,'PGFieldRequiredValue':True}
GongShang_HZ_DongChanDiYanDengJiXinXi_ShuJuYouXiaoXing={'DBColName':'ShuJuYouXiaoXing', 'refPOJOColName':'IAC_HZ_ChattelMortgageInfo.datavalidity', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'本记录有效', 'PGFieldType':'combo', 'PGComboProvider':YesNoDict,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False , 'PGFieldDefaultValue':1171,}
GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiBianHao={'DBColName':'DengJiBianHao', 'refPOJOColName':'IAC_HZ_ChattelMortgageInfo.registerednumber', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'登记编号', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiRiQi={'DBColName':'DengJiRiQi', 'refPOJOColName':'IAC_HZ_ChattelMortgageInfo.registereddate', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'登记日期', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiJiGuan={'DBColName':'DengJiJiGuan', 'refPOJOColName':'IAC_HZ_ChattelMortgageInfo.registeredoffice', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'登记机关', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False }
GongShang_HZ_DongChanDiYanDengJiXinXi_ZhaiQuanShuE={'DBColName':'ZhaiQuanShuE', 'refPOJOColName':'IAC_HZ_ChattelMortgageInfo.creditamount', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'债权数额', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_DongChanDiYanDengJiXinXi_ZhuangTai={'DBColName':'ZhuangTai', 'refPOJOColName':'IAC_HZ_ChattelMortgageInfo.status', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'状态', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_DongChanDiYanDengJiXinXi_GongShiRiQi={'DBColName':'GongShiRiQi', 'refPOJOColName':'IAC_HZ_ChattelMortgageInfo.publishdate', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'公示日期', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiRen={'DBColName':'DengJiRen', 'refPOJOColName':'IAC_HZ_ChattelMortgageInfo.regperson', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'登记人', 'PGFieldType':'Combo', 'PGComboProvider':PersonDict_Employee_or_SystemUser,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':True,'PGFieldDefaultValue':__USER_ID__,}
GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiShiJian={'DBColName':'DengJiShiJian', 'refPOJOColName':'IAC_HZ_ChattelMortgageInfo.regtime', 'DBColType':'Timestamp','PGFieldName':'', 'PGFieldLabel':'登记时间', 'PGFieldType':'datetime', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':True,'PGFieldDefaultValue':True}
GongShang_HZ_DongChanDiYanDengJiXinXi = {
    'Name':'工商动产抵押登记信息（海致）','ActionName':'工商动产抵押登记信息（海致）',
    'POJOName':'IAC_HZ_ChattelMortgageInfo',
    'POJOQuerySQL':'select obj from IAC_HZ_ChattelMortgageInfo obj where obj.'+WaiBaoZhiXin_Query2_Part,
    'COListQueryCondition':'IAC_HZ_ChattelMortgageInfo.'+WaiBaoZhiXin_Query2_Part+' order by IAC_HZ_ChattelMortgageInfo.registerednumber desc',
    'COListAdditionalQueryCondition':'" and o.DengJiRen="+'+__USER_ID__,
    'ClassName':'GongShang_HZ_DongChanDiYanDengJiXinXi',
    'DialogContentTitle':'工商动产抵押登记信息（海致）',
    'QueryConditionList': [
        GongShang_HZ_DongChanDiYanDengJiXinXi_OfCompany, GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiBianHao,
        GongShang_HZ_DongChanDiYanDengJiXinXi_GongShiRiQi,
    ],
    'TableColumnsList': [
        GongShang_HZ_DongChanDiYanDengJiXinXi_OfCompany, GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiBianHao,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiRiQi,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiJiGuan, GongShang_HZ_DongChanDiYanDengJiXinXi_ZhaiQuanShuE,
        GongShang_HZ_DongChanDiYanDengJiXinXi_ZhuangTai,
        GongShang_HZ_DongChanDiYanDengJiXinXi_GongShiRiQi, GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiRen,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiShiJian,
    ],
    'ViewColumnsList': [
        GongShang_HZ_DongChanDiYanDengJiXinXi_OfCompany, GongShang_HZ_DongChanDiYanDengJiXinXi_ShuJuYouXiaoXing,GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiBianHao,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiRiQi,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiJiGuan, GongShang_HZ_DongChanDiYanDengJiXinXi_ZhaiQuanShuE,
        GongShang_HZ_DongChanDiYanDengJiXinXi_ZhuangTai,
        GongShang_HZ_DongChanDiYanDengJiXinXi_GongShiRiQi, GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiRen,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiShiJian,
    ],
    'EditColumnsList': [
        GongShang_HZ_DongChanDiYanDengJiXinXi_OfCompany, GongShang_HZ_DongChanDiYanDengJiXinXi_ShuJuYouXiaoXing,GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiBianHao,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiRiQi, GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiJiGuan,
        GongShang_HZ_DongChanDiYanDengJiXinXi_ZhaiQuanShuE, GongShang_HZ_DongChanDiYanDengJiXinXi_ZhuangTai,
        GongShang_HZ_DongChanDiYanDengJiXinXi_GongShiRiQi,GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiRen,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiShiJian,

    ],
    'AllColumns': [
        GongShang_HZ_DongChanDiYanDengJiXinXi_bold_id, GongShang_HZ_DongChanDiYanDengJiXinXi_OfCompany,GongShang_HZ_DongChanDiYanDengJiXinXi_ShuJuYouXiaoXing,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiBianHao, GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiRiQi,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiJiGuan, GongShang_HZ_DongChanDiYanDengJiXinXi_ZhaiQuanShuE,
        GongShang_HZ_DongChanDiYanDengJiXinXi_ZhuangTai, GongShang_HZ_DongChanDiYanDengJiXinXi_GongShiRiQi,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiRen, GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiShiJian,
    ],
    'DetailCO':[],
    'MasterCORefColumn':GongShang_HZ_DongChanDiYanDengJiXinXi_bold_id,
    'MasterCOAttachments':[SelectableCompany_HZ_Attachment],'MasterCOAttachments_Reflect':[{'From':SelectableCompany_HZ_Attachment_MingCheng,'To':GongShang_HZ_DongChanDiYanDengJiXinXi_OfCompany,'DealWay':'Replace'}],
    'BusiActions':[AddAction_Default,EditAction_Default],
    'Normal_methods':'''\
        public void computeOnAttachmentClickFinished(){
        }
        private Double recompute(){
            label_help.setText("");
            label_help.setToolTipText(label_help.getText());
            return 0d;
        }'''
    }


#========================================================================================================================================
GongShang_HZ_DongChanDiYanDengJiXinXi_GuanLi = {
    'Name':'工商动产抵押登记信息管理（海致）','ActionName':'工商动产抵押登记信息管理（海致）',
    'POJOName':'IAC_HZ_ChattelMortgageInfo',
    'POJOQuerySQL':'',
    'COListQueryCondition':' order by IAC_HZ_ChattelMortgageInfo.registerednumber desc',
    'ClassName':'GongShang_HZ_DongChanDiYanDengJiXinXi_GuanLi',
    'DialogContentTitle':'工商动产抵押登记信息管理（海致）',
    'QueryConditionList': [
        GongShang_HZ_DongChanDiYanDengJiXinXi_OfCompany, GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiBianHao,
        GongShang_HZ_DongChanDiYanDengJiXinXi_GongShiRiQi, GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiRen,
    ],
    'TableColumnsList': [
        GongShang_HZ_DongChanDiYanDengJiXinXi_OfCompany, GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiBianHao,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiRiQi,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiJiGuan, GongShang_HZ_DongChanDiYanDengJiXinXi_ZhaiQuanShuE,
        GongShang_HZ_DongChanDiYanDengJiXinXi_ZhuangTai,
        GongShang_HZ_DongChanDiYanDengJiXinXi_GongShiRiQi, GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiRen,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiShiJian,
    ],
    'ViewColumnsList': [
        GongShang_HZ_DongChanDiYanDengJiXinXi_OfCompany, GongShang_HZ_DongChanDiYanDengJiXinXi_ShuJuYouXiaoXing,GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiBianHao,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiRiQi,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiJiGuan, GongShang_HZ_DongChanDiYanDengJiXinXi_ZhaiQuanShuE,
        GongShang_HZ_DongChanDiYanDengJiXinXi_ZhuangTai,
        GongShang_HZ_DongChanDiYanDengJiXinXi_GongShiRiQi, GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiRen,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiShiJian,
    ],
    'EditColumnsList': [
        GongShang_HZ_DongChanDiYanDengJiXinXi_OfCompany, GongShang_HZ_DongChanDiYanDengJiXinXi_ShuJuYouXiaoXing,GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiBianHao,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiRiQi, GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiJiGuan,
        GongShang_HZ_DongChanDiYanDengJiXinXi_ZhaiQuanShuE, GongShang_HZ_DongChanDiYanDengJiXinXi_ZhuangTai,
        GongShang_HZ_DongChanDiYanDengJiXinXi_GongShiRiQi,GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiRen,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiShiJian,
    ],
    'AllColumns': [
        GongShang_HZ_DongChanDiYanDengJiXinXi_bold_id, GongShang_HZ_DongChanDiYanDengJiXinXi_OfCompany,GongShang_HZ_DongChanDiYanDengJiXinXi_ShuJuYouXiaoXing,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiBianHao, GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiRiQi,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiJiGuan, GongShang_HZ_DongChanDiYanDengJiXinXi_ZhaiQuanShuE,
        GongShang_HZ_DongChanDiYanDengJiXinXi_ZhuangTai, GongShang_HZ_DongChanDiYanDengJiXinXi_GongShiRiQi,
        GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiRen, GongShang_HZ_DongChanDiYanDengJiXinXi_DengJiShiJian,
    ],
    'DetailCO': [],
    'MasterCORefColumn':GongShang_HZ_DongChanDiYanDengJiXinXi_bold_id,
    'MasterCOAttachments':[SelectableCompany_HZ_Attachment],'MasterCOAttachments_Reflect':[{'From':SelectableCompany_HZ_Attachment_MingCheng,'To':GongShang_HZ_DongChanDiYanDengJiXinXi_OfCompany,'DealWay':'Replace'}],
    'BusiActions':[AddAction_Default,EditAction_Default],
    'Normal_methods':'''\
        public void computeOnAttachmentClickFinished(){
        }
        private Double recompute(){
            label_help.setText("");
            label_help.setToolTipText(label_help.getText());
            return 0d;
        }'''
    }

#========================================================================================================================================
GongShang_HZ_GuQuanChuZhiDengJiXinXi_bold_id={'DBColName':'bold_id','isIDCol':True, 'refPOJOColName':'IAC_HZ_EquityPledgedInfo.bold_id', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'ID', 'PGFieldType':'Integer', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuQuanChuZhiDengJiXinXi_OfCompany={'DBColName':'OfCompany', 'refPOJOColName':'IAC_HZ_EquityPledgedInfo.ofcompany', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'实际企业名称', 'PGFieldType':'Combo', 'PGComboProvider':SelectableCompany_HZ_Dict,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':False,'PGFieldRequiredValue':True}
GongShang_HZ_GuQuanChuZhiDengJiXinXi_ShuJuYouXiaoXing={'DBColName':'ShuJuYouXiaoXing', 'refPOJOColName':'IAC_HZ_EquityPledgedInfo.datavalidity', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'本记录有效', 'PGFieldType':'combo', 'PGComboProvider':YesNoDict,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False , 'PGFieldDefaultValue':1171,}
GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiBianHao={'DBColName':'DengJiBianHao', 'refPOJOColName':'IAC_HZ_EquityPledgedInfo.registerednumber', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'登记编号', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuQuanChuZhiDengJiXinXi_ChuZhiRen={'DBColName':'ChuZhiRen', 'refPOJOColName':'IAC_HZ_EquityPledgedInfo.mortgagor', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'出质人', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuQuanChuZhiDengJiXinXi_ChuZhiRenZhengJianHaoMa={'DBColName':'ChuZhiRenZhengJianHaoMa', 'refPOJOColName':'IAC_HZ_EquityPledgedInfo.mortgagornumber', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'出质人证件号码', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuQuanChuZhiDengJiXinXi_GuQuanShuE={'DBColName':'GuQuanShuE', 'refPOJOColName':'IAC_HZ_EquityPledgedInfo.pledgeamount', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'股权数额', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhiQuanRen={'DBColName':'ZhiQuanRen', 'refPOJOColName':'IAC_HZ_EquityPledgedInfo.pledgee', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'质权人', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhiQuanRenZhengJianHaoMa={'DBColName':'ZhiQuanRenZhengJianHaoMa', 'refPOJOColName':'IAC_HZ_EquityPledgedInfo.pledgenumber', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'质权人证件号码', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiRiQi={'DBColName':'DengJiRiQi', 'refPOJOColName':'IAC_HZ_EquityPledgedInfo.registereddate', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'登记日期', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhuangTai={'DBColName':'ZhuangTai', 'refPOJOColName':'IAC_HZ_EquityPledgedInfo.type', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'状态', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuQuanChuZhiDengJiXinXi_GongShiRiQi={'DBColName':'GongShiRiQi', 'refPOJOColName':'IAC_HZ_EquityPledgedInfo.publishdate', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'公示日期', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiRen={'DBColName':'DengJiRen', 'refPOJOColName':'IAC_HZ_EquityPledgedInfo.regperson', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'登记人', 'PGFieldType':'Combo', 'PGComboProvider':PersonDict_Employee_or_SystemUser,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':True,'PGFieldDefaultValue':__USER_ID__,}
GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiShiJian={'DBColName':'DengJiShiJian', 'refPOJOColName':'IAC_HZ_EquityPledgedInfo.regtime', 'DBColType':'Timestamp','PGFieldName':'', 'PGFieldLabel':'登记时间', 'PGFieldType':'datetime', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':True,'PGFieldDefaultValue':True}
GongShang_HZ_GuQuanChuZhiDengJiXinXi = {
    'Name':'工商股权出质登记信息（海致）','ActionName':'工商股权出质登记信息（海致）',
    'POJOName':'IAC_HZ_EquityPledgedInfo',
    'POJOQuerySQL':'select obj from IAC_HZ_EquityPledgedInfo obj where obj.'+WaiBaoZhiXin_Query2_Part,
    'COListQueryCondition':'IAC_HZ_EquityPledgedInfo.'+WaiBaoZhiXin_Query2_Part+' order by IAC_HZ_EquityPledgedInfo.registerednumber desc',
    'COListAdditionalQueryCondition':'" and o.DengJiRen="+'+__USER_ID__,
    'ClassName':'GongShang_HZ_GuQuanChuZhiDengJiXinXi',
    'DialogContentTitle': '工商股权出质登记信息（海致）',
    'QueryConditionList': [
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_OfCompany, GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiBianHao,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_ChuZhiRen, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhiQuanRen,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_GongShiRiQi,
    ],
    'TableColumnsList': [
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_OfCompany, GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiBianHao,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_ChuZhiRen, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ChuZhiRenZhengJianHaoMa,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_GuQuanShuE, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhiQuanRen,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhiQuanRenZhengJianHaoMa,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiRiQi, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhuangTai,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_GongShiRiQi,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiRen, GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiShiJian,
    ],
    'ViewColumnsList': [
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_OfCompany,GongShang_HZ_GuQuanChuZhiDengJiXinXi_ShuJuYouXiaoXing, GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiBianHao,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_ChuZhiRen, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ChuZhiRenZhengJianHaoMa,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_GuQuanShuE, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhiQuanRen,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhiQuanRenZhengJianHaoMa,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiRiQi, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhuangTai,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_GongShiRiQi,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiRen, GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiShiJian,
    ],
    'EditColumnsList': [
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_OfCompany, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ShuJuYouXiaoXing,GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiBianHao,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_ChuZhiRen, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ChuZhiRenZhengJianHaoMa,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_GuQuanShuE, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhiQuanRen,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhiQuanRenZhengJianHaoMa,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiRiQi, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhuangTai,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_GongShiRiQi,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiRen, GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiShiJian,
    ],
    'AllColumns': [
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_bold_id, GongShang_HZ_GuQuanChuZhiDengJiXinXi_OfCompany,GongShang_HZ_GuQuanChuZhiDengJiXinXi_ShuJuYouXiaoXing,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiBianHao, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ChuZhiRen,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_ChuZhiRenZhengJianHaoMa, GongShang_HZ_GuQuanChuZhiDengJiXinXi_GuQuanShuE,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhiQuanRen, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhiQuanRenZhengJianHaoMa,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiRiQi, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhuangTai,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_GongShiRiQi,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiRen, GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiShiJian,
    ],
    'DetailCO': [],
    'MasterCORefColumn':GongShang_HZ_GuQuanChuZhiDengJiXinXi_bold_id,
    'MasterCOAttachments':[SelectableCompany_HZ_Attachment],'MasterCOAttachments_Reflect':[{'From':SelectableCompany_HZ_Attachment_MingCheng,'To':GongShang_HZ_GuQuanChuZhiDengJiXinXi_OfCompany,'DealWay':'Replace'}],
    'BusiActions':[AddAction_Default,EditAction_Default],
    'Normal_methods':'''\
        public void computeOnAttachmentClickFinished(){
        }
        private Double recompute(){
            label_help.setText("");
            label_help.setToolTipText(label_help.getText());
            return 0d;
        }'''
    }


#========================================================================================================================================
GongShang_HZ_GuQuanChuZhiDengJiXinXi_GuanLi = {
    'Name':'工商股权出质登记信息管理（海致）','ActionName':'工商股权出质登记信息管理（海致）',
    'POJOName':'IAC_HZ_EquityPledgedInfo',
    'POJOQuerySQL':'',
    'COListQueryCondition':' order by IAC_HZ_EquityPledgedInfo.registerednumber desc',
    'ClassName':'GongShang_HZ_GuQuanChuZhiDengJiXinXi_GuanLi',
    'DialogContentTitle': '工商股权出质登记信息管理（海致）',
    'QueryConditionList': [
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_OfCompany, GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiBianHao,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_ChuZhiRen, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhiQuanRen,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_GongShiRiQi,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiRen,
    ],
    'TableColumnsList': [
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_OfCompany, GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiBianHao,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_ChuZhiRen, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ChuZhiRenZhengJianHaoMa,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_GuQuanShuE, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhiQuanRen,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhiQuanRenZhengJianHaoMa,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiRiQi, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhuangTai,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_GongShiRiQi,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiRen, GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiShiJian,
    ],
    'ViewColumnsList': [
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_OfCompany, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ShuJuYouXiaoXing,GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiBianHao,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_ChuZhiRen, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ChuZhiRenZhengJianHaoMa,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_GuQuanShuE, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhiQuanRen,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhiQuanRenZhengJianHaoMa,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiRiQi, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhuangTai,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_GongShiRiQi,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiRen, GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiShiJian,
    ],
    'EditColumnsList': [
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_OfCompany, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ShuJuYouXiaoXing,GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiBianHao,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_ChuZhiRen, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ChuZhiRenZhengJianHaoMa,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_GuQuanShuE, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhiQuanRen,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhiQuanRenZhengJianHaoMa,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiRiQi, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhuangTai,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_GongShiRiQi,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiRen, GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiShiJian,
    ],
    'AllColumns': [
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_bold_id, GongShang_HZ_GuQuanChuZhiDengJiXinXi_OfCompany,GongShang_HZ_GuQuanChuZhiDengJiXinXi_ShuJuYouXiaoXing,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiBianHao, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ChuZhiRen,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_ChuZhiRenZhengJianHaoMa, GongShang_HZ_GuQuanChuZhiDengJiXinXi_GuQuanShuE,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhiQuanRen, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhiQuanRenZhengJianHaoMa,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiRiQi, GongShang_HZ_GuQuanChuZhiDengJiXinXi_ZhuangTai,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_GongShiRiQi,
        GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiRen, GongShang_HZ_GuQuanChuZhiDengJiXinXi_DengJiShiJian,
    ],
    'DetailCO': [],
    'MasterCORefColumn':GongShang_HZ_GuQuanChuZhiDengJiXinXi_bold_id,
    'MasterCOAttachments':[SelectableCompany_HZ_Attachment],'MasterCOAttachments_Reflect':[{'From':SelectableCompany_HZ_Attachment_MingCheng,'To':GongShang_HZ_GuQuanChuZhiDengJiXinXi_OfCompany,'DealWay':'Replace'}],
    'BusiActions':[AddAction_Default,EditAction_Default],
    'Normal_methods':'''\
        public void computeOnAttachmentClickFinished(){
        }
        private Double recompute(){
            label_help.setText("");
            label_help.setToolTipText(label_help.getText());
            return 0d;
        }'''
    }


#========================================================================================================================================
GongShang_HZ_JingYingYiChangXinXi_bold_id={'DBColName':'bold_id','isIDCol':True, 'refPOJOColName':'IAC_HZ_AbnormalOperationInfo.bold_id', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'ID', 'PGFieldType':'Integer', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_JingYingYiChangXinXi_OfCompany={'DBColName':'OfCompany', 'refPOJOColName':'IAC_HZ_AbnormalOperationInfo.ofcompany', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'实际企业名称', 'PGFieldType':'Combo', 'PGComboProvider':SelectableCompany_HZ_Dict,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':False,'PGFieldRequiredValue':True}
GongShang_HZ_JingYingYiChangXinXi_ShuJuYouXiaoXing={'DBColName':'ShuJuYouXiaoXing', 'refPOJOColName':'IAC_HZ_AbnormalOperationInfo.datavalidity', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'本记录有效', 'PGFieldType':'combo', 'PGComboProvider':YesNoDict,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False , 'PGFieldDefaultValue':1171,}
GongShang_HZ_JingYingYiChangXinXi_LieRuRiQi={'DBColName':'LieRuRiQi', 'refPOJOColName':'IAC_HZ_AbnormalOperationInfo.enroldate', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'列入日期', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_JingYingYiChangXinXi_YiChuRiQi={'DBColName':'YiChuRiQi', 'refPOJOColName':'IAC_HZ_AbnormalOperationInfo.removedate', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'移出日期', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':2,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_JingYingYiChangXinXi_LieRuJueDingJiGuan={'DBColName':'LieRuJueDingJiGuan', 'refPOJOColName':'IAC_HZ_AbnormalOperationInfo.enroloffice', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'列入决定机关', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_JingYingYiChangXinXi_YiChuJueDingJiGuan={'DBColName':'YiChuJueDingJiGuan', 'refPOJOColName':'IAC_HZ_AbnormalOperationInfo.removeoffice', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'移出决定机关', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,}
GongShang_HZ_JingYingYiChangXinXi_LieRuYuanYin={'DBColName':'LieRuYuanYin', 'refPOJOColName':'IAC_HZ_AbnormalOperationInfo.enrolreason', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'列入原因', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':3,'PGFieldHidden':False ,}
GongShang_HZ_JingYingYiChangXinXi_YiChuYuanYin={'DBColName':'YiChuYuanYin', 'refPOJOColName':'IAC_HZ_AbnormalOperationInfo.removereason', 'DBColType':'String','PGFieldName':'', 'PGFieldLabel':'移出原因', 'PGFieldType':'String', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':3,'PGFieldHidden':False ,}
GongShang_HZ_JingYingYiChangXinXi_DengJiRen={'DBColName':'DengJiRen', 'refPOJOColName':'IAC_HZ_AbnormalOperationInfo.regperson', 'DBColType':'Integer','PGFieldName':'', 'PGFieldLabel':'登记人', 'PGFieldType':'Combo', 'PGComboProvider':PersonDict_Employee_or_SystemUser,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':True,'PGFieldDefaultValue':__USER_ID__,}
GongShang_HZ_JingYingYiChangXinXi_DengJiShiJian={'DBColName':'DengJiShiJian', 'refPOJOColName':'IAC_HZ_AbnormalOperationInfo.regtime', 'DBColType':'Timestamp','PGFieldName':'', 'PGFieldLabel':'登记时间', 'PGFieldType':'datetime', 'PGComboProvider':None,'PGFieldWidthFactor':1,'PGFieldHeightFactor':1,'PGFieldHidden':False ,'PGFieldReadOnly':True,'PGFieldDefaultValue':True}
GongShang_HZ_JingYingYiChangXinXi = {
    'Name':'工商经营异常信息（海致）','ActionName':'工商经营异常信息（海致）',
    'POJOName':'IAC_HZ_AbnormalOperationInfo',
    'POJOQuerySQL':'select obj from IAC_HZ_AbnormalOperationInfo obj where obj.'+WaiBaoZhiXin_Query2_Part,
    'COListQueryCondition':'IAC_HZ_AbnormalOperationInfo.'+WaiBaoZhiXin_Query2_Part+' order by IAC_HZ_AbnormalOperationInfo.bold_id desc',
    'COListAdditionalQueryCondition':'" and o.DengJiRen="+'+__USER_ID__,
    'ClassName':'GongShang_HZ_JingYingYiChangXinXi',
    'DialogContentTitle':'工商经营异常信息（海致）',
    'QueryConditionList' : [
        GongShang_HZ_JingYingYiChangXinXi_OfCompany, GongShang_HZ_JingYingYiChangXinXi_LieRuRiQi,
    ],
    'TableColumnsList': [
        GongShang_HZ_JingYingYiChangXinXi_OfCompany, GongShang_HZ_JingYingYiChangXinXi_LieRuRiQi,
        GongShang_HZ_JingYingYiChangXinXi_LieRuJueDingJiGuan, GongShang_HZ_JingYingYiChangXinXi_YiChuRiQi,
        GongShang_HZ_JingYingYiChangXinXi_YiChuJueDingJiGuan, GongShang_HZ_JingYingYiChangXinXi_LieRuYuanYin,
        GongShang_HZ_JingYingYiChangXinXi_YiChuYuanYin,
        GongShang_HZ_JingYingYiChangXinXi_DengJiRen, GongShang_HZ_JingYingYiChangXinXi_DengJiShiJian,
    ],
    'ViewColumnsList': [
        GongShang_HZ_JingYingYiChangXinXi_OfCompany, GongShang_HZ_JingYingYiChangXinXi_ShuJuYouXiaoXing,GongShang_HZ_JingYingYiChangXinXi_LieRuRiQi,
        GongShang_HZ_JingYingYiChangXinXi_LieRuJueDingJiGuan, GongShang_HZ_JingYingYiChangXinXi_YiChuRiQi,
        GongShang_HZ_JingYingYiChangXinXi_YiChuJueDingJiGuan, GongShang_HZ_JingYingYiChangXinXi_LieRuYuanYin,
        GongShang_HZ_JingYingYiChangXinXi_YiChuYuanYin,
        GongShang_HZ_JingYingYiChangXinXi_DengJiRen, GongShang_HZ_JingYingYiChangXinXi_DengJiShiJian,
    ],
    'EditColumnsList': [
        GongShang_HZ_JingYingYiChangXinXi_OfCompany, GongShang_HZ_JingYingYiChangXinXi_ShuJuYouXiaoXing,GongShang_HZ_JingYingYiChangXinXi_LieRuRiQi,
        GongShang_HZ_JingYingYiChangXinXi_LieRuJueDingJiGuan, GongShang_HZ_JingYingYiChangXinXi_YiChuRiQi,
        GongShang_HZ_JingYingYiChangXinXi_YiChuJueDingJiGuan, GongShang_HZ_JingYingYiChangXinXi_LieRuYuanYin,
        GongShang_HZ_JingYingYiChangXinXi_YiChuYuanYin,
        GongShang_HZ_JingYingYiChangXinXi_DengJiRen, GongShang_HZ_JingYingYiChangXinXi_DengJiShiJian,
    ],
    'AllColumns': [
        GongShang_HZ_JingYingYiChangXinXi_bold_id, GongShang_HZ_JingYingYiChangXinXi_OfCompany,GongShang_HZ_JingYingYiChangXinXi_ShuJuYouXiaoXing,
        GongShang_HZ_JingYingYiChangXinXi_LieRuRiQi, GongShang_HZ_JingYingYiChangXinXi_YiChuRiQi,
        GongShang_HZ_JingYingYiChangXinXi_LieRuJueDingJiGuan,
        GongShang_HZ_JingYingYiChangXinXi_YiChuJueDingJiGuan, GongShang_HZ_JingYingYiChangXinXi_LieRuYuanYin,
        GongShang_HZ_JingYingYiChangXinXi_YiChuYuanYin,
        GongShang_HZ_JingYingYiChangXinXi_DengJiRen, GongShang_HZ_JingYingYiChangXinXi_DengJiShiJian,
    ],
    'DetailCO':[],
    'MasterCORefColumn':GongShang_HZ_JingYingYiChangXinXi_bold_id,
    'MasterCOAttachments':[SelectableCompany_HZ_Attachment],'MasterCOAttachments_Reflect':[{'From':SelectableCompany_HZ_Attachment_MingCheng,'To':GongShang_HZ_JingYingYiChangXinXi_OfCompany,'DealWay':'Replace'}],
    'BusiActions':[AddAction_Default,EditAction_Default],
    'Normal_methods':'''\
        public void computeOnAttachmentClickFinished(){
        }
        private Double recompute(){
            label_help.setText("");
            label_help.setToolTipText(label_help.getText());
            return 0d;
        }'''
    }

#========================================================================================================================================
GongShang_HZ_JingYingYiChangXinXi_GuanLi = {
    'Name':'工商经营异常信息管理（海致）','ActionName':'工商经营异常信息管理（海致）',
    'POJOName':'IAC_HZ_AbnormalOperationInfo',
    'POJOQuerySQL':'',
    'COListQueryCondition':' order by IAC_HZ_AbnormalOperationInfo.bold_id desc',
    'ClassName':'GongShang_HZ_JingYingYiChangXinXi_GuanLi',
    'DialogContentTitle':'工商经营异常信息管理（海致）',
    'QueryConditionList' : [
        GongShang_HZ_JingYingYiChangXinXi_OfCompany, GongShang_HZ_JingYingYiChangXinXi_LieRuRiQi,
        GongShang_HZ_JingYingYiChangXinXi_DengJiRen,
    ],
    'TableColumnsList': [
        GongShang_HZ_JingYingYiChangXinXi_OfCompany, GongShang_HZ_JingYingYiChangXinXi_LieRuRiQi,
        GongShang_HZ_JingYingYiChangXinXi_LieRuJueDingJiGuan, GongShang_HZ_JingYingYiChangXinXi_YiChuRiQi,
        GongShang_HZ_JingYingYiChangXinXi_YiChuJueDingJiGuan, GongShang_HZ_JingYingYiChangXinXi_LieRuYuanYin,
        GongShang_HZ_JingYingYiChangXinXi_YiChuYuanYin,
        GongShang_HZ_JingYingYiChangXinXi_DengJiRen, GongShang_HZ_JingYingYiChangXinXi_DengJiShiJian,
    ],
    'ViewColumnsList': [
        GongShang_HZ_JingYingYiChangXinXi_OfCompany,GongShang_HZ_JingYingYiChangXinXi_ShuJuYouXiaoXing, GongShang_HZ_JingYingYiChangXinXi_LieRuRiQi,
        GongShang_HZ_JingYingYiChangXinXi_LieRuJueDingJiGuan, GongShang_HZ_JingYingYiChangXinXi_YiChuRiQi,
        GongShang_HZ_JingYingYiChangXinXi_YiChuJueDingJiGuan, GongShang_HZ_JingYingYiChangXinXi_LieRuYuanYin,
        GongShang_HZ_JingYingYiChangXinXi_YiChuYuanYin,
        GongShang_HZ_JingYingYiChangXinXi_DengJiRen, GongShang_HZ_JingYingYiChangXinXi_DengJiShiJian,
    ],
    'EditColumnsList': [
        GongShang_HZ_JingYingYiChangXinXi_OfCompany, GongShang_HZ_JingYingYiChangXinXi_ShuJuYouXiaoXing,GongShang_HZ_JingYingYiChangXinXi_LieRuRiQi,
        GongShang_HZ_JingYingYiChangXinXi_LieRuJueDingJiGuan, GongShang_HZ_JingYingYiChangXinXi_YiChuRiQi,
        GongShang_HZ_JingYingYiChangXinXi_YiChuJueDingJiGuan, GongShang_HZ_JingYingYiChangXinXi_LieRuYuanYin,
        GongShang_HZ_JingYingYiChangXinXi_YiChuYuanYin,
        GongShang_HZ_JingYingYiChangXinXi_DengJiRen, GongShang_HZ_JingYingYiChangXinXi_DengJiShiJian,
    ],
    'AllColumns': [
        GongShang_HZ_JingYingYiChangXinXi_bold_id, GongShang_HZ_JingYingYiChangXinXi_OfCompany,GongShang_HZ_JingYingYiChangXinXi_ShuJuYouXiaoXing,
        GongShang_HZ_JingYingYiChangXinXi_LieRuRiQi, GongShang_HZ_JingYingYiChangXinXi_YiChuRiQi,
        GongShang_HZ_JingYingYiChangXinXi_LieRuJueDingJiGuan,
        GongShang_HZ_JingYingYiChangXinXi_YiChuJueDingJiGuan, GongShang_HZ_JingYingYiChangXinXi_LieRuYuanYin,
        GongShang_HZ_JingYingYiChangXinXi_YiChuYuanYin,
        GongShang_HZ_JingYingYiChangXinXi_DengJiRen, GongShang_HZ_JingYingYiChangXinXi_DengJiShiJian,
    ],
    'DetailCO':[],
    'MasterCORefColumn':GongShang_HZ_JingYingYiChangXinXi_bold_id,
    'MasterCOAttachments':[SelectableCompany_HZ_Attachment],'MasterCOAttachments_Reflect':[{'From':SelectableCompany_HZ_Attachment_MingCheng,'To':GongShang_HZ_JingYingYiChangXinXi_OfCompany,'DealWay':'Replace'}],
    'BusiActions':[AddAction_Default,EditAction_Default],
    'Normal_methods':'''\
        public void computeOnAttachmentClickFinished(){
        }
        private Double recompute(){
            label_help.setText("");
            label_help.setToolTipText(label_help.getText());
            return 0d;
        }'''
    }
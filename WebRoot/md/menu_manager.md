# 菜单管理

单个应用时，菜单在配置在应用对应的数据库SPT\_MENU表中，如果多应用集中在应用支撑上，应用支撑为统一入口时，则把菜单复制到数据库ESF下的SPT\_MENU中；

**注意各应用之间的菜单不要冲突；**

|字段名称	|字段类型	|	备注|
| :- | :-------: |
|MENU_ID	|varchar(20) |	菜单编号 编号规则：####\_##\_##前面四位为Appcode，后面是各层级的编号，例如：0000\_01\_01|
|MENU_NAME|	varchar(100)|	菜单名称	0p|
|PARENT_ID|	varchar(20) |	父菜单编号	，如果为空，则为根菜单|
|LINK_PATH|	varchar(255)|	菜单对应的链接	|
|APP_CODE|	char(4)	|应用编号	SPT\_APP\_INFO中的主键，例如：0000|
|DISP_ORDER	|int	|排序号	在同一个父菜单下的排序号|
|ESCRIPTION|	varchar(255)	|描述	|
|MENU_IMAGE|	varchar(100)|	图片地址	菜单对应的图片地址|
|VALID|int|	有效性	1有效，0无效|
|AUTH_ID	|varchar(8)|	权限编号	菜单对应的权限编号,ESF..SPT_AUTH表的主键，例如：00000001|
|MODULE_ID|	char(3)|	模块编号	SPT\_MODULE的主键，例如：000|
|FUNC_ID	|char(8)	|功能编号	SPT\_FRONT\_FUN中的主键|

MENU\_ID编号规则：####\_##\_##

前面四位为Appcode，后面是各层级的编号

例如：

```[sql]
INSERT INTO SPT_MENU(MENU_ID, MENU_NAME, PARENT_ID, LINK_PATH, APP_CODE, DISP_ORDER, DESCRIPTION, MENU_IMAGE, VALID, AUTH_ID, MODULE_ID, FUNC_ID)
  VALUES('0000_01_02', '组织机构管理', NULL, 'esf/organ/organ_list.do', '0000', 2, NULL, NULL, 1, '00000007', '000', '00000201')
GO
INSERT INTO SPT_MENU(MENU_ID, MENU_NAME, PARENT_ID, LINK_PATH, APP_CODE, DISP_ORDER, DESCRIPTION, MENU_IMAGE, VALID, AUTH_ID, MODULE_ID, FUNC_ID)
  VALUES('0000_01_03', '用户管理', NULL, NULL, '0000', 3, NULL, NULL, 1, '00000015', '000', NULL)
GO
INSERT INTO SPT_MENU(MENU_ID, MENU_NAME, PARENT_ID, LINK_PATH, APP_CODE, DISP_ORDER, DESCRIPTION, MENU_IMAGE, VALID, AUTH_ID, MODULE_ID, FUNC_ID)
  VALUES('0000_01_04', '应用审计', NULL, NULL, '0000', 6, NULL, NULL, 1, '00000008', '000', NULL)
GO
INSERT INTO SPT_MENU(MENU_ID, MENU_NAME, PARENT_ID, LINK_PATH, APP_CODE, DISP_ORDER, DESCRIPTION, MENU_IMAGE, VALID, AUTH_ID, MODULE_ID, FUNC_ID)
  VALUES('0000_01_04_01', '审计事件管理', '0000_01_04', 'esf/appaudit/audit_event_list.do', '0000', 1, NULL, NULL, 1, '00000013', '000', '00000601')
GO
```

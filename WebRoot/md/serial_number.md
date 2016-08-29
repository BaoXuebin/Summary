# 序列号生成

序列号生成由两张表来完成，`SPT_SERIAL_NUMBER`和`SPT_SERIAL_NUMBER_ITEM`；

表：SPT\_SERIAL\_NUMBER

表：SPT_SERIAL\_NUMBER\_ITEM

框架提供的接口：ISerialNumberService

使用方法：

```[java]
//1、在Service（或Controller）中注入；建议在Service中注入，这样事务是统一的。
@Autowired
private ISerialNumberService serialNumberService;
//
//2、调用接口中的方法，获取流水号；
//获取流水号规则
SerialNumberQueryCondition condition = new SerialNumberQueryCondition();
condition.setName(AppInfoConstants.APP_INFO_SERIAL_NAME);
SerialNumber number = serialNumberService.getSerialNumberByName(condition);
if (number == null) {
	throw new EsfException(ErrorCode.DATA_BUSINESS_ERROR, MessageFormat.format("没有找到编号规则[{0}]！",
	AppInfoConstants.APP_INFO_SERIAL_NAME));
}
//
//根据规则来生成流水号
//第一个参数：SPT_SERIAL_NUMBER_ITEM表中的ITEM_CODE；
//第二个参数：获取流水号规则；
String appId = serialNumberService.makeSimpleSerialByBatch(AppInfoConstants.APP_INFO_SERIAL_ITEM_ID, number);
```
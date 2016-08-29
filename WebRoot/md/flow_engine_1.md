# 流程引擎接口（上）

### 功能说明

流程引擎是使用xml文件类型的文件实现流程驱动功能的模块，引擎提供接口实现流程的启动、运转、结束和查询功能。具体流程信息以xml文件形式保存在特定目录下；也可以数据库形式配置进模块中，流程引擎及相关数据表都可进行配置。

流程引擎仅提供获取待办事务、已办事务、流程驱动等功能，除此之外不提供任务与流程引擎无关的功能，流程图数据，在应用启动的时候，会解析后放入到内存中。

### 接口说明

#### IEsfFlowService接口

流程引擎包中的业务层接口对象为IEsfFLowService业务层实现类，其中封装了流程驱动的各种方法。主要方法如下所示：

```java
//取特定流程待办事务，全列表
List<FlActivityView> getMyWork(String flowIds,BigDecimal version, String userId, String deptId,String organId, List<String> permissionList);
//
//获取待办事务数量
int getMyWorkCount(String flowIds, String version, String userId, String deptId, String organId, String appendSql,List<String> permissionList);
//
//获取前N条待办事务
List<FlActivityView> getMyWorkWithTop(String flowIds,String version, String userId,String deptId,String organId,String appendSql,String orderSql,List<String> permissionList,int count);
//
//分页获取待办事务
QueryResult<FlActivityView> getMyWorkByPage(String flowIds, String version, String userId,String deptId, String organId, String appendSql,String orderSql,List<String> permissionList,int pageNo,int pageSize);
//
//新增流程开始
String startFlow(String instName,String flowId,BigDecimal version,String exValue, String userId,String userName,String deptId,String deptName,String organId,String organName);
//
//签收
void saveAcceptWork(String workId, String userId, String userName);
//
//撤回
void saveWithdraw(String userId, String workId);
//
//完成工作（提交流程）
FlActivityView saveCompleteWork(String flowUuid,String workId, String operationId, String opnn,String exValue, String opIds, String userId,String userName, String deptId, String deptName, String organId,	String organName);
//
//终止流程
void saveTerminateProcess(String flowUuid, String userId,String description);
//
//获取某个待办事务
FlActivityView getFlowWork(String workId);
//
//获取当前实例的待办事务
List<FlActivityView> getFlowInstCurrentWork(String flowUuid);
//
//获得单个流程实例的所有的操作步骤
List<FlActivity> getOpinionList(String flowUuid);
//
//获得所有可选操作结果
Map<String, String> getResultListByWorkId(DicFlowId id,String workId);
//
//分页获取用户的已办事务
QueryResult<FlActivityView> getCompletedWorkMergeByPage(String userId, String deptId, String flowId, Date startDate, Date endDate,int pageNo, int pageSize, String appendSql);	
/*
* ...
*/
```

#### IFlowDefineService接口

```java
//
//清除数据
void clearDataMap();
//
//获取流程信息列表
List<DicFlow> getFlowList(boolean isReload);
//
//根据流程ID，获取流程定义信息，如果对象不存在，则返回null
DicFlow getDicFlow(DicFlowId dicFlowID);
//
//根据流程定义ID，获取所有的环节定义信息
List<DicFlowActivity> getActivityList(DicFlowId dicFlowId);
//
//根据流程定义Id，获取其第一个开始活动节点
DicFlowActivity getStartActivity(DicFlowId dicFlowId);	
//
//根据活动（环节）Id，获取活动定义，如果对象不存在则返回null
DicFlowActivity getActivity(DicFlowId dicFlowId, String activityId);
//
//根据活动（环节）Id，获取活动相关的属性定义，如果对象不存在则返回null
List<DicFlowProperty> getProperty(DicFlowId dicFlowId, String activityId);
//
//根据活动（环节）Id，获取活动操作期限，如果对象不存在则返回null
List<DicFlowDays> getDays(DicFlowId dicFlowId, String activityId);
//
//根据活动（环节）Id，获取活动操作期限列表，如果对象不存在则返回null
List<DicFlowDays> getDaysList(DicFlowId dicFlowId);
//
//根据活动（环节）ID，获取操作列表
List<DicFlowOperation> getOperationList(DicFlowId dicFlowId, String activityId);
//
//根据操作Id，获取操作定义信息，如果对象不存在则返回null
DicFlowOperation getOperation(DicFlowId dicFlowId, String operationId);
//
//根据操作Id，获取后续活动（环节）列表，返回的后续活动列表要根据 SEQUENCE 进行升序排序	
List<DicFlowPost> getPostList(DicFlowId dicFlowId, String operationId);
//
//根据后续环节Id，获取后续环节定义
DicFlowPost getPost(DicFlowId dicFlowId, String postId);
//
//根据流程定义ID，获取流程变量定义
List<DicFlowParameter> getFlowParameter(DicFlowId dicFlowId);	
//
//根据流程Id，获取具有自动完成操作定义的活动定义集合
Set<String> getAutoActivities(DicFlowId dicFlowId);
//
// ...
```

#### DicFlowUtil

应用启动时，通过IFlowDefineService来读取流程图数据，并解析放入到内存中；提供DicFlowUtil工具类，可以获取到内存中所有与流程相关的信息。

工具类中包含的一些数据：

```java
// 全流程字典，流程复合id——流程bo
private Map<DicFlowId, DicFlow> dicFlowMap = new HashMap<DicFlowId, DicFlow>();
//
// 全动作字典，动作id——动作bo
private Map<String, DicFlowActivity> dicActMap = new HashMap<String, DicFlowActivity>();
//
// 获取流程开始环节
private Map<String, DicFlowActivity> startActMap = new HashMap<String, DicFlowActivity>();
//
// 全操作结果字典，操作结果id——操作结果bo
private Map<String, DicFlowOperation> dicOpMap = new HashMap<String, DicFlowOperation>();
//
// 动作对应结果字典，动作id——操作结果list
private Map<String, List<DicFlowOperation>> dicPostOpMap = new HashMap<String, List<DicFlowOperation>>();
```


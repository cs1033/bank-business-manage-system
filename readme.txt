采用C/S架构

执行mysql目录下的bank.sql文件，初始化数据库bank

安装好必要依赖之后，进入src目录执行
python main.py

弹出初始界面
输入mysql数据库运行的主机ip地址，一般为本地，即127.0.0.1；输入想要登录的数据库名称 :bank，用户名，用户密码，点击登录，即可完成数据库登录。

之后弹出用户登录界面
此次初始化，有2个支行，每个支行一个部门，每个部门2个员工。
四个员工的身份证和密码如下
id 			password		
1			1033
2			1033
362421199911232012	1033
362421199911232013	1033

登陆后进了主页面：
连接：logout用于登出， login无作用
上层：欢迎语
4个按钮对应四个功能

客户管理：
创建客户：身份证号为PK,必须填写，默认该客户的客户经理为操作的员工
删除客户：只能删除员工负责的客户，如果客户存在着关联账户或者贷款记录，则不允许删除； 
修改客户：只能修改员工负责的客户
查询客户：可以按（户主身份证，姓名，电话，客户经理身份证）查询。查询显示，客户的基本信息、以及账户和贷款信息。采用模糊搜索，REGEXP。


账户管理
开户：只能为自己负责的客户开户，开户需填写每个属性。账户的初始余额相当于存钱，会增加支行的资产。
	账户号：自己填写,数字串（自动生成账户号，需等系统升级） 	账户类型：1（储蓄账户）2（支票账户） 	开户日期：（YYYY-MM-DD）  
	货币类型：1（人民币） （暂时只接受人民币，其它货币请待系统升级）0（支票账户）
	余额、利率、透支额：float型 	（储蓄账户透支额为0）
销户：只能为自己负责的客户销户。 销毁会清空余额和透支额，同时改变支行资产。	       
修改账户：只能为自己负责的客户修改。不能修改账户类型和账户号。 可以修改账户的持有者：添加或取消。 修改账户余额会影响支行的资产
查询：可以按（户主身份证，账户号）查询。查询显示，账户的基本信息、账户持有者的部分信息。采用模糊搜索，REGEXP。

贷款管理
增加贷款：可以为所有客户发放贷款
	自己填写,数字串（自动生成账户号，需等系统升级） 贷款金额：正整数 （若超过支行资金的一半则不能发放）
删除贷款：不能删除发放中的贷款
支付贷款：输入贷款号，填写支付金额。会自动生成付款号，和其它付款信息。付款金额出错，超出额度，会有提示
搜索：可以按（户主身份证，贷款号）查询。查询显示，贷款的基本信息、贷款申请者的部分信息、贷款支付的信息。采用模糊搜索，REGEXP。


业务统计：
可以统计（本月、本季度、本年）各个支行的储蓄、贷款业务 同时统计各个支行当前的总用户数。以柱状图和表格形式显示。




Dirs
 觉得有用的话，麻烦给个Star
 ====
1. python-unittest-requests文件夹：整体框架的构建
2. case_excel文件夹：包含对excel的操作
3. common文件夹：包含了和业务相关的包含可复用方法的脚本文件
4. config文件夹：包含配置文件的读取和配置
5. data文件夹：包含了测试用的数据
6. interface文件夹：包含接口测试的一些方法
7. interface_data文件夹：
8. report文件夹：包含报告和结果
		css文件夹：用来生成相应的html相应脚本文件
		js文件夹：用来生成相应的html相应脚本文件
		Log文件夹：包含了运行测试过程中生成的日志文件
		Runner文件夹：用来输出测试报告的脚本文件
		test_excelreport文件夹：用来保存自动生成的测试结果文件
		test_report文件夹：用来保存自动生成html文件
9. test_case文件夹：unittest套件的生成


Files
===
1. python-unittest-requests文件夹下：
    	__init__.py文件：初始化文件
    	ReadMe.md文件:框架说明文件
    	Test_Suite.py文件：程序在此处运行，包含unittest测试用例的运行，报告的生成，邮件的发送等

2. case_excel文件夹：
		__init__.py文件：初始化文件
		copy_excel.py文件:对excel文件的复制和写入
		read_excel.py文件:对excel文件的读取
3. common文件夹：
		__init__.py文件：初始化文件
		log.py文件：用于日志的输入
		my_test.py文件：unittest框架初始化
		read_config.py文件：配置文件的读取
		sendmail.py文件：用来发送邮件
		mysql_read.py文件：用来读取mysql
4. config文件夹：
		__init__.py文件：初始化文件
		config.ini文件：配置项目路径
		globalparam.py文件：全局配置文件
5. data文件夹：
		__init__.py文件：初始化文件
		TestCase.xlsx文件:接口模板文件
6. interface文件夹：
		__init__.py文件：初始化文件
		interface_method.py文件：接口方法文件（无效)
		interface_senddata.py文件：对excel组装、写入
7. test_case文件夹：
		test_test.py文件:利用ddt数据驱动对复用单个用例
8. test文件夹:


仍存在bug
===

此程序有个bug log打印会重复打印
解决方法:log.py  # 这两行代码是为了避免日志输出重复问题
        # self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
不知道为什么打印到HTML报告中，确控制台不打印了，我也是服了，这里记录下来

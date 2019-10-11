# get_course_list
获取uestc的课表，生成.ics文件，然后可以导入google日历，不用再整天盯着个截图看来看去





使用到的东西:

selenium

geckodriver

Firefox

python3.7



目前进度:20%

已完成:

* 可以获取到js渲染以后的源码了



需求：

* 等待页面加载完成的判断（包括js渲染页面完成

* 重复登陆 用户踢出 那个页面的跳转

* 把爬到的数据写成.ics的函数

* 做成web程序(要搞🐎?)   这个要在服务端部署，webdriver还得在整一下，那个登陆的时候的验证码略微有点顶

* 一键pip install，写依赖

* 密码/验证码输错重新输入

  
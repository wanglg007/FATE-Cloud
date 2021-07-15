# Fate-manager


## 1  部署指引
	

1. 本部分分为三个组件,可根据需要自行选择：mysql，fate-manager, python。
    
    由于Python涉及到版本问题，建议用户选择部署Python
    
    获取文件后，使用命令解压文件：
    tar -xzvf 【filename】
        

2. 设置部署配置相关参数：
    ```
    cd filename
    vim  common-deploy/conf/setup.conf
   ```

    参数说明：
    ```
   pbase  【设置：选择部署Python和mysql的安装根目录位置】
        pname  【设置：安装文件夹名】
        lbase  【设置：日志文件路径】
        
        mysql_path   【设置：mysql的安装子目录】
        mysql_admin_user   【设置：登入mysql用户名】
        mysql_admin_pass   【设置：登入mysql用密码】
        mysql_port   【设置：mysql运行端口】
        fate_manager_dbname   【设置：创建库名】
        mysql_ip   【设置：数据库的运行ip，默认：127.0.0.1】
        
        
        pyenv   【设置：Python的运行环境】
        
        http_port   【设置：fmate-manager运行端口】
        host   【设置：fmate-manager运行ip，默认：0.0.0.0（本机）】
        
        pro_base   【设置：fmate-manager部署地址】
        pro_name   【设置：fmate-manager项目名称】
   ```
        
        

3. 关于mysql：
    sh common-deploy/common-deploy.sh mysql
    部署，需要填写如下配置：
        pbase  【设置：选择部署Python和mysql的安装根目录位置】
        pname  【设置：安装文件夹名】
        lbase  【设置：日志文件路径】
        
        mysql_path   【设置：mysql的安装子目录】
        mysql_admin_user   【设置：登入mysql用户名】
        mysql_admin_pass   【设置：登入mysql用密码】
        mysql_port   【设置：mysql运行端口】
        fate_manager_dbname   【设置：创建库名】
        mysql_ip   【设置：数据库的运行ip，默认：127.0.0.1】
        
        
4. 关于Python：
    sh common-deploy/common-deploy.sh python
    部署，需要填写如下配置：
        pbase  【设置：选择部署Python和mysql的安装根目录位置】
        pname  【设置：安装文件夹名】
        lbase  【设置：日志文件路径】
        pyenv   【设置：Python的运行环境】


5. 关于fm：
    sh common-deploy/common-deploy.sh fm
    fm部署报错相关信息可 cd {pro_base}/{pro_name}/logs 目录下查看
    部署，需要填写如下配置：
       
        pro_base   【设置：fmate-manager部署地址】
        pro_name   【设置：fmate-manager项目名称】
     
    如用户本机已经有fate-manager在运行，用户重新安装前，停止此服务进程，再重新部署fm 
        ps -ef|grep fate_manager_server.py，
       
6. 关于用户选择不部署：Python，mysql情况，用户需要提供本机已安装软件的如下相关配置参数：
    关于Python：(支持3.6以上版本)
         pyenv   【设置：Python的运行环境】
         涉及到的Python第三方依赖，用户可以查看文件夹：python-deploy/files/requirements.txt,选择进行安装
         
    关于mysql：（注：用户需要在自己的mysql上创建一个库名，必须要与如下参数fate_manager_dbname保持一致，否则会连接不上数据库名，创建相关表失败）
        mysql_admin_user   【设置：登入mysql用户名】
        mysql_admin_pass   【设置：登入mysql用密码】
        mysql_port   【设置：mysql运行端口】
        fate_manager_dbname   【设置：创建库名】
        mysql_ip   【设置：数据库的运行ip】
        
        mysql_path   【填写绝对路劲 eg:/data/projects/common/mysql】 
        
        
    
7. 执行完步骤5，可访问路由：http:/ip:port/index/

    注：python|mysql|fate-manager为用户部署可选参数,单独执行：sh common-deploy.sh 默认为全部部署 
    
    重启fate-manager，用户可以 cd {pro_base}/{pro_name}/fate_manager 目录下,
        支持fate-manager的重启，状态查询，停止，重启功能
        执行：sh service.sh start|stop|restart|status
        


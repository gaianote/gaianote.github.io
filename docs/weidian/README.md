# Headline

## 常用地址

* [zookeeper](http://admin.dubbo.daily.vdian.net/) vdian dubbo接口管理平台
* [vguard](http://vguard.vdian.net/) 微店服务治理 [接入指南](http://vguard.daily.vdian.net/middleware/vguard-doc/docs/AppJoin/JoinSteps.html)
* [dbplus]
* [订单查询](http://order-admin.vdian.net/orderDetailQuery?orderId=815470740378607)
[电销管理系统](https://d.daily.weidian.com/tel-crm/#/)
[大数据ES管理平台](http://d.vdian.net/esms/index.html#/resource-management/index-resource) 
线上日志集群 h5_spider_online
## 我的仓库

dubbo 服务 集成到了flask

http://10.37.52.53:5000/api/dubbo/invoke?param={{param}}


## 常用sql

查询小程序是否包含咪淘导播插件 

```sql
select DISTINCT app_id from wxapp_audit_config where in_use = 1 and template_id >416 and template_id != 420 and config like "%wdlive-plugin%"  limit 100;
```


## 重要文档

* 线上ES集群 http://docs.vdian.net/pages/viewpage.action?pageId=65092919


h5埋点上报 http://log-kibana.vdian.net/  kibana zijie
 
李云鹏 2020-3-19 下午 2:35

curl -XGET "http://10.32.144.131:9200/_sql?sql=select * from h5_spider_online-* where seller_id = 320474174 and spma = "seller_pc" and spmb = "offorders-search" limit 0,1"
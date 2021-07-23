# Headline

## 常用地址

* [zookeeper](http://admin.dubbo.daily.vdian.net/) vdian dubbo接口管理平台
* [vguard](http://vguard.vdian.net/) 微店服务治理 [接入指南](http://vguard.daily.vdian.net/middleware/vguard-doc/docs/AppJoin/JoinSteps.html)
* [dbplus]


## 我的仓库


## 常用sql

查询小程序是否包含咪淘导播插件 

```sql
select DISTINCT app_id from wxapp_audit_config where in_use = 1 and template_id >416 and template_id != 420 and config like "%wdlive-plugin%"  limit 100;
```
# cps



## cps 链路排查

下单时的买家 ID,卖家 ID 是多少
下单时是否有 CPS 标
下单时商家设置的佣金是多少
下单时买家与商家是否存在 gds 关系,推手是谁
前端访问的日志埋点上报记录

有佣金 815242997233746

- 订单分析 ams有佣金 https://order-admin.vdian.net/orderDetailQuery?orderId=815472831756370


1. 查询得到 卖家 id 买家 id

http://order-admin.vdian.net/orderDetailQuery?orderId=815470740378607

```
"extend": ",,,,,,,,,,,,,,,,,,,1yl_c_createid:25313810109423;1ns_c_cuid:cfe825ed732833ed;1ys_c_external_channel:ams;source:QUICK_BUY;plat:android;1ys_c_external_biz_no:am_Eg9fdjRJMGJKa1J3NGo0RWQgAQ;,,,,,,,,,,",
```

2. 查询 cps 访问关系 ep-damo 库,最近的访问关系都会被记录

https://dbmax.vdian.net/#/mysql/1289/prod

```sql
select * from share_relation where buyer_id = "1293410865" and shop_id = "1736580162" limit 100;
```
3. 查询 cps 佣金配置 wd_ad_cps 库,rate_market_cps_config 表

`status` tinyint(4) NOT NULL DEFAULT '-1' COMMENT '推广状态 0 关闭 1 开启',

```sql
SELECT * FROM rate_market_cps_config WHERE seller_id in (1869696000,1749273600) LIMIT 10
```

4. 从大数据管理平台查询前端日志上报信息

http://d.vdian.net/esms/index.html#/resource-management

```sql
select spma,spmb,document_ref,user_agnet_client_name,report_time from h5_spider_online* where buyer_id = "1293410865"  limit 100
```

5. 查询是否是免费推手 

https://dbmax.vdian.net/#/mysql/687/prod

```sql
select * from free_share_record  where seller_id = "1736580162" and user_id = "" limit 100;
```

## 服务部署

- 预发服务 10.32.25.199 
- 文件夹 /home/www/qa-kiwi-pyserver
- 开放端口 9090
- 请求示例 http://10.32.25.199:9090/api/cps/get?order_id=815242997233746

## cps 常用链接

- 商家 CPS 配置入口 https://wd.pre.weidian.com/new-cps/#/
- CPS 中心化阵地 https://h5.pre.weidian.com/m/new-ad-cps/#/
- CPS 微店联盟 https://h5.pre.weidian.com/m/pc-vue-promote/#/itemMarket
- CPS 我的推广 https://h5.pre.weidian.com/m/rewarded/index.html?spider_token=4f06#/detail
- CPS 运营后台 http://b.pre.vdian.net/m/pc-union/item-market.html
- 渠道授权页 https://h5.pre.weidian.com/m/shop-channel-auth/auth.html?gtl=1
- 商家 pc 设置页 https://d.pre.weidian.com/weidian-pc/pc-divided-set/#/

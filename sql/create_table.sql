
# 接口信息表 v0.1
CREATE TABLE sis_interface (
  Id bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'Id',
  ServiceUrl VARCHAR(1000) default '' not null COMMENT '请求Url',
  Environment varchar(32) default '' not null COMMENT '待测环境',
	Method varchar(32) default '' not null COMMENT '请求方法',
  Parameters varchar(2000) default '' not null COMMENT '请求参数',
  Comment varchar(2000) default '' not null COMMENT '备注',
  CreateAt datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  LastEditAt datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后编辑时间',
  PRIMARY KEY (Id)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COMMENT='接口信息表';
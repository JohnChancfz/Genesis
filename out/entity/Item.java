package com.cfz.admin.entity;

import java.io.Serializable;
import javax.persistence.*;

    /**
      *
      * @author Genesis
      * https://github.com/JohnChancfz/Genesis
      *
      */
    
@Entity
@Table(name = "genesis_item")
public class Item implements Serializable{

	// ID
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	@Column(name = "id", nullable = false)
	private Integer id;

	public Integer getId() {return id;}

	public void setId(Integer id) {this.id = id;}

	// 分类id
	private Integer cid;

	public Integer getCid() {return cid;}

	public void setCid(Integer cid) {this.cid = cid;}

	// 名称
	private String name;

	public String getName() {return name;}

	public void setName(String name) {this.name = name;}

	// 描述
	private String description;

	public String getDescription() {return description;}

	public void setDescription(String description) {this.description = description;}

	// 封面图
	private String coverImg;

	public String getCoverImg() {return coverImg;}

	public void setCoverImg(String coverImg) {this.coverImg = coverImg;}

	// 内容
	private String content;

	public String getContent() {return content;}

	public void setContent(String content) {this.content = content;}

	// 标的估值
	private Double raisingMoney;

	public Double getRaisingMoney() {return raisingMoney;}

	public void setRaisingMoney(Double raisingMoney) {this.raisingMoney = raisingMoney;}

	// 投资期限(年)
	private Integer investmentCycle;

	public Integer getInvestmentCycle() {return investmentCycle;}

	public void setInvestmentCycle(Integer investmentCycle) {this.investmentCycle = investmentCycle;}

	// 项目地域
	private String region;

	public String getRegion() {return region;}

	public void setRegion(String region) {this.region = region;}

	// 创建时间annotation
	private Date createTime;

	public Date getCreateTime() {return createTime;}

	public void setCreateTime(Date createTime) {this.createTime = createTime;}
}

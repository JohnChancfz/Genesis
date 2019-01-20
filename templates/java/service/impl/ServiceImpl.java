package @{package_name}.service.impl;

import @{package_name}.dao.@{Name}Dao;
import @{package_name}.dao.support.IBaseDao;
import @{package_name}.entity.@{Name}Entity;
import @{package_name}.service.@{Name}Service;
import @{package_name}.service.support.impl.BaseServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class @{Name}ServiceImpl extends BaseServiceImpl<@{Name}Entity, Integer> implements @{Name}Service {

	@Autowired
	private @{Name}Dao @{name}Dao;

	@Override
	public IBaseDao<@{Name}Entity, Integer> getBaseDao() {
		return this.@{name}Dao;
	}


    @Override
	public void saveOrUpdate(@{Name} @{name}) {
		if(@{name}.getId() != null){
			@{Name} db = find(@{name}.getId());
			db.setUpdateTime(new Date());
			update(db);
		}else{
			role.setCreateTime(new Date());
			role.setUpdateTime(new Date());
			save(role);
		}
	}

}

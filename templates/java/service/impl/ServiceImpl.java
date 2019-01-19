package --package_name--.service.impl;

import --package_name--.dao.--name--Dao;
import --package_name--.dao.support.IBaseDao;
import --package_name--.entity.--name--Entity;
import --package_name--.service.--name--Service;
import --package_name--.service.support.impl.BaseServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class --name--ServiceImpl extends BaseServiceImpl<--name--Entity, Integer> implements --name--Service {

	@Autowired
	private --name--Dao --lower_name--Dao;

	@Override
	public IBaseDao<--name--Entity, Integer> getBaseDao() {
		return this.--lower_name--Dao;
	}


    @Override
	public void saveOrUpdate(--name-- --lower_name--) {
		if(--lower_name--.getId() != null){
			--name-- db = find(--lower_name--.getId());
			db.setUpdateTime(new Date());
			update(db);
		}else{
			role.setCreateTime(new Date());
			role.setUpdateTime(new Date());
			save(role);
		}
	}

}

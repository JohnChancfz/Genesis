package @{package_name}.service;

import @{package_name}.entity.@{Name}Entity;
import @{package_name}.service.support.IBaseService;


public interface @{Name}Service extends IBaseService<@{Name}Entity,Integer> {

    void saveOrUpdate(@{Name} @{name});

}

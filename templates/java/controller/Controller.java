package @{package_name}.controller;

import com.doudou.common.common.JsonResult;
import com.doudou.core.controller.BaseController;
import @{package_name}.service.@{Name}Service;
import com.doudou.core.service.specification.SimpleSpecificationBuilder;
import @{package_name}.entity.@{Name}Entity;
import com.doudou.core.service.specification.SpecificationOperator.Operator;

import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
@RequestMapping("/admin/@{name}")
public class @{Name}Controller extends BaseController {

	@Autowired
	private @{Name}Service @{name}Service;


	@RequestMapping(value = { "/", "/index" })
	public String index() {
		return "admin/@{name}/index";
	}

	@RequestMapping(value = { "/list" })
	@ResponseBody
	public Page<@{Name}Entity> list() {
		SimpleSpecificationBuilder<@{Name}Entity> builder = new SimpleSpecificationBuilder<@{Name}Entity>();
		String searchText = request.getParameter("searchText");
		if(StringUtils.isNotBlank(searchText)){
			builder.add("name", Operator.likeAll.name(), searchText);
			builder.addOr("description", Operator.likeAll.name(), searchText);
		}
		Page<@{Name}Entity> page = @{Name}Service.findAll(builder.generateSpecification(), getPageRequest());
		return page;
	}

	@RequestMapping(value = "/add", method = RequestMethod.GET)
	public String add(ModelMap map) {
		return "admin/@{name}/form";
	}


	@RequestMapping(value = "/edit/{id}", method = RequestMethod.GET)
	public String edit(@PathVariable Integer id,ModelMap map) {
		@{Name}Entity @{name} = @{Name}Service.find(id);
		map.put("@{name}", @{name});
		return "admin/@{name}/form";
	}


	@RequestMapping(value= {"/edit"},method = RequestMethod.POST)
	@ResponseBody
	public JsonResult edit(@{Name}Entity @{name}, ModelMap map){
		try {
			@{name}Service.saveOrUpdate(@{name});
		} catch (Exception e) {
			return JsonResult.failure(e.getMessage());
		}
		return JsonResult.success();
	}

	@RequestMapping(value = "/delete/{id}", method = RequestMethod.POST)
	@ResponseBody
	public JsonResult delete(@PathVariable Integer id,ModelMap map) {
		try {
			@{name}Service.delete(id);
		} catch (Exception e) {
			e.printStackTrace();
			return JsonResult.failure(e.getMessage());
		}
		return JsonResult.success();
	}

}

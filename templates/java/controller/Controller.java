package --package_name--.controller;

import com.doudou.common.common.JsonResult;
import com.doudou.core.controller.BaseController;
import --package_name--.service.--name--Service;
import com.doudou.core.service.specification.SimpleSpecificationBuilder;
import --package_name--.entity.--name--Entity;
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
@RequestMapping("/admin/--lower_name--")
public class --name--Controller extends BaseController {

	@Autowired
	private --name--Service --lower_name--Service;


	@RequestMapping(value = { "/", "/index" })
	public String index() {
		return "admin/--lower_name--/index";
	}

	@RequestMapping(value = { "/list" })
	@ResponseBody
	public Page<--name--Entity> list() {
		SimpleSpecificationBuilder<--name--Entity> builder = new SimpleSpecificationBuilder<--name--Entity>();
		String searchText = request.getParameter("searchText");
		if(StringUtils.isNotBlank(searchText)){
			builder.add("name", Operator.likeAll.name(), searchText);
			builder.addOr("description", Operator.likeAll.name(), searchText);
		}
		Page<--name--Entity> page = --name--Service.findAll(builder.generateSpecification(), getPageRequest());
		return page;
	}

	@RequestMapping(value = "/add", method = RequestMethod.GET)
	public String add(ModelMap map) {
		return "admin/--lower_name--/form";
	}


	@RequestMapping(value = "/edit/{id}", method = RequestMethod.GET)
	public String edit(@PathVariable Integer id,ModelMap map) {
		--name--Entity --lower_name-- = --name--Service.find(id);
		map.put("--lower_name--", --lower_name--);
		return "admin/--lower_name--/form";
	}


	@RequestMapping(value= {"/edit"},method = RequestMethod.POST)
	@ResponseBody
	public JsonResult edit(--name--Entity --lower_name--, ModelMap map){
		try {
			--lower_name--Service.saveOrUpdate(--lower_name--);
		} catch (Exception e) {
			return JsonResult.failure(e.getMessage());
		}
		return JsonResult.success();
	}

	@RequestMapping(value = "/delete/{id}", method = RequestMethod.POST)
	@ResponseBody
	public JsonResult delete(@PathVariable Integer id,ModelMap map) {
		try {
			--lower_name--Service.delete(id);
		} catch (Exception e) {
			e.printStackTrace();
			return JsonResult.failure(e.getMessage());
		}
		return JsonResult.success();
	}

}

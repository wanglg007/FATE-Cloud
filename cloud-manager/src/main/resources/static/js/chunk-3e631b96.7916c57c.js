(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-3e631b96"],{1644:function(t,a,e){},"1b96":function(t,a,e){"use strict";e.r(a);var o=function(){var t=this,a=t.$createElement,o=t._self._c||a;return o("div",{staticClass:"access-box"},[o("div",{staticClass:"system-header"},[o("el-radio-group",{staticClass:"radio",model:{value:t.radio,callback:function(a){t.radio=a},expression:"radio"}},[o("el-radio-button",{attrs:{label:"Cloud Manager"}},[t._v(t._s(t.$t("Cloud Manager")))]),o("el-radio-button",{attrs:{label:"FATE Manager"}},[t._v(t._s(t.$t("FATE Manager")))])],1)],1),o("div",{staticClass:"row-add"},[o("div",{staticClass:"btn-add"},[o("el-button",{staticClass:"access-add",attrs:{type:"text"},on:{click:t.toAdd}},[o("img",{attrs:{src:e("2fe8")}}),o("span",[t._v(t._s(t.$t("add")))])]),o("el-button",{staticClass:"go",attrs:{type:"primary"},on:{click:t.toSearch}},[t._v(t._s(t.$t("m.common.go")))]),"Cloud Manager"===t.radio?o("el-input",{staticClass:"input",attrs:{clearable:"",placeholder:t.$t("Search for Name")},model:{value:t.data.name,callback:function(a){t.$set(t.data,"name","string"===typeof a?a.trim():a)},expression:"data.name"}},[o("i",{staticClass:"el-icon-search search",attrs:{slot:"prefix"},on:{click:t.toSearch},slot:"prefix"})]):o("el-input",{staticClass:"input",attrs:{clearable:"",placeholder:t.$t("Search for Institution")},model:{value:t.data.institutions,callback:function(a){t.$set(t.data,"institutions","string"===typeof a?a.trim():a)},expression:"data.institutions"}},[o("i",{staticClass:"el-icon-search search",attrs:{slot:"prefix"},slot:"prefix"})])],1)]),o("div",{staticClass:"system-body"},["Cloud Manager"===t.radio?o("div",{staticClass:"table"},[o("el-table",{ref:"table",attrs:{data:t.cloudtableData,"header-row-class-name":"tableHead","header-cell-class-name":"tableHeadCell","cell-class-name":"tableCell",height:"100%","tooltip-effect":"light"}},[o("el-table-column",{attrs:{prop:"name",label:t.$t("Name")}}),o("el-table-column",{attrs:{prop:"adminLevel",label:t.$t("Admin-level"),align:"center","show-overflow-tooltip":""}}),o("el-table-column",{attrs:{prop:"creator",label:t.$t("Creator"),align:"center"}}),o("el-table-column",{attrs:{prop:"createTime",label:t.$t("Create Time"),align:"center"},scopedSlots:t._u([{key:"default",fn:function(a){return[o("span",[t._v(t._s(t._f("dateFormat")(a.row.createTime)))])]}}],null,!1,3031374489)}),o("el-table-column",{attrs:{prop:"status",label:t.$t("Action"),align:"right"},scopedSlots:t._u([{key:"default",fn:function(a){return[o("span",[a.row.name===t.loginName?o("el-button",{attrs:{type:"text",disabled:"",icon:"el-icon-delete-solid"}}):o("el-button",{attrs:{type:"text",icon:"el-icon-delete-solid"},on:{click:function(e){return t.todDelete(a.row)}}})],1)]}}],null,!1,559290729)})],1)],1):o("div",{staticClass:"table"},[o("el-table",{ref:"table",attrs:{data:t.managertableData,"header-row-class-name":"tableHead","header-cell-class-name":"tableHeadCell","cell-class-name":"tableCell",height:"100%","tooltip-effect":"light"}},[o("el-table-column",{attrs:{prop:"institutions",label:t.$t("Institution"),"show-overflow-tooltip":""}}),o("el-table-column",{attrs:{prop:"fateManagerId",label:t.$t("Admin ID"),"show-overflow-tooltip":""}}),o("el-table-column",{attrs:{prop:"creator",label:t.$t("Creator")}}),o("el-table-column",{attrs:{prop:"createTime",label:t.$t("Create Time")},scopedSlots:t._u([{key:"default",fn:function(a){return[o("span",[t._v(t._s(t._f("dateFormat")(a.row.createTime)))])]}}])}),o("el-table-column",{attrs:{prop:"status",label:t.$t("Status"),align:"right"},scopedSlots:t._u([{key:"default",fn:function(a){return[o("span",[1===a.row.status?o("el-button",{attrs:{type:"text"},on:{click:function(e){return t.toactivat(a.row)}}},[t._v(t._s(t.$t("m.common.unactivated")))]):t._e(),2===a.row.status?o("el-button",{attrs:{disabled:"",type:"text"}},[t._v(t._s(t.$t("m.common.activated")))]):t._e()],1)]}}])})],1)],1),o("div",{staticClass:"pagination"},[o("el-pagination",{attrs:{background:"","current-page":t.currentPage,"page-size":t.data.pageSize,layout:"total, prev, pager, next, jumper",total:t.total},on:{"current-change":t.handleCurrentChange,"update:currentPage":function(a){t.currentPage=a},"update:current-page":function(a){t.currentPage=a}}})],1)]),o("el-dialog",{staticClass:"auto-dialog",attrs:{visible:t.adddialog,width:"690px","close-on-click-modal":!1,"close-on-press-escape":!1},on:{"update:visible":function(a){t.adddialog=a}}},[o("div",{staticClass:"dialog-box"},[o("div",{staticClass:"dialog-title"},[t._v("\n          "+t._s(t.$t("Add admin"))+"\n      ")]),"FATE Manager"===t.radio?o("div",{staticClass:"dialog-line"},[t._v("\n          "+t._s(t.$t("To add"))+"\n      ")]):t._e(),o("el-form",{ref:"managerForm",staticClass:"add-input",attrs:{model:t.managerForm,"label-position":"left",rules:t.editRules,"label-width":"260px"}},[o("el-form-item",{attrs:{prop:"institutionName"}},[o("span",{staticClass:"input-title",attrs:{slot:"label"},slot:"label"},["Cloud Manager"===t.radio?o("span",[t._v(t._s(t.$t("Name")))]):t._e(),"FATE Manager"===t.radio?o("span",[t._v(t._s(t.$t("Institution")))]):t._e()]),o("el-input",{attrs:{placeholder:t.$t("Maximum of 20 chatacters")},on:{focus:function(a){return t.$refs["managerForm"].clearValidate("institutionName")}},model:{value:t.managerForm.institutionName,callback:function(a){t.$set(t.managerForm,"institutionName",a)},expression:"managerForm.institutionName"}})],1),"Cloud Manager"===t.radio?o("el-form-item",[o("span",{staticClass:"input-title",attrs:{slot:"label"},slot:"label"},[t._v(t._s(t.$t("Admin-level")))]),o("el-checkbox",{attrs:{disabled:""},model:{value:t.managerForm.levelChecked,callback:function(a){t.$set(t.managerForm,"levelChecked",a)},expression:"managerForm.levelChecked"}},[t._v(t._s(t.$t("senior admin")))])],1):t._e(),"FATE Manager"===t.radio?o("span",[o("el-form-item",[o("span",{staticClass:"input-title",staticStyle:{color:"#4E5766"},attrs:{slot:"label"},slot:"label"},[t._v(t._s(t.$t("Invitation Link Setting")))])]),o("el-form-item",[o("span",{staticClass:"input-title",attrs:{slot:"label"},slot:"label"},[t._v(t._s(t.$t("Link Type")))]),o("el-radio-group",{model:{value:t.managerForm.protocol,callback:function(a){t.$set(t.managerForm,"protocol",a)},expression:"managerForm.protocol"}},[o("el-radio",{attrs:{label:"https://"}},[t._v("HTTPS")]),o("el-radio",{attrs:{label:"http://"}},[t._v("HTTP")])],1)],1),o("el-form-item",{attrs:{prop:"network"}},[o("span",{staticClass:"input-title",attrs:{slot:"label"},slot:"label"},[t._v(t._s(t.$t("Proxy Network Access")))]),o("el-input",{staticClass:"input",attrs:{placeholder:""},model:{value:t.managerForm.network,callback:function(a){t.$set(t.managerForm,"network",a)},expression:"managerForm.network"}}),o("span",{staticClass:"reset",on:{click:t.toResetNetwork}},[t._v(t._s(t.$t("reset to default")))])],1)],1):t._e()],1),o("div",{staticClass:"dialog-foot"},[o("el-button",{attrs:{type:"primary"},on:{click:t.toOK}},[t._v(t._s(t.$t("m.common.OK")))]),o("el-button",{attrs:{type:"info"},on:{click:function(a){t.adddialog=!1,t.$refs["managerForm"].clearValidate()}}},[t._v(t._s(t.$t("m.common.cancel")))])],1)],1)]),o("el-dialog",{staticClass:"auto-dialog",attrs:{visible:t.deletedialog,width:"700px","close-on-click-modal":!1,"close-on-press-escape":!1},on:{"update:visible":function(a){t.deletedialog=a}}},[o("div",{staticClass:"dialog-box"},[o("div",{staticClass:"line-text-one"},[t._v("\n          "+t._s(t.$t("Are you sure you want to delete this administrator?"))+"\n      ")]),o("div",{staticClass:"dialog-foot"},[o("el-button",{attrs:{type:"primary"},on:{click:t.toSure}},[t._v(t._s(t.$t("m.common.sure")))]),o("el-button",{attrs:{type:"info"},on:{click:function(a){t.deletedialog=!1}}},[t._v(t._s(t.$t("m.common.cancel")))])],1)])]),o("el-dialog",{staticClass:"add-success-dialog",attrs:{visible:t.addSuccessdialog},on:{"update:visible":function(a){t.addSuccessdialog=a}}},[o("div",{staticClass:"line-text-two"},[t._v(t._s(t.$t("the administrator")))]),o("el-form",{ref:"showForm",staticClass:"add-input",attrs:{model:t.managerForm,"label-position":"left",rules:t.editRules,"label-width":"240px"}},[o("span",{staticClass:"registration-box"},[o("el-form-item",{attrs:{label:"",prop:""}},[o("span",{attrs:{slot:"label"},slot:"label"},[o("span",{staticStyle:{color:"#848C99","margin-right":"20px"}},[t._v(t._s(t.$t("Invitation Link Setting")))])])]),o("el-form-item",{attrs:{label:t.$t("Link Type"),prop:"protocol"}},[o("span",[t._v(t._s("http://"===t.managerForm.protocol?"HTTP":"HTTPS"))])]),o("el-form-item",{attrs:{label:t.$t("Proxy Network Access"),prop:"network"}},[o("span",[t._v(t._s(t.managerForm.network))])])],1),o("el-form-item",[o("span",{staticClass:"input-title",staticStyle:{"margin-left":"30px"},attrs:{slot:"label"},slot:"label"},[t._v(t._s(t.$t("Invitation Link")))]),o("span",{staticClass:"line-text-three"},[o("el-popover",{attrs:{placement:"top",width:"660",trigger:"hover",offset:"-30",content:t.managerForm.addSuccessText}},[o("span",{staticClass:"copy-link",attrs:{slot:"reference"},slot:"reference"},[t._v(t._s(t.managerForm.addSuccessText))])]),o("span",{staticClass:"copy dialogcopy",attrs:{"data-clipboard-text":t.managerForm.addSuccessText},on:{click:t.toCopy}},[t._v(t._s(t.$t("m.common.copy")))])],1)])],1),o("div",{staticClass:"dialog-footer"},[o("el-button",{staticClass:"ok-btn",attrs:{type:"primary"},on:{click:function(a){t.addSuccessdialog=!1}}},[t._v(t._s(t.$t("m.common.OK")))]),o("el-button",{staticClass:"ok-btn",attrs:{type:"info"},on:{click:function(a){t.modifyDialog=!0}}},[t._v(t._s(t.$t("m.common.modify")))])],1)],1),o("el-dialog",{staticClass:"add-success-dialog",attrs:{visible:t.modifyDialog},on:{"update:visible":function(a){t.modifyDialog=a}}},[o("div",{staticClass:"line-text-two"},[t._v(t._s(t.$t("Invitation Link Setting")))]),o("el-form",{ref:"showForm",staticClass:"add-input",attrs:{model:t.managerForm,"label-position":"left",rules:t.editRules,"label-width":"240px"}},[o("el-form-item",{attrs:{label:t.$t("Link Type"),prop:"protocol"}},[o("el-radio-group",{model:{value:t.managerForm.protocol,callback:function(a){t.$set(t.managerForm,"protocol",a)},expression:"managerForm.protocol"}},[o("el-radio",{attrs:{label:"https://"}},[t._v("HTTPS")]),o("el-radio",{attrs:{label:"http://"}},[t._v("HTTP")])],1)],1),o("el-form-item",{attrs:{label:t.$t("Proxy Network Access"),prop:"proxyNetworkAccess"}},[o("el-input",{staticClass:"input",attrs:{placeholder:""},model:{value:t.managerForm.network,callback:function(a){t.$set(t.managerForm,"network",a)},expression:"managerForm.network"}}),o("span",{staticClass:"reset",on:{click:t.toResetNetwork}},[t._v(t._s(t.$t("reset to default")))])],1)],1),o("div",{staticClass:"dialog-footer",staticStyle:{"margin-top":"25px"}},[o("el-button",{staticClass:"ok-btn",attrs:{type:"primary"},on:{click:t.toUpdata}},[t._v(t._s(t.$t("m.common.submit")))]),o("el-button",{staticClass:"ok-btn",attrs:{type:"info"},on:{click:function(a){t.modifyDialog=!1}}},[t._v(t._s(t.$t("m.common.cancel")))])],1)],1)],1)},i=[],n=(e("3b2b"),e("a481"),e("cebc")),s=e("c1df"),r=e.n(s),l=e("b311"),c=e.n(l),d=e("2f62"),m=e("90e7"),u=e("c6a8"),p={zh:{add:"添加","Today’s active data":"今日活跃数据","Cumulative active data":"累计活跃数据",Name:"用户名","Admin-level":"管理级别",Creator:"创建者","Create Time":"创建时间",Action:"操作",Institution:"机构名称","Admin ID":"管理ID",Status:"状态","Are you sure you want to delete this administrator?":"确认删除此管理账号吗?","Add admin":"添加管理员","To add":"为FATE Manager添加管理员权限，需要填写管理员所属的FATE Manager机构名以完成匹配，信息填写后不允许更改。","senior admin":"高级管理员","Maximum of 20 chatacters":"不超过20个字符","Invitation Link Setting":"邀请链接设置","Link Type":"链接类型：","Proxy Network Access":"代理网关：","Invitation Link":"邀请链接：","the administrator":"管理员链接已生成：",Modify:"修改信息","Search for Institution":"搜索机构名称","Search for Name":"搜索用户名","reset to default":"恢复默认","Cloud Manager":"云端管理","FATE Manager":"联邦管理"},en:{add:"add","Today’s active data":"Today’s active data","Cumulative active data":"Cumulative active data",Name:"Name","Admin-level":"Admin-level",Creator:"Creator","Create Time":"Create Time",Action:"Action",Institution:"Institution","Admin ID":"Admin ID",Status:"Status","Are you sure you want to delete this administrator?":"Are you sure you want to delete this administrator?","Add admin":"Add admin","To add":"To add administrtor right to FATE Manager,please fill in the institution name to which the administrator belongs. Once filled in,it cannot be modified.","senior admin":"senior admin","Maximum of 20 chatacters":"Maximum of 20 chatacters","Invitation Link Setting":"Invitation Link Setting","Link Type":"Link Type：","Proxy Network Access":"Proxy Network Access：","Invitation Link":"Invitation Link:","the administrator":"the administrator invitation link has been generated as follows:",Modify:"Modify","Search for Institution":"Search for Institution","Search for Name":"Search for Name","reset to default":"reset to default","Cloud Manager":"Cloud Manager","FATE Manager":"FATE Manager"}},g={name:"access",components:{},filters:{dateFormat:function(t){return t?r()(t).format("YYYY-MM-DD HH:mm:ss"):"--"}},data:function(){var t=this;return{fateManagerId:"",adddialog:!1,deletedialog:!1,modifyDialog:!1,addSuccessdialog:!1,radio:"Cloud Manager",currentPage:1,total:0,managertableData:[],cloudtableData:[],historydata:[],managerForm:{addSuccessText:"",institutionName:"",levelChecked:!0,protocol:"https://",network:""},data:{pageNum:1,pageSize:20},editRules:{institutionName:[{required:!0,trigger:"bulr",validator:function(a,e,o){e?e.length>20?o(new Error(t.$t("m.siteAdd.maximum20chatacters"))):o():o(new Error(t.$t("m.siteAdd.institutionRrequired")))}}],network:[{required:!0,trigger:"bulr",validator:function(a,e,o){e?o():o(new Error(t.$t("m.siteAdd.proxyNetworkAccessRequired")))}}]}}},watch:{radio:{handler:function(t){this.data={name:"",institutions:"",pageNum:1,pageSize:20},this.initList()}}},computed:Object(n["a"])({},Object(d["mapGetters"])(["getInfo","loginName"])),created:function(){this.initList(),this.toResetNetwork(),this.$i18n.mergeLocaleMessage("en",p.en),this.$i18n.mergeLocaleMessage("zh",p.zh),"FATEManager"===this.$route.query.type&&(this.radio="FATE Manager")},mounted:function(){},methods:{initList:function(){var t=this;for(var a in this.data)if(this.data.hasOwnProperty(a)){var e=this.data[a];e||delete this.data[a]}"Cloud Manager"===this.radio?Object(m["a"])(this.data).then(function(a){t.cloudtableData=a.data.list,t.total=a.data.totalRecord}):"FATE Manager"===this.radio&&Object(m["b"])(this.data).then(function(a){t.managertableData=a.data.list,t.total=a.data.totalRecord})},toOK:function(){var t=this;this.$refs["managerForm"].validate(function(a){if(a)if("Cloud Manager"===t.radio){var e={creator:t.loginName,adminLevel:1,name:t.managerForm.institutionName.trim()};Object(m["d"])(e).then(function(a){t.adddialog=!1,t.initList()})}else{var o={creator:t.loginName,institutions:t.managerForm.institutionName.trim(),protocol:t.managerForm.protocol,network:t.managerForm.network};Object(m["e"])(o).then(function(a){t.managerForm.addSuccessText=JSON.stringify(a.data.registrationLink).replace(new RegExp('"',"g"),""),t.managerForm.fateManagerId=a.data.fateManagerId,t.managerForm.protocol=a.data.protocol,t.adddialog=!1,t.initList(),t.addSuccessdialog=!0})}})},todDelete:function(t){this.deletedialog=!0,this.deleteRow=t.cloudManagerId},toSure:function(){var t=this,a={cloudManagerId:this.deleteRow};Object(m["j"])(a).then(function(a){t.deletedialog=!1,t.initList()})},toAdd:function(){this.managerForm.institutionName="",this.adddialog=!0,this.managerForm.protocol="https://"},toactivat:function(t){this.managerForm.addSuccessText=JSON.stringify(t.registrationLink).replace(new RegExp('"',"g"),""),this.managerForm.fateManagerId=t.fateManagerId,this.managerForm.institutionName=t.institutions,this.managerForm.network=t.network,this.managerForm.protocol=t.protocol,this.addSuccessdialog=!0},toUpdata:function(){var t=this,a={creator:this.loginName,institution:this.managerForm.institutionName,fateManagerId:this.managerForm.fateManagerId,network:this.managerForm.network,protocol:this.managerForm.protocol};Object(m["w"])(a).then(function(a){t.modifyDialog=!1,t.addSuccessdialog=!1,t.managerForm.addSuccessText=JSON.stringify(a.data.registrationLink).replace(new RegExp('"',"g"),""),t.managerForm.protocol=a.data.protocol,t.managerForm.network=a.data.network,t.initList(),setTimeout(function(){t.addSuccessdialog=!0},300)})},handleCurrentChange:function(t){this.data.pageNum=t,this.initList()},toCopy:function(){var t=this,a=new c.a(".dialogcopy");a.on("success",function(e){t.$message.success(t.$t("m.common.copySuccess")),a.destroy()})},toSearch:function(){this.currentPage=1,this.initList()},toResetNetwork:function(){var t=this;Object(u["F"])().then(function(a){t.managerForm.network=a.data.network})}}},f=g,h=(e("c047"),e("2877")),b=Object(h["a"])(f,o,i,!1,null,null,null);a["default"]=b.exports},"2fe8":function(t,a){t.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAAXNSR0IArs4c6QAAADhlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAAqACAAQAAAABAAAAGKADAAQAAAABAAAAGAAAAADB/VeXAAABm0lEQVRIDe1UvVXDMBC+EwzABpiC50dHJgAmCGyQDQIdpInSJClhAsIEsAFhAh4VzzTxCLCAj/sMCrIkYh5NmqjR/X7f6e5sos1Zdwf4LwVkl68ZGTPU4B7ihWhGVTUqpwcl9FWnleAb/FkDd3wgJXlXkk4bifGTkjIbG4IjrrapL5njGVsJFOjUi2+KTN2mIdZaCeKUHwsLHrL6JAn2BoW2+Ouo8ODk8F7lc7FJAjiXJFJZXZsPl7C8YYOv5fxKsBjn9fOxJSLVoQjdOSzIsLVtkItv3NmgsKged8PxT2U7zNOyh1KZEzbVo/ps6Pf17KrQDZM+Mx+LyFyX96ac5I2ZRVuAymsSopF+SDMy3NUZYFUzBcr0JgW7ULCSme6ho51uZtq+M58kmkE5zq1uX0dRjtiYBRNfo0IHDkD1oUoLMT5y7tsSL3jrMcmtHxTKrmK3CL4fL/HtiRlg9SJeH4Pwf9JWvLi2OEIEafue/OCoRQq+6wckZWN6ardJn2w17AmCZFpo7BNziYGiYrwEdz3g6f48DN7o6+3AJ4NVoRnP9rT0AAAAAElFTkSuQmCC"},c047:function(t,a,e){"use strict";var o=e("1644"),i=e.n(o);i.a}}]);
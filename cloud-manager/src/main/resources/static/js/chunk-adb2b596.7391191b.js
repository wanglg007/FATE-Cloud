(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-adb2b596"],{"0798":function(t,e){t.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAYAAABWzo5XAAAAAXNSR0IArs4c6QAAADhlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAAqACAAQAAAABAAAAEqADAAQAAAABAAAAEgAAAAC5YZBvAAAAuElEQVQ4Ee2S0Q3CMBBDncAeZIVuwAiMkEowFUIwAmzABqwAG8ACPdISX1NFVQD1gw/647Pz6p6iAhM9hj2yxRIW++Ads4Je0aA2G5xbzipscAizU18eXPxwR6ZFi/K7GeGY9EVMvtS8yKIKK1faV/IRzIu04bNhnuENLoOs5CM82UZ9keAx2OQdI7gRS4tWSA4IjGrLCjzP9c9mQJVdwF5berPGkfmY5pdNUnDCDN7UuDP664/cwBNFEiIZp9aUMQAAAABJRU5ErkJggg=="},"1af6":function(t,e,a){var n=a("63b6");n(n.S,"Array",{isArray:a("9003")})},"20fd":function(t,e,a){"use strict";var n=a("d9f6"),i=a("aebd");t.exports=function(t,e,a){e in t?n.f(t,e,i(0,a)):t[e]=a}},2737:function(t,e){t.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAYAAABWzo5XAAAABHNCSVQICAgIfAhkiAAAANhJREFUOE/lk7ENwjAQRf+ZBRjBFBA6YALIBozACCmBBtIklIzABqwQNkiHUsWT+JAjjJIAskGkwu3Jz+/+nQk/OmQ5g23B3zDLJKgY3YHsCy4720H3Ri6Tdv2t0R+1ZqfDQAwtMnUYZnJ9lRBiRYyoTIO+9x4xaAZmCcKOgCkDORgxiJRKRrkXqDJh5EQ4mwtmGA9LLUJj6AfSIgTpIxEmTyDmi0rHCy9Q3cCC6v/Te7Pv+ZysUX0h+ROjdkYN0KuMXF9DboolwBERzY0JuLe3QTcycoFc9Rsk+pMTAOdfrgAAAABJRU5ErkJggg=="},"28a5":function(t,e,a){"use strict";var n=a("aae3"),i=a("cb7c"),s=a("ebd6"),o=a("0390"),c=a("9def"),r=a("5f1b"),l=a("520a"),u=a("79e5"),p=Math.min,d=[].push,m="split",h="length",f="lastIndex",g=4294967295,A=!u(function(){RegExp(g,"y")});a("214f")("split",2,function(t,e,a,u){var v;return v="c"=="abbc"[m](/(b)*/)[1]||4!="test"[m](/(?:)/,-1)[h]||2!="ab"[m](/(?:ab)*/)[h]||4!="."[m](/(.?)(.?)/)[h]||"."[m](/()()/)[h]>1||""[m](/.?/)[h]?function(t,e){var i=String(this);if(void 0===t&&0===e)return[];if(!n(t))return a.call(i,t,e);var s,o,c,r=[],u=(t.ignoreCase?"i":"")+(t.multiline?"m":"")+(t.unicode?"u":"")+(t.sticky?"y":""),p=0,m=void 0===e?g:e>>>0,A=new RegExp(t.source,u+"g");while(s=l.call(A,i)){if(o=A[f],o>p&&(r.push(i.slice(p,s.index)),s[h]>1&&s.index<i[h]&&d.apply(r,s.slice(1)),c=s[0][h],p=o,r[h]>=m))break;A[f]===s.index&&A[f]++}return p===i[h]?!c&&A.test("")||r.push(""):r.push(i.slice(p)),r[h]>m?r.slice(0,m):r}:"0"[m](void 0,0)[h]?function(t,e){return void 0===t&&0===e?[]:a.call(this,t,e)}:a,[function(a,n){var i=t(this),s=void 0==a?void 0:a[e];return void 0!==s?s.call(a,i,n):v.call(String(i),a,n)},function(t,e){var n=u(v,t,this,e,v!==a);if(n.done)return n.value;var l=i(t),d=String(this),m=s(l,RegExp),h=l.unicode,f=(l.ignoreCase?"i":"")+(l.multiline?"m":"")+(l.unicode?"u":"")+(A?"y":"g"),b=new m(A?l:"^(?:"+l.source+")",f),_=void 0===e?g:e>>>0;if(0===_)return[];if(0===d.length)return null===r(b,d)?[d]:[];var y=0,x=0,k=[];while(x<d.length){b.lastIndex=A?x:0;var w,D=r(b,A?d:d.slice(x));if(null===D||(w=p(c(b.lastIndex+(A?0:x)),d.length))===y)x=o(d,x,h);else{if(k.push(d.slice(y,x)),k.length===_)return k;for(var C=1;C<=D.length-1;C++)if(k.push(D[C]),k.length===_)return k;x=y=w}}return k.push(d.slice(y)),k}]})},"43a8":function(t,e,a){},5118:function(t,e,a){t.exports=a("0b93")(103)},"549b":function(t,e,a){"use strict";var n=a("d864"),i=a("63b6"),s=a("241e"),o=a("b0dc"),c=a("3702"),r=a("b447"),l=a("20fd"),u=a("7cd6");i(i.S+i.F*!a("4ee1")(function(t){Array.from(t)}),"Array",{from:function(t){var e,a,i,p,d=s(t),m="function"==typeof this?this:Array,h=arguments.length,f=h>1?arguments[1]:void 0,g=void 0!==f,A=0,v=u(d);if(g&&(f=n(f,h>2?arguments[2]:void 0,2)),void 0==v||m==Array&&c(v))for(e=r(d.length),a=new m(e);e>A;A++)l(a,A,g?f(d[A],A):d[A]);else for(p=v.call(d),a=new m;!(i=p.next()).done;A++)l(a,A,g?o(p,f,[i.value,A],!0):i.value);return a.length=A,a}})},"54a1":function(t,e,a){a("6c1c"),a("1654"),t.exports=a("95d5")},"5bf3":function(t,e){t.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAYAAABWzo5XAAAABHNCSVQICAgIfAhkiAAAANtJREFUOE/lk0EOwUAUhv+/J3AEN8AJ6A0cwUpjZ6E2NDQkNhJ20p0buAI36BEcRN6TVibaIjOEldm+zDff+98b4kuHhrNcJ/oJczoKcsbvQOYFm53p4PdGNpNq/aXRH7VmpqOKGJBjFA6Oq82ufrl4PQLDaRjUnPeIwpZ4WqdiBqIJRapE7AnPk3E/dQLlJkRK4JBdyIZxtxQ/M3QEiQ9yS7DxCMIpCoOOE6hoYEDF/+m82bd8ZG+Migup+oZRNaMy6ElGtq+xWCddKIYk2pkJIHMTdCkjG8hWvwJU3ZYTVaQrBgAAAABJRU5ErkJggg=="},"644f":function(t,e,a){},"75fc":function(t,e,a){"use strict";var n=a("a745"),i=a.n(n);function s(t){if(i()(t)){for(var e=0,a=new Array(t.length);e<t.length;e++)a[e]=t[e];return a}}var o=a("774e"),c=a.n(o),r=a("c8bb"),l=a.n(r);function u(t){if(l()(Object(t))||"[object Arguments]"===Object.prototype.toString.call(t))return c()(t)}function p(){throw new TypeError("Invalid attempt to spread non-iterable instance")}function d(t){return s(t)||u(t)||p()}a.d(e,"a",function(){return d})},"774e":function(t,e,a){t.exports=a("d2d5")},9003:function(t,e,a){t.exports=a("0b93")(176)},"95d5":function(t,e,a){var n=a("40c3"),i=a("5168")("iterator"),s=a("481b");t.exports=a("584a").isIterable=function(t){var e=Object(t);return void 0!==e[i]||"@@iterator"in e||s.hasOwnProperty(n(e))}},"9b4d":function(t,e){t.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAAXNSR0IArs4c6QAAADhlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAAqACAAQAAAABAAAAGKADAAQAAAABAAAAGAAAAADB/VeXAAAB10lEQVRIDe1UMVbCQBCdCT4s1RMQCgUrvQG5gfEE4gmkRKvYACWcQG8A3CDeQCsfz4JwAyiJT8aZhJFkNzywsnELdubvn/kzs0sA/teOCeCO863H7v3EB6A7RPSIKATAQdStjcwAxwT28SU5Igwl+bRT4w098VPRfIaDvLvx3GB6DMtlkmSDcs2rVZX9IIttbGqxnetiqwAnbybtAw24/bkmiXrnUfVhciGVK6Y246SY7tsFAHwieIu6dakqtwTXZJJcbb6LlxyRnUIBGQ/GcYOS6gE0gQRziY/8E7A5FD+3qBTkfHYKBSD+9FOi8yy7jiDF0l++0GuWa4l4Wjn2o95pmOWIXSxA5PHZIuqevQop24H43IXcST/q1D3x3fa7C4iXYpurUIBvz+ckIyUXdaBnyY5OAAhXbP/E6Lkl4LY/PMDVEZeZkM3qNVD3tfiIi7qRWHNMlgA4Xz4/S4DDcihJdlYvJOHGMaSxEAqky/onr8czjoLqXEm7duHySMdcWMPk2h0AVlikYo6GyuUTFZVLRceZmsmK/AKBIhpj/NngxLfJKeLTFpYF7y0gnw1+intVnVWx7oBfzyJL+J1NM5NvCRA5/Ipsohlo+zSjValp4//IX0/gG7o0qPKsZLd8AAAAAElFTkSuQmCC"},a745:function(t,e,a){t.exports=a("f410")},a81a:function(t,e,a){"use strict";var n=a("43a8"),i=a.n(n);i.a},aae3:function(t,e,a){var n=a("d3f4"),i=a("2d95"),s=a("2b4c")("match");t.exports=function(t){var e;return n(t)&&(void 0!==(e=t[s])?!!e:"RegExp"==i(t))}},aead:function(t,e,a){"use strict";var n=a("644f"),i=a.n(n);i.a},aebd:function(t,e,a){t.exports=a("0b93")(26)},c6a8:function(t,e,a){"use strict";a.d(e,"J",function(){return i}),a.d(e,"p",function(){return s}),a.d(e,"h",function(){return o}),a.d(e,"H",function(){return c}),a.d(e,"E",function(){return r}),a.d(e,"K",function(){return l}),a.d(e,"I",function(){return u}),a.d(e,"s",function(){return p}),a.d(e,"M",function(){return d}),a.d(e,"C",function(){return m}),a.d(e,"j",function(){return h}),a.d(e,"i",function(){return f}),a.d(e,"t",function(){return g}),a.d(e,"L",function(){return A}),a.d(e,"D",function(){return v}),a.d(e,"y",function(){return b}),a.d(e,"z",function(){return _}),a.d(e,"f",function(){return y}),a.d(e,"g",function(){return x}),a.d(e,"u",function(){return k}),a.d(e,"B",function(){return w}),a.d(e,"x",function(){return D}),a.d(e,"A",function(){return C}),a.d(e,"a",function(){return S}),a.d(e,"e",function(){return L}),a.d(e,"w",function(){return O}),a.d(e,"n",function(){return j}),a.d(e,"b",function(){return E}),a.d(e,"k",function(){return I}),a.d(e,"d",function(){return $}),a.d(e,"q",function(){return N}),a.d(e,"o",function(){return R}),a.d(e,"N",function(){return B}),a.d(e,"m",function(){return T}),a.d(e,"F",function(){return V}),a.d(e,"G",function(){return J}),a.d(e,"c",function(){return z}),a.d(e,"O",function(){return Q}),a.d(e,"l",function(){return Y}),a.d(e,"r",function(){return P}),a.d(e,"v",function(){return U});var n=a("b775");function i(t){return Object(n["a"])({url:"/cloud-manager/api/site/page/cloudManager",method:"post",data:t})}function s(t){return Object(n["a"])({url:"/cloud-manager/api/group/findPagedRegionInfoNew",method:"post",data:t})}function o(t){return Object(n["a"])({url:"/cloud-manager/api/site/check",method:"post",data:t})}function c(t){return Object(n["a"])({url:"/cloud-manager/api/site/addNew",method:"post",data:t})}function r(t){return Object(n["a"])({url:"/cloud-manager/api/site/cloudManager/network",method:"post",data:t})}function l(t){return Object(n["a"])({url:"/cloud-manager/api/site/updateNew",method:"post",data:t})}function u(t){return Object(n["a"])({url:"/cloud-manager/api/site/delete",method:"post",data:t})}function p(t){return Object(n["a"])({url:"/cloud-manager/api/site/find",method:"post",data:t})}function d(t){return Object(n["a"])({url:"/cloud-manager/api/site/checkWeb",method:"post",data:t})}function m(t){return Object(n["a"])({url:"/cloud-manager/api/site/ip/list",method:"post",data:t})}function h(t){return Object(n["a"])({url:"/cloud-manager/api/site/ip/deal",method:"post",data:t})}function f(t){return Object(n["a"])({url:"/cloud-manager/api/site/checkSiteName",method:"post",data:t})}function g(t){return Object(n["a"])({url:"/cloud-manager/api/system/page",method:"post",data:t})}function A(t){return Object(n["a"])({url:"/cloud-manager/api/system/history",method:"post",data:t})}function v(t){return Object(n["a"])({url:"/cloud-manager/api/site/ip/query/history",method:"post",data:t})}function b(t){return Object(n["a"])({url:"/cloud-manager/api/site/institutions",method:"post",data:t})}function _(t){return Object(n["a"])({url:"/cloud-manager/api/site/institutions/all/dropdown",method:"post",data:t})}function y(t){return Object(n["a"])({url:"/cloud-manager/api/authority/cancel",method:"post",data:t})}function x(t){return Object(n["a"])({url:"/cloud-manager/api/authority/cancelList",method:"post",data:t})}function k(t){return Object(n["a"])({url:"/cloud-manager/api/authority/history/fateManager",method:"post",data:t})}function w(t){return Object(n["a"])({url:"/cloud-manager/api/authority/status",method:"post",data:t})}function D(t){return Object(n["a"])({url:"/cloud-manager/api/authority/details",method:"post",data:t})}function C(t){return Object(n["a"])({url:"/cloud-manager/api/authority/review",method:"post",data:t})}function S(t){return Object(n["a"])({url:"/cloud-manager/api/fate/user/institutions",method:"post",data:t})}function L(t){return Object(n["a"])({url:"/cloud-manager/api/authority/currentAuthority",method:"post",data:t})}function O(t){return Object(n["a"])({url:"/cloud-manager/api/dropdown/version",method:"post",data:t})}function j(t){return Object(n["a"])({url:"/cloud-manager/api/exchange/exchange/page",method:"post",data:t})}function E(t){return Object(n["a"])({url:"/cloud-manager/api/exchange/add",method:"post",data:t})}function I(t){return Object(n["a"])({url:"/cloud-manager/api/exchange/delete",method:"post",data:t})}function $(t){return Object(n["a"])({url:"/cloud-manager/api/exchange/rollsite/add",method:"post",data:t})}function N(t){return Object(n["a"])({url:"/cloud-manager/api/exchange/rollsite/page",method:"post",data:t})}function R(t){return Object(n["a"])({url:"/cloud-manager/api/exchange/query",method:"post",data:t})}function B(t){return Object(n["a"])({url:"/cloud-manager/api/exchange/rollsite/publish",method:"post",data:t})}function T(t){return Object(n["a"])({url:"/cloud-manager/api/exchange/rollsite/delete",method:"post",data:t})}function V(t){return Object(n["a"])({url:"/cloud-manager/api/exchange/rollsite/update",method:"post",data:t})}function J(t){return Object(n["a"])({url:"/cloud-manager/api/product/page",method:"post",data:t})}function z(t){return Object(n["a"])({url:"/cloud-manager/api/product/add",method:"post",data:t})}function Q(t){return Object(n["a"])({url:"/cloud-manager/api/product/update",method:"post",data:t})}function Y(t){return Object(n["a"])({url:"/cloud-manager/api/product/delete",method:"post",data:t})}function P(t){return Object(n["a"])({url:"/cloud-manager/api/product/version",method:"post",data:t})}function U(t){return Object(n["a"])({url:"/cloud-manager/api/product/name",method:"post",data:t})}},c8bb:function(t,e,a){t.exports=a("54a1")},d2d5:function(t,e,a){a("1654"),a("549b"),t.exports=a("584a").Array.from},e3fc:function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"site-box"},[n("div",{staticClass:"site"},[n("div",{staticClass:"site-header"},[n("el-button",{staticClass:"add",attrs:{type:"text"},on:{click:t.addsite}},[n("img",{attrs:{src:a("9b4d")}}),n("span",[t._v(t._s(t.$t("m.common.add")))])]),n("el-input",{staticClass:"input input-placeholder",attrs:{placeholder:t.$t("m.site.searchSiteOrParty"),clearable:""},model:{value:t.data.condition,callback:function(e){t.$set(t.data,"condition","string"===typeof e?e.trim():e)},expression:"data.condition"}}),n("el-select",{staticClass:"sel-role input-placeholder",attrs:{filterable:"",multiple:"","collapse-tags":"",placeholder:t.$t("m.common.institution")},model:{value:t.data.institutionsArray,callback:function(e){t.$set(t.data,"institutionsArray",e)},expression:"data.institutionsArray"}},t._l(t.institutionsSelectList,function(t,e){return n("el-option",{key:e,attrs:{label:t.label,value:t.value}})}),1),n("el-button",{staticClass:"go",attrs:{type:"text"},on:{click:t.toFold}},[t.activeName.length>0?n("span",[t._v(t._s(t.$t("m.common.foldAll")))]):n("span",[t._v(t._s(t.$t("m.common.unfoldAll")))])]),n("el-button",{staticClass:"go",attrs:{type:"primary"},on:{click:t.toSearch}},[t._v(t._s(t.$t("m.common.go")))])],1),n("div",{staticClass:"collapse"},[t._l(t.institutionsItemList,function(e,i){return n("el-collapse",{key:i,model:{value:t.activeName,callback:function(e){t.activeName=e},expression:"activeName"}},[n("el-collapse-item",{attrs:{name:e.institutions}},[n("template",{slot:"title"},[n("span",{staticClass:"ins"},[t._v(t._s(e.institutions))]),e.tooltip&&t.siteState?n("img",{attrs:{src:a("0798"),alt:""},on:{click:function(a){return a.stopPropagation(),t.toshowins(e.institutions)}}}):t._e(),e.historyList.length>0?n("span",[t.siteState?n("el-popover",{attrs:{placement:"bottom","visible-arrow":!1,width:"700",offset:-340,"popper-class":"site-history",trigger:"click"},model:{value:e.visible,callback:function(a){t.$set(e,"visible",a)},expression:"itm.visible"}},[n("div",{staticClass:"content"},[n("div",{staticClass:"title"},[n("div",{staticClass:"title-time"},[t._v(t._s(t.$t("m.common.time")))]),n("div",{staticClass:"title-history"},[t._v(t._s(t.$t("m.common.history")))])]),n("div",{staticClass:"content-box"},t._l(e.historyList,function(e,a){return n("div",{key:a},[n("div",{staticClass:"title-time"},[t._v(t._s(t._f("dateFormat")(e.updateTime)))]),n("div",{staticClass:"title-history"},[e.cancel.length>0?n("span",[t._v("\n                                                  "+t._s(t.$t("m.site.canceledAuthorization"))+"\n                                                   "+t._s(e.institutions)+"\n                                                   "+t._s(t.$t("m.site.to"))+"\n                                                  "),t._l(e.cancel,function(a,i){return n("span",{key:i},[i===e.cancel.length-1?n("span",[t._v(t._s(a))]):n("span",[t._v(t._s(a)+",")])])}),t._v("\n                                                  "+t._s(t.$t("m.site.sitesOfPlaceHodler"))+"\n                                              ")],2):t._e(),e.agree.length>0?n("span",[t._v("\n                                                  "+t._s(t.$t("m.site.agreedAuthorze"))+"\n                                                   "+t._s(e.institutions)+"\n                                                   "+t._s(t.$t("m.site.viewAites"))+"\n                                                  "),t._l(e.agree,function(a,i){return n("span",{key:i},[i===e.agree.length-1?n("span",[t._v(t._s(a))]):n("span",[t._v(t._s(a)+",")])])}),t._v("\n                                                  "+t._s(t.$t("m.site.sitesOfPlaceHodler"))+"\n                                              ")],2):t._e(),e.reject.length>0?n("span",[t._v("\n                                                  "+t._s(t.$t("m.site.rejectedAuthorize"))+"\n                                                  "+t._s(e.institutions)+"\n                                                  "+t._s(t.$t("m.site.viewAites"))+"\n                                                  "),t._l(e.reject,function(a,i){return n("span",{key:i},[i===e.reject.length-1?n("span",[t._v(t._s(a))]):n("span",[t._v(t._s(a)+",")])])}),t._v("\n                                                  "+t._s(t.$t("m.site.sitesOfPlaceHodler"))+"\n                                              ")],2):t._e()])])}),0)]),n("img",{staticClass:"tickets",attrs:{slot:"reference",src:a("2737"),alt:""},on:{click:function(e){return e.stopPropagation(),t.gethistory(i)}},slot:"reference"})]):t._e()],1):n("span",{staticClass:"ins"},[n("img",{staticClass:"disable",attrs:{src:a("5bf3"),alt:""}})]),n("div",{staticClass:"sitenum"},[n("span",[t._v(t._s(e.number))]),n("span",[1===e.number||0===e.number?n("span",[t._v(t._s(t.$t("m.site.siteJoined")))]):n("span",[t._v(t._s(t.$t("m.site.sitesJoined")))])])])]),t.siteState&&e.authoritylist&&e.authoritylist.length>0?n("div",{staticClass:"msg-warn"},[n("span",[t._v("\n                          "+t._s(e.institutions)+"\n                      ")]),t._v("\n                      "+t._s(t.$t("m.site.canView"))+"\n                      "),t._l(e.authoritylist,function(a,i){return n("span",{key:i},[i===e.authoritylist.length-1?n("span",[t._v(t._s(a))]):n("span",[t._v(t._s(a)+",")])])}),t._v("\n                      "+t._s(t.$t("m.site.sitesOfPlaceHodler"))+"\n                      "),n("el-button",{staticClass:"btn",attrs:{type:"text"},on:{click:function(a){return t.toshowcancelAuthor(e.authoritylist,e.institutions)}}},[t._v("\n                          "+t._s(t.$t("m.site.cancalAuthorization"))+"\n                      ")])],2):t._e(),n("sitetable",{ref:"sitelist",refInFor:!0,attrs:{institutions:e.institutions,condition:t.data.condition}})],2)],1)}),0===t.institutionsItemList.length?n("div",{staticClass:"no-data"},[t._v(t._s(t.$t("m.common.noData")))]):t._e(),n("div",{staticClass:"pagination"},[n("el-pagination",{attrs:{background:"","current-page":t.currentPage,"page-size":t.data.pageSize,layout:"total, prev, pager, next, jumper",total:t.total},on:{"size-change":t.handleSizeChange,"current-change":t.handleCurrentChange,"update:currentPage":function(e){t.currentPage=e},"update:current-page":function(e){t.currentPage=e}}})],1)],2),n("el-dialog",{staticClass:"add-author-dialog",attrs:{visible:t.tipsVisible,width:"700px"},on:{"update:visible":function(e){t.tipsVisible=e}}},[n("div",{staticClass:"line-text-one"},[t._v(" "+t._s(t.$t("m.site.fateManeger"))+'\n              " '),n("span",{staticStyle:{color:"#217AD9"}},[t._v(t._s(t.tipstempData.institutions))]),t._v(' "\n          ')]),n("div",{staticClass:"line-text-one"},[t._v("\n              "+t._s(t.$t("m.site.appliedView"))+"\n              "),"1"===t.tipstempData.scenarioType?n("span"):t._e(),"2"===t.tipstempData.scenarioType?n("span",[t._v(t._s(t.$t("m.common.guest")))]):t._e(),"3"===t.tipstempData.scenarioType?n("span",[t._v(t._s(t.$t("m.common.host")))]):t._e(),t._v("\n              "+t._s(t.$t("m.site.sitesOf"))+"\n          ")]),n("div",{staticClass:"line-text-one",staticStyle:{color:"#217AD9"}},t._l(t.tipstempData.insList,function(e,a){return n("span",{key:a},[a===t.tipstempData.insList.length-1?n("span",[t._v(t._s(e))]):n("span",[t._v(" "+t._s(e)+",")])])}),0),n("div",{staticClass:"line-text-two"},[t._v("\n              "+t._s(t.$t("m.site.selectApprove"))+"\n          ")]),n("div",{staticClass:"line-text-two"},[t._v("\n              "+t._s(t.$t("m.site.authorizationReject"))+"\n          ")]),n("div",{staticClass:"dialog-main"},[n("el-checkbox-group",{model:{value:t.tipstempData.institucheckList,callback:function(e){t.$set(t.tipstempData,"institucheckList",e)},expression:"tipstempData.institucheckList"}},t._l(t.tipstempData.institucheckboxList,function(t,e){return n("div",{key:e},[n("el-checkbox",{attrs:{label:t}},[n("tooltip",{staticStyle:{"vertical-align":"top"},attrs:{width:"255px",content:t,placement:"top"}})],1)],1)}),0)],1),n("div",{staticClass:"dialog-footer"},[n("el-button",{staticClass:"ok-btn",attrs:{type:"primary"},on:{click:t.totipsAction}},[t._v(t._s(t.$t("m.common.sure")))]),n("el-button",{staticClass:"ok-btn",attrs:{type:"info"},on:{click:function(e){t.tipsVisible=!1}}},[t._v(t._s(t.$t("m.common.cancel")))])],1)]),n("el-dialog",{staticClass:"cancel-author-dialog",attrs:{visible:t.cancelAuthorVisible,width:"700px"},on:{"update:visible":function(e){t.cancelAuthorVisible=e}}},[n("div",{staticClass:"line-text-one"},[t._v(t._s(t.$t("m.site.selectCancel")))]),n("div",{staticClass:"line-text-one"},[t._v(t._s(t.$t("m.site.theAuthorization"))+"\n              "),n("span",{staticStyle:{color:"#217AD9"}},[t._v(t._s(t.canceltempData.institutions))]),t._v("\n              "+t._s(t.$t("m.site.authorizationTo"))+"\n          ")]),"2"===t.canceltempData.scenarioType||"3"===t.canceltempData.scenarioType?n("span",[n("div",{staticClass:"siteType"},[t._v(t._s(t.$t("m.site.hostSites"))+" :")]),t.canceltempData.hostboxList.length>0?n("div",{staticClass:"dialog-main"},[n("el-checkbox",{staticStyle:{"margin-bottom":"10px"},attrs:{indeterminate:t.canceltempData.hostisnate},on:{change:t.hostChange},model:{value:t.canceltempData.hostAll,callback:function(e){t.$set(t.canceltempData,"hostAll",e)},expression:"canceltempData.hostAll"}},[t._v(t._s(t.$t("m.common.all")))]),n("el-checkbox-group",{on:{change:t.hostStieChange},model:{value:t.canceltempData.hostList,callback:function(e){t.$set(t.canceltempData,"hostList",e)},expression:"canceltempData.hostList"}},t._l(t.canceltempData.hostboxList,function(t,e){return n("div",{key:e},[n("el-checkbox",{attrs:{label:t}},[n("tooltip",{staticStyle:{"vertical-align":"top"},attrs:{width:"255px",content:t,placement:"top"}})],1)],1)}),0)],1):n("div",{staticClass:"no-data-line"},[n("span",{staticClass:"no-data"},[t._v(t._s(t.$t("m.common.noData")))])])]):t._e(),"2"===t.canceltempData.scenarioType||"3"===t.canceltempData.scenarioType?n("span",[n("div",{staticClass:"siteType"},[t._v(t._s(t.$t("m.site.hostSites"))+" :")]),t.canceltempData.guestboxList.length>0?n("div",{staticClass:"dialog-main"},[n("el-checkbox",{staticStyle:{"margin-bottom":"10px"},attrs:{indeterminate:t.canceltempData.guestisnate},on:{change:t.guestChange},model:{value:t.canceltempData.guestAll,callback:function(e){t.$set(t.canceltempData,"guestAll",e)},expression:"canceltempData.guestAll"}},[t._v(t._s(t.$t("m.common.all")))]),n("el-checkbox-group",{on:{change:t.guestStieChange},model:{value:t.canceltempData.guestList,callback:function(e){t.$set(t.canceltempData,"guestList",e)},expression:"canceltempData.guestList"}},t._l(t.canceltempData.guestboxList,function(t,e){return n("div",{key:e},[n("el-checkbox",{attrs:{label:t}},[n("tooltip",{staticStyle:{"vertical-align":"top"},attrs:{width:"255px",content:t,placement:"top"}})],1)],1)}),0)],1):n("div",{staticClass:"no-data-line"},[n("span",{staticClass:"no-data"},[t._v(t._s(t.$t("m.common.noData")))])])]):t._e(),"1"===t.canceltempData.scenarioType?n("span",[n("div",{staticClass:"dialog-main"},[n("el-checkbox",{staticStyle:{"margin-bottom":"10px"},attrs:{indeterminate:t.canceltempData.allisnate},on:{change:t.allChange},model:{value:t.canceltempData.allAll,callback:function(e){t.$set(t.canceltempData,"allAll",e)},expression:"canceltempData.allAll"}},[t._v(t._s(t.$t("m.common.all")))]),n("el-checkbox-group",{on:{change:t.allStieChange},model:{value:t.canceltempData.allList,callback:function(e){t.$set(t.canceltempData,"allList",e)},expression:"canceltempData.allList"}},t._l(t.canceltempData.allboxList,function(t,e){return n("div",{key:e},[n("el-checkbox",{attrs:{label:t}},[n("tooltip",{staticStyle:{"vertical-align":"top"},attrs:{width:"255px",content:t,placement:"top"}})],1)],1)}),0)],1)]):t._e(),n("div",{staticClass:"dialog-footer"},["1"===t.canceltempData.scenarioType?n("el-button",{staticClass:"ok-btn",attrs:{type:"primary",disabled:0===t.canceltempData.allList.length},on:{click:t.tocancelAuthor}},[t._v(t._s(t.$t("m.common.sure")))]):n("el-button",{staticClass:"ok-btn",attrs:{type:"primary",disabled:0===t.canceltempData.guestList.length&&0===t.canceltempData.hostList.length},on:{click:t.tocancelAuthor}},[t._v(t._s(t.$t("m.common.sure")))]),n("el-button",{staticClass:"ok-btn",attrs:{type:"info"},on:{click:function(e){t.cancelAuthorVisible=!1}}},[t._v(t._s(t.$t("m.common.cancel")))])],1)])],1)])},i=[],s=(a("96cf"),a("3b8d")),o=(a("ac6a"),a("28a5"),a("cebc")),c=a("c6a8"),r=a("90e7"),l=a("c1df"),u=a.n(l),p=a("2f62"),d=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"site-body"},[a("div",{staticClass:"table"},[a("el-table",{attrs:{data:t.tableData,"header-row-class-name":"","header-cell-class-name":"",border:"","cell-class-name":"","max-height":"255"},on:{"filter-change":t.tofilter}},[a("el-table-column",{attrs:{prop:"",type:"index",label:t.$t("m.common.index"),width:"70"}}),a("el-table-column",{attrs:{prop:"siteName",label:t.$t("m.common.siteName"),"show-overflow-tooltip":"","min-width":"85"},scopedSlots:t._u([{key:"default",fn:function(e){return[2===e.row.status||3===e.row.status?a("span",{staticClass:"todetail",on:{click:function(a){return t.sitedetail(e.row)}}},[t._v(t._s(e.row.siteName))]):1===e.row.status?a("span",{staticClass:"todetail",on:{click:function(a){return t.siteInfo(e.row)}}},[t._v(t._s(e.row.siteName))]):a("span",{staticClass:"todetail"},[t._v(t._s(e.row.siteName))])]}}])}),a("el-table-column",{attrs:{prop:"partyId",label:t.$t("m.common.partyID")}}),a("el-table-column",{attrs:{prop:"networkAccessEntrances",label:t.$t("m.site.networkEntrances"),width:"220"},scopedSlots:t._u([{key:"default",fn:function(e){return[e.row.networkAccessEntrancesArr.length>2?a("div",[a("el-popover",{attrs:{placement:"bottom","popper-class":"scope","visible-arrow":!1,offset:-40,trigger:"hover"}},[t._l(e.row.networkAccessEntrancesArr,function(e,n){return a("div",{key:n,staticStyle:{"line-height":"25px"}},[t._v(t._s(e))])}),a("div",{staticClass:"icon-caret",attrs:{slot:"reference"},slot:"reference"},[a("span",[t._v(t._s(e.row.networkAccessEntrancesArr[0]+"..."))]),a("i",{staticClass:"el-icon-caret-bottom icon-caret"})])],2)],1):a("div",[t._v(t._s(e.row.networkAccessEntrances.split(";")[0]))])]}}])}),a("el-table-column",{attrs:{prop:"networkAccessExits",label:t.$t("m.site.networkExits"),width:"200"},scopedSlots:t._u([{key:"default",fn:function(e){return[e.row.networkAccessExitsArr.length>2?a("div",[a("el-popover",{attrs:{placement:"bottom","popper-class":"scope","visible-arrow":!1,offset:-30,trigger:"hover"}},[t._l(e.row.networkAccessExitsArr,function(e,n){return a("div",{key:n,staticStyle:{"line-height":"25px"}},[t._v(t._s(e))])}),a("div",{staticClass:"icon-caret",attrs:{slot:"reference"},slot:"reference"},[a("span",[t._v(t._s(e.row.networkAccessExitsArr[0]+"..."))]),a("i",{staticClass:"el-icon-caret-bottom"})])],2)],1):a("div",[t._v(t._s(e.row.networkAccessExits.split(";")[0]))])]}}])}),a("el-table-column",{attrs:{filters:t.roleTypeSelect,"filter-multiple":!1,"column-key":"role","filter-placement":"bottom",prop:"role",label:t.$t("m.common.role"),"min-width":"70"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("span",[t._v(t._s(1===e.row.role?"Guest":"Host"))])]}}])}),a("el-table-column",{attrs:{filters:t.fateVersionSelect,"filter-multiple":!1,"column-key":"fateVersion","filter-placement":"bottom",prop:"fateVersion",label:"FATE","show-overflow-tooltip":"","min-width":"80"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("span",[t._v(t._s(e.row.fateVersion))])]}}])}),a("el-table-column",{attrs:{prop:"activationTime",label:t.$t("m.site.activationTime"),"min-width":"125","show-overflow-tooltip":""},scopedSlots:t._u([{key:"default",fn:function(e){return[a("span",[t._v(t._s(t._f("dateFormat")(e.row.activationTime)))])]}}])}),a("el-table-column",{attrs:{filters:t.siteStatusSelect,"filter-multiple":!1,"column-key":"status","filter-placement":"bottom",prop:"status",label:t.$t("m.site.status"),"min-width":"90"},scopedSlots:t._u([{key:"default",fn:function(e){return[1===e.row.status?a("span",[t._v("Not Joined")]):t._e(),2===e.row.status?a("span",[t._v("Joined")]):t._e(),3===e.row.status?a("span",[t._v("Deleted")]):t._e()]}}])}),a("el-table-column",{attrs:{prop:"",label:t.$t("m.site.serviceStatus"),"min-width":"110","show-overflow-tooltip":""},scopedSlots:t._u([{key:"default",fn:function(e){return[a("span",[t._v(t._s(1===e.row.detectiveStatus?"Unavailable":"Available"))])]}}])}),a("el-table-column",{attrs:{prop:"",label:t.$t("m.common.action"),"min-width":"70",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){return[3===e.row.status?a("el-button",{staticClass:"btn",attrs:{type:"text",disabled:""}},[a("i",{staticClass:"el-icon-delete-solid "})]):a("el-button",{attrs:{type:"text"}},[a("i",{staticClass:"el-icon-delete-solid delete",on:{click:function(a){return t.handleDelete(e.row)}}})])]}}])})],1)],1),a("div",{staticClass:"pagina"},[a("el-pagination",{attrs:{background:"","current-page":t.currentPage,"page-size":t.data.pageSize,layout:"total, prev, pager, next, jumper",total:t.total},on:{"size-change":t.handleSizeChange,"current-change":t.handleCurrentChange,"update:currentPage":function(e){t.currentPage=e},"update:current-page":function(e){t.currentPage=e}}})],1),a("el-dialog",{staticClass:"site-delete-dialog",attrs:{visible:t.dialogVisible,width:"700px"},on:{"update:visible":function(e){t.dialogVisible=e}}},[a("div",{staticClass:"line-text-one"},[t._v(t._s(t.$t("m.site.sureDelete"))+'"'+t._s(t.delSitename)+'"?')]),a("div",{staticClass:"line-text-two"},[t._v(t._s(t.$t("m.site.cantUndo")))]),a("div",{staticClass:"dialog-footer"},[a("el-button",{staticClass:"ok-btn",attrs:{type:"primary"},on:{click:t.okAction}},[t._v(t._s(t.$t("m.common.OK")))])],1)])],1)},m=[],h=a("75fc"),f={name:"Siteatble",components:{},props:{institutions:{type:String,default:function(){return""}},condition:{type:String,default:function(){return""}}},filters:{dateFormat:function(t){return t?u()(t).format("YYYY-MM-DD HH:mm:ss"):"--"}},data:function(){return{total:0,currentPage:1,delSitename:"",deleteRowId:"",dialogVisible:!1,tableData:[],fateVersionSelect:[],fateServingVersionSelect:[],siteStatusSelect:[{value:1,text:"Not Joined"},{value:2,text:"Joined"},{value:3,text:"Delete"}],roleTypeSelect:[{value:1,text:"Guest"},{value:2,text:"Host"}],data:{pageNum:1,pageSize:10}}},created:function(){var t=this;this.$nextTick(function(e){t.initList(),t.togetversion("fate_version"),t.togetversion("fate_serving_version")})},methods:{tofilter:function(t){for(var e in t)this.data[e]=t[e][0];this.data.pageNum=1,this.currentPage=1,this.initList()},initList:function(){var t=this;for(var e in this.tableData=[],this.data.institutions=this.institutions,this.data.condition=this.condition,this.data)if(this.data.hasOwnProperty(e)){var a=this.data[e];a||delete this.data[e]}Object(c["J"])(this.data).then(function(e){t.total=e.data.totalRecord,e.data.list.forEach(function(t){t.networkAccessExitsArr=t.networkAccessExits.split(";"),t.networkAccessEntrancesArr=t.networkAccessEntrances.split(";")}),t.tableData=Object(h["a"])(e.data.list)})},togetversion:function(t){var e=this,a={institutions:this.institutions,versionName:t};Object(c["w"])(a).then(function(a){a.data.forEach(function(a){var n={};n.value=a,n.text=a,"fate_version"===t?e.fateVersionSelect.push(n):e.fateServingVersionSelect.push(n)})})},handleSizeChange:function(t){},handleCurrentChange:function(t){this.data.pageNum=t,this.initList()},handleDelete:function(t){this.dialogVisible=!0,this.deleteRowId=t.id,this.delSitename=t.siteName},okAction:function(){var t=this,e={id:this.deleteRowId};Object(c["I"])(e).then(function(e){t.dialogVisible=!1,t.initList()})},sitedetail:function(t){this.$store.dispatch("setSiteName",t.siteName),this.$router.push({name:"detail",path:"/federated/detail",query:{id:t.id}})},siteInfo:function(t){this.$store.dispatch("setSiteName",t.siteName),this.$router.push({name:"siteadd",path:"/federated/siteadd",query:{type:"siteinfo",id:t.id}})}}},g=f,A=(a("a81a"),a("2877")),v=Object(A["a"])(g,d,m,!1,null,null,null),b=v.exports,_=a("5118"),y=a("a5b0"),x={name:"Site",components:{tooltip:y["a"],sitetable:b},filters:{dateFormat:function(t){return t?u()(t).format("YYYY-MM-DD HH:mm:ss"):"--"}},data:function(){return{activeName:[],currentPage:1,total:0,tipsVisible:!1,tipstempData:{institucheckList:[],institucheckboxList:[],institutions:"",insList:[],scenarioType:""},siteState:"",historyList:[],cancelAuthorVisible:!1,canceltempData:{scenarioType:"",institutions:"",allList:[],allboxList:[],allisnate:!1,allAll:!1,hostList:[],hostboxList:[],hostisnate:!1,hostAll:!1,guestList:[],guestboxList:[],guestisnate:!1,guestAll:!1},institutionsItemList:[],institutionsSelectList:[],data:{condition:"",pageNum:1,pageSize:20}}},computed:Object(o["a"])({},Object(p["mapGetters"])(["getInfo"])),watch:{activeName:{handler:function(t){localStorage.setItem("activeName",t)}}},created:function(){var t=this;this.$nextTick(function(e){t.getinsSelectList(),t.info(),t.getinitinstitutions(),localStorage.getItem("activeName").length>0&&(t.activeName=localStorage.getItem("activeName").split(",").filter(function(t){return t}))})},methods:{info:function(){var t=this;Object(r["v"])().then(function(e){t.siteState="",e.data&&e.data.forEach(function(e){"Site-Authorization"===e.functionName&&(t.siteState=1===e.status)})})},getinsSelectList:function(){var t=Object(s["a"])(regeneratorRuntime.mark(function t(){var e,a=this;return regeneratorRuntime.wrap(function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,Object(c["z"])();case 2:e=t.sent,e.data.institutionsSet.forEach(function(t,e){var n={};n.value=t,n.label=t,a.institutionsSelectList.push(n)});case 4:case"end":return t.stop()}},t)}));function e(){return t.apply(this,arguments)}return e}(),getinitinstitutions:function(){var t=Object(s["a"])(regeneratorRuntime.mark(function t(){var e,a,n=this;return regeneratorRuntime.wrap(function(t){while(1)switch(t.prev=t.next){case 0:for(e in this.data)this.data.hasOwnProperty(e)&&(a=this.data[e],a&&"[]"!==JSON.stringify(a)||delete this.data[e]);return t.next=3,Object(c["y"])(this.data).then(function(t){n.total=t.data&&t.data.totalRecord,n.institutionsItemList=[];var e=[];t.data.list.forEach(function(){var t=Object(s["a"])(regeneratorRuntime.mark(function t(a,n){var i,s,o,r,l;return regeneratorRuntime.wrap(function(t){while(1)switch(t.prev=t.next){case 0:return a.historyList=[],a.visible=!1,e.push(a),i={institutions:a.institutions,pageNum:1,pageSize:100},t.next=6,Object(c["u"])(i);case 6:return s=t.sent,s.data.list.forEach(function(t){var e={agree:[],reject:[],cancel:[]};e.updateTime=t.updateTime,e.institutions=t.institutions,t.authorityApplyReceivers.forEach(function(t){2===t.status?e.agree.push(t.authorityInstitutions):3===t.status?e.reject.push(t.authorityInstitutions):4===t.status&&e.cancel.push(t.authorityInstitutions)}),a.historyList.push(e)}),o={institutions:a.institutions},t.next=11,Object(c["e"])(o);case 11:return r=t.sent,a.authoritylist=r.data,l={institutions:[a.institutions]},t.next=16,Object(c["B"])(l).then(function(t){t.data.length>0?a.tooltip=!0:a.tooltip=!1});case 16:case"end":return t.stop()}},t)}));return function(e,a){return t.apply(this,arguments)}}()),Object(_["setTimeout"])(function(){n.institutionsItemList=[].concat(e)},500)});case 3:return t.abrupt("return",this.institutionsItemList);case 4:case"end":return t.stop()}},t,this)}));function e(){return t.apply(this,arguments)}return e}(),gethistory:function(t){this.institutionsItemList.forEach(function(e,a){a!==t&&(e.visible=!1)});var e=!this.institutionsItemList[t].visible;this.$set("this.institutionsItemList",this.institutionsItemList[t].visible,e)},toSearch:function(){var t=this;this.data.pageNum=1,this.getinitinstitutions().then(function(e){e.forEach(function(e,a){t.$refs["sitelist"][a].initList()})})},handleSizeChange:function(t){},handleCurrentChange:function(t){var e=this;this.data.pageNum=t,this.getinitinstitutions().then(function(t){t.forEach(function(t,a){e.$refs["sitelist"][a].initList()})})},addsite:function(){this.$store.dispatch("setSiteName","Add a site"),this.$router.push({name:"siteadd",path:"/federated/siteadd",query:{type:"siteadd"}})},toshowins:function(t){var e=this;this.tipstempData.institucheckList=[],this.tipstempData.institucheckboxList=[],this.tipstempData.insList=[],this.tipstempData.scenarioType="";var a={institutions:t};this.tipstempData.institutions=t,Object(c["x"])(a).then(function(t){e.tipstempData.insList=t.data.institutionsList,e.tipstempData.scenarioType=t.data.scenarioType,t.data.institutionsList.forEach(function(t){e.tipstempData.institucheckboxList.push(t)}),e.tipsVisible=!0})},totipsAction:function(){var t=this,e={approvedInstitutionsList:this.tipstempData.institucheckList,institutions:this.tipstempData.institutions};Object(c["A"])(e).then(function(e){t.$message.success("success"),t.getinitinstitutions(),t.info(),t.tipsVisible=!1})},toshowcancelAuthor:function(t,e){var a=this;this.canceltempData.institutions=e,this.canceltempData.allAll=!1,this.canceltempData.allisnate=!1,this.canceltempData.allboxList=[],this.canceltempData.allList=[],this.canceltempData.hostAll=!1,this.canceltempData.hostisnate=!1,this.canceltempData.hostboxList=[],this.canceltempData.hostList=[],this.canceltempData.guestAll=!1,this.canceltempData.guestisnate=!1,this.canceltempData.guestboxList=[],this.canceltempData.guestList=[];var n={institutions:e};Object(c["g"])(n).then(function(t){if(t&&t.data){var e=t.data.scenarioType;a.canceltempData.scenarioType=e,"1"===e?t.data.all.forEach(function(t){a.canceltempData.allboxList.push(t)}):"2"!==e&&"3"!==e||(t.data.guestList&&t.data.guestList.forEach(function(t){a.canceltempData.guestboxList.push(t)}),t.data.hostList&&"2"!==e&&t.data.hostList.forEach(function(t){a.canceltempData.hostboxList.push(t)})),a.cancelAuthorVisible=!0}})},tocancelAuthor:function(){var t=this,e={all:this.canceltempData.allList,guestList:this.canceltempData.guestList,hostList:this.canceltempData.hostList,institutions:this.canceltempData.institutions};Object(c["f"])(e).then(function(e){t.cancelAuthorVisible=!1,t.getinitinstitutions(),t.info()})},allChange:function(t){this.canceltempData.allList=t?this.canceltempData.allboxList:[],this.canceltempData.allisnate=!1},allStieChange:function(t){var e=t.length;this.canceltempData.allAll=e===this.canceltempData.allboxList.length,this.canceltempData.allisnate=e>0&&e<this.canceltempData.allboxList.length},hostChange:function(t){this.canceltempData.hostList=t?this.canceltempData.hostboxList:[],this.canceltempData.hostisnate=!1},hostStieChange:function(t){var e=t.length;this.canceltempData.hostAll=e===this.canceltempData.hostboxList.length,this.canceltempData.hostisnate=e>0&&e<this.canceltempData.hostboxList.length},guestChange:function(t){this.canceltempData.guestList=t?this.canceltempData.guestboxList:[],this.canceltempData.guestisnate=!1},guestStieChange:function(t){var e=t.length;this.canceltempData.guestAll=e===this.canceltempData.guestboxList.length,this.canceltempData.guestisnate=e>0&&e<this.canceltempData.guestboxList.length},toFold:function(){this.activeName.length>0?this.activeName=[]:this.activeName=this.institutionsItemList.map(function(t){return t.institutions})}}},k=x,w=(a("aead"),Object(A["a"])(k,n,i,!1,null,null,null));e["default"]=w.exports},f410:function(t,e,a){a("1af6"),t.exports=a("584a").Array.isArray}}]);
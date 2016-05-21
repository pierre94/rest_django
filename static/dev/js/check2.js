function gspan(cobj) {       //获取表单后的span 标签 显示提示信息

    if (cobj.nextSibling.nodeName != 'SPAN') {

        gspan(cobj.nextSibling);

    } else {

        return cobj.nextSibling;

    }

}


//检查表单 obj【表单对象】， info【提示信息】 fun【处理函数】  click 【是否需要单击， 提交时候需要触发】

function check(obj, info, fun, click) {

    var sp = gspan(obj);

    obj.onfocus = function () {

        sp.innerHTML = info;

        sp.style.color = "black"

    }


    obj.onblur = function () {

        if (fun(this.value)) {

            sp.innerHTML = "输入正确！";

            sp.style.color = "green";

        } else {

            sp.innerHTML = info;
            sp.style.color = "red";

        }

    }


    if (click == 'click') {

        obj.onblur();

    }

}


onload = regs;//页面载入完执行


function regs(click) {

    var stat = true;        //返回状态， 提交数据时用到

    username = document.getElementsByName('name')[0];

    password = document.getElementsByName('password')[0];

    chkpass = document.getElementsByName('re_password')[0];

    email = document.getElementsByName('email')[0];


    check(username, "用户名由2~10个汉字、英文字母或数字组成", function (val) {

        var re1 = /^[\u4E00-\u9FFF]{2,10}$/;
        var re2 = /^[0-9a-zA-Z]{2,10}$/;
        if (re1.test(val) || re2.test(val)) {
            return true;
        }
        else {
            status = false;
            return false;
        }

    }, click);


    check(password, "密码必须在6-13位之间", function (val) {

        if (val.match(/^\S+$/) && val.length >= 6 && val.length <= 13) {

            return true;

        } else {

            stat = false;

            return false;

        }

    }, click);


    check(chkpass, "确定密码要和上面一致，规则也要相同", function (val) {

        if (val.match(/^\S+$/) && val.length >= 6 && val.length <= 13 && val == password.value) {

            return true;

        } else {

            stat = false;

            return false;

        }

    }, click);


    check(email, "请按邮箱规则输入", function (val) {

        if (val.match(/\w+@\w+\.\w/)) {

            return true;

        } else {

            stat = false;

            return false;

        }

    }, click);

    return stat;

}